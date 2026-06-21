# 多媒体

### 更改 Swing/Bolero 音效 (Arkamys)
!!! note ""
    只有当车机中存在相应参数集时，Arkamys 才会正确发声。参数集用 VCP 或 ODIS 刷入，该参数集文件不公开。

``` yaml
单元 5F → 长编码:
字节 11 – 位 2 (Škoda Surround 和 Virtual Subwoofer 项): 激活
字节 08 – 位 6 (VDA Low Frequency Input): 激活
→ 应用
```

### 更改 Swing/Bolero 开机画面
``` yaml
单元 5F → 长编码:
字节 18: 把值 00 改为所需值
01-vRS
02-SCOUT
03-Laurin & Klement
04-GreenLine
07-MonteCarlo (用于 swing 2 和 3)
08-SportLine (仅 swing 3)
→ 应用
```
保存编码后，需通过重启车机来应用新值（在 swing 上 — 长按电源键）。  
下次车机首次开机时（撤防后）即可看到新画面。

### 在 Swing/Bolero 车机中停用 AM 波段
``` yaml
单元 5F → 长编码:
字节 14 – 位 1: 激活
```

### 更改「车辆状态」菜单中车辆的显示样式
``` yaml
单元 5F → 长编码:
字节 01 – 位 0~23:
– 035201, 车型: Škoda Rapid
– 035203, 车型: Škoda Rapid Spaceback
- 035331, 车型: Škoda Rapid FL (NH3)
– 036200, 车型: Škoda Fabia
– 036202, 车型: Škoda Fabia Combi
– 037301, 车型: Škoda Octavia 掀背
– 038401, 车型: Škoda Superb 掀背
→ 应用
```

### 更改车机开机时画面的显示时长
``` yaml
单元 5F → 适配:
Time display for start screen → 2.0 s – 设为所需值
→ 应用
```
20103

### 自行加装后门扬声器后激活之 (Swing/Bolero/Amundsen)
``` yaml
单元 5F → 长编码:
字节 04 – 位 0~31 → 选择
- ВЕ000000 (4 通道 / 6 个无源扬声器)
如果后门安装了带高音头的 2 分频音响，相应选择：
— FF000000 (4 通道 / 8 个无源扬声器)。
→ 应用
```

### 激活低频模拟输入 AUX-IN
``` yaml
单元 5F → 长编码:
字节 8 – 位 4: 激活
→ 应用
```

### 激活 USB 输入
``` yaml
单元 5F → 长编码:
字节 19 – 位 6~7 → 选择值
- 80 (USB 功能) 或
- С0 (USB 和 iPhone 功能)
→ 应用
```

### 更改麦克风灵敏度
``` yaml
单元 5F → 适配:
Microphone sensitivity → 0 dB – 设为所需值。
→ 应用
```
* 该参数设为负值会提高麦克风信号的音量。负值越小，增益越大。
20103

### 熄火时显示行车电脑读数
``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2-menu_display_board_computer_clamp_15_off → 由 not activated 切换为 activated
→ 应用
```
20103

### Swing/Bolero 上的驾校模式
``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2-menu_display_driving_school → 由 not activated 切换为 activated
Car_Function_Adaptations_Gen2-menu_display_driving_school_over_threshold_high → 由 not activated 切换为 activated
Car_Function_List_CAN_Gen2-Driving_school → 由 Not available 切换为 available
Car_Function_List_CAN_Gen2-Driving_school_msg_bus → 由 Not available 切换为 Comfort data bus
→ 应用
```
20103

### 激活 Swing 3 的「越野」模式
``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2 – menu_display_compass_clamp_15_off: 激活
Car_Function_Adaptations_Gen2 – menu_display_compass_over_threshold_high: 激活
Car_Function_Adaptations_Gen2 – menu_display_compass: 激活
→ 应用
```
20103

### 激活工程菜单 (Engineering Testmode) Swing 2
仅可使用 VAS5054 和 ODIS-E
```
启动 ODIS-E 程序
选择项目 (SK25X 或 SK26X) → 启动
选择单元 5F → Diagnostic session (诊断会话)
在弹出的小窗中选择：
Development mode (开发者模式) → Execute (执行)
然后：Adaptation/parameter (适配) →
Developer mode (开发者模式) → 输入值 Activated
```

# 在工程菜单中设定声音参数
长按 Setup 键直到屏幕出现菜单 Engineering Testmode 即可启动工程菜单。  
选择：Software System – Audio Management →  
在 Loudness 项打勾  
然后选择：Input Gain Offset，在下面各项把电平提高 13 dB  
* FM source — +12  
* Media File Player — +9  
* BT audio — +13  
退出工程菜单，并在声音设置中按需微调平衡和均衡器。  
完成所有声音设置后，建议停用工程菜单。有观点认为它在激活状态下会消耗蓄电池电量。

### 开启冬令时到夏令时的切换

``` yaml
单元 5F → 适配:
Summertime: 把 automatic, manual 改为 Europe
→ 应用
```
20103

### 连接第二部手机。Swing 3

一部手机可用于通话，另一部用于听音乐。

``` yaml
单元 5F → 适配:
Dtmf_without_active_call: 激活
Support_second_phone: 激活
Support_for_response_and_hold: 激活
→ 应用
```
20103

``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 11 – 位 6: 激活 (telephone2_BAP)
→ 应用
```
