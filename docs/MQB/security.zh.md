# 安全

## 中控锁

### 电动行李厢盖参数集

| 车辆         | 参数集<br/>(ODIS XML)                    | 备注                     |
|:-------------|:-----------------------------------------|:-------------------------|
| 所有品牌     | [(下载)](../parameters/6D.ZIP)           | 所有可能的参数集         |


### Kick Close – 用脚的动作关闭行李厢
!!! note ""
    对于 Tiguan，B7 单元的固件版本不能低于 N。  
    对于 Superb，L 即可。  
    如果 BCM 单元硬件低于 H38，则无法把 B7 单元固件升到高于 G  

``` yaml title="登录密码: 31347"
单元 09 → 适配:
- Kick_and_close: installed
→ 应用
```
``` yaml title="登录密码: 31347"
单元 B7 → 适配:
- Coding_kick and_close_function: 激活
- Coding_easyclose_locking:  激活
→ 应用
```

### 在无报警系统时激活防盗系统功能
:octicons-verified-24: Škoda Karoq  
如果在不用钥匙的情况下打开已锁的车门（例如砸碎玻璃），车辆会鸣警

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Anti-theft device:
- Akusticher Alarm Signalhorn: 激活
- Diebstahlwarnangle: 激活
→ 应用
```
 
### 激活 Easy Open

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Verdecksteuergeraet:
- Virtuelles_Pedal_HMI_einstellba: 激活
- Virtuelles_Pedal_Verbau: 激活
- Virtuelles_Pedal: 激活
→ 应用
```

``` yaml title="登录密码: 20103"
单元 B7 → 适配:
Byte9_VIP:
- active_vip: 激活
- 行李厢门开启控制单元, 传感器 1, 阈值 1: 5 → 69
- 行李厢门开启控制单元, 传感器 1, 定时器值 3: 0 → 9
- 行李厢门开启控制单元, 传感器 1, 定时器值 4: 226 → 34
- 行李厢门开启控制单元, 传感器 1, 定时器值 5: 255 → 34
- 行李厢门开启控制单元, 传感器 2, 定时器值 5: 108 → 24
- 行李厢门开启控制单元, 车型: fe → 22
```

!!! warning ""
	编码后需执行执行机构测试
	Control_supply_voltage_vip
	
### 用 Easy Close 按键关闭行李厢门时设防

!!! tip ""
    有了此功能，按下行李厢延迟关闭按键后，车辆会完全自行落锁。  
    车辆会发出关闭提示音
  
=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 B7 → 编码:
    byte9_Vip
    - Coding_easy close_locking: 激活
    → 应用
    ```

=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 20103"
    单元 B7 授权访问: 激活
    byte9_Vip 
    - coding easy close locking: 激活
    ```

### 调节原厂报警的体积传感器灵敏度

``` yaml title="登录密码: 31347"
单元 09 → 适配:
防盗报警, 车内监控 / Interior_Monitoring_Sensitivity:
- 灵敏度 / sensitivity: 70%（默认 100%）
→ 应用
```

### 用遥控器按键开关行李厢

``` yaml title="登录密码: 20103"
单元 B7 → 适配:
byte9_Vip:
- Coding_kick and_close_function: 激活
→ 应用
```

### 选择性开门

!!! tip ""
    首次按开门键时只打开驾驶员车门。  
    再次按下时（需在首次按下后 5 秒内）会打开其余所有门。

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 适配:
    Central Locking 
    - Selective (Single) Door Locking: 激活
    → 应用
    ```

=== "在 VCDS 中编码" 
    ```yaml title="登录密码: 31347"
    09-中央电子  
    编码 - 07 → 长编码:
    字节 0 – 位 0 (Selective Central Locking (Single Door Locking) active): 激活  
    退出 → 保存  
    ```

### 起步时自动落锁、拔钥匙时自动解锁

``` yaml title="登录密码: 20103"
单元 B7 → 适配:
ZV Autolock:
- Automatisches Entriegeln: 停用（关闭解锁）
- Automatisches Verriegeln bei Geschwindigkeit: 停用（关闭落锁）
→ 应用
```
  
### 点火开启时遥控钥匙仍可用

!!! tip ""
    有了此功能，可以发动车辆、锁车、走开，仍能用钥匙远程开启车辆或行李厢。

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 适配:
    ZV allgemein (Access control) 
    - Funk bei Klemme 15 ein: 激活
    → 应用
    ```

=== "在 OBD11 中编码" 
    ``` yaml title="登录密码: 31347"
    09 车载电气网络控制单元 → 安全访问 (登录: 31347) → 适配  
    ZV allgemein 
    - Funk bei Klemme 15 ein: 激活
    ``` 

### 点火开启时 Kessy 门把手仍工作

=== "在 ODIS 中编码"
    ``` yaml
    单元 B7 → 编码:
    Terminal 15 characteristics of passive entry exit function
    - 原值 – Function only allowed for terminal 15 off
    - 新值 – Function only allowed for terminal 15 on or off
    → 应用
    ```

