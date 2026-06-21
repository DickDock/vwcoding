# 加装

### [PR-PWH] 灯光辅助、雨量传感器、Coming/Leaving Home

!!! info "传感器编号"
    5Q0 955 547A — 2016MY  
    5Q0 955 547B — 2017MY  
    传感器可互换。即 547A 可用于 2016MY，反之亦然。

``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 06 – 位 0-1 选择 02 已安装光照传感器 [PR-8K3/8K9+8N6]
字节 06 – 位 3: 激活
字节 07 – 位 0-1 选择 03 Coming/Leaving 功能类型: Seat/Škoda/Volkswagen
字节 07 – 位 5: 开启
字节 13 – 位 5: 开启
→ 应用（需重启单元）
```

``` yaml title="登录密码: 31347"
单元 09 → 编码:
在设备列表中选择 5Q0 955 547B 光照/雨量传感器 (RLHS)
字节 0 – 字节 1-2 – 选择 185E 或 984D（用于带挡风玻璃加热的车）
最终编码取值为 — 00 18 5E
带挡风玻璃加热的车 — 00 98 4D
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Assistance light functions-Assistenzfahrlicht bei Regen – active
Assistance light functions-AFL Zeitverzoegerung – 2 000 ms
Assistance light functions-Lichtsensorempfindlichkeit – normal
Assistance light functions-Assistance_lighting_sensitivity_ajustable — present
Comfort illumination-Coming Home Verbaustatus – automatic
Comfort illumination-Menuesteuerung Coming Home Werkseinstellung – active
Comfort illumination-Menueeinstellung Cominghome – 10 s
Comfort illumination-Coming Home Leuchten – Low beam
Comfort illumination-Coming-home Einschaltereignis – Driver door
Comfort illumination-Helligkeitsschwelle Infrarot-Messung – 72.0
Comfort illumination-Leaving-Home Verbausstatus – Enabled
Comfort illumination-lho_aktiviert – active
Comfort illumination-lho_zeit – 10 s
Comfort illumination-Helligkeitsschwelle Forward-Messung – 100
Driving light and parking light-Menueeinstellung CHO LHO – Menuesteuerung Zeit aktivieren
Windshield wiper-Regensensor aktivieren – activated
Rear Window Wiper-Komfortwischen Heck – active
Rear Window Wiper-Menuesteuerung Komfortwischen HW – active
→ 应用
```

支持通过前雾灯实现 Coming Home/Leaving Home 功能的 Corner
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB40-Light_Function_B_12 — 原为 Abbiegelicht links, 改为 nicht aktive – 保存
Leuchte13NL RB3-Light_Function_B_13 — 原为 Abbiegelicht rechts, 改为 nicht aktive – 保存
Leuchte12NL LB40-Light_Function_C_12 – Abbiegelicht links
Leuchte12NL LB40-Dimming_CD_12 – 100
Leuchte13NL RB3-Light_Function_C_13 – Abbiegelicht rechts
Leuchte13NL RB3-Dimming_CD_13 – 100
→ 应用
```

