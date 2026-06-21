
# 前大灯

### 熄火后保留自动远光模式

``` yaml title="登录密码: 31347"
单元 09 (车载电气网络) → 适配:
Fernlicht_assistent:
- Fernlichtassistent Reset: not active
→ 应用 
```
  
### 调节光线传感器

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 编码 → 子块 RLHS:
    3CA8DD: 大灯不那么晚开启, 大约 1200lx
    3CA8D7: 大灯非常晚才开启, 800lx 时
    ```
  
=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 – 车载电气网络电子 → 编码 → 子块 RLHS:
    字节 0 和 2: 3C A8 D7 # (1)!
    ```

    1. 字节 0 – 第 2,3,4,5 位, 字节 2 – 第 0,1,2,4,6,7 位

### 泊车时来自后视镜的机动照明

!!! note ""
    此适配仅适用于装有 Area View 环视的车辆

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 适配:
    Aussenlicht_uebergreifend:
    – Umfeldleuchte_als_Manoevrierleuchte: 激活 
    → 应用
    ```
    ``` yaml title="登录密码: 31347"
    单元 6C → 编码:
    – Manoeuvre_Light: 激活
    → 应用（需重启单元）
    ```

=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 31347"
    Block 6C — Rear view camera system → Coding → Long coding:
    字节 8 – 位 2 (Manoeuvre_Light): 激活  
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/Manoeuvre_Light.jpg)

### 开启远光时点亮雾灯

左前雾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB45:
- Lichtfunktion B 12: Fernlicht links (左远光时点亮), 原为 nicht aktiv
→ 应用
```
右前雾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte13NL RB5:
- Lichtfunktion B 13: Fernlicht rechts (右远光时点亮), 原为 nicht aktiv
→ 应用
```

### 开启雾灯时远光与雾灯交替频闪（频闪灯）

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 适配:
    Aussenlicht_Front (Driving light and parking light):
    - Zahl der aktivern Sheinwerfer Auf 2 limitieren: limitieren (原为 in Betrieb lassen)
    → 应用
    ```

=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 31347"
    9 车载电气网络控制单元 → 安全访问 (登录: 31347) → 编码:
    Aussenlicht_Front:
    - Zahl der aktiven Scheinwerfer auf 2 limitieren: limitieren (原为 in Betrieb lassen)
    ```
  
### 远光与近光交替频闪（卤素大灯的频闪变体）

左近光
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte6ABL LC5:
- Lichtfunktion B 6: Lichthupe generell 改为 not active
- Lichtfunktion C 6: not active 改为 Lichthupe generell
- Dimming Direction CD 6: maximize 改为 minimize
→ 应用
```

右近光
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte7ABL RB1:
- Lichtfunktion B 7: Lichthupe generell 改为 not active
- Lichtfunktion C 7: not active 改为 Lichthupe generell
- Dimming Direction CD 7: maximize 改为 minimize
→ 应用
```
	
### 关闭雾灯时远光与雾灯交替频闪（频闪灯）

左前雾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB45:
- Dimming direction CD 12: maximum
- Dimmwert CD 12: 0 改为 110
- Lichtfunktion C 12: Lichthupe generell (原为 Nebellicht rechts)
→ 应用
```

右前雾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte13NL RB5:
- Dimming direction CD 13: maximum
- Dimmwert CD 13: 0 改为 110
- Lichtfunktion C 13: Lichthupe generell (原为 Nebellicht rechts)
→ 应用
```

### 更改超车或变道模式下转向灯的闪烁次数

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Blinker:
- Komfortblinken Blinkzyklen (Turn signal control): 改为所需次数 2-5
→ 应用
```

### 卤素大灯的美式转向灯风格（随 DRL 半亮常亮）

!!! note ""
    适用于转向灯内装白炽灯泡的车辆

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte0BLK VLB36:
- Lichtfunktion D0: Standlicht allgemein (Schlusslicht, Positionslicht, Begrenzungslicht) 
- Dimmwert CD0: 0 改为 30
- Lichtfunktion E0: Blinken Links Dunkelphase
- Dimming Direction EF0: maximize 改为 minimize
→ 应用
---
Leuchte1BLK VRB20:
- Lichtfunktion D1: Standlicht allgemein (Schlusslicht, Positionslicht, Begrenzungslicht)
- Dimmwert CD1: 0 改为 30
- Lichtfunktion E1: Blinken Rechts Dunkelphase
- Dimming Direction EF1: maximize 改为 minimize
 → 应用
```

### 转向灯与 DRL 交替闪烁（卤素大灯）

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte2SL VLB10:
- Lichtfunktion G 2: Blinken links Hellphase  
- Dimmwert GH 2: 0  
- Dimming Direction GH 2: minimize  
→ 应用  
---
Leuchte3SL VRB21:
- Lichtfunktion G 3: Blinken rechts Hellphase  
- Dimmwert GH 3: 0  
- Dimming Direction GH 3: minimize  
→ 应用
```

!!! tip "Audi Style"
    ``` yaml
    - Lichtfunktion G 2: Blinken links aktiv (beide Phase)  
    - Dimmwert GH 2: 20 到 35 之间的值  
    - Lichtfunktion G 2: Blinken links aktiv (beide Phase)  
    - Dimmwert GH 3: 20 到 35 之间的值  
    ```
  
### 关闭近光/DRL 的提示

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_uebergreifend:
- Fahrlichtwarnung_Hinweis_Konfig: kein_Hinweis (原为 Hinweis_in_LDS-Stellung_Null_und_SL)
→ 应用
```

### 拉起手刹时关闭 DRL

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Front:
- Tagfahrlicht Dauerfahrlicht bei Handbremse abschalten: 激活
→ 应用
```

### 灯光开关在 0 位时关闭 DRL

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Front:
- Tagfahrlicht nur in Schalterstellung AUTO: 激活
→ 应用
```

### 设置菜单中的"日间行车灯"项, 以便仅在需要时关闭 DRL

在灯光设置菜单中会出现"日间行车灯"项：  
![Screenshot](../images/MQB/daylight.jpg)

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Front:
Tagfahrlicht aktivierung durch BAP oder Bedienfolge moeglich: 激活:
→ 应用
```

### 雾灯中的 LED

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB45:
- Lasttyp 12: 6-LED Lichtmodul
→ 应用
---
Leuchte13NL RB5:
- Lasttyp 13: 6-LED Lichtmodul
→ 应用
```

降低 LED 亮度：

``` yaml
Leuchte12NL LB45:
- DimmwertAB 12: 60
→ 应用
---
Leuchte13NL RB5:
- DimmwertAB 13: 60
→ 应用
```

### 下车前用自动送行照明而非晃远光

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_uebergreifend:
- Coming Home Verbaustatus: 自动
- Menueeinstellung Cominghome: # 点亮时长
→ 应用
```

### 挂入倒挡时点亮前雾灯

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Static AFS light (静态自适应照明系统):
- Bei Rueckwaertsfahrt: double sided (双侧)
→ 应用
```

### 弯道照明系统 (CORNER)

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB45:
- Lichtfunktion D 12: Abbieglicht links (原为 nicht aktiv)
→ 应用
---
Leuchte13NL RB5:
- Lichtfunktion D 13: Abbieglicht rechts (原为 nicht aktiv)
→ 应用
```
	
更改弯道照明的开启速度

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Static AFS light (静态自适应照明系统):
- Untere Geschwindigkeitsschwelle (Lower speed limit): 0 km/h
- Obere Geschwindigkeitsschwelle (Upper speed threshold): 50 km/h # (1)!
→ 应用
```

1. 允许设置不大于 60 的值。要关闭该功能需设为 0
