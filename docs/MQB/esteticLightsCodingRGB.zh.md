
# RGB 氛围灯的安装与设置

本材料是以下资源的副本：https://www.drive2.ru/l/553166225153198981/  

!!! info "RGB 氛围灯包含哪些内容"
    1. 车门饰条变色照明  
    2. 脚部变色照明  
    3. 中控台凹槽变色照明  
    4. 车内顶灯的单色背景照明  
    5. 通过车机原厂菜单调节颜色和亮度  
    6. 颜色配置与驾驶模式绑定  
    7. 颜色与驾驶员（或钥匙）绑定  
    8. 车门口袋照明（灯罩编号 8W0919390A, B, C, D）  

### 文件与说明链接
+ [ODIS_E 09 单元的驾驶模式绑定（适配）](../odis-files/09 – LIN RGB.PRE)

### 对车辆配置的要求：

1. 车载电气网络单元 BCM 版本 High 5Q0937084CG/CQ/DD/DH。  
High 版本在俄罗斯仅装于带全景天窗照明的车辆，或带原厂彩色照明的 Scoda Octavia。  
在任何其他配置上都**必须**更换 BCM。版本 5Q0937084CF/CP/DC 不支持多色照明。  
此外，整套方案无法在任何 5Q0937086 BCM（Passat B8、Kodiaq）上实现，该 BCM 上多色脚部照明无法工作。  
  
2. 车门饰板单色照明，如果没有，则需更换车门饰板（后门不必装车门模块）  
![Screenshot](../images/MQB/RGB/doors_parts.jpg)

3. 要实现颜色与驾驶模式绑定的功能，重要的是确认网关 (J533 或 19 单元) 软件版本不低于 4344 或 5344，且索引为 Q 及以上，否则需要找会刷写并加载参数集的人

## 原理

1. 车内所有彩色 LED 都由 LIN 总线控制，因此每个 LED 接 3 根线 +、-、Lin 总线  
2. BCM 中的 LIN RGB – 接口 С 的引脚 29  
3. 氛围灯顶灯同样由 LIN 控制  
4. BCM 中顶灯的 LIN – 接口 А 的引脚 15  
5. 有若干个氛围灯通道可从车机调节：车门、脚部、前面板、中控台、顶灯、全景天窗照明。  

每台 MQB 平台车都有自己的特点，某些通道的调节可能不存在：  

+ Tiguan 全都支持  
+ Golf 不支持显示和调节顶灯  
+ Octavia 不支持显示和调节中控台

![Screenshot](../images/MQB/RGB/esteticRGB.PNG)
  
### 接线图

![Screenshot](../images/MQB/RGB/scheme_rgb.jpg)

J519 – BCM  
L2** — LED  
SC8 – 保险丝  

### 工具

1. 拆内饰用的撬板套装  
2. 带 4.5-5 mm 金属钻头的电钻  
3. Dremel 或用于在中控台凹槽开孔的工具  
4. 端子压接钳  
5. 用于处理待装 LED 的锋利刀具  

### 配件

为在车门、脚部、中控台安装 RGB LED 所需布线的配件：  
![Screenshot](../images/MQB/RGB/zap1.jpg)
![Screenshot](../images/MQB/RGB/zap2.jpg)
![Screenshot](../images/MQB/RGB/zap3.jpg)
![Screenshot](../images/MQB/RGB/zap4.jpg)
![Screenshot](../images/MQB/RGB/zap5.jpg)

接下来视需要而定，不用这些也可以。这些元件用于在车门与饰板之间（前门）做线束「断点」，这是由门内布线逻辑决定的 —— 部分布线走饰板、部分走车门，有接插件后需要时拆装更方便。  
![Screenshot](../images/MQB/RGB/zap6.jpg)

顶灯  
![Screenshot](../images/MQB/RGB/zap7.jpg)
带全景天窗车辆的顶灯：  
前灯 — 3G0947105E  
后 1 — 3G9947292A  
后 2 — 3G9947291A  

## 铺设所有必要的线束

