# 3Q0/3QD* (MFK 2.0) 辅助摄像头编码

**本说明仅适用于 3Q0980654 摄像头**  

带自适应车道引导的 Lane Assist —— 自适应引导避免了在车道间「乒乓」式摆动。  
这是个很棒的选项，能让你在驾驶时放松、无需时刻找车道中心，在高速公路上简直不可或缺。 

Traffic Jam Assist —— 拥堵辅助。  
这是 Lane Assist 的扩展，可从 0 km/h 工作。在拥堵中车辆自行微调方向、加速和制动，无需驾驶员参与。停车超过 3 秒后，起步需按 RES 或踩油门踏板。

Emergency Assist —— 紧急停车辅助。  
如果驾驶员不愿或无法参与驾驶，车辆会先用声音、再用急促的制动来唤醒他，  
如果之后仍不接管，车辆会自行打开双闪并停车。

Sign Assist —— 交通标志识别辅助。显示摄像头读取到的标志。 

## 辅助摄像头固件

位于此处：[固件与参数集](camAssistFirmwares.md){ .md-button .md-button--primary }

## 辅助系统激活

### 矩阵大灯 IQ Light

``` yaml
单元 A5 (辅助摄像头) → 编码:
AFS_coding_Light_Assist: Matrixbeam
→ 应用 
```

### 激活辅助系统呼出按键（适用于 5Q0 953 502 AJ / Valeo 408 876）

``` yaml title="登录密码: 20103"
单元 16 → 适配:
转向柱电子模块
驾驶辅助系统按键
已安装
→ 应用
```

### 激活不带自适应车道引导的 Lane Assist

!!! warning
    激活 Lane Assist 无需更新已安装辅助摄像头的参数集
  
在仪表盘上开启 Lane Assist 显示
``` yaml
单元 17 (组合仪表/ActiveInfoDisplay) → 编码:
字节 04 – 位 6 (Lane_assist): 激活
字节 11 – 位 1 (Lane_assist_BAP): 激活
```

辅助摄像头配置  
可以使用现成编码：  
000307060007040100220044C150890080000E20004000 
``` yaml
单元 A5 (辅助摄像头) → 编码:
字节 14 – 将值改为 A0/A1
字节 16 – 位 7: 激活（或将该字节值改为 90/98）
```

``` yaml title="登录密码: 20103"
单元 A5 (辅助摄像头) → 适配:
Lan_assist_system_mode (车道保持辅助开启状态) - Selection_over_menu  
Lane_assist_warning_intensity (车道保持辅助预警强度) - Selection_over_menu 
Personalization of lane dept. warning Cl. 15 on (Clamp 15 开启时介入时机的个性化) - Last Setting (上次设置)
→ 应用 
```

HCA – 告知转向单元存在 Lane Assist
``` yaml title="登录密码: 19249"
单元 44 (转向助力) → 编码:
字节 01 – 位 3 (Heading_control_assist): 激活
→ 应用 
```

在菜单中开启新功能
``` yaml
单元 5F (多媒体) → 适配:
Car_Function_List_BAP_Gen2:
- LDW_HCA_0x19: activated
Car_Function_Adaptations_Gen2:
- menu_display_Lane_Departure_Warning: 激活
- menu_display_Lane_Departure_Warning_over_threshold_high: 激活
→ 应用 
```

告知泊车辅助单元存在 Lane Assist（适用于 PLA3.0 12 探头者）

!!! note ""
    在 2020 年款 Tiguan 2G 上，PLA3.0 在系统中可能是 10 单元，而非 76
  
``` yaml
单元 76 → 编码:
车道保持辅助，与转向助力相关
字节 3 – 位 5 (HeadingControl Unterstutzung Auswahl): 激活 (Spurhalteassistent aktiviert)
→ 应用 
```

### 激活完整套件：自适应 Lane Assist、Traffic Jam Assist、Sign Assist

带自适应车道引导的 Lane Assist —— 避免车道间「乒乓」式摆动。  
这是个很棒的选项，能让你在驾驶时放松、无需时刻找车道中心，在高速公路上简直不可或缺。

!!! warning
    Traffic Jam Assist 工作需要已安装辅助摄像头的参数集。  
    位于此处：[固件与参数集][1]

[1]: camAssistFirmwares.md

告知空调单元 (08) 已安装摄像头加热。  

=== "在 ODIS 中编码"
    ``` yaml
    单元 08 → 编码:  
    字节 08 – 位 0 (Camera heating): 已安装
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 08 – 长编码:
    摄像头加热元件: 未安装 → 已安装
    ```

告知 ACC radar 已安装摄像头  

=== "在 ODIS 中编码"
    ``` yaml
    单元 13 (自适应巡航) → 编码:
    字节 03 – 位 6 (Front_camera): 已安装
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 13 → 长编码:
    Front_camera: 未安装 → 已安装
    ```

