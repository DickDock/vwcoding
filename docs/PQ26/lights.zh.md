
# 灯光控制

### 开后备厢时关闭牌照灯
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte 25KZL HA60-Light_Control_HD_AB_25 – 把「Always」改为「Only if closed」
→ 应用
```

### 开后备厢时停用车内照明
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Interior lighting-Innenlicht bei offenem Heckdeckel einschalten, 把「active」改为「not active」
→ 应用
```

### 转向灯与 LED DRL 交替闪烁
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte4TFL LB43-Light_Function_G_4, Blinken links/rechts Hellphase
Leuchte4TFL LB43-Dimming_GH_4, 0
Leuchte4TFL LB43-Dimming_Direction_GH_4, minimize
Leuchte5 TFL RB6-Light_Function_G_5, Blinken links/rechts Hellphase
Leuchte5 TFL RB6-Dimming_GH_5, 0
Leuchte5 TFL RB6-Dimming_Direction_GH_5, minimize
→ 应用
```

### 拉手刹时熄灭 DRL
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Daytime running lights-Tagfahrlicht Dauerfahrlicht bei Handbremse abschalten — active
19 款：
Aussenlicht_Front-Tagfahrlicht_Dauerfahrlicht_bei_Handbremse_abschalten: 激活
→ 应用
```

### 仅在灯光开关 AUTO 位时点亮 DRL
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Daytime running lights-Tagfahrlicht nur in Schalterstellung AUTO,active
19 款：
Aussenlicht_Front — Tagfahrlicht nur in Schalterstellung AUTO,激活
→ 应用
```

### CORNER 功能（用前雾灯照亮转弯）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
（无 Coming Home/Leaving Home 的车辆）:
Leuchte12NL LB40-Light_Function_B_12 — Abbiegelicht links
Leuchte13NL RB3-Light_Function_B_13 — Abbiegelicht rechts
（已激活 Coming Home/Leaving Home 的车辆）:
Leuchte12NL LB40-Light_Function_C_12 – Abbiegelicht links
Leuchte12NL LB40-Dimming_CD_12 – 100
Leuchte12NL LB40-Dimming_Direction_CD_12 – maximize
Leuchte13NL RB3-Light_Function_C_13 – Abbiegelicht rechts
Leuchte13NL RB3-Dimming_CD_13 – 100
Leuchte13NL RB3-Dimming_Direction_CD_13 – maximize
设定 CORNER 的开启/关闭速度:
static AFS light-Lower speed threshold, 0.0 km/h
static AFS light-Upper speed threshold, 40.0 km/h (可设为 50 km/h)
挂倒挡时点亮两个前雾灯（出厂带此功能时为标准）
static AFS light-bei Rueckwaertsfahrt – both sides
→ 应用
```

### LED 牌照灯（适配）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte25KZL HA60-Type_Of_Load_25 — 2* 5W – 把值改为「LED Kleinleistung ohne Open Load Diagnose」(LED)
Leuchte25KZL HA60-Dimming_AB_25 – 100 – 改为「127」
→ 应用
```

### 激活右后雾灯
```
Rapid 上无法实现。没有单独负责右后雾灯的通道。到灯的导线缺失。
可从左灯引线供电。
```

### 后示廓灯随 DRL 一起点亮（带牌照灯和仪表照明）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Daytime running lights-Tagfahrlicht-Dauerfahrlicht aktiviert zusaetzlich Standlicht: active
19 款：
Aussenlicht_Front-Tagfahrlicht-Dauerfahrlicht aktiviert zusaetzlich Standlicht: 激活
→ 应用
```

### DRL 模式下点亮后示廓灯（不带牌照灯和仪表照明）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte23SL HLC7-Light_Function_D_23 → 选择 – Daytime running lights → 保存
Leuchte24SL HRA69-Light_Function_D_24 → 选择 → Daytime running lights → 保存
Leuchte23SL HLC7-Dimming_CD_23:  「75」 → 保存
Leuchte24SL HRA69-Dimming_CD_24:  「75」 → 保存
→ 应用
```

### 频闪灯：前雾灯 — 远光

!!! warning "" 
    采用这种编码时，无法把远光与前雾灯同时使用。
  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Driving light and parking light:
- max_scheinwerfer_2limitieren: 激活
19 款：
Aussenlicht_Front:
- max_scheinwerfer_2limitieren → in_Betrieb_lassen: 激活
→ 应用
```