19 款：
``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 0 – 字节 1-2 – 选择 185E (984D)
或填入现成编码: 00185Е (00984D)
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
辅助照明功能-Rain/light sensor → Rain/light sensor
辅助照明功能-Humidity sensor → 已安装
辅助照明功能-Will Beam assistant: responsivity adjustable via BAP → 有
Aussenlicht_uebergreifend-Light rotary sw. with AFL → 是
Windshield wiper-rain_sensor_function → 已安装
辅助照明功能-Assistenzfahrlicht bei Regen – 激活
辅助照明功能-AFL Zeitverzoegerung – 0 ms
辅助照明功能-Lichtsensorempfindlichkeit – 正常
Aussenlicht_uebergreifend-Coming Home Verbaustatus – 自动
Aussenlicht_uebergreifend-Menuesteuerung Coming Home Werkseinstellung – 激活
Aussenlicht_uebergreifend-Menueeinstellung Cominghome – 10 s
Aussenlicht_uebergreifend-Coming Home Leuchten – 近光
Aussenlicht_uebergreifend-Coming-home Einschaltereignis – Driver door
Aussenlicht_uebergreifend-Helligkeitsschwelle Infrarot-Messung – 72.0
Aussenlicht_uebergreifend-Leaving-Home Verbausstatus – 允许
Aussenlicht_uebergreifend-lho_aktiviert – 激活
Aussenlicht_uebergreifend-lho_zeit – 10 s
Aussenlicht_uebergreifend-Helligkeitsschwelle Forward-Messung – 100
Aussenlicht_uebergreifend-Menueeinstellung CHO LHO – Menuesteuerung Zeit aktivieren
Aussenlicht_uebergreifend-Lichtdrehschalter_mit_Nebellicht_bei_Assistenzfahrlicht – 是
Windshield wiper — Regensensor aktivieren – 激活
→ 应用
```

### [PR-8X0] 把原厂卤素大灯更换为原厂氙气大灯
``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 06 – 位 5-6 – 把 00 改为 20
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte6ABL LB44 – Type_Of_Load_6 – 选择 Xenon Abblendlicht
Leuchte7ABL RB5 – Type_Of_Load_7 – 选择 Xenon Abblendlicht
→ 应用 
```

### [PR-PXE] 安装双氙气
``` yaml title="登录密码: 31347"
单元 09 → 编码:
Lower_beam_lamp_typ – GDL
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte 0 BLK VL B35 — 即左前转向灯:
- Dimming_AB_0 — 128
- Light_Function_A_0 — Blinken links Hellphase
- Type_Of_Load_0 — LED Blinkleuchten
Leuchte 1 BLK VR B23 — 即右前转向灯:
- Dimming_AB_1 — 128
- Light_Function_A_1 — Blinken rechts Hellphase
- Type_Of_Load_1 — LED Blinkleuchten
Leuchte2SL VL B22 — 即左前示廓灯:
- Dimming_AB_2 — 100
- Dimming_CD_2 — 30
- Dimming_Direction_CD_2 — maximize
- Dimming_Direction_EF_2 — minimize
- Dimming_EF_2 — 28
- Light_Function_A_2 — Daytime running lights
- Light_Function_C_2 — Parking light
- Light_Function_D_2 — Parking light left
- Light_Function_E_2 — Blinken links Hellphase
- Type_Of_Load_2 — LED Tagfahrlichtmodul Signal
Leuchte3SL VR B36 — 即右前示廓灯:
- Dimming_AB_3 — 100
- Dimming_CD_3 — 30
- Dimming_Direction_CD_3 — maximize
- Dimming_Direction_EF_3 — minimize
- Dimming_EF_3 — 28
- Light_Function_A_3 — Daytime running lights
- Light_Function_C_3 — Parking light
- Light_Function_D_3 — Parking light right
- Light_Function_E_3 — Blinken rechts Hellphase
- Type_Of_Load_3 — LED Tagfahrlichtmodul Signal
Leuchte4TFL LB43 — 即左 DRL:
- Dimming_AB_4 — 127
- Dimming_CD_4 — 127
- Dimming_Direction_CD_4 — maximize
- Dimming_Direction_EF_4 — minimize
- Dimming_EF_4 — 0
- Light_Function_A_4 — Daytime running lights
- Light_Function_C_4 — Parking light
- Light_Function_D_4 — Parking light left
- Light_Function_E_4 — Blinken links aktiv
- Type_Of_Load_4 — LED Tagfahrlichtmodul Versorgung
Leuchte5 TFL RB6— 即右 DRL:
- Dimming_AB_5 — 127
- Dimming_CD_5 — 127
- Dimming_Direction_CD_5 — maximize
- Dimming_Direction_EF_5 — minimize
- Dimming_EF_5 — 0
- Light_Function_A_5 — Daytime running lights
- Light_Function_C_5 — Parking light
- Light_Function_D_5 — Parking light right
- Light_Function_E_5 — Blinken rechts aktiv
- Type_Of_Load_5 — LED Tagfahrlichtmodul Versorgung
Leuchte6ABL LB44 — 即左近光:
- Dimming_AB_6 — 100
- Dimming_CD_6 — 100
- Dimming_Direction_CD_6 — maximize
- Light_Function_A_6 — Abblendlicht links
- Light_Function_B_6 — ComingHome LeavingHome
- Light_Function_C_6 — Left high beam
- Light_Function_D_6 — Headlamp flasher
- Type_Of_Load_6 — Xenon Abblendlicht
Leuchte7ABL RB5 — 即右近光:
- Dimming_AB_7 — 100
- Dimming_CD_7 — 100
- Dimming_Direction_CD_7 — maximize
- Light_Function_A_7 — Abblendlicht rechts
- Light_Function_B_7 — ComingHome LeavingHome
- Light_Function_C_7 — Right high beam
- Light_Function_D_7 — Headlamp flasher
- Type_Of_Load_7 — Xenon Abblendlicht
Leuchte8FL LB42 — 即左远光:
- Dimming_AB_8 — 100
- Light_Function_A_8 — Left high beam
- Light_Function_B_8 — Headlamp flasher
- Type_Of_Load_8 — Shutter
Leuchte9FL RB7 — 即右远光:
- Dimming_AB_9 — 100
- Light_Function_A_9 — Right high beam
- Light_Function_B_9 — Headlamp flasher
- Type_Of_Load_9 — Shutter
→ 应用 
```