1. 如果你车的配置在保险丝盒中没有第 8 号保险丝 (SC8)，则需安装它，RGB 照明的所有供电都汇到这个保险丝。  
2. 拆下蓄电池端子。  
3. 拆下车门饰板、车内门槛内饰、车内门柱下部，为方便起见拆下前排座椅。  

#### 车门  
1. 钻开扬声器（钻掉铆钉），断开车门接插件并拆下车门线束。注意 —— 拆原厂胶带时，记下所有密封条的出厂安装尺寸、胶带缠绕长度等。如果之后装配时出错，可能下个冬天就要修柔性连接处的线束。  
2. 在车门线束中编入 3 根线：2 根 0.35 mm，1 根 0.5 mm。  
3. 从车门接插件一侧用相应端子压接（车门接插件用 12527545852）。  
4. 把线拉到饰板上 LED 的安装位置，前门要在车门与饰板之间预留布线断点（所需配件清单见上文）。  
5. 用 N90764701 端子压接新的 LED 接插件：LED 接插件针脚分配和线径：1 — 正极 0.5 mm，2 – LIN 0.35 mm，4 — 地 0.35 mm。  
6. 先全部通断检测、检查压接质量，再装回原位，铆好扬声器。  
7. 把 3 根线压接到位于门柱上的接插件中，LIN 总线线拉到 BCM，「正极」供电拉到先前装好的保险丝，地用环形端子压接并固定到最近的接地螺栓，端子 12527512135。  
8. 内饰先不装，转去铺设脚部 RGB 照明布线。  
![Screenshot](../images/MQB/RGB/doors.jpg)
  
#### 座椅  
1. 断开座椅红色接插件、安全气囊接插件，并拆开座椅一侧的接插件。  
2. 沿原厂布线从座椅接插件到 LED 安装位置铺设三根线 2 根 0.35 mm，1 根 0.5 mm。  
3. 用 N90764701 端子压接 LED 接插件：LED 接插件针脚分配和线径：1 — 正极 0.5 mm，2 – LIN 0.35 mm，4 — 地 0.35 mm。  
4. 用为座椅接插件购买的端子压接线的另一端。  
5. 从卡扣上取下座椅接插件的对接部分，并在其中用相应端子压接 3 根线 — 2 根 0.35 mm，1 根 0.5 mm，"正极"线拉到先前装好的保险丝，LIN – 到 BCM，地用环形端子压接并拧到最近的接地螺栓。  
6. 把支架 4M08815479B9 安装到座椅下方的弹簧上，并在其中装入脚部照明灯。  
7. 按相反顺序装回所有部件。  
![Screenshot](../images/MQB/RGB/seats.jpg)
  
#### 中控台  
1. 拆下空调饰板。  
2. 拆下空调面板。  
3. 拆下通道侧板。  
4. 把 2 根 0.35 mm、1 根 0.5 mm 的线打成束。  
5. 压接 LED 接插件。  
6. 把"正极"线拉到装好的保险丝，LIN – 到 BCM，地用环形端子压接并固定到最近的接地螺栓，或取一颗带螺母的螺栓拧到中控台金属加强件上，那里接地良好。  
7. 转去把这一切接入 BCM。  
![Screenshot](../images/MQB/RGB/console.jpg)
  
#### 前部脚部照明灯  
1. 把 2 根 0.35 mm、1 根 0.5 mm 的线打成束。  
2. 压接 LED 接插件。  
3. 把"正极"线拉到装好的保险丝，LIN – 到 BCM，地用环形端子压接并固定到最近的接地螺栓。  
4. 如果出厂没有原厂灯具支架，则购买并装到位。  
5. 把驾驶员脚部灯罩装到油门踏板上方的原厂位置，接好接插件。  
6. 把乘客脚部灯罩装到乘客右脚上方的原厂位置。  

### 在 BCM 中连接 LIN 总线

