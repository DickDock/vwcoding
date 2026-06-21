# 雨刮 / 雨量光照传感器

### Swing 菜单中的雨刮维修位置
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper – Menuesteuerung Frontwischer: 激活
→ 应用
```

### 熄火时雨刮自动归位

!!! note ""
    解决熄火时雨刮停在玻璃中间半路的问题。
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper:
- Wischer stop bei KL15 aus: 停用
→ 应用
```

### 前雨刮的附加回刮（残滴擦拭）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Rear Window Wiper – Traenenwischen Heck: 激活
Windshield wiper – Traenenwischen Front Status: 激活
→ 应用
```

### 更改光照传感器灵敏度
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Assistance light functions-Lichtsensorempfindlichkeit → 由 normal (正常) 改为 "non sensitive" (不灵敏)
→ 应用
```

### 关闭大灯清洗
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper-SRA Waschzeit → 把 2300 ms 改为 0
→ 应用
```

### 增大大灯清洗的触发间隔与时间

负责在第几次洗挡风玻璃时触发大灯清洗的参数。  
若把标准的「9」改为 1 — 则每次都会触发。  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper-Anzahl Betaetigungen Frontwaschanlage pro SRA Aktivierung → 输入「15」
→ 应用
```

负责挡风玻璃清洗拨杆保持时长（达到该时长才触发大灯清洗）的参数
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper — SRA Verzoegerungszeit → 把标准的 0 ms 改为例如 1500 ms (1,5 秒)
→ 应用
```

大灯清洗工作几秒
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper — SRA Waschzeit → 标准值 600 ms。
→ 应用
```

### 关闭挂倒挡时后雨刮的触发
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Rear Window Wiper-Komfortwischen Heck → not active
→ 应用
```
或通过车机菜单

### 后雨刮自动开启

!!! note ""
    当前雨刮长时间以 2 档连续工作时，后雨刮开始触发。
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Rear Window Wiper – Automatisches Heckwischen: 激活
→ 应用
```

### 雨刮除霜位置
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Windshield wiper – Frontwischer Abtauposition → Abtauposition temperaturunabhaengig Referenzwischen 
→ 应用
```
