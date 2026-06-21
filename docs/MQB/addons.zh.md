# 加装

### 辅助摄像头

设备：  
1. 辅助摄像头  
2. 护罩  
3. 无 FLA 的无边框后视镜  
4. 后视镜固定护罩  
5. 线束  

接线图：  
摄像头 A5 (R242) 1 脚 -→ ACC 雷达 (J428) 6 脚  
摄像头 A5 (R242) 7 脚 -→ ACC 雷达 (J428) 5 脚  
6 脚 — "+"  
5 脚 — "-"  
2 脚 — Can extended low – 后视镜接插件 8 脚  
8 脚 — Can extended high – 后视镜接插件 3 脚  
4 脚 — 摄像头加热器正极线  
10 脚 — 摄像头加热器负极线  
  
接线图  
![Screenshot](../images/MQB/addons/A5-scheme.jpeg)  

标定靶板  
![Screenshot](../images/MQB/addons/Front_maket.jpg)  

[(摄像头编码)](3Q0_assistants)
[(摄像头标定)](3Q0_calibration)

### 触控式空调面板

``` yaml
单元 08 → 编码:
Climate_style → display 改为 Anzeige Front und Heck
→ 应用（需重启单元）
```
``` yaml
单元 08 → 适配:
Detection_time_tap:
- par_Detection_time_tap: 600 ms
Detection_time_hold:
- par_Detection_time_hold: 600 ms
Off_time_neighbor_key_during_sliding:
- par_Off_time_neighbor_key_during_sliding: 400 ms
Sensitivity_touch:
- par_Sensitivity_touch: 0
Steps_temp_slider:
- par_Steps_temp_slider: 8
Step_size_temp_slider:
- par_Step_size_temp_slider: 0.5°C
22_degree_jump_temp_slider:
- par_22_degree_jump_temp_slider: not_active
Flick_function_temp_slider:
- par_Flick_function_temp_slider: not_active
Profile_selection_touch:
- par_Profile_selection_touch: 0
dimming_characteristic_new_1:
- X1: 0
- Y1: 16
- X2: 10
- Y2: 16
- X3: 50
- Y3: 60
- X4: 100
- Y4: 125
- X5: 150
- Y5: 500
- X6: 253
- Y6: 1,000
dimming_characteristic_new_2:
- X1: 0
- Y1: 0
- X2: 10
- Y2: 100
- X3: 25
- Y3: 250
- X4: 50
- Y4: 500
- X5: 75
- Y5: 750
- X6: 100
- Y6: 1,000
dimming_characteristic_new_3:
- X1: 0
- Y1: 6
- X2: 10
- Y2: 6
- X3: 50
- Y3: 12
- X4: 100
- Y4: 25
- X5: 150
- Y5: 100
- X6: 253
- Y6: 300
dimming_characteristic_new_4:
- X1: 0
- Y1: 20
- X2: 10
- Y2: 20
- X3: 50
- Y3: 60
- X4: 100
- Y4: 120
- X5: 150
- Y5: 800
- X6: 253
- Y6: 1,000
dimming_characteristic_new_5:
- X1: 0
- Y1: 10
- X2: 10
- Y2: 10
- X3: 50
- Y3: 50
- X4: 100
- Y4: 100
- X5: 150
- Y5: 1,000
- X6: 253
- Y6: 1,000
dimming_characteristic_new_6:
- X1: 0
- Y1: 4
- X2: 10
- Y2: 4
- X3: 50
- Y3: 15
- X4: 100
- Y4: 30
- X5: 150
- Y5: 600
- X6: 253
- Y6: 1,000
dimming_characteristic_new_7:
- X1: 0
- Y1: 20
- X2: 10
- Y2: 20
- X3: 50
- Y3: 50
- X4: 100
- Y4: 100
- X5: 150
- Y5: 800
- X6: 253
- Y6: 1,000
dimming_characteristic_new_8:
- X1: 0
- Y1: 8 
- X2: 10
- Y2: 8 
- X3: 50
- Y3: 20 
- X4: 100
- Y4: 25 
- X5: 150
- Y5: 600 
- X6: 253
- Y6: 1,000 
dimming_characteristic_new_9:
- X1: 0
- Y1: 14 
- X2: 10
- Y2: 14 
- X3: 50
- Y3: 32 
- X4: 100
- Y4: 41 
- X5: 150
- Y5: 800 
- X6: 253
- Y6: 1,000 
dimming_characteristic_new_10:
- X1: 0
- Y1: 10 
- X2: 10
- Y2: 10 
- X3: 50
- Y3: 25 
- X4: 100
- Y4: 50 
- X5: 150
- Y5: 800 
- X6: 253
- Y6: 1,000 
damping_dimming_characteristic_01:
- PWM_Daempfung_Aufdimmen: 0.2 s
- PWM_Daempfung_Abdimmen: 0.1 s
damping_dimming_characteristic_02:
- PWM_Daempfung_Aufdimmen: 0.2 s
- PWM_Daempfung_Abdimmen: 0.1 s
damping_dimming_characteristic_03:
- PWM_Daempfung_Aufdimmen: 0.2 s
- PWM_Daempfung_Abdimmen: 0.1 s
damping_dimming_characteristic_04:
- PWM_Daempfung_Aufdimmen: 0.2 s
- PWM_Daempfung_Abdimmen: 0.1 s
Sun_sensor_supplier_differentiation:
- par_Sun_sensor_supplier_differentiation: none
→ 应用
```