1. 从 BCM 上取下接插件（离我们最近的接插件），扳开白色卡箍同时按下锁扣，可能要费点劲，位置不好操作。  
2. 剪断固定外壳的扎带。  
3. 压开卡爪并取出接插件的 2 个内部部分。  
4. 按引脚 29 找到插孔。  
5. 用 N90764701 端子压接所需长度的线。  
6. 把压接好的线插入引脚 29 的插孔。  
7. 把线打成束并按「星形」方式将其与之前拉好的所有 LIN 线（4 根来自车门、4 根来自座椅、1 根来自中控台）连接，VAG 有专用连接器，但我没那么讲究，把所有线拧在一起并用套管压接。  
8. 全部绝缘并归位。  
9. 按相反顺序装回所有部件，这时就用得上扎带了。  
10. LIN 已拉好。  
![Screenshot](../images/MQB/RGB/lin.jpg)

### 连接到保险丝

类似前面的 LIN 连接，把所有"正极"线汇到一起，连接到之前装好的、由保险丝供电的线上。

### 在车门安装 LED

1. 按原厂单色灯样机械改造 LED，Passat 和 Tiguan 的 LED 安装位形状和尺寸不一致，前后 LED 卡扣不同，装 LED 时要注意这点。  
2. 把它们装到照明条的原厂位置。  
3. 固定排线，使装饰板时不被损坏。  
4. 把车门饰板装回原位。  

### 在中控台安装 LED

1. 最好按 ELSA 说明完全拆下中控台
2. 用 Dremel 锯出导光体的窗口
3. 制作导光体
4. 把导光体插入中控台并固定
5. 把 LED 套到导光体上并接好接插件
6. 带氛围照明的顶灯布线

### 在顶部安装氛围灯罩

1. 用撬板撬起玻璃部分并从接插件上断开。  
2. 把撬板插入灯罩本身的卡槽并取出带灯泡的部分。  
3. 撬起并取下 Glonass 按键盖板。  
4. 拧下四周 4 颗 Torx 自攻螺丝。  
5. 取下灯罩前盖以及通往后视镜的钟形盖板。  
6. 断开接插件并取下框架。  
7. 重新压接接插件（使用 N90764701 端子）：  
![Screenshot](../images/MQB/RGB/plafon_pin.jpg)

