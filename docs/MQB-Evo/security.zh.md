# 安全

### 在车辆菜单中启用自动中控锁

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
ZV_Autolock:
- ZV_autolock_autounlock_hmi: adjustable
→ Apply
```

### 关闭点火状态下开门时的警告音

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0159-0161

``` yaml 
Control unit 9 → Adjustments:
Clamp_Control:
- Ignition_Active_Message: No_display
→ Apply
```

### DSG 在 park 位时自动解锁车门

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
ZV_Autolock
- automatic_unlock_nar: active
→ Apply
```

### 关闭启停系统

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 7084-7312

``` yaml 
Control unit 19 → Adjustments:
Slave_component_list:
- Battery Monitoring Control Module: no
→ Apply
```

!!! note ""
    在 45V 电气系统的车辆上无效。  
    此外，网关中会残留错误："Subsystem_multiple_plug_identified"
    AID 或信息娱乐系统中不会出现错误提示。

### 关闭中控锁的在线解锁

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
OCU:
- Remote_Unlock_Lock: not_active
→ Apply
```

### 启用车库门遥控器

:octicons-verified-24: SFD: yes

``` yaml title="Tested SW: 0161"
Control unit 9 → Adjustments:
UGDO:
- ugdo_transmitter: installed
- ugdo_via_mmi_configurable: active
→ Apply
```

``` yaml title="Tested SW: 1941"
Control unit 5F → Adjustments:
Car_Function_List_BAP:
- UGDO_0x14_msg_bus: activated
- UGDO_0x14: clamp_15
Car_Function_Adaptations:
- menu_display_ugdo_over_threshold_high: activated
- menu_display_ugdo: activated
→ Apply
```

### 用车钥匙打开后备厢

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

``` yaml 
Control unit 9 → Adjustments:
ZV Heck:
- Direktauswurf_heckdeckel: active
→ Apply
```

### 点火开启时也能用钥匙切换中控锁

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0161

!!! error ""
    看不出有变化，也许在参数集中关联

``` yaml 
Control unit 09 → Adjustments:
ZV allgemein:
- Funk_bei_Kl15_ein: active
→ Apply
```

### 走开时自动落锁（忘记锁车时）

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0174 – 0183

!!! error ""
    仅在软件版本 0174 及以上可用。低于 0174 的版本无法实现。  
    从后备厢侧向走开时无效。

``` yaml 
Control unit 09 → Adjustments:
Automatische_Funktionen:
- Automatisches_Verriegeln_aktiv: activated
DevCod_IDGeber_Suche:
- Unterdrueckung_zyklischer _Suchen_bei_entriegeltem_Fahrzeug_aktiv: not_activated
DevCod_Nutzerkonfigurationen:
- HMIMenue_Aktivierung_Nah_Mittel_Fern_aktiv: activated
→ Apply
```

``` yaml title="Login code: 10587"
Control unit B7 → Adjustments:
Passive_Komfort:
- Passive_Komfort_Oeffnen_aktiv: activated
- Passive_Komfort_Togglen_aktiv: activated
DevCod_AutomatischeFunktionen:
- Slowpolling_Rechtecksignal_Aktiv: activated
→ Apply
```
