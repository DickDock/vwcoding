# 巡航控制功能

### 激活定速巡航（无距离调节）

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0395

``` yaml title="login code: 20103"
Control unit 13 → Coding:
Cruise_control_mode: activated
→ Apply
```

### 关闭右侧超车限制 (ACC)

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0395

``` yaml title="login code: 20103"
Control unit 13 → Coding:
Overtaking_right_prevention: deactivated
→ Apply
```

### 将 ACC 调整为 1 km/h 步进

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0395

!!! note ""
    轻按 +/- 为 1 km/h，稍长按为 +/- 10 km/h

``` yaml title="login code: 20103"
Control unit 13 → Coding:
Operation_mode: Operation_mode_2
→ Apply
```

### 在车辆菜单中可调的 ACC 弯道辅助

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0395

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml title="Login code: 20103"
Control unit 13 → Coding:
Curve_assistent_CarMenu: activated
→ Apply
```

### 在车辆菜单中可调的 ACC 限速器

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0395

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml title="Login code: 20103"
Control unit 13 → Coding:
Speed_limit_assistent_CarMenu: activated
→ Apply
```