## 编码

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior_light_lamp_configuration:
- Ambiente_Applikationsleisten_in_Tuertafel: установл. (车门饰条)
- Ambiente_Lautsprecher: не установл.
- Ambiente_Applikationsleisten_in_Instrumententafel: не установл.
- Cockpitbeleuchtung: не установл.
- Mittelkonsolenbeleuchtung: установл. (中控台灯)
- Dachbeleuchtung: установл. (顶灯 Ambient+)
- Panoramaschiebedachbeleuchtung: не установл.
- Fussraumbeleuchtung: установл. (脚部照明)
- LIN-Dachkonsole lokal aktivierbar: акт. (激活顶灯的 LIN 控制)
- Ambientemenue mit globalem aus: акт. (氛围灯总体调节)
- Ambientemenue mit alle Zonen: акт. (分区单独调节)
- Ambient_Farbliste_HMI: акт. (激活颜色选择色阶显示)
- Ambience_light_colorlist_default: 1
→ 应用
```

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior_light_2nd_generation:
- Aufloesung Dimmzeit: 0.8
- weicher Farbwechsel: акт.
- Tuertafelbeleuchtung mehrfarbig: акт. (车门饰条彩色)
- Instrumententafelbeleuchtung mehrfarbig: не акт.
- Cockpitbeleuchtung mehrfarbig: не акт.
- Lautsprecherbeleuchtung mehrfarbig: не акт.
- Mittelkonsolenbeleuchtung mehrfarbig: акт. (中控台 LED 彩色)
- Dachbeleuchtung mehrfarbig: не акт. (顶灯单色)
- Panoramaschiebedachbeleuchtung mehrfarbig: не акт.
- Panoramaschiebedachbeleuchtung bei geoeffnetem Rollo deaktivieren: не акт.
- BAP Farbwert Farbe 1: 1
- BAP Farbwert Farbe 2: 4
- BAP Farbwert Farbe 3: 5
- Defaultwert Ambienteprofil Mittelkonsole: 80 (灯罩默认亮度)
- Defaultwert Ambienteprofil Dach: 80 (灯罩默认亮度)
- Defaultwert Ambienteprofil Farbe: 8
- Defaultwert Ambienteprofil Fussraum: 80 (灯罩默认亮度)
- Defaultwert Ambienteprofil Tuer: 80 (灯罩默认亮度)
- Ambiente_Farbliste_HMI_mit_Farbtransformation: акт. (启用屏幕与 LED 颜色分别指定, 以匹配屏幕色与 LED 可显示色)
- Helligkeit_Tuertafelbeleuchtung_nicht_berechnen: не акт. (关闭禁止调节)
- Helligkeit Instrumententafelbeleuchtung nicht berechnen: акт.
- Helligkeit Cockpitbeleuchtung nicht berechnen: акт.
- Helligkeit Lautsprecherbeleuchtung nicht berechnen: акт.
- Helligkeit Mittelkonsolenbeleuchtung nicht berechnen: не акт. (关闭禁止调节)
- Helligkeit Dachbeleuchtung nicht berechnen: не акт. (关闭禁止调节)
- Helligkeit Panoramaschiebedachbeleuchtung nicht berechnen: акт.
- Farbausgabe Tuertafelbeleuchtung nicht berechnen: не акт. (关闭禁止调节)
- Farbausgabe Instrumententafelbeleuchtung nicht berechnen: акт.
- Farbausgabe Cockpitbeleuchtung nicht berechnen: акт.
- Farbausgabe Lautsprecherbeleuchtung nicht berechnen: акт.
- Farbausgabe Mittelkonsolenbeleuchtung nicht berechnen: не акт.(关闭禁止调节)
- Farbausgabe Dachbeleuchtung nicht berechnen: не акт.(关闭禁止调节)
- Farbausgabe Panoramaschiebedachbeleuchtung nicht berechnen: акт.
- LIN-Dachkonsole mit Flaechenlicht: установл. (顶灯背景照明)
- Ambiente_Farbwahl_FPA_waehlbare_Kopplung: акт. (驾驶模式绑定)
- Ambiente_Fahrprofil_Individual: 1
- Ambiente_Farbwahl_FPA_waehlbare_Kopplung_Status_hmi_default: сопряжены (驾驶模式绑定)
→ 应用
```

通道的亮度与调节平滑度
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior_light_parameter:
- p_adaption_kundenwunsch_tuer: 0.67 (调节线性度)
- p_helligkeit_entriegelt_tueren: 100
- p_helligkeit_max_tueren: 100
- p_helligkeit_HD_auf_zuendung_ein_tueren: 126
- p_helligkeit_HD_auf_zuendung_aus_tueren: 127
- p_helligkeit_dieseTuer_auf_zuendung_ein_tueren: 100
- p_helligkeit_andereTuer_auf_zuendung_ein_tueren: 100
- p_helligkeit_Fzg_geschlossen_zuendung_ein_tueren: 126
- p_helligkeit_dieseTuer_auf_zuendung_aus_tueren: 100
- p_helligkeit_andereTuer_auf_zuendung_aus_tueren: 100
- p_helligkeit_einausstieg_tueren: 100
- p_helligkeit_Fzg_geschlossen_zuendung_aus_tueren: 127
- p_helligkeit_Tueren_geschlossen_HD_auf_zuendung_aus_tueren: 100
- p_helligkeit_Tueren_geschlossen_HD_zu_zuendung_aus_tueren: 100
- p_helligkeit_Tueren_geschlossen_schluessel_ab_tueren: 100
- p_helligkeit_Fzg_geschlossen_schluessel_ab_tueren: 100