### 湿度传感器

传感器 3Q0907643 安装在原厂污浊空气传感器的位置  

``` yaml
单元 08 → 编码:
字节 9 – 位 4-5 (10 – 已安装车外空气湿度传感器 / Sensor_for_air_humidity_outside): 激活
Reduction of window misting outside at high humidity: Matching glass temperature model
→ 应用（需重启单元）
```
``` yaml
单元 08 → 适配:
Reduction of window misting outside at high humitity:
- param_Reduction_of_window_misting_outside_at_high_humitity: Matching coding
→ 应用
```

### DYNAUDIO 

``` yaml
单元 19 → 适配:
Installation list – specified installations:
- Sound System: Not coded
- Digital Sound System Control Module: Yes
GW_Enable_CAN_Timeout_DTC:
- Sound System: Enabled
→ 应用
```
``` yaml
单元 5F → 编码:
byte_4_Channel_1_HT: not_installed
byte_4_Channel_1_TT: not_installed
byte_4_Channel_2_HT: not_installed
byte_4_Channel_2_TT: not_installed
byte_4_Channel_3_HT: not_installed
byte_4_Channel_3_TT: not_installed
byte_4_Channel_4_HT: not_installed
byte_4_Channel_4_TT: not_installed
byte_5_Channel_5_HT: not_installed
byte_5_Channel_5_TT: not_installed
byte_5_Channel_6_HT: not_installed
byte_5_Channel_6_TT: not_installed
byte_5_Channel_7_HT: not_installed
byte_5_Channel_7_TT: not_installed
byte_5_Channel_8_HT: not_installed
byte_5_Channel_8_TT: not_installed
byte_6_Channel_9_HT: not_installed
byte_6_Channel_9_TT: not_installed
byte_6_Channel_10_HT: not_installed
byte_6_Channel_10_TT: not_installed
byte_6_Channel_11_HT: not_installed
byte_6_Channel_11_TT: not_installed
byte_6_Channel_12_HT: not_installed
byte_6_Channel_12_TT: not_installed
byte_7_Channel_13_HT: not_installed
byte_7_Channel_13_TT: not_installed
byte_7_Channel_14_HT: not_installed
byte_7_Channel_14_TT: not_installed
byte_7_Channel_15_HT: not_installed
byte_7_Channel_15_TT: not_installed
byte_7_Channel_16_HT: not_installed
byte_7_Channel_16_TT: not_installed
byte_11_Sound_System: Sound_System_external_MOST
→ 应用（需重启单元）
```
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Sound System: yes
Startup_screen_sticker_HMI: 2
Car_Function_List_BAP_Gen2:
- Amplifier_0x2D: not activated
- Amplifier_0x2D_msg_bus: Databus Infotainment
→ 应用
```

### [PR-KA1] 倒车影像摄像头

??? note "接线说明" 
    1. 30 号端子正极取自 Quadlock 接插件的红色或红黄色粗线  
    2. 地线取自 Quadlock 接插件的棕色粗线  
    3. 信息娱乐 CAN 总线 — 来自摄像头的信号  
    - 12 号脚应连接摄像头视频电缆的「屏蔽层」/屏蔽 — 黑色线  
    - 6 号脚 – 同一电缆的中心芯线 — 白色线  
    4. 这是蓝色接插件最边上的两个脚。  
    - 橙紫色 — 接 Quadlock 的橙紫色 — 灰色接插件第 6 触点  
    - 橙棕色 — 接 Quadlock 的橙棕色 — 灰色接插件第 12 触点  
    检查时务必关闭后备厢！  

``` yaml
单元 19 → 设备列表:
6C (摄像头): 已安装
→ 应用
```
车机设置
``` yaml title="登录密码: 20103"
单元 5F → 编码:
字节 19 – 位 4 (byte_19_Rear_View_Low): 停用
→ 应用
```
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Car_Function_List_BAP_Gen2:
- VPS_0x0B: 激活
- VPS_0x0B_msg_bus: Databus 改为 Infotainment
→ 应用
```

