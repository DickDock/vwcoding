# 2Q0* (MFK 3.0) 辅助摄像头编码

**本说明仅适用于 2Q0980653 摄像头**  

带自适应车道引导的 Lane Assist —— 自适应引导避免了在车道间「乒乓」式摆动。  
这是个很棒的选项，能让你在驾驶时放松、无需时刻找车道中心，在高速公路上简直不可或缺。 

Traffic Jam Assist —— 拥堵辅助。  
这是 Lane Assist 的扩展，可从 0 km/h 工作。在拥堵中车辆自行微调方向、加速和制动，无需驾驶员参与。停车超过 3 秒后，起步需按 RES 或踩油门踏板。  
激活需要参数集。  

Emergency Assist —— 紧急停车辅助。  
如果驾驶员不愿或无法参与驾驶，车辆会先用声音、再用急促的制动来唤醒他，  
如果之后仍不接管，车辆会自行打开双闪并停车。

Sign Assist —— 交通标志识别辅助。显示摄像头读取到的标志。  
激活需要 SWaP 码。分步说明：[2Q0 摄像头 SWaP](2Q0_swap.md)。

## 功能扩展 SWaP 码

100E1000 — 增强车道引导 (aLDW)  
100E1100  
100E1200  
100E1300  
100E1400  
100E1500  
100E1600 — 路径上的物体识别  
100E1700 — 行人识别 (FCPW)  
100E0F00 — 标志识别 (TSR/VZE)  

## 辅助摄像头固件

位于此处：[固件与参数集][1]

[1]: camAssistFirmwares.md

## 辅助系统激活

### 激活 Light Assist —— 远光辅助

``` yaml title="登录密码: 31347"
单元 09 (车载电气网络) → 适配:
Fernlicht_assistent:
- Erweiterte_Fernlichtsteuerung: "AFS: FLA: BCM-Fernlicht" 或 "AFS: FLA: Fernlicht ueber AFS"
- Menuesteuerung Fernlichtassistent Werkseinstellung: available
- Menuesteuerung Fernlichtassistent: available
- Fernlichtassistent Reset: 停用
→ 应用 
```
``` yaml
单元 A5 (辅助摄像头) → 编码:  
字节 15 – 位 5-7: (20) AFS_coding_Light_Assist,High_Beam_Assist
→ 应用 
```

### 激活车道保持辅助 (Lane Assist) 

在仪表盘上开启 Lane Assist 显示
``` yaml
单元 17 (组合仪表/ActiveInfoDisplay) → 编码:
字节 04 – 位 6 (Lane_assist): 激活
字节 11 – 位 1 (Lane_assist_BAP): 激活
```

HCA – 告知转向单元存在 Lane Assist
``` yaml title="登录密码: 19249"
单元 44 (转向助力) → 编码:
字节 03 – 位 1 (Heading_control_assist): 激活
→ 应用 
```

在菜单中开启新功能
``` yaml
单元 5F (多媒体) → 适配:
Car_Function_List_BAP_Gen2:
- LDW_HCA_0x19: 激活
- LDW_HCA_0x19_msg_bus: CAN_Extended
Car_Function_Adaptations_Gen2:
- menu_display_Lane_Departure_Warning: 激活
- menu_display_Lane_Departure_Warning_over_threshold_high: 激活
→ 应用 
```

告知泊车辅助单元存在 Lane Assist（适用于 PLA3.0 12 探头者）

!!! note ""
    PLA3.0 在系统中可能是 10 单元，而非 76
  
``` yaml
单元 76 → 编码:
车道保持辅助，与转向助力相关
字节 3 – 位 5 (HeadingControl Unterstutzung Auswahl): 激活 (Spurhalteassistent aktiviert)
→ 应用 
```

辅助摄像头配置
``` yaml
单元 A5 (辅助摄像头) → 编码:  
字节 08 – 位 5-7 (Point_of_intervention): A0 late, setting over menu
字节 09 – 位 0-1 (Configuration_for_lane_departure_warning_Kl15): 03 Last_setting
字节 09 – 位 7 (HC): (1) coded
字节 09 – 位 2-3 (Lane_assist_system_mode): 0C Selection_over_menu
字节 09 – 位 4-5 (HC advanced takeover request): (1) coded
字节 17 – 位 0 (HC messages): (1) coded
→ 应用 
```
