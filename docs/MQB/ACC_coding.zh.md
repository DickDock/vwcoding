
# 自适应巡航控制。编码

### 允许自适应巡航 (ACC) 从右侧超车/超越

!!! tip ""
    默认情况下，如果左侧车道有慢车（即便道路空旷），ACC 系统也会让车辆减速。

=== "在 ODIS 中编码"
    ``` yaml
    单元 13 → 编码:
    Overtaking_right_prevention (Vermeidung für unzulässigen Überholvorgang): 停用
    → 应用
    ```
=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 20103"
    单元 13 (自适应巡航控制) → 安全访问 → 登录密码 20103 → 长编码:
    Overtaking_right_prevention: 停用
    → 应用
    ```
=== "在 VCDS 中编码" 
    ``` yaml title="登录密码: 20103"
    单元 13 Adaptive Cruise Control → 长编码:
    字节 2 – 位 5 (Overtaking_right_prevention): 停用  
    退出 → 保存
    ``` 
    ![Screenshot](../images/MQB/overtake.png)
  
### 激活自适应巡航 (ACC) 工作模式的独立选择（不受所选驾驶模式影响）

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 13 → 编码:
    Drive_pmode_selection: MMI 菜单 自适应巡航控制 (ACC)
    → 应用
    ```
=== "在 VCDS 中编码" 
    ``` yaml title="登录密码: 20103"
    单元 13 Adaptive Cruise Control → 编码 → 长编码:
    字节 3 – 位 7 (Drive_pmode_selection, 0=MMI menu ACC / 1=Driving profile selection): 停用 
    退出 → 保存
    ``` 
    ![Screenshot](../images/MQB/acc.png)

### 延长自适应巡航 (ACC) 的起步等待时间

默认情况下，Stop & Go 系统在完全停车后只激活 3 秒。超过该时间后，只能用方向盘上的按键或油门踏板继续行驶。  

无法取消此限制，但在最新固件版本上可将时间间隔延长到 10 秒。需要带 5QA 单元的倒车雷达。  

固件要求：  
```
3QF907561, 5Q0907561: SW 0780, H10-H11  
2Q0907561, 2Q0907572: SW 0383, H01-H04
```

``` yaml
单元 13 → 编码:
字节 11 – 位 0 (Pretriggertime_reduction): 停用  
→ 应用
```

### 调节容差（仅适用于 5Q0 radar）

![Screenshot](../images/MQB/pacc_offset.jpeg)  

菜单项「考虑允许车速」直接开启或关闭 ACC 根据导航标志或摄像头识别结果进行的车速调节模式。
``` yaml
单元 13 → 编码:
Tempolimitassistent_CarMenu: 激活
```

「自适应巡航控制」菜单中的允许偏差设置项
``` yaml
单元 13 → 编码:
zul_Regelabweichung_CarMenu: large
```

你为某个标志设定的限制将被保存，并在每次识别到这些标志时自动套用。
``` yaml
单元 13 → 编码:
pACC_Learning_drivers_offset: 激活
```

### 设置 Front Assist 预警
``` yaml
单元 13 → 编码:
adjustability_awv_pre_warning: 停用
default_value_awv_pre_warning: 激活
```
