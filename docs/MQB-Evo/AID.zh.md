# 仪表盘 Active Info Display (AID)

### 更改车速表最大刻度

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

``` yaml 
Control unit 17 → Adjustments:
Speedometer_final_value:
- Speedometer_final_value: 
variant_0 = 260km/h
variant_1 = 280 km/h
variant_2 = 240 km/h
variant_3 = 300 km/h
variant_4 = 320 km/h
→ Apply
```

### AID 中的附加视图

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

``` yaml 
Control unit 17 → Adjustments:
Unlock_views:
- view_6: active
→ Apply
```
![Screenshot](../images/MQB-Evo/AID_additional.png)  

### AID 的样式

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

AID 中的 Golf 8 GTE (Hybrid) 视图
![Screenshot](../images/MQB-Evo/AID_view_7.png)  
``` yaml 
Control unit 17 → Adjustments:
Unlock_views:
- view_7: activ
→ Apply
```

AID 中的 Golf 8 GTI 视图
![Screenshot](../images/MQB-Evo/AID_view_8.png)  
``` yaml 
Control unit 17 → Adjustments:
Unlock_views:
- view_8: active
→ Apply
```

AID 中的 Golf 8 R 视图
![Screenshot](../images/MQB-Evo/AID_view_9.png)  
``` yaml 
Control unit 17 → Adjustments:
unlock_views:
- view_9: active
→ Apply
```

### AID (Active Info Display) 中的越野视图

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

![Screenshot](../images/MQB-Evo/AID_offroad.png)  

``` yaml 
Control unit 17 → Adjustments:
Unlock_views:
- view_10: active
→ Apply
```

### 在 AID 信息窗口中激活方向盘转角显示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

![Screenshot](../images/MQB-Evo/AID_steering_angle.png)  

!!! note ""
    可能需要在 AID 菜单中激活

``` yaml 
Control unit 17 → Adjustments:
Offroad:
- Offroad: yes
→ Apply
```

### 在 AID 信息窗口中激活增压压力显示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470 (none GTE)

!!! note ""
    可能需要在 AID 菜单中激活

![Screenshot](../images/MQB-Evo/AID_boost_pressure.png)  

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Boost_Pressure: active
→ Apply
```

### 在 AID 信息显示窗口中激活 G 值显示

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

![Screenshot](../images/MQB-Evo/AID_g-force.png)  

!!! note ""
    可能需要在 AID 菜单中激活

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- G_Meter: active
→ Apply
```

### 在 AID 信息显示窗口中激活扭矩显示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470 (none GTE)

![Screenshot](../images/MQB-Evo/AID_torque.png)  

!!! note ""
    可能需要在 AID 菜单中激活

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Engine_Torque: active
→ Apply
```

### 在 AID 信息显示中激活发动机功率显示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470 (none GTE)

![Screenshot](../images/MQB-Evo/AID_engine_power.png)  

!!! note ""
    可能需要在 AID 菜单中激活

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Engine_Power: active
→ Apply
```

### 在 AID 信息窗口中激活变速箱温度显示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

![Screenshot](../images/MQB-Evo/AID_transmission_temp.png)  

!!! note ""
    可能需要在 AID 菜单中激活

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Transmission_Temperature: active
→ Apply
```

### 带圈数计数的圈速计时器

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

!!! note ""
    可能需要在 AID 菜单中激活

![Screenshot](../images/MQB-Evo/lap_timer_1.png)  

``` yaml 
Control unit 17 → Coding:
Laptimer: yes
→ Apply
```

与圈速计时器配合使用的圈数计数器：

![Screenshot](../images/MQB-Evo/lap_timer_2.png)  

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Laptimer: active
→ Apply
```

### 在 AID (Active Info Display) 中激活加油量显示

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

!!! note ""
    可能需要在 AID 菜单中激活

![Screenshot](../images/MQB-Evo/AID_refueling.png)  

``` yaml 
Control unit 17 → Coding:
Refuel_volume: yes
→ Apply
```

### 自定义 AID (Active Info Display) 中的 logo

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

!!! note ""
    部分 logo 仅在零件号为 5H0920340B 及以上的车速表的 Golf 8 R 视图中出现！

``` yaml 
Control unit 17 → Adjustments:
Logo:
- logo: no_Logo = select
→ Apply
```

![Screenshot](../images/MQB-Evo/R_logo.png) ![Screenshot](../images/MQB-Evo/R_alt_logo.png) ![Screenshot](../images/MQB-Evo/GTE_logo.png) ![Screenshot](../images/MQB-Evo/GTI_logo.png) ![Screenshot](../images/MQB-Evo/GTD_logo.png) 

Logo_1 = R  
Logo_2 = R alternative style  
Logo_3 = GTE  
Logo_4 = GTI  
Logo_5 = GTD  

