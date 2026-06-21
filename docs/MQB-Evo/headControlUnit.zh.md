# 车机

### 导航地图同时显示在 AID 和信息娱乐屏幕上

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1803-1941

!!! note ""
    仅在重启信息娱乐系统后生效

``` yaml 
Control unit 5F → Adjustments:
Dashboard_Display_Configuration:
- ability_switch_nav_maps: no
- navigation_map_compression_mode: H264
- navigation_map_resolution: 1
- navigation_map_transmission_mode: IP_streaming
→ Apply
```

或者：

``` yaml 
Control unit 5F → Adjustments:
Dashboard_Display_Configuration:
- navigation_map_resolution: 2
- navigation_map_transmission_mode: MOST_High
→ Apply
```

### 教练模式

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1803-1941

![Screenshot](../images/MQB-Evo/MIB3_driver.png) 

``` yaml 
Control unit 5F → Adjustments:
Car_Function_Adaptations:
- menu_display_driving_school_over_threshold_high: activated
- menu_display_driving_school: activated
→ Apply
```

### 从 HMI 关闭登录界面/用户功能

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1803-1941

!!! note ""
    所有用户功能将被停用，无商店、无更新。

``` yaml 
Control unit 5F → Adjustments:
function_configuration_pso:
- iaa_function: not activated
→ Apply
```

### 关闭导航系统在行驶中的输入锁定

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1803-1941

``` yaml 
Control unit 5F → Adjustments:
Disabled_menu_contents:
- FB_MEDIA_19: non_blocked
- FB_MISC_14: non_blocked
- FB_MISC_19: non_blocked
- FB_MISC_18: non_blocked
- FB_MISC_31: non_blocked
- FB_MISC_29: non_blocked
- FB_MISC_25: non_blocked
- FB_MISC_33: non_blocked
- FB_MISC_44: non_blocked
- FB_MISC_41: non_blocked
→ Apply
```

### 开启/关闭收音机的 AM 频段

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 1941

``` yaml 
Control unit 5F → Adjustments:
function_configuration_radio:
- AM_disable: activated
→ Apply
```

### 在 HMI 中启用夏令时设置

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 1941

``` yaml 
Control unit 5F → Adjustments:
Summer_Time_Shift_Method:
- shift_method: none
→ Apply
```

### 无 Harman/Kardon 音响也启用 Comp Improve Sound Quality

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 1941

!!! Note ""
    这里音质是否真的更好，见仁见智

``` yaml 
Control unit 5F → Adjustments:
function_configuration_sound:
- brand_sound: Beats
→ Apply
```

### 开启/关闭 MIB3 启动画面中的 Harman/Kardon logo

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 1941

![Screenshot](../images/MQB-Evo/MIB3_harman_logo.png)  

``` yaml 
Control unit 5F → Adjustments:
Startup_Screen_Sticker_HMI:
- Startup_Screen_Sticker_HMI: 3 (0 = no logo, 3 = Harman/Kardon logo)
→ Apply
```

### 允许连接多部手机

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1941

``` yaml 
Control unit 5F → Adjustments:
function_configuration_phone:
- Support_second_phone: none (one, two, three)
→ Apply
```

### 关闭 Android Auto 的限制

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1941

``` yaml 
Control unit 5F → Adjustments:
nhtsa_properties:
- nhtsa_limitation_switches_for_androidauto_no_video_playback: not activated
- nhtsa_limitation_switches_for_androidauto_no_text_input: not activated
- nhtsa_limitation_switches_for_androidauto_no_setup_configuration: not activated
- nhtsa_limitation_switches_for_androidauto_limit_displayed_message_length: not activated
→ Apply
```

### 激活 hybrid radio

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1983

``` yaml 
Control unit 5F → Adjustments:
function_configuration_radio:
- Hybrid_Radio_additional_online_data activated
→ Apply
```

### 调节 MIB3 启动画面

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 1941

!!! Note
    (0 = VW, 2 = GTD, 3 = GTI, 6 = R, 7 = R-Line, 8 = Alltrack, 18 = Peak Edition)

![Screenshot](../images/MQB-Evo/MIB3_boot_logo.png)  

``` yaml 
Control unit 5F → Adjustments:
function_configuration_hmi:
- screenings: 3
→ Apply
```

### 显示 U 盘中的图片

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1899-1941

!!! error ""
    无法成功编码

``` yaml 
Control unit 5F → Adjustments:
function_configuration_media:
- picture_viewer: on
→ Apply
```

### HMI 中的越野监视器

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1941

!!! error ""
    无法成功编码

``` yaml 
Control unit 5F → Adjustments:
Car_Function_Adaptations:
- menu_display_compass_over_threshold_high: activated
- menu_display_compass: activated
Car_Function_List_BAP:
- compass_0x15_msg_bus: Databus_Infotainment
- compass_0x15: activated
→ Apply
```

### 欢迎音

:octicons-verified-24: SFD: yes

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 5F [Tested SW: 1899-1941] → Adjustments:
function_configuration_audio:
- welcome_sound: on
- function_configuration_sound:
- vehicle_leaving_sound: activated
- vehicle_readiness_sound: activated
→ Apply
```

``` yaml 
Control unit 47[Tested SW: 4319] → Adjustments:
function_configuration_audio:
- welcome_sound: on
→ Apply
```

### 连接蓝牙耳机

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1941

!!! error ""
    无法成功编码

``` yaml 
Control unit 5F → Adjustments:
function_configuration_connectivity:
- Bluetooth_Headphones: available
→ Apply
```

### 关闭用户选择

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1941

!!! error ""
    菜单栏中只显示一个地球图标；第二个图标不再出现。不清楚后台还发生了什么。

``` yaml 
Control unit 5F → Adjustments:
privacy_mode:
- supress_privacy_mode: active
→ Apply
```
