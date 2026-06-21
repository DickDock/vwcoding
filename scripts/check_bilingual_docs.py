#!/usr/bin/env python3
"""Verify that docs/ Markdown pages exist in every required language.

Russian (`name.md`) is the default/base language. Translations live next to the
base file with a locale suffix: `name.en.md`, `name.zh.md`.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Translation locales stored as `name.<lang>.md` next to the Russian base file.
KNOWN_LANGS = ("en", "zh")
# Locales that every base page MUST provide a translation for.
REQUIRED_LANGS = ("en", "zh")

# Pages that intentionally exist in a single language only.
SKIP_STEMS: set[str] = set()


def is_doc(path: Path) -> bool:
    return path.suffix == ".md" and path.is_file()


def lang_suffix(path: Path) -> str | None:
    """Return the translation locale of a file, or None for a base (RU) file."""
    for lang in KNOWN_LANGS:
        if path.name.endswith(f".{lang}.md"):
            return lang
    return None


def base_path(path: Path) -> Path:
    """Map any file to its Russian base `.md` (idempotent for base files)."""
    lang = lang_suffix(path)
    if lang:
        return path.with_name(path.name[: -len(f".{lang}.md")] + ".md")
    return path


def tr_path(base: Path, lang: str) -> Path:
    return base.with_name(f"{base.stem}.{lang}.md")


def rel(path: Path) -> str:
    return str(path.relative_to(DOCS))


def base_key(path: Path) -> str:
    return str(base_path(path).relative_to(DOCS))


def check_all_pairs() -> list[str]:
    errors: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        if not is_doc(path):
            continue
        if base_key(path) in SKIP_STEMS:
            continue
        base = base_path(path)
        if lang_suffix(path):
            # Orphan translation: a `name.<lang>.md` without its Russian base.
            if not base.exists():
                errors.append(f"Missing Russian base for {rel(path)}")
            continue
        # Base (Russian) file must provide every required translation.
        for lang in REQUIRED_LANGS:
            if not tr_path(base, lang).exists():
                errors.append(f"Missing {lang} pair for {rel(base)}")
    return errors


def changed_files(base_ref: str) -> set[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base_ref}...HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"git diff failed: {result.stderr.strip()}")
    files: set[Path] = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line.startswith("docs/") or not line.endswith(".md"):
            continue
        files.add(ROOT / line)
    return files


def check_changed_pairs(base_ref: str) -> list[str]:
    """Keep all language versions in sync within a single PR.

    - If the Russian base changed, every required translation must change too.
    - A translation-only edit is allowed as long as the Russian base exists.
    """
    errors: list[str] = []
    changed = changed_files(base_ref)
    touched: set[str] = set()
    for path in changed:
        if not is_doc(path):
            continue
        if base_key(path) in SKIP_STEMS:
            continue
        touched.add(base_key(path))

    for key in sorted(touched):
        base = DOCS / key
        if base in changed:
            for lang in REQUIRED_LANGS:
                tr = tr_path(base, lang)
                if tr not in changed:
                    errors.append(
                        f"{rel(base)} changed without matching update to {rel(tr)}"
                    )
        elif not base.exists():
            for lang in KNOWN_LANGS:
                tr = tr_path(base, lang)
                if tr in changed:
                    errors.append(
                        f"{rel(tr)} changed but Russian base {rel(base)} is missing"
                    )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="Verify that every docs/*.md base page has all required translations",
    )
    parser.add_argument(
        "--changed",
        metavar="BASE_REF",
        help="On PRs: keep Russian and its translations in sync; translation-only edits OK",
    )
    args = parser.parse_args()

    if not args.all and not args.changed:
        args.all = True

    errors: list[str] = []
    if args.all:
        errors.extend(check_all_pairs())
    if args.changed:
        errors.extend(check_changed_pairs(args.changed))

    if errors:
        print("Bilingual documentation check failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print("Bilingual documentation check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
