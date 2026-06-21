# 制动与轮胎

### 起步时的 ASR 设定（抑制起步抖动）

!!! tip ""
    冬季条件下推荐值 Maximum — 可消除起步打滑。
``` yaml title="登录密码: 40168"
单元 03 → 适配:
Starting vibration reduction → 选择所需值: Strong (强), Normal (正常), Maximum (最大)
→ 应用
```

### 激活 Hill Hold Control（坡道起步辅助）
``` yaml
单元 03 → 长编码:  
字节 16 – 位 0: 激活
→ 应用
```
要使其生效需从内存重新读取单元设置（用原厂防盗设防/撤防一次，持续 5-10 秒）

### Hill Hold Control 的适配（设定）
``` yaml title="登录密码: 40168"
单元 03 → 适配:
Berganfahrassistent → 选择所需值: early (早), normal (正常), 较晚
→ 应用
```

### 制动盘烘干

!!! note ""
    有 3 个等级：schwach (1-弱), stark (3-强), mittel (2-中)
``` yaml title="登录密码: 40168"
单元 03 → 适配:
Brake disk drying → 选择 Stufe 2 (mittel) (等级 2 (中))
→ 应用
```

### HBA 设定（制动辅助）

!!! tip "" 
    推荐值 – sport
``` yaml title="登录密码: 40168"
单元 03 → 适配:
Hydraulic brake assistant → 选择 normal (正常) (或选择所需值) 
→ 应用
```

### 制动系统压力设定
``` yaml title="登录密码: 40168"
单元 03 → 适配:
Overboost in brake system → 标准值 6 — (选择所需值)
→ 应用
```

### 添加菜单项 ESC-sport、ESC-off（用于带 ESC 的车辆）
``` yaml title="登录密码: 40168"
单元 03 → 长编码:  
ESC Sport + ASR 关闭
字节 16:
位 04: 停用
位 03, 06: 激活
ESC On/Off
字节 16:
位 04: 停用
位 05 — 激活
ESC On/Off + ASR 关闭
字节 16:
位 04: 停用
位 03, 05: 激活
ESC On/Off + ESC Sport
字节 16:
位 04: 停用
位 06: 激活
→ 应用
```

### 激活 XDS

!!! warning "无法激活"
    TRW 公司生产的 ESC/ABS 单元 (Electronic Brake Control — EBC 460) 不支持该功能。  
    SW: 6R0 614 517 BQ, 6R0 614 517 CA 或 6R0 614 517 CG

### EDS 系统的触发阈值
``` yaml title="登录密码: 40168"
单元 03 → 长编码:  
字节 17 – 位 0-3
01 – 1.6MPI/66 kW/90 л.с./155 nm
02 – 1.6MPI/81 kW/110 л.с./155 nm 配 MT
03 – 1.6MPI/81 kW/110 л.с./155 nm 配 AT
04 – 1.0TSI/70 kW/95 л.с./160 nm 和 1.2TSI/66 kW/90 л.с./160 nm
05 – 1.2TSI/81 kW/110 л.с./175 nm 和 1.0TSI/81 kW/110 л.с./200 nm
06 – 1.4TSI/92 kW/125 л.с./200 nm 配 DSG
07 – 1.4TDI/66 kW/90 л.с./230 nm 配 MT
08 – 1.4TDI/66 kW/90 л.с./230 nm 配 DSG
09 – 1.6TDI/85 kW/115 л.с./250 nm
→ 应用
```

### 间接式胎压监测 TPMS
第一代系统
``` yaml title="登录密码: 40168"
单元 03 → 长编码:  
字节 16 – 位 1: 激活
字节 16 – 位 2: 激活
字节 19 – 位 7: 激活
→ 应用
```

``` yaml title="登录密码: 20103"
单元 5F → 适配:
Car_Function_List_BAP_Gen2 – tire_pressure_system_0x07 → 由「未激活」改为「激活」
Car_Function_List_BAP_Gen2 – tire_pressure_system_0x07_msg_bus → 由「数据总线 动力」改为「数据总线 舒适」
Car_Function_Adaptations_Gen2 – menu_display_rdk → 由「未激活」改为「激活」
→ 应用
```

``` yaml
单元 17 (5JA-920-7XX) → 长编码:  
字节 04 – 位 0: 激活
→ 应用
```
``` yaml title="登录密码: 20103"
单元 03 → 适配:
胎压监测指示 → 选择「默认」「灵敏」或「不灵敏」
胎压监测系统, 轮胎选择 → 选择「普通」「未知」或「SST 轮胎」
→ 应用
```

开启显示具体车轮：
``` yaml title="登录密码: 40168"
单元 03 → 长编码:  
字节 15 – 位 3: 激活 (代替 61 – 69)
→ 应用
```