- p_adaption_kundenwunsch_fussraum: 0.67
- p_helligkeit_entriegelt_fussraum: 100
- p_helligkeit_max_fussraum: 100
- p_helligkeit_HD_auf_zuendung_ein_fussraum: 126
- p_helligkeit_HD_auf_zuendung_aus_fussraum: 127
- p_helligkeit_dieseTuer_auf_zuendung_ein_fussraum: 100
- p_helligkeit_andereTuer_auf_zuendung_ein_fussraum: 100
- p_helligkeit_Fzg_geschlossen_zuendung_ein_fussraum: 126
- p_helligkeit_dieseTuer_auf_zuendung_aus_fussraum: 100
- p_helligkeit_andereTuer_auf_zuendung_aus_fussraum: 100
- p_helligkeit_einausstieg_fussraum: 100
- p_helligkeit_Fzg_geschlossen_zuendung_aus_fussraum: 127
- p_helligkeit_Tueren_geschlossen_HD_auf_zuendung_aus_fussraum: 100
- p_helligkeit_Tueren_geschlossen_HD_zu_zuendung_aus_fussraum: 100
- p_helligkeit_Tueren_geschlossen_schluessel_ab_fussraum: 100
- p_helligkeit_Fzg_geschlossen_schluessel_ab_fussraum: 100

- p_adaption_kundenwunsch_miko: 0.67
- p_helligkeit_entriegelt_miko: 100
- p_helligkeit_max_miko: 100
- p_helligkeit_HD_auf_zuendung_ein_miko: 126
- p_helligkeit_HD_auf_zuendung_aus_miko: 127
- p_helligkeit_dieseTuer_auf_zuendung_ein_miko: 100
- p_helligkeit_andereTuer_auf_zuendung_ein_miko: 100
- p_helligkeit_Fzg_geschlossen_zuendung_ein_miko: 126
- p_helligkeit_dieseTuer_auf_zuendung_aus_miko: 100
- p_helligkeit_andereTuer_auf_zuendung_aus_miko: 100
- p_helligkeit_einausstieg_miko: 100
- p_helligkeit_Fzg_geschlossen_zuendung_aus_miko: 100
- p_helligkeit_Tueren_geschlossen_HD_auf_zuendung_aus_miko: 100
- p_helligkeit_Tueren_geschlossen_HD_zu_zuendung_aus_miko: 100
- p_helligkeit_Tueren_geschlossen_schluessel_ab_miko: 100
- p_helligkeit_Fzg_geschlossen_schluessel_ab_miko: 100

- p_adaption_kundenwunsch_dach: 1
- p_helligkeit_entriegelt_dach: 100
- p_helligkeit_max_dach: 100
- p_helligkeit_HD_auf_zuendung_ein_dach: 100
- p_helligkeit_HD_auf_zuendung_aus_dach: 100
- p_helligkeit_dieseTuer_auf_zuendung_ein_dach: 100
- p_helligkeit_andereTuer_auf_zuendung_ein_dach: 100
- p_helligkeit_Fzg_geschlossen_zuendung_ein_dach: 126
- p_helligkeit_dieseTuer_auf_zuendung_aus_dach: 100
- p_helligkeit_andereTuer_auf_zuendung_aus_dach: 100
- p_helligkeit_einausstieg_dach: 100
- p_helligkeit_Fzg_geschlossen_zuendung_aus_dach: 100
- p_helligkeit_Tueren_geschlossen_HD_auf_zuendung_aus_dach: 100
- p_helligkeit_Tueren_geschlossen_HD_zu_zuendung_aus_dach: 100
- p_helligkeit_Tueren_geschlossen_schluessel_ab_dach: 100
- p_helligkeit_Fzg_geschlossen_schluessel_ab_dach: 100
→ 应用
```

在车机屏幕上显示小太阳和图形
``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_ambienteumfang_mehrfarbig_HMI: 100
- p_ambienteumfang_mehrfarbig_HMI_2: 100
- p_ambienteumfang_mehrfarbig_HMI_3: 0
- p_ambienteumfang_mehrfarbig_HMI_4: 0
→ 应用
```

在车机屏幕上显示小太阳和单色图形
``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_ambientelicht_verbauinformation_HMI: 1
- p_ambientelicht_verbauinformation_HMI_2: 10001
- p_ambientelicht_verbauinformation_HMI_3: 10
- p_ambientelicht_verbauinformation_HMI_4: 0
→ 应用
```

换色速度 ms
``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_t_HMI_verzoegerung_helligkeitswerte: 200
→ 应用
```