19 款：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Front-Low beam: bulb type → HID
Leuchte 0 BLK VL B35-Dimming_AB_0 → 127
Leuchte 0 BLK VL B35-Light_Function_A_0 → Blinken links Hellphase
Leuchte 0 BLK VL B35-Type_Of_Load_0 → LED Blinkleuchten
Leuchte1BLK VRB23-Dimming_AB_1 → 127
Leuchte1BLK VRB23-Light_Function_A_1 → Blinken rechts Hellphase
Leuchte1BLK VRB23-Type_Of_Load_1 → LED Blinkleuchten
Leuchte2SL VLB22-Dimming_AB_2 → 100
Leuchte2SL VLB22-Dimming_CD_2 → 30
Leuchte2SL VLB22-Dimming_Direction_CD_2 → maximize
Leuchte2SL VLB22-Dimming_Direction_EF_2 → minimize
Leuchte2SL VLB22-Dimming_EF_2 → 0
Leuchte2SL VLB22-Light_Function_A_2 → Daytime running lights
Leuchte2SL VLB22-Light_Function_B_2 → not active
Leuchte2SL VLB22-Light_Function_C_2 → Parking light
Leuchte2SL VLB22-Light_Function_D_2 → Parking light left
Leuchte2SL VLB22-Light_Function_E_2 → Blinken links aktiv
Leuchte2SL VLB22-Light_Function_F_2 → not active
Leuchte2SL VLB22-Light_Function_G_2 → not active
Leuchte2SL VLB22-Light_Function_H_2 → not active
Leuchte2SL VLB22-Type_Of_Load_2 → LED Tagfahrlichtmodul Signal
Leuchte3SL VRB36-Dimming_AB_3, 100
Leuchte3SL VRB36-Dimming_CD_3, 30
Leuchte3SL VRB36-Dimming_Direction_CD_3 → maximize
Leuchte3SL VRB36-Dimming_Direction_EF_3 → minimize
Leuchte3SL VRB36-Dimming_EF_3 → 0
Leuchte3SL VRB36-Light_Function_A_3 → Daytime running lights
Leuchte3SL VRB36-Light_Function_B_3 → not active
Leuchte3SL VRB36-Light_Function_C_3 → Parking light
Leuchte3SL VRB36-Light_Function_D_3 → Parking light right
Leuchte3SL VRB36-Light_Function_E_3 → Blinken rechts aktiv
Leuchte3SL VRB36-Light_Function_F_3 → not active
Leuchte3SL VRB36-Light_Function_G_3 → not active
Leuchte3SL VRB36-Light_Function_H_3 → not active
Leuchte3SL VRB36-Type_Of_Load_3 → LED Tagfahrlichtmodul Signal
Leuchte4TFL LB43-Dimming_AB_4 → 127
Leuchte4TFL LB43-Dimming_CD_4 → 127
Leuchte4TFL LB43-Dimming_Direction_CD_4 → maximize
Leuchte4TFL LB43-Dimming_Direction_EF_4 → minimize
Leuchte4TFL LB43-Dimming_EF_4 → 0
Leuchte4TFL LB43-Light_Function_A_4 → Daytime running lights
Leuchte4TFL LB43-Light_Function_C_4 → Parking light
Leuchte4TFL LB43-Light_Function_D_4 → Parking light left
Leuchte4TFL LB43-Light_Function_E_4 → Blinken links aktiv
Leuchte4TFL LB43-Type_Of_Load_4 → LED Tagfahrlichtmodul Versorgung
Leuchte5 TFL RB6-Dimming_AB_5 → 127
Leuchte5 TFL RB6-Dimming_CD_5 → 127
Leuchte5 TFL RB6-Dimming_Direction_CD_5 → maximize
Leuchte5 TFL RB6-Dimming_Direction_EF_5 → minimize
Leuchte5 TFL RB6-Dimming_EF_5 → 0
Leuchte5 TFL RB6-Light_Function_A_5 → Daytime running lights
Leuchte5 TFL RB6-Light_Function_C_5 → Parking light
Leuchte5 TFL RB6-Light_Function_D_5 → Parking light right
Leuchte5 TFL RB6-Light_Function_E_5 → Blinken rechts aktiv
Leuchte5 TFL RB6-Type_Of_Load_5 → LED Tagfahrlichtmodul Versorgung
Leuchte6ABL LB44-Dimming_AB_6 → 100
Leuchte6ABL LB44-Dimming_CD_6 → 100
Leuchte6ABL LB44-Dimming_Direction_CD_6 → maximize
Leuchte6ABL LB44-Light_Function_A_6 → Abblendlicht links
Leuchte6ABL LB44-Light_Function_B_6 → ComingHome LeavingHome
Leuchte6ABL LB44-Light_Function_C_6 → Left high beam
Leuchte6ABL LB44-Light_Function_D_6 → Headlamp flasher
Leuchte6ABL LB44-Type_Of_Load_6 → Xenon Abblendlicht
Leuchte7ABL RB5-Dimming_AB_7 → 100
Leuchte7ABL RB5-Dimming_CD_7 → 100
Leuchte7ABL RB5-Dimming_Direction_CD_7 → maximize
Leuchte7ABL RB5-Light_Function_A_7 → Abblendlicht rechts
Leuchte7ABL RB5-Light_Function_B_7 → ComingHome LeavingHome
Leuchte7ABL RB5-Light_Function_C_7 → Right high beam
Leuchte7ABL RB5-Light_Function_D_7 → Headlamp flasher
Leuchte7ABL RB5-Type_Of_Load_7 → Xenon Abblendlicht
Leuchte8FL LB42-Dimming_AB_8 → 127
Leuchte8FL LB42-Light_Function_A_8 → Left high beam
Leuchte8FL LB42-Light_Function_B_8 → Headlamp flasher
Leuchte8FL LB42-Type_Of_Load_8 → Shutter (Camera lock)
Leuchte9FL RB7-Dimming_AB_9 → 127
Leuchte9FL RB7-Light_Function_A_9 → Right high beam
Leuchte9FL RB7-Light_Function_B_9 → Headlamp flasher
Leuchte9FL RB7-Type_Of_Load_9 → Shutter (Camera lock)
→ 应用 
```

### 把尾灯更换为 LED
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte23SL HLC7 – Type_Of_Load_23 → Allgemeine LED mit Open Load Diagnose 
Leuchte23SL HLC7 – Dimming_AB_23 → 100
Leuchte24SL HRA69 – Type_Of_Load_24 → Allgemeine LED mit Open Load Diagnose 
Leuchte24SL HRA69 – Dimming_AB_24 → 100
```

