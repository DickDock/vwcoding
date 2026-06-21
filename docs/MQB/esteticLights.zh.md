
# 车内照明编码

### 车内照明平滑开启与关闭

!!! tip ""
    车内所有按键的背光平滑地亮起和熄灭，看起来非常自然、漂亮。 
  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Suchbeleuchtung_allgemein:
- KL58 Einschalten mit Rampe →  Active
→ 应用
```

### 启停按键 Start-Stop Engine 的脉动呼吸

``` yaml title="登录密码: 20103"
单元 B7 Kessy 安全访问 → 适配:
DeveloperCoding Search lights:
- ZAT_illumination_concept_mybeat_clamp58xt: 激活
- ZAT_illumination_modus_mybeat_clamp58xt: 激活
→ 应用
```

### 颜色配置

+ [ODIS_E 无 RGB 车辆的 30 色色阶，用于 09 单元（适配）](../odis-files/09 – Шкала на 30 цветов.PRE)  
+ [ODIS_E 无 RGB 车辆的 10 色色阶，用于 09 单元（适配）](../odis-files/09 – Шкала на 9 цветов.PRE)

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior_light_2nd_generation / 第 2 代车内照明:
- Mittelkonsolenbeleuchtung mehrfarbig: акт
→ 应用
---
Interior_light_lamp_configuration / 车内照明, 灯具配置:
- Ambientemenue mit globalem aus: акт.
- Ambientemenue mit alle Zonen: акт.
- Ambient_Farbliste_HMI: акт.
→ 应用
---
Ambience_lightning_color_list / Ambientelicht Farbliste / 氛围灯
所有项的旧值: 0
— Rotwert Farbe 1: 217
— Gruenwert Farbe 1: 221
— Blauwert Farbe 1: 235
— Rotwert Farbe 2: 255
— Gruenwert Farbe 2: 172
— Blauwert Farbe 2: 5
— Rotwert Farbe 3: 253
— Gruenwert Farbe 3: 108
— Blauwert Farbe 3: 55
— Rotwert Farbe 4: 222
— Gruenwert Farbe 4: 70
— Blauwert Farbe 4: 20
— Rotwert Farbe 5: 252
— Gruenwert Farbe 5: 116
— Blauwert Farbe 5: 240
— Rotwert Farbe 6: 132
— Gruenwert Farbe 6: 76
— Blauwert Farbe 6: 222
— Rotwert Farbe 7: 0
— Gruenwert Farbe 7: 102
— Blauwert Farbe 7: 225
— Rotwert Farbe 8: 1
— Gruenwert Farbe 8: 192
— Blauwert Farbe 8: 255
— Rotwert Farbe 9: 0
— Gruenwert Farbe 9: 204
— Blauwert Farbe 9: 0
— Rotwert Farbe 10: 182
— Gruenwert Farbe 10: 255
— Blauwert Farbe 10: 57
	→ 应用
```

??? tip "这些数字是什么？"
    - Rotwert Farbe 1: 217
    - Gruenwert Farbe 1: 221
    - Blauwert Farbe 1: 235
  
    这是颜色选择色阶的 RGB 格式颜色。 
    可以在适配前用调色工具（例如 https://www.colorspire.com/rgb-color-wheel）编好自己想要的颜色列表
	
??? note "扩展颜色"
    扩展颜色在 9 单元的适配中设置： 
    Ambience_lightning_color_list_2

### 根据驾驶模式选择颜色

+ [ODIS_E 19 单元编码](../odis-files/19 – FPA AMB.PRE)
+ [ODIS_E 09 单元的驾驶模式绑定（适配）](../odis-files/09 – Привязка профилей движения.PRE)

!!! warning ""
    所装网关的软件版本不能低于 4344 或 5344，且索引为 Q 及以上

氛围灯菜单

``` yaml
单元 19 → 编码:
FPA_Funktion_AMB: 激活
→ 应用（需重启单元）
```

``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2:
- Menu_display_ambient_illumination — 开启
- Menu_display_ambient_illumination_clamp_15_off — 未激活
- Menu_display_ambient_illumination_over_threshold_high — 开启
- Menu_display_ambient_illumination_standstill — 未激活
- Menu_display_ambient_illumination_after_disclaimer — 未激活
→ 应用 
```

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior_light_lamp_configuration / 车内照明, 灯具配置:
- Ambientemenue mit globalem aus — акт.
- Ambientemenue mit alle Zonen — акт.
- Ambient_Farbliste_HMI — акт.
- Ambience_light_colorlist_default — 1 (或 0)
- Farbwahl ueber HMI — 未激活
- Farbwahl ueber Fahrprofil — 未激活
→ 应用

Interior_light_2nd_generation / 第 2 代车内照明:
- Ambiente_Fahrprofil_Individual — 7
- Ambiente_Farbwahl_FPA_waehlbare_Kopplung — active
- Ambiente_Farbwahl_FPA_waehlbare_Kopplung_Status_hmi_default — 已绑定 (coupled)
- Mittelkonsolenbeleuchtung mehrfarbig — акт.
→ 应用
```

驾驶模式

!!! tip "模式说明"
    Fahrprofil_0 — 熄火状态开门时  
    Fahrprofil_2 — 普通 — 蓝色  
    Fahrprofil_3 — 运动 — 红色  
    Fahrprofil_4 — 越野 — 浅紫色  
    Fahrprofil_5 — 经济 — 绿色  
    Fahrprofil_7 — 个性化 — 紫色  
    Fahrprofil_10 — 雪地 — 浅蓝  
    Fahrprofil_11 — 个性化越野模式  

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Ambientelicht Zuordnung der Farbe zum Fahrprofi:
- Fahrprofil_0 — 1
- Fahrprofil_1 — 1
- Fahrprofil_2 — 7
- Fahrprofil_3 — 4
- Fahrprofil_4 — 6
- Fahrprofil_5 — 9
- Fahrprofil_6 — 8
- Fahrprofil_7 — 5
- Fahrprofil_8 — 1
- Fahrprofil_9 — 1
- Fahrprofil_10 — 8
- Fahrprofil_11 — 1
- Fahrprofil_12 — 1
- Fahrprofil_13 — 1
- Fahrprofil_14 — 1
- Fahrprofil_15 — 1
→ 应用
```

模式切换速度
``` yaml title="登录密码: 31347"
单元 19 → 适配:
Driving Profile Selection Parameter:
- Driving Profile Selection Toogle Time Adaptation — 把 2000 ms 改为 0
→ 应用
```

### 打开行李厢时关闭车内照明

!!! tip ""
    最初打开行李厢盖时，不仅行李厢、连车内也会亮灯

``` yaml title="登录密码: 31347"
单元 09 → 适配:
第 2 代车内照明:
- Innenlicht bei offenem Heckdeckel einschalten: 停用
→ 应用
```