泊车辅助设置
``` yaml
单元 76 → 编码:
字节 2 – 位 4-5 (10 – Camera Type: Rear View Camera (RVC)): 激活
→ 应用（需重启单元）
```

!!! note ""
    如果未做摄像头标定 — 会一直报错 — 缺少基础参数。

!!! warning "安装中国产摄像头"
    车机也可以连接不支持轨迹线的中国产摄像头。但这种情况下需要修改若干编码：
    ``` yaml
    单元 5F → 编码:
    字节 19 – 位 4 (byte_19_Rear_View_Low): 激活
    → 应用
    ```
    ``` yaml
    单元 5F → 适配:
    Car_Function_List_BAP_Gen2 
    - VPS_0x0B: 停用
    → 应用
    ```

标定靶板  
![Screenshot](../images/MQB/addons/Rear_maket.jpg)  

### Kessy 后门把手

设备：  
— 门把手 510837205G 510837206G  
— Tiguan 前门成套线束  
— 线束对接接插件  
— 门接插件用针脚各 6 个 12527545852 和 12527512135  
— Kessy 单元用针脚 6 个 N90764701  

右门接线图：  
![Screenshot](../images/MQB/addons/kessy-2.jpeg)  

左门接线图：  
![Screenshot](../images/MQB/addons/kessy-1.jpeg)  

布线原理：  
1. 从把手引出 4 根线 - 3 根到 Kessy 单元，1 根接地。  
2. 需将 3 根来自把手的线穿过饰板上的橡胶护套。  
3. 然后线穿过波纹管到门接插件。  
4. 从接插件引线到 Kessy 单元。  

步骤：
1. 拆门（拆下饰板），按 ELSA 说明拆下旧把手并装上新把手，把线从门的「潮湿」部分引到外面，铺设时注意不要让玻璃下降时刮到它。  
2. 把成品线束的 3 根线从把手引到门接插件，地线缠到门单元的接地点上，与原厂线束捆在一起，并在门与门柱之间压接接插件，为此需部分拆下门内线束。  
3. 把线压接到后门接插件。  
4. 把把手压接到门柱接插件。  
5. 沿门槛和脚部照明线束，把线从门柱铺到 Kessy 单元，并按说明压接单元。  

``` yaml
单元 B7 → 编码:
字节 0 – 位 2 (左后门 Kessy 门把手, Activation of Kessy door handle, left rear door): 激活
字节 0 – 位 3 (右后门 Kessy 门把手, Activation of Kessy door handle, right rear door): 激活
字节 1 – 位 2 (关闭左后门被动进入, Passive entry left rear door handle): 停用
字节 1 – 位 3 (关闭右后门被动进入, Passive entry right rear door handle): 停用
→ 应用
```

### [PR-7Y1,7Y5] Side Assist – 盲区监测系统

!!! note ""
    雷达有 2 种类型。自 2020 年起供货的雷达无需解除组件保护和进行标定

参数集：

| 设备 ID                       | 固件                                                            |                      参数集<br/>(ODIS XML)                       |
|-------------------------------|-----------------------------------------------------------------|:--------------------------------------------------------------------:|
| 2Q0907685B / 2Q0907686B (176) | [(下载)](../firmwares/DB_03C_7100_2G0_MB19_VW3260EUK0BA.frf) | [(下载)](../parameters/DB_03C_7100_2G0_MB19_VW3260EUK0BA.xml.zip) |
| 2Q0907685C / 2Q0907686C       | [(下载)](../firmwares/DB_03C_7100_2G0_MB19_VW4820EUK0BA.frf) | [(下载)](../parameters/DB_03C_7100_2G0_MB19_VW4820EUK0BA.xml.zip) |

``` yaml
单元 19 → 设备列表:
3C (变道系统): 已安装
CF (变道系统): 已安装
Gateway_Component_List:
- Node_0x4E: coded
- Node_0x8A: coded
→ 应用
```
仪表盘编码
``` yaml
单元 17 → 编码:
Lane_change_assistant: yes
Lane_change_assistant_BAP: yes
→ 应用（需重启单元）
```
自适应巡航编码
``` yaml
单元 13 → 编码:
Control_module_for_lane_assistance: installed
Lane_change_support: 激活
→ 应用（需重启单元）
```
ABS 编码
``` yaml
单元 03 → 编码:
字节 29 – 位 7: 激活 (1XXXXXXX)
→ 应用（需重启单元）
```
车机编码
``` yaml
单元 5F → 编码:
Car_Function_List_BAP_Gen2:
- SWA_0x1A: 激活
- SWA_0x1A_msg_bus → 附加数据总线 (CAN_Extended)
Car_Function_Adaptations_Gen2:
- menu_display_lane_assistant: 激活
- menu_display_lane_assistant_over_threshold_high: 激活
```