### 频闪灯：前雾灯 — 远光（晃远光时）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte12NL LB40-Light_Function_G_12: 由 not active 改为 Headlamp flasher
Leuchte12NL LB40-Dimming_Direction_GH_12: 由 maximize 改为 minimize
Leuchte13NL RB3-Light_Function_G_13: 由 not active 改为 Headlamp flasher
Leuchte13NL RB3-Dimming_Direction_GH_13: 由 maximize 改为 minimize
→ 应用
```

### 频闪灯：近光 – 远光（晃远光时）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte6ABL LB44-Light_Function_C_6, 由「not active」改为「Headlamp flasher」
Leuchte6ABL LB44-Dimming_Direction_CD_6, 由「maximize」改为 minimize
Leuchte7ABL RB5-Light_Function_C_7, 由「not active」改为「Headlamp flasher」
Leuchte7ABL RB5-Dimming_Direction_CD_7, 由「maximize」改为 minimize
→ 应用
```

### 频闪灯：DRL LED – 远光
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Leuchte4TFL LB43-Light_Function_G_4 – Lichthupe (Headlamp flasher)*
Leuchte4TFL LB43-Dimming_GH_4 → 0
Leuchte4TFL LB43-Dimming_Direction_GH_4 – minimize
Leuchte5 TFL RB6-Light_Function_G_5 – Lichthupe (Headlamp flasher)*
Leuchte5 TFL RB6-Dimming_GH_5 – 0
Leuchte5 TFL RB6-Dimming_Direction_GH_5 – minimize
→ 应用
```

### Coming Home（灯光送行）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Comfort illumination-Coming Home Verbaustatus – automatic (带光照传感器的车辆) 或 manual (无光照传感器的车辆)
Comfort illumination-Menuesteuerung Coming Home Werkseinstellung – active
Comfort illumination-Menueeinstellung Cominghome – 10 s (功能工作时长)
Comfort illumination-Coming Home Leuchten – Low beam (通过近光) 或 Fog light (通过前雾灯)
Comfort illumination-Coming-home Einschaltereignis – Driver door(由驾驶员车门触发) 或 Ignition(由点火触发)
Comfort illumination-Helligkeitsschwelle Infrarot-Messung –0
如果选用近光：
Leuchte6ABL LB44-Light_Function_B_6 – Coming Home Leaving Home
Leuchte7ABL RB5-Light_Function_B_7 – Coming Home Leaving Home
如果选用前雾灯：
Leuchte12NL LB40-Light_Function_B_12 — Coming Home Leaving Home
Leuchte13NL RB3-Light_Function_B_13 — Coming Home Leaving Home
灯光迎接 — Leaving-Home（仅在有光照传感器时）
Comfort illumination-Leaving-Home Verbausstatus – Enabled
Comfort illumination-lho_aktiviert – active
Comfort illumination-lho_zeit – 10 s
Coming Home/ Leaving Home 配倒车灯
Leuchte28RFL C3-Light_Function_C_28 – Coming Home Leaving Home
Leuchte28RFL C3-Dimming_CD_28 – 100
Leuchte28RFL C3-Dimming_Direction_CD_28 – maximize
19 款：
Aussenlicht_uebergreifend — Coming Home Verbaustatus – automatic (带光照传感器的车辆) 或 manual (无光照传感器的车辆)
Aussenlicht_uebergreifend — Menuesteuerung Coming Home Werkseinstellung – active
Aussenlicht_uebergreifend — Menueeinstellung Cominghome – 10 s
Aussenlicht_uebergreifend — Coming Home Leuchten – Low beam (近光) 或 Fog light (前雾灯)
Aussenlicht_uebergreifend — Coming-home Einschaltereignis – Driver door (带光照传感器的车辆) 或 Ignition (无光照传感器的车辆)
Aussenlicht_uebergreifend — Helligkeitsschwelle Infrarot — Messung – 72.0
如果选用近光：
Leuchte6ABL LB44 — Light_Function_B_6 – Coming Home Leaving Home
Leuchte7ABL RB5 — Light_Function_B_7 – Coming Home Leaving Home
如果选用前雾灯：
Leuchte6ABL LB44 — Light_Function_B_6 – 改为 not active
Leuchte7ABL RB5 — Light_Function_B_7 – 改为 not active
Leuchte12NL LB40-Light_Function_B_12 — Coming Home Leaving Home
Leuchte13NL RB3-Light_Function_B_13 — Coming Home Leaving Home
灯光迎接 — Leaving-Home（仅在有光照传感器时）
Aussenlicht_uebergreifend — Leaving-Home Verbausstatus – Enabled (允许)
Aussenlicht_uebergreifend — lho_aktiviert – active
Aussenlicht_uebergreifend — lho_zeit – 10 s
→ 应用
```

### 舒适转向灯（19 款）

!!! note ""
    可能的搜索名称：Au?enlicht_Blinker, Komfortblinken, Blinkzyklen。
  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Aussenlicht_Blinker:
- Komfortblinken_Blinkzyklen – 选择 1 到 5 之间的值（出厂默认 – 3）
→ 应用
```
