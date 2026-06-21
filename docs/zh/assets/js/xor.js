let decodeString = "c9d2";
let codeLength = 4;

// 本地化：按站点语言（zh/en/ru，默认 ru）选择弹窗文本。原项目仅俄/英双语并列，
// 这里拆成单语，让中文站显示中文。检测依据 URL 路径（最可靠，不依赖 <html lang>）。
const xorI18n = (function () {
  const lang = location.pathname.indexOf("/zh/") !== -1 ? "zh"
             : location.pathname.indexOf("/en/") !== -1 ? "en" : "ru";
  const table = {
    lengthMismatch: {
      ru: "Длина вводимого значения должна быть {0} символа.",
      en: "Input HEX value must be exactly {0} characters long.",
      zh: "输入值的长度必须为 {0} 个字符。"
    },
    hexOnly: {
      ru: "Допустимы только HEX символы (0-9, A-F).",
      en: "Only HEX characters (0-9, A-F) are allowed.",
      zh: "只允许 HEX 字符（0-9、A-F）。"
    }
  };
  return {
    t: function (key, a0, a1) {
      let s = table[key][lang];
      if (a0 !== undefined) s = s.split("{0}").join(a0);
      if (a1 !== undefined) s = s.split("{1}").join(a1);
      return s;
    }
  };
})();

function init() {
  const urlParams = new URLSearchParams(window.location.search);
  const codeParam = urlParams.get('code');

  if (codeParam) {
    document.getElementById("origCode").value = codeParam;
    calculateXor();
  }
}

function calculateXor() {
  let input = document.getElementById("origCode").value.trim();
  let result = '';

  if (input.length !== codeLength) {
    alert(xorI18n.t("lengthMismatch", codeLength));
    return;
  }

  if (!/^[0-9a-fA-F]+$/.test(input)) {
    alert(xorI18n.t("hexOnly"));
    return;
  }

  for (let index = 0; index < codeLength; index++) {
    const a = parseInt(input.charAt(index), 16);
    const b = parseInt(decodeString.charAt(index), 16);
    const temp = (a ^ b).toString(16).toUpperCase();
    result += temp;
  }

  document.getElementById("calcCode").value = result;
}

function clearAll() {
  document.getElementById("origCode").value = "";
  document.getElementById("calcCode").value = "";
}