写入物理 LED
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ambient_lighting_lin_slaves_modules:
- pa_einzeladresse_slave_1: 1
- pa_verbauinfo_slave_1: установл.
- pa_fehlerort_slave_1: 0

- pa_einzeladresse_slave_2: 2
- pa_verbauinfo_slave_2: установл.
- pa_fehlerort_slave_2: 0

- pa_einzeladresse_slave_3: 3
- pa_verbauinfo_slave_3: установл.
- pa_fehlerort_slave_3: 0

- pa_einzeladresse_slave_4: 4
- pa_verbauinfo_slave_4: установл.
- pa_fehlerort_slave_4: 0

- pa_einzeladresse_slave_5: 0
- pa_verbauinfo_slave_5: не установл.
- pa_fehlerort_slave_5: 0

- pa_einzeladresse_slave_6: 0
- pa_verbauinfo_slave_6: установл.
- pa_fehlerort_slave_6: 0

- pa_einzeladresse_slave_7: 0
- pa_verbauinfo_slave_7: не установл.
- pa_fehlerort_slave_7: 0

- pa_einzeladresse_slave_8: 0
- pa_verbauinfo_slave8: не установл.
- pa_fehlerort_slave8: 0

- pa_einzeladresse_slave_9: 0
- pa_verbauinfo_slave_9: не установл.
- pa_fehlerort_slave_9: 0

- pa_einzeladresse_slave_10: 0
- pa_verbauinfo_slave_10: не установл.
- pa_fehlerort_slave_10: 0

- pa_einzeladresse_slave_11: 0
- pa_verbauinfo_slave_11: не установл.
- pa_fehlerort_slave_11: 0

- pa_einzeladresse_slave_:12: 0
- pa_verbauinfo_slave_12: не установл.
- pa_fehlerort_slave_12: 0

- pa_einzeladresse_slave_13: 0
- pa_verbauinfo_slave_13: не установл.
- pa_fehlerort_slave_13: 0

- pa_einzeladresse_slave_14: 0
- pa_verbauinfo_slave_14: не установл.
- pa_fehlerort_slave_14: 0

- pa_einzeladresse_slave_15: 0
- pa_verbauinfo_slave_15: не установл.
- pa_fehlerort_slave_15: 0

- pa_einzeladresse_slave_16: 0
- pa_verbauinfo_slave_16: не установл.
- pa_fehlerort_slave_16: 0

- pa_einzeladresse_slave_17: 0
- pa_verbauinfo_slave_17: не установл.
- pa_fehlerort_slave_17: 0

- pa_einzeladresse_slave_18: 0
- pa_verbauinfo_slave_18: не установл.
- pa_fehlerort_slave_18: 0

- pa_einzeladresse_slave_19: 0
- pa_verbauinfo_slave_19: не установл.
- pa_fehlerort_slave_19: 0