### 关闭安全带未系警告

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1400-7380

``` yaml 
Control unit 17 → Adjustments:
Deactivate_belt_warning:
- State: yes
→ Apply
```

### 更改仪表的启动画面

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 7360-7380

``` yaml 
Control unit 17 → Coding:
derivative: derivative_1 (normal Golf), derivative_3 (Golf R)
→ Apply
```

### 更改 Golf R 视图中转速表显示的颜色

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 7360-7380

``` yaml 
Control unit 17 → Adjustments:
Adjustments:
- tachometer_colour: Rot 0, Grün 0, Blau 0
→ Apply
```

示例：  
紫色: 127, 0, 255  
蓝色: 0, 0, 255  

### 更改 AID (Active Info Display) 中的车外温度警告阈值

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

``` yaml 
Control unit 17 → Adjustments:
outside_temperature:
- p_ice_warning_exit_temperature: 6° (按需调整，最高 10°C)
- p_ice_warning_entry_temperature: 4° (按需调整，最高 10°C)
- p_storage_time_engine_off: 180 (按需调整，重新启动发动机后警告会再次出现)  
→ Apply
```

### 关闭挂入倒挡时的提示音（DSG 在 "R"）

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

!!! note ""
    仅在点火状态切换后生效

``` yaml 
Control unit 17 → Adjustments:
Acoustics_driving_position_R:
- Acoustics_driving_position_R: not_active
→ Apply
```

### 关闭切换 AID 显示时的动画

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3470

``` yaml 
Control unit 17 → Adjustments:
Locking_display_content:
- Locking_decoration_animation: yes
→ Apply
```

### 激活 0-100km/h、80-120km/h 和 1/4 英里加速测量

:octicons-verified-24: SFD: yes

![Screenshot](../images/MQB-Evo/acceleration_1.png){ width="300" } ![Screenshot](../images/MQB-Evo/acceleration_2.png){ width="300" } ![Screenshot](../images/MQB-Evo/acceleration_3.png){ width="300" } 

``` yaml title="Tested SW: 1447"
Control unit 4B → Coding:
Function_activation_speed_up_measuring: activated
Speed_up_measuring_0_to_100_km_per_h: activated
Speed_up_measuring_80_to_120_km_per_h: activated
Time_measuring_for_0_to_QuaterMile: activated
→ Apply
```

``` yaml title="Tested SW: 3470"
Control unit 17 → Adjustments:
Displayable_content_configuration:
Acceleration_measurement: display
→ Apply
```

!!! warning ""
    在 4B 单元更改编码后，必须执行大灯的基本设置！  
    这似乎与仪表的软件版本有关。可能仅在 B 版本上需要，但尚未确认。

### AID 信息窗口中的指南针显示

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 3470

![Screenshot](../images/MQB-Evo/AID_compass.png)  

``` yaml 
Control unit 17 → Coding:
navigation_compass: yes
→ Apply
```

### 更改即将到来的保养提示的时机

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 3470

``` yaml 
Control unit 17 → Adjustments:
Service_early_warning_in_days:
- time: 30d (按需调整)
→ Apply
```

### 在 AID 信息窗口中显示扭矩分配

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

!!! error ""
    显示项存在，但看不出有功能，可能仅 Golf R 上有

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Torque_Distibution: active
→ Apply
```

### 在 AID (Active Info Display) 中显示驾驶模式

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 3460-3470

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 17 → Adjustments:
Displayable_content_configuration:
- Display_FPA: display
→ Apply
```

### 车速表中的扩展刻度

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 3460-3470

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 17 → Coding:
Tachometer_erweiterte_Skalenteilung: yes
→ Apply
```

### GPS 圈速计时器

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1447

!!! error ""
    1. 请勿编码，否则你会得到一个空白显示且无法退出菜单！
    2. 在 AID 5H0920340A SW 3470 上测试过

!!! tip "如何撤销此编码"
    如果你不顾警告已经编码了，必须关闭自动钥匙分配。 
    为此，进入信息娱乐系统，选择 "User -> Setup -> Automatic Key Assignment"，并禁用该功能。 
    之后，重启 MIB，方法是按住 "Power" 按钮约 20 秒，或锁车并等待 15 分钟。

    如果仍需要钥匙分配：  
    1. 重新启用钥匙分配。  
    2. 用钥匙 1 锁车。  
    3. 用钥匙 1 解锁。  
    4. 选择用户。  
    5. 用钥匙 1 锁车并等待 15 分钟。  
    6. 用钥匙 2 重复同样的过程。  

``` yaml 
Control unit 4B → Coding:
Gps_laptimer_round_route: not_activated
Gps_laptimer_distance_route: not_activated
→ Apply
```