### 更换蓄电池
!!! tip "蓄电池规格选项"
    61Ah 300A(DIN) 或 540(EN)  
    70Ah 340А(DIN) 或 570(EN)  
    80Ah 380А(DIN) 或 640(EN)  
    92Ah 520А(DIN) 或 870(EN)  
    95Ah 450А(DIN) 或 750(EN)  
    110Ah 520А(DIN) 或 870(EN)  
``` yaml
单元 19 → 适配:
Battery Adaption – Battery capacity – 填入所需值
Battery Adaption – Battery serial number – 值加 1。
→ 应用（需重启单元）
```

### [PR-QQ8] 车内 LED 背景氛围照明
通过一条空闲电路实现，接到 T46b/45 输出。  
针脚编号 — А 018 545 8626  
中控台储物格照明灯 - 7P6 919 390 A KT1  
接插件外壳 - 8K0 973 754  
接插件针脚 – N907 647 01  
脚部照明灯 - 8J0947409А  
脚部照明灯接插件 - 4B0 971 832  

``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 17 – 位 0: 激活
字节 17 – 位 4: 激活
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte10SHUTTER LRB45 – Dimming_AB_10 – 100
Leuchte10SHUTTER LRB45 – Fehlerort_mittleres_Byte_DTC-DFCC_10 – 03
Leuchte10SHUTTER LRB45 – Light_Function_A_10 – Ambientelicht 1
Leuchte10SHUTTER LRB45 – Type_Of_Load_10 – LED Kleinleistung ohne Open Load Diagnose.
→ 应用 
```
默认亮度在以下通道中设定：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambient lighting – Defaultwert Ambienteprofil Vorn – 80%
→ 应用 
```