- pa_einzeladresse_slave_20: 0
- pa_verbauinfo_slave_20: не установл.
- pa_fehlerort_slave_20: 0
→ 应用
```

写入 LED 调节组及其用途
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ambient_lighting_lin_slaves_groups:
- pa_verbauinfo_gruppe_1: 多色
- pa_lichtfunktion_gruppe_1: 车门
- pa_korrekturfaktor_gruppe_1: 1

- pa_verbauinfo_gruppe_2: 多色
- pa_lichtfunktion_gruppe_2: 中控台
- pa_korrekturfaktor_gruppe_2: 1.2

- pa_verbauinfo_gruppe_3: не установл.
- pa_lichtfunktion_gruppe_3: 车门
- pa_korrekturfaktor_gruppe_3: 1

- pa_verbauinfo_gruppe_4: не установл.
- pa_lichtfunktion_gruppe_4: 车门
- pa_korrekturfaktor_gruppe_4: 1

- pa_verbauinfo_gruppe_5: не установл.
- pa_lichtfunktion_gruppe_5: 车门
- pa_korrekturfaktor_gruppe_5: 1

- pa_verbauinfo_gruppe_6: не установл.
- pa_lichtfunktion_gruppe_6: 车门
- pa_korrekturfaktor_gruppe_6: 1

- pa_verbauinfo_gruppe_7: не установл.
- pa_lichtfunktion_gruppe_7: 车门
- pa_korrekturfaktor_gruppe_7: 1

- pa_verbauinfo_gruppe_8: не установл.
- pa_lichtfunktion_gruppe_8: 车门
- pa_korrekturfaktor_gruppe_8: 1

- pa_verbauinfo_gruppe_9: не установл.
- pa_lichtfunktion_gruppe_9: 车门
- pa_korrekturfaktor_gruppe_9: 1

- pa_verbauinfo_gruppe_10: не установл.
- pa_lichtfunktion_gruppe_10: 车门
- pa_korrekturfaktor_gruppe_10: 1

- pa_verbauinfo_gruppe_11: 单色
- pa_lichtfunktion_gruppe_11: 脚部空间
- pa_korrekturfaktor_gruppe_11: 1.2

- pa_verbauinfo_gruppe_12: не установл.
- pa_lichtfunktion_gruppe_12: 车门
- pa_korrekturfaktor_gruppe_12: 1

- pa_verbauinfo_gruppe_13: не установл.
- pa_lichtfunktion_gruppe_13: 车门
- pa_korrekturfaktor_gruppe_13: 1

- pa_verbauinfo_gruppe_14: 3_not_defined
- pa_lichtfunktion_gruppe_14: 脚部空间
- pa_korrekturfaktor_gruppe_14: 1.2

- pa_verbauinfo_gruppe_15: не установл.
- pa_lichtfunktion_gruppe_15: 车门
- pa_korrekturfaktor_gruppe_15: 1
→ 应用
```

基础颜色列表
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambience_lightning_color_list:
- Rotwert Farbe 1: 217
- Gruenwert Farbe 1: 221
- Blauwert Farbe 1: 235

- Rotwert Farbe 2: 255
- Gruenwert Farbe 2: 172
- Blauwert Farbe 2: 5

- Rotwert Farbe 3: 253
- Gruenwert Farbe 3: 108
- Blauwert Farbe 3: 55

- Rotwert Farbe 4: 222
- Gruenwert Farbe 4: 70
- Blauwert Farbe 4: 20

- Rotwert Farbe 5: 252
- Gruenwert Farbe 5: 116
- Blauwert Farbe 5: 240

- Rotwert Farbe 6: 132
- Gruenwert Farbe 6: 76
- Blauwert Farbe 6: 222

- Rotwert Farbe 7: 0
- Gruenwert Farbe 7: 102
- Blauwert Farbe 7: 225

- Rotwert Farbe 8: 1
- Gruenwert Farbe 8: 192
- Blauwert Farbe 8: 255

- Rotwert Farbe 9: 0
- Gruenwert Farbe 9: 204
- Blauwert Farbe 9: 0

- Rotwert Farbe 10: 182
- Gruenwert Farbe 10: 255
- Blauwert Farbe 10: 57
→ 应用
```

第二组可设置颜色
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambience_lightning_color_list_2:
- Rotwert Farbe 11: 255
- Gruenwert Farbe 11: 255
- Blauwert Farbe 11: 0

- Rotwert Farbe 12: 5
- Gruenwert Farbe 12: 102
- Blauwert Farbe 12: 192

- Rotwert Farbe 13: 222
- Gruenwert Farbe 13: 70
- Blauwert Farbe 13: 21

- Rotwert Farbe 14: 1
- Gruenwert Farbe 14: 204
- Blauwert Farbe 14: 0

- Rotwert Farbe 15: 80
- Gruenwert Farbe 15: 80
- Blauwert Farbe 15: 80
→ 应用
```

LED 用颜色
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambience_lightning_color_list_lin:
- Rotwert_Farbe_1_lin: 120
- Gruenwert_Farbe_1_lin: 231
- Blauwert_Farbe_1_lin: 71

