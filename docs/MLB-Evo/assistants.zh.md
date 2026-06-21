
# 辅助系统激活

### Lane Assist 激活

!!! warning ""
    激活该辅助无需参数集

``` yaml title="登录密码: 20103"
单元 A5 (辅助摄像头) → 编码:
ALDW_lane_assist: 已安装
→ 应用
```

在菜单中开启新功能
``` yaml
单元 5F (多媒体) → 适配:
Car_Function_List_BAP_Gen2:
- LDW_HCA_0x19: 激活
- LDW_HCA_0x19_msg_bus: Terminal 15
Car_Function_Adaptations_Gen2:
- menu_display_Lane_Departure_Warning: 激活
- menu_display_Lane_Departure_Warning_over_threshold_high: 激活
→ 应用 
```

HCA – 告知转向助力单元存在 Lane Assist
``` yaml
单元 44 (转向助力) → 编码:
车道保持辅助，与转向助力相关
字节 03 – 位 1 (heading_control_assist): 激活
→ 应用 
```

``` yaml title="登录密码: 20103"
单元 09 (车载电气网络) → 适配:
Heading Control config: heading_control
→ 应用 
```

在仪表盘上开启 Lane Assist 显示
``` yaml
单元 17 (组合仪表/ActiveInfoDisplay) → 编码:
Lane_assist: yes
→ 应用 
```

``` yaml
单元 A5 (辅助摄像头) → 适配:
Lane_departure_warning_on_state: Selection_over_menu_default_on
→ 应用 
Personalisation_for_lane_departure_warning:
- TT_activated_not_activated: last_setting
→ 应用 
```

### 交通标志辅助激活（车辆须配备摄像头）

!!! warning ""
    激活该辅助可能需要参数集

车辆摄像头将读取交通标志并在仪表中显示限速。

``` yaml
单元 5F (多媒体) → 适配:
Vehicle function list BAP:
- traffic_sign_recognition_0x21: 激活
Vehicle menu operation:
- menu_display_road_sign_identification: 激活
- menu_display_road_sign_identification_over_threshold_high: 激活
→ 应用 
```
``` yaml title="登录密码: 20103"
单元 A5 (辅助摄像头) → 编码:
字节 1 – 位 0 (Traffic Sign Recognition (FTE) active): 激活
→ 应用
```
``` yaml
单元 17 (组合仪表/ActiveInfoDisplay) → 编码:
字节 5 – 位 2: 激活
→ 应用 
```
``` yaml title="登录密码: 20103"
单元 A5 (辅助摄像头) → 适配:
Display end of speed limit symbol: active
Display valid additional signs: 00100111
→ 应用 
```

### Emergency 辅助激活

!!! warning ""
    激活该辅助可能需要参数集
  
``` yaml title="登录密码: 20103"
单元 A5 (辅助摄像头) → 适配:
EA_emergency_assist: Variant_2
→ 应用 
```
``` yaml
单元 13 (自适应巡航) → 编码:
Emergency_steer_assist: 激活
→ 应用 
```
``` yaml
单元 46 (舒适系统中央模块) → 编码:
central_locking_system_emergency_assist: 激活
→ 应用 
```

### 在抬头显示上显示辅助系统
:octicons-verified-24: Audi
``` yaml
单元 82 → 编码:
Road sign detection: not available → available (显示交通标志)
Lane Departure Warning: not available → available (显示 Lane Assist)
→ 应用 
```

### 在 Audi Q7 4M 上激活 Lane Assist

!!! warning
    在出厂未激活 Lane Assist 的车辆上，无法将其完全关闭。  
    这是由于左侧拨杆端部缺少机械按键：

``` yaml
单元 A5 (辅助摄像头) → 编码:
HC: Coded
HC_mob_line: Coded
→ 应用 
```

``` yaml
单元 A5 (辅助摄像头) → 适配:
Personalization of lane dept. warning Cl. 15 on: Off
→ 应用 
```

``` yaml title="登录密码: 31347"
单元 09 → 编码:
heading_control_config: heading_control
→ 应用 
```

``` yaml
单元 44 → 编码:
Heading Control Assistant: Active
→ 应用 
```

``` yaml
单元 5F → 适配:
Car_Function_List_BAP_Gen2:
LDW_HCA_0x19: activated
LDW_HCA_0x19_msg_bus: Terminal 15

Car_Function_Adaptations_Gen2:
menu_display_Lane_Departure_Warning: activated
menu_display_Lane_Departure_Warning_over_threshold_high: activated
→ 应用 
```

``` yaml
单元 17 → 编码:
Lane Assist: yes
→ 应用 
```

``` yaml
单元 CB (若有) → 编码:
HCA: Active
→ 应用 
```

``` yaml
单元 82 (若有) → 编码:
Lane Departure Warning: Available
→ 应用 
```

``` yaml
单元 3C (若有) → 编码:
Lane_Departure_Warning_System: with_Lane_Departure_Warning_System
→ 应用 
```