### [PR-8T6] 限速器
在定速巡航 [PR-8T2] 激活时可实现。  
2016 款所需方向盘拨杆零件号 - 6C0953513FIGI  
2017 款 - 6C6953513DIGI  
支持 [PR-8T6] 功能的踏板零件号 — 6C1723503B。  

``` yaml
单元 01 → 编码:
字节 6 – 位 2: 激活
→ 应用 
```
``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 18 – 位 7: 激活
→ 应用 
```

### [PR-KA1] 连接倒车影像摄像头
倒车影像摄像头 5JA827566。可装于 Swing (5JA035871D)、Bolero (5Q0035840B)。  
按以下接线图连接摄像头：  
T4/1pin — +12V;  
T4/2pin — 地;  
T4/3pin — 未使用;  
T4/4pin — 接倒挡开启信号（蓝黑色线）。  
视频电缆接到车机的 CVBS+ 和 CVBS- 接插件。  

``` yaml
单元 5F → 编码:
字节 19 – 位 4: 开启
→ 应用 
```
若有泊车雷达单元
``` yaml
单元 10 → 编码:
字节 02 – 位 0: 开启
字节 02 – 位 4: 开启
→ 应用 
```

### [PR-XXX +4LB, 4LC] 多功能方向盘
4LB 用于车机的控制元件  
4LC 用于车机和电话的控制元件  
方向盘选项（供参考）：  
565064241B CXA. 多功能方向盘（真皮）黑/黑。  

``` yaml
单元 19 → 编码:
字节 1 – 位 0: 激活
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 20 – 位 1: 激活
→ 应用 
```
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Car_Function_List_CAN_Gen2 – MFL — available
Car_Function_List_BAP_Gen2 – MFA_0x0F — activated
→ 应用
```

