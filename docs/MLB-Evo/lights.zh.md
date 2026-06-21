
# 灯光设备

### 更改转向灯闪烁次数

``` yaml
单元 46 → 适配:
Turn signal control (转向灯控制):
- Freeway flashing (高速公路上转向灯的工作、闪烁循环次数): 新值（默认 3）
→ 应用
```

也可以更改设防和撤防时的闪烁次数

### 用远光晃灯时不关闭近光

!!! note ""
    在大灯关闭和近光开启时都有效

``` yaml title="登录密码: 31347"
单元 09 → 编码:
lowbeam_at_flash: not_active: 激活
→ 应用
```

### 在 DRL 模式下激活后示廓灯

``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 2 – 位 3 (SL_AT_DRL): 激活
→ 应用
```

### 设置（或关闭）向仪表盘输出"请开灯"提示

``` yaml title="登录密码: 31347"
单元 09 → 编码:
headlight_hint_0: lds_at_null
headlight_hint_1: lds_at_parkinglight
→ 应用
```

### 在菜单中设置自适应灯光功能

``` yaml title="登录密码: 31347"
单元 09 → 编码:
mmi_adaptive_light: not_active
→ 应用
```

### 在菜单中关闭 DRL

``` yaml title="登录密码: 31347"
单元 09 → 编码:
drl_mmi: 激活
→ 应用
```

### 拉起手刹时关闭 DRL

``` yaml title="登录密码: 31347"
单元 09 → 编码:
drl_break: 激活
→ 应用
```

### 提高 DRL 亮度

``` yaml title="登录密码: 31347"
单元 09 → 编码/适配:
sl_at_drl: active
```

### 尾灯动画
:octicons-verified-24: Audi
!!! warning ""
    仅在配备顶配灯组的车辆上有效

``` yaml
单元 46 → 编码:
SBBR_variant: 0 → 1
→ 应用
```
