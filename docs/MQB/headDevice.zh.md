
# 车机

### 编码标注解读

menu_display_xxx_clamp_15_off – 熄火时工作  
menu_display_xxx_over_threshold_high – 行驶中工作  
menu_display_xxx_standstill – 待机时工作  
menu_display_xxx_after_disclaimer – 某种提示之后工作

### 解锁工程菜单  

在此之前，可能需要先把 ODIS E [切换到编程模式](../../utils/odis-e/#_4)
``` yaml title="登录密码: 12345"
单元 5F → 适配:
开发者模式 (Developer mode): 激活
```

### 更换车辆皮肤
有时换装别的车机后，上面装的是另一台 VW 车的配置。  

VW Tiguan 示例：  
``` yaml
单元 5F → 编码:
byte_0_brand: _VW
byte_1_Car_Class: 3
byte_1_Car_Generation: 7
byte_2_Car_Derivate: 6
byte_2_Car_Derivate_Supplement: 0
→ 应用 
```

### 同时通过蓝牙连接两部手机

``` yaml
单元 5F → 适配:
function_configuration_phone:
- Support_second_phone: none → 修改
- Support_for_response_and_hold: off → on
- Dtmf_without_active_call: off → on
- _user_menu_three_way_calling: not_installed → installed
→ 应用 
```

``` yaml
单元 17 → 编码:
telephone2_BAP: no → yes
→ 应用
```

## ICC 电子语音放大器

要激活该放大器，需加载参数集：  
[(ODIS 用参数集)](../parameters/5F_ICC_ONLY.xml.zip)

加载参数集后，必须长按电源键重启车机！

### 关闭车机启动时的音量跳变
有时开机时音量比关车时设定的大得多。

``` yaml
单元 5F → 适配:
Adjustment_fm_tuner_mono_stereo:
- l_hf_stereo_lower_threshold: 20 dBµV (原为 37 dBµV)
→ 应用 
```

### 关闭收音机的 AM 波段
左下角原本无用的 AM/FM「切换器」会变为手动调台图标  
![Screenshot](../images/MQB/fm.jpg)

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 5F → 编码:
    byte_14_AM_disable: 激活
    → 应用（需重启单元）
    ```

=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    5F – MMI / RNS  
    编码 - 07 → 长编码:
    字节 1 – 位 1 (byte_14_AM_disable): 激活  
    退出 → 保存
    ```
    ![Screenshot](../images/MQB/am_radio.jpg)

### 车机开机画面

``` yaml
单元 5F → 编码:
字节 18 – 把 00 改为
    01 — Hybrid
    02 — GTD
    03 — GTI
    04 — BlueMotion
    05 — E-Golf
    06 — R-Line
    07 — Golf R
→ 应用（需重启单元）
```

音响系统 logo
``` yaml
单元 5F → 适配:
Startup_screen_sticker_hmi (默认为 0000) - 改为
    1 — fender premium audio system
    2 — dynaudio
→ 应用 
```

### 把车机菜单显示从翻页改为平铺

=== "在 ODIS 中编码"
	```
	单元 5F → 编码:
    byte_17_Skinning: Skin_1 → Skin_5
    → 应用（需重启单元）
    ```
  
=== "在 VCDS 中编码"
    ```
    5F – MMI / RNS  
    编码 - 07 → 长编码:
    字节 17: Skin_1 → Skin_5 
    退出 → 保存  
    ```

### 行车视频、行驶中运行 MirrorLink
:octicons-verified-24: Discover PRO

``` yaml
单元 5F → 适配:
nhtsa_properties:
- nhtsa_limitation_switches_for_carplay_no_softKeyboard: 停用 (CarPlay, 行驶中可调出键盘)
- nhtsa_limitation_switches_for_androidauto_limit_displayed_message_length: 停用 (AA, 关闭行驶中输出消息长度限制)
- nhtsa_limitation_switches_for_androidauto_no_setup_configuration: 停用 (AA, 行驶中可进入设置)
- nhtsa_limitation_switches_for_androidauto_no_text_input: 停用 (AA, 关闭行驶中文本输入禁止)
- nhtsa_limitation_switches_for_androidauto_no_video_playback: 停用 (АА, 行驶中可播放视频)
→ 应用 
```

对于所有其他设备，需要额外加载专用 ZDC 容器或 ODIS 用 XML 参数集
[(ODIS 用参数集)](../parameters/5F_3Q0035864C_V03935274HX_VIM_MIM.xml.zip)
  
### 车机中设置仪表盘的菜单
:octicons-verified-24: Škoda Octavia  

``` yaml
单元 5F → 适配:
Car_function_list_bap_gen2_extended:
- display_configuration_0x45: 激活
- display_configuration_0x45_msg_bus: CAN_Comfort
→ 应用 
```
  
### Off Road Display

![Screenshot](../images/MQB/offroad.jpg)
  
!!! note ""
    在第二代 Tiguan 上，Composition Media 6"、Discover Media、Discover Pro 信息系统中无需在 5F 单元编码即可工作。  

``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2
menu_display_compass → "active" (default not active)
menu_display_compass_over_threshold_high → "active" (default not active) 
menu_display_compass_clamp_15_off  → "active" (default not active)
→ 应用  
  
Car_Function_List_BAP_Gen2
compass_0x15 "active" (default not active)
→ 应用 
``` 
  
!!! warning ""
    对于 Composition Media 8"，需要对 5F 单元编码。  
    编码后单元中会残留一个不可清除的错误，但不影响功能
  
=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 5F → 编码:
    字节 24 – 位 02 (Navigation System): 激活（原为 "02" 00000010，变为 "06" 00000110）
    → 应用（需重启单元）
    ```
  
=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    5F – MMI / RNS  
    编码 - 07 → 长编码:
    字节 24 – 位 2 (Navigation System): 激活
    或修改二进制值 – 原为 "02" 00000010，变为 "06" 00000110  
    退出 → 保存
    ```

### 教练模式

!!! tip ""
    适配后需重启车机
  
``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2:
- menu_display_driving_school – 由未激活改为激活
- menu_display_driving_school_over_threshold_high – 由未激活改为激活
Car_Function_List_CAN_Gen2:
- Driving_school – 由不可用改为可用
→ 应用
```

### 开启个性化

!!! tip ""
    编码须在发动机未启动时进行

``` yaml title="登录密码: 20103"
单元 17 → 编码:
字节 10 – 个性化
选择「开」
→ 应用
```

``` yaml title="登录密码: 31347"
单元 09 → 适配:
个性化 / Personalisierung:
- Personalisierung_Profilfunkion → profiles_active
- Personalisierung_aktiv → Active
- Aktivierungsoption_im_HMI-Menue_sichtbar → Active
- Benutzerkontenverwaltung_in_HMI-Menue_sichtbar → Active
- Personalisierungsfunktionen_in_HMI-Menue_sichtbar → Active
- PSO_FSG_Setup2_Bit_1 → Active
- PSO_FSG_Setup2_Bit_2 → Active
→ 应用
```

激活个性化
!!! tip ""
    这一系列动作是为了让车辆不要总是进入「访客」模式。

``` yaml title="登录密码: 31347"
单元 09 → 适配:
个性化 / Personalisierung
- Profil_Variante: Konto (v. 1.x)
```
保存、点一下、锁车。  

创建配置文件，然后改为：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
个性化 / Personalisierung
- Profil_Variante: Konto (v. 2.x)
```
保存、点一下、锁车。  
改为：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
个性化 / Personalisierung
- Profil_Variante: Konto (v. 1.x)
```

### 使用 glonass 天线进行导航和指南针
:octicons-verified-24: Discover Pro · :octicons-verified-24: Discover Media
  
``` yaml
单元 5F → 适配:
Navigation_GNSS_Receiver_Setting:
- default_hw_reception: 停用
- gps: 停用
- galileo: 停用
- glonass: 停用
- compass: 停用
- external_gps_1: 激活
- external_gps_2: 停用
→ 应用
```

``` yaml
单元 75 → 适配:
GPS: internal_GPS_output_on_CAN
Navigation_Type: Type_2:
- Gnss_data_rate:
Data Rate: 5 Hz (原为 1)
→ 应用
```