将远光辅助类型从普通改为 MDF —— 可遮蔽或不眩目的远光。把辅助加入菜单
``` yaml title="登录密码: 31347"
单元 09 (车载电气网络) → 适配:
Aussenlicht_Blinker:
- Warnblinken_durch_Fahrerassistenz: available
Fernlicht_assistent:
- Erweiterte_Fernlichtsteuerung: AFS, FLA, Fernlicht ueber AFS → AFS, FLA, Fernlicht (GLW,MDF)
- Menuesteuerung Fernlichtassistent: available
- Fernlichtassistent Reset: 停用
- Menuesteuerung Fernlichtassistent Werkseinstellung: available
- Assistance_lighting_sensitivity_adjustable: detected
→ 应用 
```

在仪表盘上开启 Lane Assist 和交通标志显示

=== "在 ODIS 中编码"
    ``` yaml
    单元 17 (组合仪表/ActiveInfoDisplay) → 编码:
    字节 04 – 位 6 (Lane_assist): 激活
    字节 11 – 位 1 (Lane_assist_BAP): 激活（把 lane assist 加入仪表盘辅助菜单）
    字节 05 – 位 2 (traffic_sign_display): 激活
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 17 → 长编码:
    车道保持辅助: 否 → 是
    交通标志识别: 否 → 是
    车道保持辅助, BAP, 路径: 否 → 是
    ```

激活已安装的单元。需要添加 A5（前部辅助系统传感器）并移除单元 20（带 FLA 摄像头的后视镜）

=== "在 ODIS 中编码"
    ``` yaml
    单元 19 (网关) → 适配:
    Gateway_Component_List: Node_0x30: not_coded
    Gateway_Component_List: Node_0x4F: coded
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 19 → 适配:
    远光辅助: 未编码
    驾驶员前部辅助系统传感器: 已编码
    ```

