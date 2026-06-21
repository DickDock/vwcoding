# BCM（单元 09）—— 灯光与舒适

!!! warning ""
    在 MEB 上向 **09** 写入需要 **SFD**（2024+ —— **SFD2**）。

### Coming Home / Leaving Home —— 时长

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 31347"
单元 09 → 适配:
Coming_home_time:
- Coming_home_time: 30 s
Leaving_home_time:
- Leaving_home_time: 30 s
→ 应用
```

按自己的需要选择数值（秒）。在你的 SW 中通道名可能是 `Coming_home` / `Leaving_home`。

### 落锁时自动折叠后视镜

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 31347"
单元 09 → 编码:
Mirror_fold_in: automatic
→ 应用
```

如果没有该通道 —— 功能可能只能通过菜单实现，或在该 PR 上不存在。

### 舒适开窗（长按钥匙）

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 31347"
单元 09 → 适配:
Comfort_open:
- Comfort_open: active
Comfort_close:
- Comfort_close: active
→ 应用
```

### 氛围灯（若已安装）

MEB 上的 ambient 区域编码与 [MQB-Evo / aestheticLights](../MQB-Evo/aestheticLights.md) 接近。请核对 ambient package 的 PR。
