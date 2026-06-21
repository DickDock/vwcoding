# 空调系统控制

### 在 "Auto" 模式下显示风量档位

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

!!! warning ""
    仅适用于带旋钮的旧式空调

``` yaml 
Control unit 08 → Adjustments:
Blower display during auto mode:
Blower display during auto mode: activated
→ Apply
```

### 保存 AirCare 设置

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
Filtering_interior_air_saving: 
- Filtering_interior_air_saving: not_active (Will not be stored), active (Will be stored), depending_on_standing_time (Stored depending on standing time)
→ Apply
```

### 一定时间后自动将座椅加热降至较低档位

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
Time for seat heating power reduction Level 3 to level 2: 
- param_Time_for_seat_heating_power_reduction_Level_3_to_level_2: 0 min (adjust value as desired, 0 = off)
Time for seat heating power reduction Level 2 to level 1:
- param_Time_for_seat_heating_power_reduction_Level_2_to_level_1: 0 min (adjust value as desired, 0 = off)
→ Apply
```

### 保存内循环设置

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
Save air recirculation status at terminal 15 off:
- Save air recirculation status at terminal 15 off: storring, Do_not_store, resttime_dependent_storage (Stored depending on standing time)
→ Apply
```

### 启用 "gentle"、"medium"、"intensive" 风量档位
:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
Climate_style:
- Climate_style: display
→ Apply
```

![Screenshot](../images/MQB-Evo/climate_settings.png)  

### 调节座椅加热温度

!!! note ""
    "lower" 是启动温度  
    "upper" 是关闭温度

``` yaml
Control unit 08 → Adjustments:
Seat_Heating_Level_Adaptation:
- Seat_heating_stage_1_lower_threshold: 20,0 [UN]_°C (stage 1)
- Seat_heating_stage_1_upper_threshold: 20,5 [UN]_°C (stage 1)
- Seat_heating_stage_2_lower_threshold: 20,0 [UN]_°C (stage 1)
- Seat_heating_stage_2_upper_threshold: 20,5 [UN]_°C (stage 1)
- Seat_heating_stage_3_lower_threshold: 33,0 [UN]_°C (stage 2)
- Seat_heating_stage_3_upper_threshold: 33,5 [UN]_°C (stage 2)
- Seat_heating_stage_4_lower_threshold: 33,0 [UN]_°C (stage 2)
- Seat_heating_stage_4_upper_threshold: 33,5 [UN]_°C (stage 2)
- Seat_heating_stage_5_lower_threshold: 50,0 [UN]_°C (stage 3)
- Seat_heating_stage_5_upper_threshold: 50,5 [UN]_°C (stage 3)
- Seat_heating_stage_6_lower_threshold: 50,0 [UN]_°C (stage 3)
- Seat_heating_stage_6_upper_threshold: 50,5 [UN]_°C (stage 3)
→ Apply
```

### 保存座椅加热设置

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
Seat heating level driver side, saving condition:
- param_Seat_heating_level_driver_side,_saving_condition: not_active, 10_minutes_activ, active (Last configuration will be stored)
→ Apply
```

``` yaml
Control unit 08 → Adjustments:
Seat heating level passenger side, saving condition:
- param_Seat_heating_level_passenger_side,_saving_condition: not_active, 10_minutes_activ, active (Last configuration will be stored)
→ Apply
```

### 永久关闭方向盘加热

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0440-0531

``` yaml
Control unit 08 → Adjustments:
- Heated_steering_wheel_and_Heated_steering_wheel_automatic_mode: not_installed
→ Apply
```