环视系统编码（如有）
``` yaml
单元 6C → 编码:
equipment_RTA: installed
→ 应用（需重启单元）
```
泊车辅助
``` yaml
单元 76 → 编码:
Rear_Cross_Traffic: Alert: mit RCTA
→ 应用（需重启单元）
```
辅助摄像头（如有）
``` yaml
单元 A5 → 编码:
SWA: Coded
→ 应用（需重启单元）
```
变道辅助
``` yaml
单元 3C → 编码:
Pre_Sense: without_Pre_Sense
Rear_Cross_Traffic_Alert: with_RCTA
ECU for draw bar: no ECU for draw bar
steering: left-hand drive
Rear_Axle_Steering: without_Rear_Axle_Steering
Lane_Departure_Warning_System: with_Lane_Departure_Warning_System
Front_Sensors_Driver_Assistance_System: with_Front_Sensors_Driver_Assistance_System
Diagnosis_RCTA: tone_via_PLA
→ 应用（需重启单元）
```

### 自动大灯

为此需要新的灯光开关 5G0941431BD 和光照雨量传感器 5Q0955547C

安装开关
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_uebergreifend:
- LDS_mit_AFL: Yes
→ 应用
```

安装光照雨量传感器
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Lighting_Assist_Adaptation:
- Regen_Lichtsensor: LIN_Regen_Licht_Sensor
- Feuchtesensor: Installed (如果有湿度传感器)
```

完成这些编码后，光照雨量传感器会出现在 9 单元的编码中。
向其写入编码：
``` yaml title="登录密码: 31347"
单元 09 → 编码 → 子块 RLHS:
- 3CA8DD — 大灯不那么晚开启, 大约 1200lx
- 3CA8D7 — 大灯非常晚才开启, 800lx 时
```

### [PR-7K3] Direct RDKS/TPMS – 直接式胎压监测系统

RDKS (Reifen Druck Kontrolle System) 或 TPMS (Tires Pressure Monitoring System)

参数集：

| 设备 ID         |                     参数集<br/>(ODIS XML)                     |
|-----------------|:-----------------------------------------------------------------:|
| 5Q0907273B      | [(下载)](../parameters/65_5Q0907273B_0009_V03935251EE.xml.zip) |

!!! note "所需操作"
    1. 在右后翼子板（保险杠下方原厂位置）安装 RDKS 系统天线 (5Q0907273B)  
    2. 铺设线束、连接电源和 CAN 总线  
    3. 安装胎压传感器 (5Q0907275B)
    3. 向天线加载参数集、对车辆系统编码  

![Screenshot](../images/MQB/addons/rdks-1.jpg)  

ELSA 中的接线图（使用 4 根线 — 12V 电源、地线，以及 CAN Ext High 和 Low 总线）
![Screenshot](../images/MQB/addons/rdks-2.jpg) 

CAN 总线位于发动机舱盖开启拉手附近、饰板后面。接插件 T17a，针脚 12 (CAN High) 和 13 (CAN Low)
![Screenshot](../images/MQB/addons/rdks-3.jpg)
电源取自保险丝盒。如果「原厂」7 号保险丝已被占用，可使用空闲的 45 号或 38 号。

编码
``` yaml
单元 19 → 设备列表:
65 (胎压监测系统控制单元): 已安装
→ 应用
```

关闭间接式胎压（如果之前已激活）
``` yaml
单元 03 → 编码:
字节 27 – 位 4,5,6: 停用
字节 28 – 位 7: 停用
→ 应用（需重启单元）
```
``` yaml
单元 17 → 编码:
字节 4 – 位 0 (Indirect Tire Pressure Monitoring System(TPMS) installed / 胎压监测指示): 停用
→ 应用（需重启单元）
```

激活 RDKS
``` yaml
单元 17 → 编码:
字节 3 – 位 7 (Direct Tire Pressure Monitoring System(TPMS) installed / 胎压监测指示): 激活
字节 11 – 位 2 (Direct Tire Pressure Monitoring System(TPMS) BAP installed): 激活
→ 应用（需重启单元）
```

在车机菜单中激活
``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2:
- menu_display_rdk: 激活
- menu_display_rdk_over_threshold_high: 激活
→ 应用 
---
Car_Function_List_BAP_Gen2:
- tire_pressure_system_0x07: 激活
- tire_pressure_system_0x07_msg_bus: CAN_Extended
→ 应用 
```

编码后需行驶约 1 公里以激活系统
