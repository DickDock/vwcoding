# 车门、车窗、中控锁、遥控钥匙与原厂防盗

### 关闭安全带未系提醒
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 00 – 位 2-4: 改为值 00
→ 应用
```

### 关闭开门时「点火已开启」的（声音/消息）提示
``` yaml
单元 17 (5JA 920 7XX) → 适配:
Ignition active message – actuator — 原为「Driver door」, 改为「No display」
→ 应用
```

### 开任意车门时开启「点火已开启」的（声音/消息）提示
``` yaml
单元 17 (5JA 920 7XX) → 适配:
Ignition active message – actuator — 原为「Driver door」, 改为「All Doors」
→ 应用
```

### 为不带 Swing/Bolero 的 Entry/Activ 配置实现车门自动上锁/解锁：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control – automatisches Verriegeln bei Geschwindigkeit: 激活
Access control – automatisches Entriegeln: 激活
Access control – Autolock Autounlock wirkt auf Heck —→ active 
→ 应用
```
19 款：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV Autolock – Autolock_Autounlock_wirkt_auf_Heck: 激活
ZV Autolock – automatisches_Entriegeln: 激活
ZV Autolock – Automatisches_Verriegeln_bei_Geschwindigkeit: 激活
→ 应用
```

### 车速达到 15 km/h 时自动锁门，拔钥匙时解锁。

!!! tip "可选项"
    Clobal Entriegelung — 所有车门一起  
    Einzeltuerentriegelung – 驾驶员车门单独打开  
    Seitenselektive Oeffnung – 同一侧的所有车门  
    Individuell selective Oeffnung Kessy – 使用无钥匙进入系统时的单独开门  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control – automatisches Verriegeln bei Geschwindigkeit: 激活
Access control – automatisches Entriegeln: 激活
Access control – ZV Türentriegelung → 原为 Clobal Entriegelung
→ 应用
```

### 发动机运转时遥控钥匙无线电通道工作
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control – Funk bei Klemme 15 ein: 激活
→ 应用
```
19 款
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV allgemein – Funk bei Klemme 15 ein: 激活
→ 应用
```

### 熄火时喇叭工作
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Auxiliary functions – Signalhorn ohne KL15: 激活
→ 应用
```

### 激活原厂防盗报警
``` yaml title="登录密码: 31347"
单元 09 → 长编码:
字节 12 – 位 0: 激活
→ 应用
```
用原厂遥控钥匙锁车后，再用钥匙开门时会触发：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control – Akustischer Alarm Signalhorn: 激活
→ 应用
```
用钥匙转动门锁芯时触发：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control – DWA Alarmverzoegerung → 由「immidiat_driver_door_contact_thatcham」改为「delay_driver_door_lock_cylinder_skoda」
→ 应用
```

!!! note ""
    要使其生效需从内存重新读取单元设置（用原厂防盗设防/撤防一次，持续 5–10 秒）

### 开启原厂遥控器开/关锁的声音确认（无原厂防盗）
\+ 在 Swing2 菜单中添加该功能的控制项
``` yaml
单元 09 → 长编码: 
字节 5 – 位 0: 激活
字节 5 – 位 2: 激活
字节 5 – 位 4: 激活
→ 应用
```
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Acknowledgement signals — Akustische Rueckmeldung entriegeln: "Active" (开锁时的声音)
Acknowledgement signals — Akustische Rueckmeldung verriegeln: "Active" (关锁时的声音)
Acknowledgement signals — Dauer der Akustischen Rueckmeldung vom Einfachhorn: kurz (kurz — 短促声（感觉上刚开始响就立刻中断）；normal — 正常, 比短促稍长（如同正常按一下喇叭的声音）)
Acknowledgement signals – Optical feedback during locking → Decelerate
Acknowledgement signals – Optische Rueckmeldung Komfortschliessen: 激活
Acknowledgement signals – Optische Rueckmeldung 3.Bremsleuchte → not active
Acknowledgement signals — Menuesteuerung akustische Rueckmeldung: "Active" (Swing 中「开锁/关锁…」一节里的项)
Acknowledgement signals – Akustische Rueckmeldung global: 激活
Acknowledgement signals — Akustische Rueckmeldung Signalhorn: "Active" (声音)
→ 应用
```

### 通过原厂喇叭实现撬车报警（19 款）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Anti-theft device – Akustischer_Alarm_Signalhorn: 激活
Anti-theft device – anti_theft_alarm_system: 激活
Anti-theft device – Alarmsignal: frequency modulated
Anti-theft device – Sirenen_Alarmzahl: 10 Alarme
→ 应用
```

### 熄火时车窗升降器工作
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2 – Freigabenachlauf FH bei Kl 15 aus → 由 not active 改为 active
→ 应用
```
19 款：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV Komfort (Fensterheber) - Freigabenachlauf FH bei Kl 15 aus: 激活
→ 应用
```

### 设定熄火后驾驶员车门车窗升降器的工作时长
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2-FH SAD Kl15Aus Freigabezeit: 600 s (熄火后 10 分钟)
→ 应用
```
19 款：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV Komfort (Fensterheber)-FH SAD Kl15Aus Freigabezeit → 600 s
→ 应用
```

### 开门时车窗升降器工作
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2-Freigabenachlauf FH bei Tueroeffnen → 由 not active 改为 active
→ 应用
```
19 款：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV Komfort (Fensterheber)-Freigabenachlauf FH bei Tueroeffnen: 激活
→ 应用
```

### 用原厂遥控钥匙舒适控制驾驶员车门车窗升降器
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2 – Comfort closing: 激活
Access control 2 – Comfort opening: 激活
Access control 2 – Fahrertuerbedienung Fensterheber oeffnen: 激活
Access control 2 – Fahrertuerbedienung Fensterheber schliessen: 激活
Access control 2 – Funk Komfort oeffnen: 激活
Access control 2 – Funk Komfort schliessen: 激活
Access control 2 – Komfortbedienung global: 激活
Access control 2 – Menuesteuerung Komfortbedienung einstellbar → adjustable
→ 应用
```
然后需在车机弹出的菜单中开启相应选项。

对于使用简单 blues 车机的人，只需激活：
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2 – Comfort closing: 激活
Access control 2 – Comfort opening: 激活
Access control 2 – Funk Komfort oeffnen: 激活
Access control 2 – Funk Komfort schliessen: 激活
Access control 2 – Komfortbedienung global: 激活
→ 应用
```

### 锁车时自动关闭驾驶员车门车窗（19 款）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
ZV Komfort (Fensterheber) - 舒适关窗: 激活
ZV Komfort (Fensterheber) - 舒适开窗: 不激活
ZV Komfort (Fensterheber) - BAP_Komfortschliessen: 激活
ZV Komfort (Fensterheber) - Fahrertuerbedienung Fensterheber oeffnen: 激活
ZV Komfort (Fensterheber) - Fahrertuerbedienung Fensterheber schliessen: 激活
ZV Komfort (Fensterheber) - Funk Komfort oeffnen: 激活
ZV Komfort (Fensterheber) - Funk Komfort schliessen: 激活
ZV Komfort (Fensterheber) - Komfortbedienung global: 激活
ZV Komfort (Fensterheber) - Menuesteuerung Komfortbedienung einstellbar: adjustable
ZV Komfort (Fensterheber) - Schliesszylinder_Komfort_oeffnen: 激活
ZV Komfort (Fensterheber) - Schliesszylinder_Komfort_schliessen: 激活
→ 应用
```