- Rotwert_Farbe_2_lin: 255
- Gruenwert_Farbe_2_lin: 200
- Blauwert_Farbe_2_lin: 0

- Rotwert_Farbe_3_lin: 245
- Gruenwert_Farbe_3_lin: 73
- Blauwert_Farbe_3_lin: 6

- Rotwert_Farbe_4_lin: 255
- Gruenwert_Farbe_4_lin: 9
- Blauwert_Farbe_4_lin: 2

- Rotwert_Farbe_5_lin: 255
- Gruenwert_Farbe_5_lin: 134
- Blauwert_Farbe_5_lin: 106

- Rotwert_Farbe_6_lin: 106
- Gruenwert_Farbe_6_lin: 140
- Blauwert_Farbe_6_lin: 162

- Rotwert_Farbe_7_lin: 0
- Gruenwert_Farbe_7_lin: 110
- Blauwert_Farbe_7_lin: 254

- Rotwert_Farbe_8_lin: 29
- Gruenwert_Farbe_8_lin: 255
- Blauwert_Farbe_8_lin: 153

- Rotwert_Farbe_9_lin: 0
- Gruenwert_Farbe_9_lin: 255
- Blauwert_Farbe_9_lin: 4

- Rotwert_Farbe_10_lin: 57
- Gruenwert_Farbe_10_lin: 132
- Blauwert_Farbe_10_lin: 0
→ 应用
```

LED 用颜色的第二部分
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambience_lightning_color_list_lin_2:
- Rotwert_Farbe_11_lin: 255
- Gruenwert_Farbe_11_lin: 255
- Blauwert_Farbe_11_lin: 0

- Rotwert_Farbe_12_lin: 120
- Gruenwert_Farbe_12_lin: 231
- Blauwert_Farbe_12_lin: 71

- Rotwert_Farbe_13_lin: 120
- Gruenwert_Farbe_13_lin: 230
- Blauwert_Farbe_13_lin: 80

- Rotwert_Farbe_14_lin: 121
- Gruenwert_Farbe_14_lin: 231
- Blauwert_Farbe_14_lin: 71

- Rotwert_Farbe_15_lin: 130
- Gruenwert_Farbe_15_lin: 241
- Blauwert_Farbe_15_lin: 80
→ 应用
```

驾驶模式与颜色编号
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambientelicht Zuordnung der Farbe zum Fahrprofil:
- pFahrprofil_0: 1 熄火时的模式
- pFahrprofil_1: 1
- pFahrprofil_2: 7 普通
- pFahrprofil_3: 4 运动
- pFahrprofil_4: 6 越野
- pFahrprofil_5: 9 经济
- pFahrprofil_6: 8
- pFahrprofil_7: 5 个性化
- pFahrprofil_8: 1
- pFahrprofil_9: 1
- pFahrprofil_10: 8 雪地
- pFahrprofil_11: 1
- pFahrprofil_12: 1
- pFahrprofil_13: 1
- pFahrprofil_14: 1
- pFahrprofil_15: 1
→ 应用
```

``` yaml
单元 19 → 编码:
FPA_Funktion_AMB: 激活
→ 应用（需重启单元）
```

提高模式切换速度
``` yaml
单元 19 → 适配:
Driving Profile Selection Parameter:
- Driving Profile Selection Toogle Time Adaptation: 把 2000 ms 改为 0
→ 应用
```

车门口袋照明的编码
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ambient_lighting_lin_slaves_groups:
- pa_verbauinfo_gruppe_7: Multi_color
- pa_lichtfunktion_gruppe_7: door
- pa_korrekturfaktor_gruppe_7: 1.00
- pa_verbauinfo_gruppe_8: Multi_color
- pa_lichtfunktion_gruppe_8: door
- pa_korrekturfaktor_gruppe_8: 1.00
- pa_verbauinfo_gruppe_9: Multi_color
- pa_lichtfunktion_gruppe_9: door
- pa_korrekturfaktor_gruppe_9: 1.00
- pa_verbauinfo_gruppe_10: Multi_color
- pa_lichtfunktion_gruppe_10: door
→ 应用
```
