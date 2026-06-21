# 前部辅助摄像头 (A5)

### Travel-Assist 激活时可在车辆菜单中调节转向阻力

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3129-3405

![Screenshot](../images/MQB-Evo/travel_assist_setting.png)

``` yaml 
Control unit A5 → Coding:
HC_Warn_Intensity: Setting_over_menu
→ Apply
```

### 调节车道保持辅助的介入点

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3129-3405

``` yaml 
Control unit A5 → Coding:
Point_of_intervention: early (intervenes early), late (intervenes late), early_setting_over_menu (Intervenes early, no settings in the menu), late_setting_over_menu (Intervenes late, no settings in the menu)
→ Apply
```

### 保存车道保持辅助设置（在点火状态切换时）

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3129-3405

``` yaml 
Control unit A5 → Coding:
Configuration_for_lane_departure_warning_Kl15: last_setting
→ Apply
```

### 车道保持辅助的介入点可在车辆菜单中调节

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3129-3405

``` yaml 
Control unit A5  → Coding:
Point_of_intervention: early, late, early_setting_over_menu, late_setting_over_menu
→ Apply
```

### 在 60km/h 以下激活车道保持辅助

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3129-3303

!!! error ""
    在 60km/h 以下无功能

``` yaml 
Control unit A5  → Coding:
Hc_variante: Variante_1
→ Apply
```
