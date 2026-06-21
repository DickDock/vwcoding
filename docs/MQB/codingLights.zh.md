
# 灯光设备编码

!!!note ""
    感谢 [Вячеслав](https://www.drive2.ru/users/slavian116) 协助制作本说明  

### 照明通道工作原理图

![Screenshot](../images/MQB/light_scheme.jpg)

不同车型（Tiguan、Škoda、Golf、Passat）灯具到通道的对应关系可能不同。 

### VW Tiguan 2 前灯通道列表

| 灯具名称                                       |                 BASIS LED                 |                     MID LED |
|-----------------------------------------------|:-----------------------------------------:|----------------------------:|
| Leuchte0BLK VLB36 / Leuchte1BLK VRB20         |          左/右 转向灯                     |                             |
| Leuchte2SL VLB10 / Leuchte3SL VRB21           |          左/右 DRL 控制                   |                             |
| Leuchte4TFL LB44 / Leuchte5TFL RB32           |          左/右 DRL                        |                             |
| Leuchte6ABL LC5 / Leuchte7ABL RB1             |          左/右 近光                       |          左/右 近光         |
| Leuchte8FL LB39 / Leuchte9FL RB2              |          左/右 远光                       |          左/右 DRL          |
| Leuchte10SHUTTER LB23 / Leuchte11SHUTTER RB22 |          左/右 近光诊断                   |      模块供电 / 空          |
| Leuchte12NL LB45 / Leuchte13NL RB5            |          左/右 雾灯                       |          左/右 雾灯         |

### VW Tiguan 2 尾灯通道列表

| 灯具名称                                                                   |                             BASIS                             |                                          HIGH |
|----------------------------------------------------------------------------|:-------------------------------------------------------------:|----------------------------------------------:|
| Leuchte16BLK SLB35BLK SL KC9 /<br/>Leuchte17TFL R BLK SRB3TFL R BLK SR KC3 |                                                               |                 左/右 示廓灯 |
| Leuchte18BLK HLA60 / Leuchte19BLK HRC31                                    |               左/右 转向灯               |               左/右 转向灯 |
| Leuchte20BR LA71 / Leuchte21BR RC8                                         | 左/右 翼子板上的刹车灯 + 示廓灯 |                 左/右 刹车灯 |
| Leuchte22BR MA57                                                           |                    高位刹车灯                    |                       高位刹车灯 |
| Leuchte23SL HLC10 / Leuchte24SL HRA65                                      |        左/右 后门上的示廓灯        | 左/右 后门上的示廓灯 |
| Leuchte25KZL HA59                                                          |                       牌照灯                        |                              牌照灯 |
| Leuchte26NSL LA72 / Leuchte27NSL RC6                                       |                       左雾灯 / 空                       |              左雾灯 / 尾门上的刹车灯 |
| Leuchte28RFL LC11 / Leuchte29RFL RA64                                      |                   空 / 右倒车灯                   |                     左/右 倒车灯 |
  
### 其他灯具列表

Leuchte 35 LED Warnblinktaster C48 – 双闪按键  
Leuchte30FR LC72 – 车内脚部照明
  
### 通道解读

以 Leuchte9FL RB2 为例。

Leuchte9FL RB2 – [Leuchte][9][FL][R][B2]

[Leuchte] - 灯  
[9] - 灯编号  
[FL] - 灯功能标识（常与实际不符）  
[R] - 位置 – rechts (右)/links (左)  
[B2] - BCM 上的触点（接口 В, 引脚 2）

| 灯功能缩写 | 德语名称                                                                                                                             | 中文名称              |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| ABL                        | <span style="font-weight:bold">A</span>b<span style="font-weight:bold">b</span>lend<span style="font-weight:bold">l</span>icht       | 近光          |
| AMBL                       | <span style="font-weight:bold">Amb</span>iente<span style="font-weight:bold">l</span>icht                                            | 氛围灯 |
| BLK                        | <span style="font-weight:bold">Bl</span>in<span style="font-weight:bold">k</span>en                                                  | 转向灯            |
| BR                         | <span style="font-weight:bold">Br</span>emslicht                                                                                     | 刹车灯           |
| FL                         | <span style="font-weight:bold">F</span>ern<span style="font-weight:bold">l</span>icht                                                | 远光          |
| FR                         | <span style="font-weight:bold">F</span>uss<span style="font-weight:bold">r</span>aumlicht                                            | 脚部照明         |
| HD                         | <span style="font-weight:bold">H</span>eck<span style="font-weight:bold">d</span>eckel                                               | 行李厢盖      |
| KZL                        | <span style="font-weight:bold">K</span>enn<span style="font-weight:bold">z</span>eichen<span style="font-weight:bold">l</span>euchte | 牌照灯      |
| NL                         | <span style="font-weight:bold">N</span>ebel<span style="font-weight:bold">l</span>icht                                               | 前雾灯           |
| NSL                        | <span style="font-weight:bold">N</span>ebel<span style="font-weight:bold">s</span>chluss<span style="font-weight:bold">l</span>icht  | 后雾灯             |
| RFL                        | <span style="font-weight:bold">R</span>ueck<span style="font-weight:bold">f</span>ahr<span style="font-weight:bold">l</span>icht     | 倒车灯            |
| SL                         | <span style="font-weight:bold">S</span>tand<span style="font-weight:bold">l</span>icht                                               | 示廓灯              |
| TFL                        | <span style="font-weight:bold">T</span>ag<span style="font-weight:bold">f</span>ahr<span style="font-weight:bold">l</span>icht       | DRL 日间行车灯                   |

### 灯具类型

每个灯都可指定其类型 – Lasttypen

??? note "可能的灯具类型及其编号"
    | 灯具类型编号 | 类型说明  |
    |:------------------:|:------------------:|
    | 1 | LED Tagfahrlichtmodul Versorgung   |
    | 2 | Shutter; Diagnosesensierung für "LED low"   |
    | 3 | Xenon Abblendlicht   |
    | 4 | LED Tagfahrlichtmodul Signal   |
    | 5 | LED Abblendlicht   |
    | 6 | LED Lichtmodul   |
    | 7 | Reserved_07   |
    | 8 | allgemeine Glühlampe 12W   |
    | 9 | allgemeine Glühlampe 27W; auch H15   |
    | 10 | allgemeine Scheinwerfer   |
    | 11 | Abblendlicht   |
    | 12 | Blinkleuchten   |
    | 13 | Bremsleuchten   |
    | 14 | kombinierte Blink- Bremsleuchten   |
    | 15 | allgemeine Glühlampe 6W; auch H6W   |
    | 16 | 2* 3W   |
    | 17 | 4* 3W   |
    | 18 | 2* 5W   |
    | 19 | 3* 5W   |
    | 20 | 4* 5W   |
    | 21 | 2* 13W Blinker   |
    | 22 | 2* 16W Blinker   |
    | 23 | allgemeine Scheinwerfer   |
    | 24 | 2* 5W KZL + LED Sidemarker   |
    | 25 | allgemeine Glühlampe innen- oder Außenlicht   |
    | 32 | allgemeine LED bis 12W   |
    | 33 | LED-Modul Blinkleuchten   |
    | 34 | LED Bremsleuchten   |
    | 35 | kombinierte LED Blink-Bremsleuchten   |
    | 36 | LED Kleinleistung   |
    | 37 | allgemeine LED bis 12W   |
    | 38 | LED Blinkleuchten   |
    | 39 | LED Bremsleuchten   |
    | 40 | allgemeine LED   |
    | 41 | LED Kleinleistung   |
    | 42 | LED dritte Bremsleuchte   |
    | 43 | allgemeine LED   |
    | 44 | LED Fußraum- oder -Innenleuchte   |
    | 45 | allgemeine LED bis 6W   |
    | 46 | LED Kleinleistung  |


### 

Lampendefektbitposition 和 Fehlerort mittleres Byte DTC-DFCC —— 两个字段，指明用于检查灯具是否存在及是否正常工作的位。

这是通过 BAP 总线传输的诊断信息

### 照明功能

!!! warning "VCDS 警告"
    在 VCDS（也就是大家爱叫的 Вася）里，不知为何把这些功能做了翻译。结果选择列表中一堆值名称相同。  
    请务必小心

??? note "73 个功能"
  
    | 功能名称 | 功能说明 |
    |------------------|------------------|
    | nicht aktiv          | 未开启  |
    | nicht_definiert_4c   | 始终以 30% 亮度工作，开启双闪时在 50% 和 100% 亮度间交替 |
    | nicht_definiert_c4   | 开启双闪时在 50% 和 100% 亮度间交替 |
    | aktiv 100% 	       | 始终开启  |
    | Blinken links Hellphase | 左转向灯亮起时工作 |
    | Blinken links Dunkelphase | 左转向灯熄灭时工作 |
    | Blinken rechts Hellphase | 右转向灯亮起时工作 |
    | Blinken rechts Dunkelphase | 右转向灯熄灭时工作 |
    | Blinken links aktiv (beide Phase) | 左转向灯工作时持续工作 |
    | Blinken rechts aktiv (beide Phase) | 右转向灯工作时持续工作 |
    | Standlicht allgemein (Schlusslicht, Positionslicht, Begrenzungslicht) | 示廓灯模式下点亮 |
    | Parklicht links (beidseitiges Parklicht aktiviert li & re) | 驻车灯模式下点亮左侧（点火关闭） |
    | Parklicht rechts | 驻车灯模式下点亮右侧（点火关闭） |
    | Abblendlichts links | 左近光时点亮 |
    | Abblendlicht rechts | 右近光时点亮 |
    | Fernlicht links | 左远光时点亮 |
    | Fernlicht rechts | 右远光时点亮 |
    | Lichthupe generell | 晃远光时开启 |
    | Lichthupe bei bereits aktivem Abblendlicht oder bereits aktivem Dauerfahrlicht | Flasher with already active dimmed headlights or already active long-term driving light |
    | Lichthupe bei nicht aktivem Abblendlicht oder bereits aktivem Dauerfahrlicht | Flasher with not active dimmed headlights or already active long-term driving light |
    | Nebellicht links | 开启左雾灯时点亮 |
    | Nebellicht rechts | 开启右雾灯时点亮 |
    | Tagfahrlicht | DRL 时点亮 |
    | Dauerfahrlicht | DRL 时点亮 |
    | Abbiegelichts rlinks | 开启左 Corner 时点亮 |
    | Abbiegelichts rechts | 开启右 Corner 时点亮 |
    | Bremslicht | 踩刹车时点亮 |
    | Rueckfahrlicht | 挂入倒挡时点亮 |
    | Nebelschlusslicht | 开启后雾灯时点亮 |
    | Nebelschlusslicht wenn kein Anhaenger gesteckt und Rechtsverkehr | Rear fog light when no trailer attached and right-hand traffic |
    | Nebelschlusslicht wenn kein Anhaenger gesteckt und Linksverkehr | Rear fog light when no trailer attached and left-hand traffic |
    | Fernlicht über Assistent aktiviert | High beam assistant activated |
    | Coming Home oder Leaving Home aktiv | Coming Home Leaving Home or active |
    | Standlicht vorn (Positionslicht; Begrenzungslicht) | Auxiliary light (position light, parking light) |
    | Nebelschlusslicht auch wenn ein Anhaenger gesteckt | Rear fog light even when trailer fitted |
    | Heckdeckel offen | 打开行李厢时点亮 |
    | Heckdeckel geschlossen | 关闭行李厢时点亮 |
    | CCP-Lichtfunktion: Nach Kl.30-Reset auf 0 initialisiert und ueber CCP aenderbar | CCP-light function: After Terminal 30 reset is initialized to 0 and can be changed via CCP |
    | Quittierungsfunktion 1 | Acknowledge 1 |
    | Klemme 30G | Terminal 30G |
    | Dimmung klemme 58xs | 由车内调光旋钮调节亮度 |
    | Dimmung Klemme 58xt | Dimming terminal 58xt |
    | Dimmung Klemme 58xd | (Terminal 58xd dimmer)Terminal 58xd dimmer |
    | Klemme 15 mit Nachlauf bis Fahrzeugstillstand | Terminal 15 with a lag after vehicle standstill |
    | Klemme 15 ohne Nachlauf| Terminal 15 without running |
    | Innenlicht | 车内照明, 开门时平滑点亮 |
    | Kofferraumlicht | 开启行李厢照明时点亮（行李厢打开时） |
    | Fussraumlicht | 脚部照明 |
    | Ambientelicht 1 | 中控台照明 1 | 
    | Ambientelicht 2 | 中控台照明 2 |
    | Ambientelicht 3 | 车门照明 3 |
    | Ambientelicht 4 | Ambient lighting 4 |
    | Ambientelicht 5 | Ambient lighting 5 |
    | Umfeldbeleuchtung | Ambient lighting |
    | Tuerausstiegslicht vorn links | 打开左前门时点亮 |
    | Tuerausstiegslicht vorn rechts | 打开右前门时点亮 |
    | Tuerausstiegslicht hinten links | 打开左后门时点亮 |
    | Tuerausstiegslicht hinten rechts | 打开右后门时点亮 |
    | Tuerausstiegslichtv links | 打开左侧车门时点亮 |
    | Tuerausstiegslichtv rechts | 打开右侧车门时点亮 |
    | Fahrzeug mit Automatik Start-Stopp ist im Stopp-Modu(s) | Vehicle with automatic start-stop is in stop Modu (s) |
    | Klemme 75 Variante a_vfzg | Terminal 75 variant a_vfzg  |
    | Klemme 75 Variante vfzg | Terminal 75 variant vfzg  |
    | beidseitiges Dauerparklicht | Both sides permanent parking light |
    | Blinken links aktiv (beide Phasen); Auf- und Abdimmend mit p_t_blinken_rampe | Flashing left active (both phases);Dimming up and down with p_t_ flash ramp |
    | Blinken rechts aktiv (beide Phasen); Auf- und Abdimmend mit p_t_blinken_rampe | Flashing right active (both phases);Dimming up and down with p_t_ flash ramp |
    | Schlusslicht aktiv ohne Bremslicht aktiv;ist deaktiviert;wenn Bremslicht aktiv ist !!! | Taillight active without stop light; disabled if the brake light is active !!! |
    | Aktive Blinkfunktion hat ein auf 1 gesetztes zugeordnetes Bit in pa_dynamisch_blinken | Active flashing function Bit1 is set t associated in pa_ dynamic_flash  |
    | Motorraumlicht| 打开发动机舱（机盖）时点亮 |
    | Fahrzeug ist nicht fahrbereit (Motor läuft nicht; Elektroantrieb nicht aktiv o.ä.) | Vehicle is not roadworthy (electric drive not active or similar, engine is not running) |
    | Handbremse ist angezogen| Hand brake is applied |
    | Debug-Lichtfunktion (in Anlehnung an CCP) | Debug light function (based on CCP) |
    | Debug-Lichtfunktion Fehlerspeicher | Debug light function error memory |
    | Versorgungsbedarf der LCM Module | Supply requirements of the LCM modules |
    | Zuschaltung Trennrelais für 2. Batterie | Switching cut-off relay for 2nd battery |
  
### 功能组链

每个灯最多分为 8 个功能、4 个亮度值和 4 个亮度方向。  

Lichtfunktion A, B, C, D, E, F, G, H —— 灯在车载网络中的功能。当某外部事件发生时开启。  

每个通道有四对 – AB CD EF GH，即一个通道里总共可写入八个功能。  
而且每对都能设定自己的工作链。  

照明组越靠后越重要：GH > EF > CD > AB。新事件的发生会覆盖当前事件，功能 H 优先级最高。

如果闪烁功能编码在 AB 和 CD 组，而雾灯编码为功能 E，
那么当雾灯开启时，即使你打转向灯，相应侧的转向信号也会持续常亮！

每个功能组中都有亮度选项和亮度变化方向。

例如，
```
Lichtfunktion C 6:	nicht aktiv  
Lichtfunktion D 6:	nicht aktiv  
Dimmwert CD 6:	0  
Dimming Direction CD 6: maximize  
```

这表示对照明功能 C 和 D 只能设定一个亮度变化方向和一个亮度变化值。  

照明功能组 AB 没有亮度调节方向，因为灯在常态下是关闭的。  
取而代之的是「Lichtansteuerung HD AB」- HD 表示行李厢盖，可编码为「Always」和「only_if_closed」。  
因此，如果你想仅在行李厢盖关闭时点亮该光源，则应编码为「only_if_closed」。

### 亮度

每个通道每对都有灯的调光选项 – Dimmwert。  

卤素灯的调节范围为 0 到 100。  
LED 的调节范围为 0 到 127。  

设为 127 时 —— 它们不再响应界面中的调光，只有开/关。  
设为 126 时 —— 亮度上限更高，且保留调光。

此字段不接受高于 127 的值。与其他字段不同，它是 7 位的，单元会把第八位清零。

!!! warning ""
    并非所有 LED 都可调光。  
    亮度的增减通过增减 PWM 信号的占空比实现。  
    设置过低的亮度 (< 25) 时通道可能报错。  

### 亮度调节

调节亮度有 Dimming direction 选项。  
亮度方向只有两个值：  

+ minimize（降低到设定值）  
+ maximize（提高到设定值）

### 编码示例

我们想让雾灯随远光一起闪烁。

1. 找到所需灯具：左侧 Leuchte12NL LB45，右侧 Leuchte13NL RB5。
2. 找一个空闲的照明功能组。本例为 CD
3. 为左灯设定功能：  
    ```
    Lichtfunktion C 12: Lichthupe generell (晃远光时开启)  
    Dimming direction CD 12: maximum  (提高亮度)  
    Dimmwert CD 12: 0 → 100
    ```
4. 为右灯设定功能： 
    ``` 
    Lichtfunktion C 13: Lichthupe generell (晃远光时开启)  
    Dimming direction CD 13: maximum  (提高亮度)  
    Dimmwert CD 13: 0 → 100  
    ```

### 大灯基本标定 
在有 AFS 错误挂起时进行。发动机须启动、大灯开启

``` yaml title="登录密码: 20103"
单元 4B → 基本设置 (04) 
大灯基本设置 (002) → 读取
双手握住方向盘（车辆已启动、大灯亮），把方向盘向左打到底并保持 3 秒。 
把方向盘向右打到底同样保持 3 秒。然后回正方向盘，等待 3 秒 → 保存
基本设置确认 (003) → 应用
```
