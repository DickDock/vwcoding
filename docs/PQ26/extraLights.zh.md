# 非标准灯光方案

### DRL (LED) 与近光同时点亮
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte4TFL LB43: Light_Function_C_4 → Abblendlicht links
Leuchte4TFL LB43: Dimming_CD_4 → 127
Leuchte5 TFL RB6: Light_Function_C_5 → Abblendlicht rechts
Leuchte5 TFL RB6: Dimming_CD_5 → 127
→ 应用
```

### 示廓灯模式下点亮 DRL（灯光开关在示廓灯位时，开大灯则 DRL 关闭）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Daytime running lights:
- Standlicht aktiviert zusaetzlich Tagfahrlicht: 激活 
---
19 款：
Aussenlicht_Front:
- Standlicht aktiviert zusaetzlich Tagfahrlicht: 激活
→ 应用
```

### 转向灯工作侧的 DRL 减弱
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte4TFL LB43: Light_Function_G_4 → Blinken links Rampe
Leuchte4TFL LB43: Dimming_GH_4 → 0 (或其他百分比值)
Leuchte4TFL LB43: Dimming_Direction_GH_4 → minimize
Leuchte5 TFL RB6: Light_Function_G_5 → Blinken rechts Rampe
Leuchte5 TFL RB6: Dimming_GH_5 → 0 (或其他百分比值)
Leuchte5 TFL RB6: Dimming_Direction_GH_5 → minimize
→ 应用
```

### DRL 与转向灯同相闪烁
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte 4TFL LB43: Lichtfunktion G 4 → Blinken links Dunkelpase
Leuchte 4TFL LB43: Dimmwert GH 4 → 0
Leuchte 4TFL LB43: Dimming Direction GH 4 → minimize
Leuchte 5TFL RB6: Lichtfunktion G 5 → Blinken rechts Dunkelpase
Leuchte 5TFL RB6: Dimmwert GH 5 → 0
Leuchte 5TFL RB6: Dimming Direction GH 5 → minimize
→ 应用
```

### 转向灯工作侧的前示廓灯减弱
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte2SL VLB22 – Light_Function_E_2 → Blinken links Rampe
Leuchte2SL VLB22 – Dimming_EF_2 → 0 (或其他百分比值)
Leuchte2SL VLB22 – Dimming_Direction_EF_2 → minimize
Leuchte3SL VRB36 – Light_Function_E_3 → Blinken rechts Rampe
Leuchte3SL VRB36 – Dimming_EF_3 → 0 (或其他百分比值)
Leuchte3SL VRB36 – Dimming_Direction_EF_3 → minimize
→ 应用
```

### US-Standlicht Blinker（通过转向灯半亮实现示廓灯）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte 0 BLK VL B35 – Light_Function_C_0 → Standlicht
Leuchte 0 BLK VL B35 – Dimming_CD_0 → 35
Leuchte 0 BLK VL B35 – Dimming_Direction_CD_0 → maximize
Leuchte 0 BLK VL B35 – Light_Function_E_0 → Blinken links Dunkelpase
Leuchte 0 BLK VL B35 – Dimming_EF_0 → 0
Leuchte 0 BLK VL B35 – Dimming_Direction_EF_0 → minimize
Leuchte1BLK VRB23 – Light_Function_C_1 → Standlicht
Leuchte1BLK VRB23 – Dimming_CD_1 → 35
Leuchte1BLK VRB23 – Dimming_Direction_CD_1 → maximize
Leuchte1BLK VRB23 – Light_Function_E_1 → Blinken rechts Dunkelpase
Leuchte1BLK VRB23 – Dimming_EF_1 → 0
Leuchte1BLK VRB23 – Dimming_Direction_EF_1 → minimize
→ 应用
```

### US-Standlicht nur bei Standlicht（仅在灯光开关示廓灯位时，通过转向灯半亮实现示廓灯）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte 0 BLK VL B35 – Light_Function_A_0 → Standlicht Vorn
Leuchte 0 BLK VL B35 – Dimming_AB_0 → 35
Leuchte 0 BLK VL B35 – Light_Function_C_0 → Abblendlicht links
Leuchte 0 BLK VL B35 – Light_Function_D_0 → Blinken links Dunkelpase
Leuchte 0 BLK VL B35 – Dimming_CD_0 → 0
Leuchte 0 BLK VL B35 – Dimming_Direction_CD_0 → minimize
Leuchte 0 BLK VL B35 – Light_Function_E_0 → Blinken links Hellphase
Leuchte 0 BLK VL B35 – Dimming_EF_0 → 100
Leuchte 0 BLK VL B35 – Dimming_Direction_EF_0 → maximize
Leuchte1BLK VRB23 – Light_Function_A_1 → Standlicht Vorn
Leuchte1BLK VRB23 – Dimming_AB_1 → 35
Leuchte1BLK VRB23 – Light_Function_C_1 → Abblendlicht rechts
Leuchte1BLK VRB23 – Light_Function_D_1 → Blinken rechts Dunkelpase
Leuchte1BLK VRB23 – Dimming_CD_1 → 0
Leuchte1BLK VRB23 – Dimming_Direction_CD_1 → minimize
Leuchte1BLK VRB23 – Light_Function_E_1 → Blinken rechts Hellphase
Leuchte1BLK VRB23 – Dimming_EF_1 → 100
Leuchte1BLK VRB23 – Dimming_Direction_EF_1 → maximize
→ 应用
```

### 开近光/远光时熄灭前示廓灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte2SL VLB22 – Light_Function_A_2 → Standlicht — 改为 Standlicht vorn
Leuchte3SL VRB36 – Light_Function_A_3 → Standlicht — 改为 Standlicht vorn
→ 应用
```