HCA – 告知转向单元存在 Lane Assist

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 19249"
    单元 44 (转向助力) → 编码:
    字节 03 – 位 0 (Heading_control_assist): 激活
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 19249"
    单元 44 → 长编码:
    车道保持辅助: 激活
    ```

大灯单元设置

!!! warning "注意！"
    更改此单元的编码会重置大灯的基本设置。[如何恢复基本设置？](../codingLights/#_12)

=== "在 ODIS 中编码"
    ``` yaml
    单元 4B (多功能模块) → 编码:
    字节 10 – 位 6 (mdf_activation): 激活
    headlamp_coding_word: 1
    multi_function_camera: installed
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 4B → 编码: 
    headlamp_coding_word: 0 → 1
    mdf_activation: 未解锁 → 已解锁
    ```

告知 ABS 单元具备紧急停车能力
``` yaml
单元 03 (ABS) → 编码:
字节 29 – 位 5 (Electromechanical parking brake): 激活 (emergenay braking)
→ 应用 
```

设置单元 3C（变道辅助）
``` yaml
单元 3C → 编码:
Lane_Departure_Warning_System:_with_Lane_Departure_Warning_System
Front_Sensors_Driver_Assistance_System:_with_Front_Sensors_Driver_Assistance_System
→ 应用 
```

告知泊车辅助单元存在 Lane Assist（适用于 PLA 12 探头者）

!!! note "有用信息"
    在 2020 年款 Tiguan 2G 上，PLA3.0 在系统中可能是 10 单元，而非 76
  
``` yaml
单元 76 → 编码:
车道保持辅助，与转向助力相关
字节 3 – 位 5 (HeadingControl Unterstutzung Auswahl): 激活 (Spurhalteassistent aktiviert)
→ 应用 
```

在菜单中开启新功能
``` yaml
单元 5F (多媒体) → 适配:
Car_Function_List_BAP_Gen2:
- LDW_HCA_0x19: 激活
- traffic_sign_recognition_0x21: 激活
- traffic_sign_recognition_0x21_msg_bus: CAN_Extended (附加数据总线)
Car_Function_Adaptations_Gen2:
- menu_display_Lane_Departure_Warning: 激活
- menu_display_Lane_Departure_Warning_over_threshol d_high: 激活
- menu_display_road_sign_identification: 激活
- menu_display_road_sign_identification_over_threshold_high: 激活
→ 应用 
```

告知抬头显示单元（如有）
``` yaml
单元 82 → 编码:
Road_sign_detection: available
Lane_departure_warning: available
→ 应用 
```

辅助摄像头配置。 

!!! note "现成编码"
    ```yaml
    000307060007040100222346C154890098000E20004000
    ```
    请非常仔细地核对该编码与车上实际具备的选项是否相符。  
    为方便起见可使用带 A5 单元解析的[位计算器](../../utils/longCoding)。  
    例如，可将现成编码[在计算器中打开](../../utils/longCoding/?code=000307060007040100222346C154890098000E20004000&label=A5_3Q0)

``` yaml
单元 A5 (辅助摄像头) → 编码:
Brand: VW
Class: A
Generation: Generation_7
Bodystyle: Suv
Expansion: Not_coded
Production_region: EU
Country_variant: Europe
Chassis: Steel_springs
Steering_bar: Not_coded
Windshield: Heat_protecting_glass
Traffic_side: Right_traffic
PSD_Version: PSD_15 # (1)!
Navigation: MIB_High # (2)!
AAG: Coded # (3)!
SWA (Side assist): Coded # (4)!
ACC: Coded
Pedestrian_break: Not_coded
Blind_spot_detection: Not_coded
Rain_light_sensor: Coded
Main_unit: enabled
PLA: Coded # (5)!
ESP: Coded
Personalize_VZE:	Not_Coded
Lan_assist_system_mode: Selection_over_menu
Personalized_key: Version_1.x
Networking_variant: MQB
Radar_interface: Coded
Perso_HC: Last_setting # (6)!
Point_of_intervention: early_setting_over_menu
LaneAssist_AGW_output: disabled
Lane_assist_off_text: disabled
Emergency_Assist: EA_Variant_2
Traffic Sign Recognition (TSR/VZE): coded
HC_mob_line: Not_coded
HC: Coded
FCWP_default_on_prewarning: last_mode
FCWP_delivery_status_prewarning: off
FCWP_extended_prewarning_settings: Not_coded
FCWP_warning_indicator: Not_coded
FCWP: Not_coded
FLA_Additional_High_Beam: no_Additional_High_Beam
FLA_Headinglight_type: LED
Mains_frequency: 50_Hz
AFS_coding_Light_Assist: Dynamic_Light_Assist (Tiguan 2021 用 Matrixbeam)
HC_LONGPRESS: Not_Coded (仅 Audi)
→ 应用 
```

1. 预测性路线数据。取决于所装车机（若无导航则为 `Not coded`）
2. 导航类型。取决于所装车机
3. 若已安装拖车钩
4. 若已安装盲区监测
5. 若已安装 Park Assist
6. 熄火时记忆所选模式

!!! warning ""
    此适配会关闭"标志不工作"预警的显示

``` yaml title="在 ODIS 中需以开发者模式进入 A5 单元，登录 89687"
单元 A5 (辅助摄像头) → 适配:
Road_sign_recognition_fusion_mode (交通标志识别: Fusion 模式): Road_Sign_Fusion
Lane_assist_warning_intensity (车道保持辅助预警强度): Selection_over_menu 
Personalisation_point_of_intervention (介入时机个性化): Last Setting (上次设置)
Adaptation_tsr:
- Par_relevance_mode: enabled  
- Par_country_mode: manuel  
- Par_country_code_RSR: 205 # (1)!
- Par_country_code_VZF: 205  
→ 应用 
```

1. 对独联体国家可使用波兰的值。可选值列表：  
    57 — 捷克  
    68 — 爱沙尼亚 (50/90/90)  
    73 — 芬兰  
    74 — 法国  
    82 — 德国  
    118 — 拉脱维亚  
    124 — 立陶宛 (50/90/130)  
    172 — 波兰 (50/60/90/100/120/140)  
    173 — 葡萄牙  
    177 — 罗马尼亚  
    178 — 俄罗斯  
    197 — 西班牙  
    205 — 瑞典 (50/90/110)  

!!! note "BAP Personalization"
    BAP Personalization —— 针对车上每把钥匙个性化设置的编程。对于 Tiguan 车型该选项未启用 —— 取值不影响任何东西。 

### 分离交通标志显示
可以在车机上显示来自导航数据库的交通标志（Sat Nav Speed Limits），  
而在 AID（Virtual Cockpit）上显示来自辅助摄像头的标志。  

![Screenshot](../images/MQB/VZA.png)

``` yaml
单元 5F (多媒体) → 适配:
Car_Function_List_BAP_Gen2:
- traffic_sign_recognition_0x21: 停用
→ 应用 
Car_Function_Adaptations_Gen2:
- menu_display_road_sign_identification: 停用
- menu_display_road_sign_identification_over_threshold_high: 停用
→ 应用 
```

``` yaml
单元 5F (多媒体) → 编码:
byte_24_vza: 激活
```

### 接近路口时的路口照明
顶配 MID LED 大灯能在路口激活侧向照明，并能根据导航数据在接近转弯时自行转动光束。 

``` yaml
单元 4B → 编码:
psd_data: 激活
Crossing_light_with_route_data: 激活 —— 接近路口时开启侧向照明
Predictive_afs: 激活 —— 根据导航地图控制弯道照明
```

!!! warning ""
    此后需要进行大灯基本设置！  
