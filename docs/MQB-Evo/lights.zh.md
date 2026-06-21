# 灯光管理

### 发动机启动时的 IQ-Light 演示

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 1447

!!! warning ""
    仅适用于配备 IQ-Light 的车辆。

``` yaml 
Control unit 4B [Tested SW: 1447]
Adjustments:
Präsentationslauf_dynamisches_Kurvenlicht:
- Präsentationslauf_dynamisches_Kurvenlicht: aktiv
Reference_Run_Start_Condition:
- Reference_Run_Start_Condition: Motorstart / “Klemme 15” when turning on the ignition
Reference_Run_Activation_Effect:
- par_Reference_Run_Activation_Effect: Activation effect enabled by mtor start
```

### 根据光线灵敏度改变灯光功能

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 9 → Adjustments:
Lighting_Assist_Adaptation:
- Lichtsensorempfindlichkeit: normal (Adjust as desired)
→ Apply
```

### 保存远光辅助设置（在点火状态切换时）

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 9 → Adjustments:
Fernlicht_assistent:
- Fernlichtassistent Reset: not_active
→ Apply
```

### 在车辆菜单中激活可调日间行车灯

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 9 → Adjustments:
Tagfahrlicht:
- Tagfahrlicht Aktivierung durch BAP oder Bedienfolge moeglich: active
→ Apply
```

### 在车辆菜单中可调的 DWA 确认音（上锁与解锁）

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 9 → Adjustments:
ZV Quittierungen:
- Quittungston_hmi_einstellbar: active
- Quittierungston_bei_entriegeln: active
- Quittungs_ton_bei_verriegeln: active
→ Apply
```

仅当没有报警系统、或没有通过喇叭发出的确认音时：

```
Quittungston_ueber_hupe: active
```

### 尾灯作为日间行车灯

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
Tagfahrlicht:
- Tagfahrlicht-Dauerfahrlicht aktiviert zusaetzlich Standlicht: active
→ Apply
```

### 调节 Coming Home 灯光

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
BAP_Funktionsstatus:
- Coming_home_Leuchten: Abblendlicht oder Nebellicht
→ Apply
```

### 关闭"灯光已关闭"警告

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
Fahrlichthinweis:
- Fahrlicht_Hinweis_mehrfach: not_active
- Fahrlichtwarnung_Hinweis_Konfig: kein_Hinweis
→ Apply
```

### 天黑时仍保持灯光关闭

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
Licht_bedienung:
- LTM_BGL_Wegabhängig: not_active
- LTM_BGL_Geschwindigkeitsabhängig: not_active
- LTM_BGL_Geschwindigkeitsabhängig_Parameter: not_active
- LTM_GlobalOFF_Wegabhängig: not_active
- LTM_GlobalOFF_Geschwindigkeitsabhängig: not_active
- LTM_GlobalOFF_Geschwindigkeitsabhängig_Parameter: not_active
- Beleuchtung_LTM_Auto_LED_58xt_logik: not_active
- Beleuchtung_Auto_LED_bei_Nebelfunktion: not_active
→ Apply
```

### 上锁和解锁车辆时让转向灯闪烁

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 09 → Adjustments:
Dynamisch Blinken:
- ZV_Blinken_zu: active (oder not_active für deaktiviert)
- ZV_Blinken_auf: active (oder not_active für deaktiviert)
→ Apply
```

### 调节 coming home 和 leaving home

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 09 → Adjustments:
Coming-Home_and_Leaving-Home:
- Menueeinstellung CHO LHO: Menuesteuerung aktivieren
Coming-Home_and_Leaving-Home:
- Menueeinstellung Leaving-home Zeit per BAP: 10 seconds (bis 90 sec)
- Menueeinstellung Cominghome: 10 seconds (bis 90 sec)
- Menueeinstellung Cominghome bei Tag: 10 seconds (bis 90 sec)
- Menueeinstellung Leaving-home bei Tag: 10 seconds (bis 90 sec)
→ Apply
```

### 白天也启用 coming home 和 leaving home（灯光开关在 "Auto" 位置）

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 09 → Adjustments:
Coming-Home_and_Leaving-Home:
- Tagfahrlicht mit CHO bei Tag in Stellung AUTO: active
- Tagfahrlicht mit LHO bei Tag in Stellung AUTO: active
→ Apply
```

### 灯带（两侧大灯之间）作为日间行车灯

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

!!! error ""
    看不出有变化，也许在参数集中关联

2020 年 CW45 车型之前：
``` yaml 
Control unit 09 → Adjustments:
Leuchte 2 SL VL B20:
- Lichtfunktion B 2: Tagfahrlicht
Leuchte 3 SL VR B32:
- Lichtfunktion B 3: Tagfahrlicht
→ Apply
```

2020 年 CW48 车型起：
``` yaml 
Control unit 09 → Adjustments:
Leuchte 31 AMBL 1 C61:
- Lichtfunktion B 31: Tagfahrlicht
Leuchte 32 AMBL 2 C35:
- Lichtfunktion B 32: Tagfahrlicht
→ Apply
```

### 关闭灯带（两侧大灯之间）

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

!!! error ""
    看不出有变化，也许在参数集中关联

2020 年 KW48 之前：
``` yaml 
Control unit 09 → Adjustments:
Leuchte 2 SL VL B20:
- Lichtfunktion A 2: not_active
- Lichtfunktion D 2: not_active
Leuchte 3 SL VR B32:
- Lichtfunktion A 3: not_active
- Lichtfunktion D 3: not_active
→ Apply
```

2020 年 KW48 之后：
``` yaml 
Control unit 09 → Adjustments:
Leuchte 31 AMBL 1 C61:
- Lichtfunktion A 31: not_active
- Lichtfunktion D 31: not_active
Leuchte 32 AMBL 2 C35:
- Lichtfunktion A 32: not_active
- Lichtfunktion D 32: not_active
→ Apply
```

### 两侧示廓灯

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 09 → Adjustments:
Standlicht:
- Parklicht ueber LSS aktiviert: dual sided
→ Apply
```