=== "在 VCDS 中编码" 
    ``` yaml
    单元 B7  
    编码 - 07 → 长编码 → 允许 ASAM 数据:
    字节 0 – 位 4 (Terminal 15 characteristics of passive entry exit function): 激活  
    退出 → 保存
    ```
  
### 关闭驾驶员车门时自动设防

=== "在 ODIS 中编码"
    ``` yaml
    单元 B7 → 编码:
    Locking for door slamming active: 激活
    → 应用
    ```

=== "在 VCDS 中编码" 
    ``` yaml
    单元 B7  
    编码 - 07 → 长编码 → 允许 ASAM 数据:
    字节 1 – 位 4 (关门动作锁门已开启): 激活  
    退出 → 保存
    ```
  
### 中控锁开/关时的声音提示

``` yaml title="登录密码: 31347"
单元 09 → 适配:
应答信号:
- Akustische Rueckmeldung entriegeln (开车): 激活
- Akustische Rueckmeldung verriegeln (锁车): 激活
- Menuesteuerung akustische Rueckmeldung: 激活
- Akustische Rueckmeldung global: 激活
- Akustische Rueckmeldung Signalhorn: 激活
→ 应用
```

!!! warning ""
    编码后需在车机菜单中勾选

### 长按遥控钥匙按键开关天窗（随中控锁一起关闭）

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Schiebedach:
- SAD Komfort schliessen: 激活
- SAD Komfort oeffnen: 激活
→ 应用
```

完全打开天窗

=== "在 ODIS 中编码"
    ``` yaml
    单元 00CA – 滑动天窗控制单元 → 适配:
    Control_unit_for_sun_roof_convenience_functions / Power sunroof control module – convenience function
    - Convenience_opening_target_attitude / 舒适开启时的目标位置: Tilting_position → Sliding_position
    → 应用
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 00CA – 滑动天窗控制单元 → 适配:
    Komfortfunktionen
    - 舒适开启时的目标位置: 掀起位置 → 滑移位置
    → 应用
    ```

## 驾驶员位置舒适入座

!!! tip ""
    Easy Entry 功能 —— 轻松入座，关闭点火并开门后座椅后移，开启时复位
  
``` yaml
单元 36 – 驾驶员座椅调节单元 → 编码:
字节 3 – 位 1 (Easy_Entry_front): 激活
字节 9 – 位 6 (Easy_Entry_front_over_MMI): 激活
→ 应用（需重启单元）
```

``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2:
- menu_display_seat_configuration: 激活
- menu_display_seat_configuration_over_threshold_high: 激活
→ 应用 

Car_Function_List_BAP_Gen2:
- driver_seat_0x10: 激活
- driver_seat_0x10_msg_bus — 舒适总线
→ 应用 
```

## 乘客位置舒适入座

!!! tip ""
    Easy Entry 功能 —— 轻松入座，关闭点火并开门后座椅后移，开启时复位
  
``` yaml
单元 36 – 驾驶员座椅调节单元 → 编码:
字节 6 – 位 4 (EasyEntry_Enable_Passenger_over_DriverMMI): 激活
→ 应用（需重启单元）
```
  
``` yaml
单元 6 – 乘客座椅调节单元 → 编码:
字节 3 – 位 1 (Easy_Entry_front): 激活
字节 9 – 位 6 (Easy_entry_front_over_MMI): 激活
字节 6 – 位 4 (EasyEntry_Enable_Passenger_over_DriverMMI): 激活
→ 应用（需重启单元）
```

``` yaml
单元 5F → 适配:
Car_Function_Adaptations_Gen2:
- menu_display_seat_configuration: 激活
- menu_display_seat_configuration_over_threshold_high: 激活
→ 应用 

Car_Function_List_BAP_Gen2:
- Passenger_Seat_0x20: 激活
- Passenger_Seat_0x20_msg_bus — 舒适总线  
→ 应用 
```

## 车窗控制

### 关门时泄压
:octicons-verified-24: Škoda

!!! tip ""
    关闭前门时车窗下降 1 cm 以降低车内压力
``` yaml
单元 42 → 编码:
Short_drop: 激活
→ 应用
```

``` yaml
单元 52 → 编码:
Short_drop: 激活
→ 应用
```

### 熄火时车窗仍可工作及其工作时长

!!! tip ""
    熄火时车窗仍可工作，但若开/关了车门 —— 车窗就停止工作

=== "在 ODIS 中编码"  
    ``` yaml
    单元 09 → 适配:
    Acces control (ZV Komfort)
    - Freigabenachlauf FH bei Tueroeffnen abbrechen: Activ 改为 NotActiv
    - FH SAD Kl15Aus Freigabezeit: 600 s（熄火后 10 分钟）改为任意其他秒数
    → 应用
    ```

=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 车载电气网络控制 → 安全访问 (登录: 31347) → 编码:
    ZV Komfort
    - Freigabenachlauf FH bei Tueroeffnen abbrechen: 激活
    ```
