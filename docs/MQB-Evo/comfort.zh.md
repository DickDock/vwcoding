# 舒适

### 关闭后窗雨刮的间歇刮水功能

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
Heckwischer_steuerung:
- Traenenwischen Heck: not_active
→ Apply
```

### 启用后窗雨刮的自动激活

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
Heckwischer_steuerung:
- Automatisches Heckwischen: active
Geschwindigkeit, anpassen wie gewünscht:
- Komofortwischen Heck Intervallpausenzeit Stufe Intervall LSS AUS: 10 [UN]_s
- Komofortwischen Heck Intervallpausenzeit Stufe Intervall: 7 [UN]_s
- Komofortwischen Heck Intervallpausenzeit Stufe Automatik: 7 [UN]_s
- Komofortwischen Heck Intervallpausenzeit Stufe 1: 5 [UN]_s
- Komofortwischen Heck Intervallpausenzeit Stufe 2: 3 [UN]_s
- Einzelansteuerung Heckintervallwischen Zeitintervall 1: 8 [UN]_s
- Einzelansteuerung Heckintervallwischen Zeitintervall 2: 16 [UN]_s
→ Apply
```

### 开/关车门时自动升降车窗

:octicons-verified-24: SFD: no

``` yaml title="Tested SW: 0330-0350"
Control unit 42 → Coding:
short_drop: active
→ Apply
```

``` yaml title="Tested SW: 0330-0350"
Control unit 52 → Coding:
Coding:
short_drop: active
→ Apply
```

### 后视镜折叠时激活迎宾照地灯

:octicons-verified-24: SFD: no

``` yaml title="Tested SW: 0330"
Control unit 42 → Coding:
turn_off_front_field_light_with_folded_mirror: not_active
→ Apply
```

``` yaml title="Tested SW: 0330"
Control unit 52 → Coding:
Coding:
turn_off_front_field_light_with_folded_mirror: not_active
→ Apply
```

### 用遥控钥匙舒适开/关天窗

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0040

``` yaml 
Control unit CA → Adjustments:
Control_unit_for_sun_roof_convenience_functions:
- Convenience_opening_target_attitude: sliding_position
→ Apply
```

### 行驶中保持天窗翘起角度

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0040

``` yaml 
Control unit CA → Adjustments:
Speed_dependent_control:
- Sliding_sunroof_reduce_tilting_position: not_active
→ Apply
```

### 调节或关闭发动机声浪发生器

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 0001

``` yaml 
Control unit A9 → Adjustments:
Loudness_actuator_for_structure_borne_sound: 0-100% (0 = off, 1-100% = volume)
→ Apply
```

### 调节方向盘加热的自动启动温度

:octicons-verified-24: SFD: ??? :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
LIN-SMLS_konfig_1:
- k_i_offset: 4 [UN]_°C (Below 4°C is considered cold, for example)
→ Apply
```

### 在抬头显示上显示圈速计时器

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 2032

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 82 → Adjustments:
Laptimer: yes
→ Apply
```

### 调节座椅通风

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161-0183

``` yaml 
Control unit 09 → Adjustments:
Sitzlüfterkennlinie:
- Level_1_Sitz: 30 % (stage 1)
- Level_1_Lehne: 30 % (stage 1)
- Level_2_Sitz: 30 % (stage 1)
- Level_2_Lehne: 30 % (stage 1)
- Level_3_Sitz: 50 % (stage 2)
- Level_3_Lehne: 50 % (stage 2)
- Level_4_Sitz: 50 % (stage 2)
- Level_4_Lehne: 50 % (stage 2)
- Level_5_Sitz: 75 % (stage 3)
- Level_5_Lehne: 75 % (stage 3)
- Level_6_Sitz: 80 % (stage 3)
- Level_6_Lehne: 80 % (stage 3)
→ Apply
```

### 通过门把手舒适开窗

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161-0183

!!! Note ""
    要求：门把手内置传感器 (Kessy)

``` yaml 
Control unit 09 → Adjustments:
Kessyfunktion:
- Komfortbedienung_fh_oeffnen_ueber_kessy: active

ZV Komfort_Fensterheber:
- Komfortbedienung_fh_oeffnen_ueber_sz: active
- Komfort_oeffnen: active
→ Apply
```

``` yaml title="login code: 10587"
Control unit B7 → Adjustments:
Passive_Komfort:
- Passive_Komfort_Oeffnen_aktiv: activated
- Passive_Komfort_Togglen_aktiv: activated
→ Apply
```