### 前示廓灯与转向灯反相交替闪烁
方案 А – 一侧交替闪烁时 — 另一侧示廓灯熄灭
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte2SL VLB22 – Light_Function_E_2 → Blinken links Dunkelpase
Leuchte2SL VLB22 – Dimming_EF_2 → 100
Leuchte2SL VLB22 – Dimming_Direction_EF_2 → maximize
Leuchte3SL VRB36 – Light_Function_E_3 → Blinken rechts Dunkelpase
Leuchte3SL VRB36 – Dimming_EF_3 → 100
Leuchte3SL VRB36 – Dimming_Direction_EF_3 → maximize
→ 应用
```
方案 Б – 一侧交替闪烁时 — 另一侧示廓灯点亮
* 仅与「开近光/远光时熄灭前示廓灯」一项配合使用
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte2SL VLB22 – Light_Function_E_2 → Blinken links Dunkelpase
Leuchte2SL VLB22 – Light_Function_F_2 → Blinken rechts aktiv
Leuchte2SL VLB22 – Dimming_EF_2 → 100
Leuchte2SL VLB22 – Dimming_Direction_EF_2 → maximize
Leuchte3SL VRB36 – Light_Function_E_3 → Blinken rechts Dunkelpase
Leuchte3SL VRB36 – Light_Function_F_3 → Blinken links aktiv
Leuchte3SL VRB36 – Dimming_EF_3 → 100
Leuchte3SL VRB36 – Dimming_Direction_EF_3 → maximize
→ 应用
```

### 提高倒车灯亮度
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte28RFL C3 — Dimmer АВ 28 – 100% → 改为 125%
→ 应用
```

### 提高前雾灯亮度
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB40 – Dimmer АВ 12 – 100% → 改为 125%
Leuchte13NL RB3 – Dimmer АВ 12 – 100% → 改为 125%
→ 应用
```

### 提高近光和远光亮度

!!! warning ""
    需要明白，这些操作会缩短灯泡寿命。  
    寿命缩短的大致情况见下表。  
    ![Screenshot](../images/PQ26/lamp_table.png)  

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte6ABL LB44 – Dimming_AB_6 → 100% - 改为 120%
Leuchte7ABL RB5 – Dimming_AB_7 → 100% - 改为 120%
Leuchte9FL RB7 – Dimming_AB_9 → 100% - 改为 120%
Leuchte8FL LB42 – Dimming_AB_8 → 100% - 改为 120%
→ 应用
```

### 挂倒挡并开双闪时倒车灯与转向灯交替闪烁
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte28RFL C3 – Light_Function_C_28 → Blinken Links Hellphase
Leuchte28RFL C3 – Light_Function_D_28 → Blinken Rechts Hellphase
Leuchte28RFL C3 – Dimming_CD_28 → 0
Leuchte28RFL C3 – Dimming_Direction_CD_28 → minimize
→ 应用
```

### 开门侧点亮刹车灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte20BR LA70 – Light_Function_C_20 → Tuerausstiegslichtv links (开左侧车门时)。
Leuchte20BR LA70 – Dimming_CD20 → 100
Leuchte20BR LA70 – Dimming_Direction_CD20 → maximize
Leuchte21BR RC8 – Light_Function_C_21 → Tuerausstiegslichtv rechts (开右侧车门时)
Leuchte21BR RC8 – Dimming_CD21 → 100
Leuchte21BR RC8 – Dimming_Direction_CD21 → maximize
→ 应用
```

### 开后备厢时点亮侧转向灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte16BLK SLC11 – Light_Function_C_16 → Rear lid open
Leuchte16BLK SLC11 – Dimming_CD_16 → 50
Leuchte17 BLK SR A72 – Light_Function_C_17 → Rear lid open
Leuchte17 BLK SR A72 – Dimming_CD_17 → 50
→ 应用
```