### [PR-6E7] 在中央扶手安装 USB 插座
1. USB 插座。编号: 5Q0 035 726L  
2. 插座面板: 5JA 863 618 9B9  
3. 扶手左护盖: 5JA 864 279 B 9B9  
4. 扶手右护盖: 5JA 864 280 B 9B9  
5. 接插件: 8K0 973 754B  
6. 接插件针脚: N 907 647 01 – 2 个  
7. 导线约 3 米。  
在保险丝盒附近连接。  
负极 – 接螺栓。正极 – 接空闲保险丝（可接常通的，也可接点火开启时通电的）。

### 自行加装后激活车内氛围照明（19 款）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
氛围照明-Ambience_borders_front → 已安装
Leuchte32AMBL 2C64-Dimming_AB_32 → 100
Leuchte32AMBL 2C64-Fehlerort_mittleres_Byte_DTC-DFCC_32 → 03
Leuchte32AMBL 2C64-Light_Control_HD_AB_32 → Always
Leuchte32AMBL 2C64-Light_Function_A_32 → Ambientelicht 1
Leuchte32AMBL 2C64-Type_Of_Load_32 → LED Kleinleistung ohne Open Load Diagnose
→ 应用 
```

### [PR-8G1] 远光辅助 FLA 

2017 款之前（需核实！）
``` yaml
单元 19 → 设备列表:
0 (远光控制辅助): 激活
→ 应用（需重启单元）
```
``` yaml title="登录密码: 31347"
单元 09 → 编码:
字节 02 – 位 0~2 – 01, 照明: 带远光辅助的卤素大灯 [PR-8ID+8G1] 
→ 应用 
```
``` yaml
单元 20 (8X0-857-511.lbl) → 编码:
字节 00 – 位 0-4 – 01 大灯类型: 卤素 02 大灯类型: 双氙气 
字节 01 – 位 0-1 – 01 驾驶方向: 左舵 
字节 02 – 位 0-7 – 8f 垂直偏移 Škoda Octavia (5E) 
字节 03 – 位 0-7 – 6b 校正（红色）双氙气 Škoda Octavia (5E) 
字节 04 – 位 0-7 – 76 校正（红色）卤素 Škoda Octavia (5E) 
字节 05 – 位 0-7 – 76 校正（红色）尾灯 Škoda Octavia (5E) 
字节 06 – 位 0-7 – 5D 校正（蓝色）双氙气 Škoda Octavia (5E) 
字节 07 – 位 0-7 – 52 校正（蓝色）卤素 Škoda Octavia (5E) 
字节 08 – 位 0-7 – 52 校正（红色）尾灯 Škoda Octavia (5E)
字节 09 – 位 0-7 – 20 校正 (UCR) 双氙气 Škoda Octavia (5E)
字节 10 – 位 0-7 – 34 校正 (UCR) 卤素 Škoda Octavia (5E)
字节 11 – 位 0-7 – 3E 校正 (UCR) 尾灯 Škoda Octavia (5E) 
字节 12 – 位 0-7 – 00 Function Switch Memory Off 
→ 应用 
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Assistance light functions – Menuesteuerung Fernlichtassistent, adjustable 
Assistance light functions – Menuesteuerung Fernlichtassistent Werkseinstellung, adjustable 
→ 应用 
```

19 款：
``` yaml
单元 19 → 设备列表:
0 (远光控制辅助): 激活
→ 应用（需重启单元）
```
``` yaml
单元 20 → 编码:
字节 0 – 值 01 或 02（卤素/氙气）
字节 1 – 值 01 或 02（卤素/氙气）
字节 3 – 值 0F
→ 应用 
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Fernlicht_assistent-Expanded high beam control, 把 Halogen 改为 Halogen, FLA
Fernlicht_assistent-Fernlichtassistent_Reset: 激活
Fernlicht_assistent-Menuesteuerung_Fernlichtassistent: 已安装
Fernlicht_assistent-Menuesteuerung_Fernlichtassistent_Werkseinstellung: 已安装
```
