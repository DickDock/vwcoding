
# 轮胎配置设置

!!! note "轮胎参数集生成器"
    [在线 TMPS 生成器](../utils/tiresCoding.md){ .md-button .md-button--primary }

### 通过 Individual 配置设置胎压监测系统

!!! tip
    在旧版 OBD11 中翻译被弄反了（普通 — 满载）
  
普通负载设置
``` yaml
单元 65 → 适配:
前轴标称胎压，普通: 255 → 22 (如需 2.2 bar)
后轴标称胎压，普通: 255 → 22 (如需 2.2 bar)
→ 应用
```

满载设置
``` yaml
单元 65 → 适配:
前轴满载标称胎压: 255 → 26 (如需 2.6 bar)
后轴满载标称胎压: 255 → 26 (如需 2.6 bar)
→ 应用
```
### 创建自定义轮胎配置

[在线 TMPS 生成器](../utils/tiresCoding.md){ .md-button .md-button--primary }

支持的单元：  
3AA907273D; 3AA907273F; 3AA907273H; 5Q0907273; 5Q0907273B; 7P6907273H; 7P6907273L.

生成时需选择所需格式（用哪个工具加载）和正确的轮胎单元。 
然后为其创建/填充胎压表。 
名称可以是任意内容 —— 轮胎规格、Winter-Summer 等名称等。但所有名称只能用拉丁字母！

生成的文件用 ODIS E 或 VCDS 刷入 65 单元：

Diagnostic function – Write Data Record

![Screenshot](../images/MQB/odis-e-tires.png) 

加载数据后，设置菜单将如下所示：  
![Screenshot](../images/MQB/tires.png) 
  
!!! warning
    写入后车辆会暂时变成"圣诞树" —— 所有单元都会报错和失效。  
    不必担心 —— 10 分钟内一切会自行修复。
  
### 胎压间接监测

![Screenshot](../images/MQB/analog_tires.png) 

在 ABS 单元中激活
``` yaml
单元 03 → 编码:
字节 27 – 激活位 4,5（第 1 种方案）或位 4,5,6（第 2 种方案 – 用于倒车雷达） 
字节 28 – 位 7: 激活
→ 应用（需重启单元）
```

激活仪表盘上的显示
``` yaml
单元 17 → 编码:
字节 4 – 位 0 (Indirect Tire Pressure Monitoring System(TPMS) installed / 胎压监测指示): 激活
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
- tire_pressure_system_0x07_msg_bus: CAN_Comfort (也可能 Suspension_data_bus)
→ 应用 
```

!!! note ""
    编码后需打开点火、打开车机，并在胎压监测界面上按下虚拟 SET 键