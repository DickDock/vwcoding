
# 后视镜与雨刮参数

### 后视镜折叠时后视镜外部照明的工作

``` yaml
单元 52 → 编码:
字节 1 – 位 5 (turn_off_front_light_with_folded_mirror): not_active (原为 active)
```

``` yaml
单元 42 → 编码:
字节 1 – 位 5 (turn_off_front_light_with_folded_mirror): not_active (原为 active)
```

### 倒车时右侧后视镜下翻（若出厂未激活）

!!! note ""
    仅在后视镜调节摇杆拨到 R 位置时有效  
  
!!! note ""
    后视镜下翻到的位置可自行设定：  
    1) 打开车辆  
    2) 拉起电子机械驻车制动  
    3) 打开点火  
    4) 变速箱挂入空挡  
    5) 现在挂入倒挡  
    6) 把乘客侧后视镜调到你舒适的位置  
    7) 后视镜位置会为你开门所用的钥匙记忆  

``` yaml
单元 52 → 编码:
字节 4 – 位 2 和 3 (mirror_lowering_with_rear_gear): 激活
```

``` yaml title="登录密码: 31347"
单元 09 → 适配:
 Spiegelverstellung (OBD11 的 Access control):
- Spiegelabsenkung bei Rueckwaertsfahrt: 激活
- Menuesteuerung Spigelabsenkung: 激活
→ 应用
```

### 启动发动机时展开后视镜

!!! tip ""
    后视镜仅在打开点火时展开，而非每次开车门时展开。机构磨损更小

!!! warning ""
    此适配仅在 VW Tiguan 上有效

=== "在 ODIS 中编码" 
    ``` yaml title="登录密码: 31347"
    单元 09 → 适配:
    Spiegelverstellung
    - Signalisierung_Spiegelanklappung: 未激活
    → 应用
    ```

=== "在 OBD11 中编码" 
    ``` yaml title="登录密码: 31347"
    单元 09 车载电气网络控制 → 安全访问 (登录: 31347) → 编码:
    Access control
    - Signalisierung_Spiegelanklappung: 激活
    ```

### 长按车门关闭按键或原厂遥控钥匙的关闭按键折叠侧后视镜

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Spiegelverstellung:
- Funk Spiegelanklappung Modus: by look command via remote control key → by convenience operation via remote control key
→ 应用
```

### 设置大灯清洗

关闭每第 10 次开启风窗清洗时大灯清洗的触发
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Scheinwerferreinigung:
- Anzahl Betaetigungen Frontwaschanlage pro SRA Aktivierung: 10 → 0
→ 应用
```

等效做法：
```
Scheinwerferreinigunglage → 未激活
```
  
长按风窗清洗拨杆后触发
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Scheinwerferreinigung:
- SRA Verzoegerungszeit: 0 → 2500 (мс)
→ 应用
```

关闭大灯上的第二次"喷水"（不推荐）
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Scheinwerferreinigung:
- SRA Nachwaschzeit: 10 → 0 (мс)
→ 应用
```

### 雨刮的维修位置

!!! note ""
    Service position：默认 166.505329 度，往小调。  
  
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Service position: 输入所需值
→ 应用
Alternative position 2（熄火时雨刮的位置）
→ 应用
```

### 雨刮维修位置 —— 车机中的菜单
:octicons-verified-24: Škoda · :octicons-verified-24: 带 MIB3 的车辆
``` yaml title="登录密码: 31347"
单元 09 → 适配:
Front wiper:
- Menuesteuerung Frontwischer: active
→ 应用
```

### 关闭清洗泵开启延迟（雨刮不会在干玻璃上刮蹭）

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Front wiper:
- Mindestwaschzeit_Frontwischer: 0 ms → 300 ms
- Timer_DWP_SRA_delay: 300 ms → 0 ms
```

### 余滴清扫 – 风窗玻璃

!!! note ""
    寒冷季节该功能不工作（5.5℃ 起）

``` yaml title="登录密码: 31347"
单元 09 → 编码 → 子块 1:
04EDFD (旧值 04EDDD)
→ 应用
```

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Front_wiper 
Traenenwischen Front Status: 激活
→ 应用
```

### 后雨刮在雨中的工作

``` yaml title="登录密码: 31347"
单元 09 → 适配:
后雨刮 (Rear Wiper / Heckwischersteuerung)
Automatisches Heckwischen: 激活
→ 应用
```
