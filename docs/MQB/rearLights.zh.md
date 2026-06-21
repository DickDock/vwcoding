
# 尾灯

### 2021 款 Tiguan 的动态转向灯（用于 IQ Light 大灯）

!!! info ""
    在 BCM 单元版本 5Q0937084DP H42 上验证过  

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Blinker:
- PreCrash_RECAS: PreCrash_passiv 改为 PreCrash_activ
- Richtungs_blinken_links: 激活 – 左侧流水转向灯。
- Richtungs_blinken_rechts: 激活 – 右侧流水转向灯。
- Warnblinken_Zuendung_EIN: 激活 – 点火开启时的双闪。
- Warnblinken_Zuendung_AUS: 激活 – 点火关闭时的双闪。
- ZV_Blinken_zu: 激活 – 设防时的流水转向灯。
- ZV_Blinken_auf: 激活 – 撤防时的流水转向灯。
→ 应用
``` 

### 开门时用后刹车灯警示

!!! tip "可能的取值"
    Tuerausstiegslicht hinten links/rechts – 仅后门  
    Tuerausstiegslicht vorne links/rechts – 仅前门  
    Tuerausstiegslicht links/rechts – 前门和后门  

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte20BR LA71:
- At Lichtfunktion B 20: 新值
→ 应用
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte21BR RC8:
- At Lichtfunktion B 21: 新值
→ 应用
```

### 后示廓灯与转向灯交替闪烁

!!! tip ""
    后示廓灯在转向灯开启时熄灭、关闭时重新点亮（转向灯每个闪烁周期）
  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte16BLK SLB35BLK SL KC9:
- Lichtfunktion G 16: 由 not active 改为 Blinken rechts Hellphase
Leuchte16SL HLC10:
- Dimming Direction GH 16: 由 maximize 改为 minimize
---
Leuchte17TFL R BLK SRB3TFL R BLK SR KC3:
- Lichtfunktion G 17: 由 not active 改为 Blinken links Hellphase
Leuchte17SL HLC10:
- Dimming Direction GH 17: 由 maximize 改为 minimize
---
Leuchte23SL HLC10:
- Lichtfunktion G 23: 由 not active 改为 Blinken links Hellphase
- Dimming Direction GH 23: 由 maximize 改为 minimize
---
Leuchte24SL HRA65:
- Lichtfunktion G 24: 由 not active 改为 Blinken rechts Hellphase
- Dimming Direction GH 24: 由 maximize 改为 minimize
```

### 挂倒挡并开双闪时倒车灯与转向灯交替闪烁

``` yaml title="登录密码: 31347"
单元 09 → 编码:
Leuchte 28RFL LC11:
- Lichtfunktion C: Active 改为 Blinken Links Hellphase
- Lichtfunktion D: 保持 Not Active
- Dimmwert CD: 保持「0」
- Dimming Direction CD: maximize 改为 minimize
→ 应用
---
Leuchte 29RFL RA64:
- Lichtfunktion C: Active 改为 Blinken Rechts Hellphase
- Lichtfunktion D: 保持 Not Active
- Dimmwert CD: 保持「0」
- Dimming Direction CD: maximize 改为 minimize
→ 应用
```

### 仅 DRL 模式下点亮后示廓灯 — HIGH 尾灯的「F」字样始终点亮

!!! warning ""
    网上充斥着设定 Tagfahrlicht 功能的建议。  
    那是不正确的！

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte23SL HLC10 (左尾灯):
- Lichtfunktion D: 23 → (Dauerfahrlicht) Daytime running lights (原为 nicht aktiv)
- Dimmwert CD 23: 0 → 127
---
Leuchte24SL HRA65 (右尾灯):
- Lichtfunktion D: 24 → (Dauerfahrlicht) Daytime running lights (原为 nicht aktiv)
- Dimmwert CD 23: 0 → 127
---
Leuchte16BLK SLB35BLK SL KC9 (翼子板上的左尾灯):
- Lichtfunktion D: 16 → (Dauerfahrlicht) Daytime running lights (原为 nicht aktiv)
- Dimmwert CD 16: 0 → 127
---
Leuchte17TFL R BLK SRB3TFL R BLK SR KC3 (翼子板上的左尾灯):
- Lichtfunktion C: 17 → (Dauerfahrlicht) Daytime running lights (原为 nicht aktiv)
- Dimmwert CD 17: 0 → 127
→ 应用
```

### 为 BASIS 尾灯点亮后示廓灯各段

![Screenshot](../images/MQB/basicPTF.png)

尾门上的左尾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte23SL HLC10:
- Lichtfunktion C 23: Daytime running lights
- Lichtfunktion E 23: Освещение багажного отсека 或 Luggage compartment light
- Lichtfunktion F 23: Стоп-сигнал 或 Brake light
- Dimming Direction EF 23: minimize
- Dimmwert CD 23: 60
→ 应用
```

尾门上的右尾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte24SL HRA65:
- Lichtfunktion C 24: Daytime running lights -16
- Lichtfunktion E 24: Освещение багажного отсека 或 Luggage compartment light
- Lichtfunktion F 24: Стоп-сигнал 或 Brake light
- Dimming Direction EF 24: minimize
- Dimmwert CD 24: 60
→ 应用
```

翼子板上的左尾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte20BR LA71:
- Lichtfunktion C 20: Daytime running lights
- Lichtfunktion E 20: Стоп-сигнал 或 Brake light
- Dimmwert CD 20: 13
- Dimmwert EF 20: 60
→ 应用
```

翼子板上的右尾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte21BR RC8:
- Lichtfunktion C 21: Daytime running lights
- Lichtfunktion E 21: Стоп-сигнал 或 Brake light 
- Dimmwert CD 21: 13
- Dimmwert EF 21: 60
→ 应用
```

打开行李厢盖时关闭其上的尾灯：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte23SL HLC10:
- Lichtfunktion G 23: Rear lid open (原为 nicht aktiv)
- Dimming Direction GH 23: minimize
→ 应用
```
``` yaml title="登录密码: 31347"
单元 09 → 适配
Leuchte24SL HLC10:
- Lichtfunktion G 24: Rear lid open (原为 nicht aktiv)
- Dimming Direction GH 24: minimize
→ 应用
```

### 基于刹车灯的后雾灯

![Screenshot](../images/MQB/newPTF.png)

关闭主后雾灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte26NSL LA72:
- Lichtfunktion A: nicht aktiv (原为 Nebelschlusslicht wenn kein Anhaenger gesteckt und Rechtsverkehr)
→ 应用
```

点亮刹车灯各段
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte27NSL RC6:
- Lichtfunktion B: Nebelschlusslicht wenn kein Anhaenger gesteckt und Rechtsverkehr (原为 Nicht aktiv)
- Lichtfunktion C: Kofferraumlicht (原为 Nebelschlusslicht wenn kein Anhaenger gesteckt und Rechtsverkehr)
→ 应用
```

如果还需要点亮倒车灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte28RFL LC11 和 Leuchte29RFL RA64:
- Lichtfunktion В: Nebelschlusslicht wenn kein Anhaenger gesteckt und Rechtsverkehr (原为 Nicht aktiv)
→ 应用
```
