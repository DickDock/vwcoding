
# 车机

### 关闭收音机的 AM 波段

效果：左下角原本无用的 AM/FM「切换器」会变为手动调台图标

``` yaml title="登录密码: 20103"
单元 5F → 编码:
byte_14_AM_disable
选择「开」
→ 应用（需重启单元）
```

### 在泊车辅助模式中开启 360 摄像头
:octicons-verified-24: Audi e-tron 带 360 摄像头
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Visual display for park assist: OPS display → with OPS 360°
→ 应用
```

### 车速 > 30 km/h 时开启倒车影像
:octicons-verified-24: Audi e-tron
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Switch-off speed for parking assist: 150 → 140
→ 应用
```

### 无线 Car Play
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
配置:
- Apple_DIO_Wireless: 激活
- Google_GAL_Wireless: 激活
- wlan_5ghz_switch: 激活
→ 应用
```

### 关闭连接手机时自动启动 CarPlay 或 AndroidAuto
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
function_configuration_media:
- app_start_automatically_on_customer_device: on → off
→ 应用
```

### 从 USB 或 SD 查看照片
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
function_configuration_media:
- picture_viewer: off → on
→ 应用
```

### 激活 MirrorLink（适用于已激活 Audi Smartphone Interface 的车辆）
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
function_configuration_connectivity:
- Mirror_link: off → on
→ 应用
```

### 激活行车视频

``` yaml title="登录密码: 20103"
单元 5F → 适配:
Speed:
- testmode_video_speed_off: 255
→ 应用
```

!!! note ""
    需要使用 development mode  

### 激活行驶中操作导航

``` yaml title="登录密码: 20103"
单元 5F → 适配:
locked menu contents:
- FB_NAV_3: non_blocked
→ 应用
```

### 用 SIM 卡拨打电话的功能
:octicons-verified-24: Audi
!!! note ""
    适用于配备 SIM 卡槽的车辆，可用该 SIM 卡拨打电话

``` yaml title="登录密码: 20103"
单元 5F → 适配:
Vehicle_configuration:
- Phone_module_operation_mode: data_only → voice_and_data
- Support_for_response_and_hold: off → on
- Support_of_threeway_calling: off → on
- sim_data_only_sms_support: on → off
- Internal_SIM_card_usage: Never → Always
→ 应用
```

### 向多媒体系统连接蓝牙耳机的功能
:octicons-verified-24: Audi
```
单元 5F → 编码:
byte_16_Bluetooth_Headphones: off
→ 应用
```

### 关闭行驶中 MMI 部分功能的锁定
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Vehicle_configuration:
- unblock_functions_while_piloted_driving: blocked
→ 应用
```

### 关闭用户选择界面
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 5F → 适配:
menu_IAA_PSO_over_threshold_high: 停用
menu_IAA_PSO_clamp_15_off: 停用
menu_IAA_PSO: 停用
→ 应用
```

### 驾驶员欢迎音
:octicons-verified-24: Audi
``` yaml
单元 5F → 适配:
function_configuration_audio:
- welcome_sound: off → on
→ 应用并重启车机
```
