
# 安全

### 按点火状态锁门（中控锁）
:octicons-verified-24: Audi
``` yaml
单元 46 → 编码:
central_locking_system_lock_unlock_at_engine_running: 激活
→ 应用
```

### 自动开门（仅开门，不会自动关门）
:octicons-verified-24: Audi
``` yaml
单元 46 → 编码:
automatic_opening: not_active: 激活
automatic_closing: not_active: 激活
keyless_light_illumination: not_active: 激活
→ 应用
```

``` yaml
单元 46 → 适配:
Personalized_settings_vehicle:
- Keyless_access_automatic_open: not_active: 激活
→ 应用
```

### 发动机运行时锁车

``` yaml
单元 46 → 编码:
字节 9 – 位 7: 激活 
→ 应用（需重启单元）
```

### 撤防时的声音确认

!!! note ""
    需配备原厂防盗报警
  
``` yaml
单元 46 → 编码:
字节 4 – 位 6: 激活 
→ 应用（需重启单元）
```
``` yaml
单元 46 → 适配:
Sounder_settings:
- Beeptime_opening_central_locking: double_beep
→ 应用
```

车机中会出现相应菜单

### 用车门上的按键开/关已启动的车辆

``` yaml
单元 46 → 编码:
central_locking_system_lock_unlock_then_engine_running: yes
unlocking_hatchback_via_kessy_at_s_contact_active: yes
```
