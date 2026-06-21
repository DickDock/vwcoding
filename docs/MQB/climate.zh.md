
# 空调系统控制

### 自动模式下显示 Climatronic 风扇转速

=== "在 ODIS 中编码"
    ``` yaml
    单元 08 → 编码:
    字节 11 – 位 6 (Blower display during auto mode): 激活（把值 00001110 改为 01001110）
    → 应用（需重启单元）
    ```
  
=== "在 OBD11 中编码"
    ```yaml
    单元 08 – 加热与空调装置电子模块 → 长编码:
    自动模式下的风扇模式指示: 激活
    ```
  
=== "在 VCDS 中编码"
    ```yaml
    08 – 空调控制  
    编码 - 07 → 长编码:
    字节 11 – 位 6: 激活  
    如果没有第 6 位，只能改码本身 —— 把值 00001110 改为 01001110  
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/climate.jpg)  

### 记忆前排座椅加热的上次档位

!!! tip ""
    说明/目的：永久记忆驾驶员座椅上次所选的加热强度。是把车更精细地调成自己习惯的实用功能。

=== "在 ODIS 中编码"
    ``` yaml
    单元 08 → 适配:
    Speicherung der Sitzheizungsstufe Fahrer (Retention of driver's seat heater level): 激活 
    → 应用
    Speicherung der Sitzheizungsstufe Beifahrer (Retention of passenger's seat heater level): 激活
    → 应用
    ```
  
=== "在 OBD11 中编码"
    ```yaml
    08 加热与空调装置电子模块 → 适配  
    记忆驾驶员座椅加热档位: акт (原为 акт 10 分钟)
    记忆前排乘客座椅加热档位: акт
    ```
  
### 根据车外温度自动加热方向盘

!!! warning "重要信息"
    对于 2020 年的车，此编码可在以下工具中进行：
      - ODIS E 12 或 ODIS S 6 版本
      - OBD11
    在旧版 ODIS 或 VCDS 中编码会导致方向盘加热完全失效  

!!! tip ""
     有 2 种模式：  
     Lenkradtemperatur – 按方向盘内传感器
     Aussentemperatur – 按车外温度传感器
     Lenkradtemperatur – 在点火时若方向盘温度低则开启。适合在高速行驶时
     Aussentemperatur – 始终工作

=== "在 ODIS 中编码"
    ``` yaml
    单元 8 → 编码:
    加热与空调装置电子模块 / Heated_steering_wheel_automatic_mode
    - 方向盘加热, 自动模式: 由「未安装」改为所需值
    → 应用
    ```
  
=== "在 OBD11 中编码"
    ```yaml
    08 加热与空调装置电子模块 → 长编码:
    方向盘加热, 自动模式
    ```
  
=== "在 VCDS 中编码"
    ```yaml
    08 空调控制 → 编码 - 07 → 长编码:  
    字节 13 – 位 2: 按方向盘内传感器  
    字节 13 – 位 3: 按车外温度  
    两个位不能同时开启！
    如果没有位选项，可改字节本身的值: 14（按方向盘内传感器）或 18（按车外温度）  
    退出 → 保存 
    ``` 
    ![Screenshot](../images/MQB/wheel.png)  

### 后视镜随后窗一起加热（不适用于 Tiguan）

!!! note ""
     此编码不适用于 Tiguan 车型

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 31347"
    单元 09 → 编码:
    后窗加热开启时后视镜加热也开启: 激活
    → 应用（需重启单元）
    ```
  
=== "在 VCDS 中编码" 
    ```yaml title="登录密码: 31347"
    09 – 车载电气网络电子模块  
    编码 - 07 → 长编码:
    字节 15 – 位 3 (Mirror Heating ON while Rear Window Heater ON): 激活
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/rear.jpg)  

### 后视镜随后窗一起加热（用于 Tiguan）

无论驾驶员车门上的后视镜控制摇杆在何位置，都让后视镜加热随后窗加热一起开启

``` yaml
单元 52 → 编码:
字节 9 – 位 2 (rear_window_heater_trigger): 激活
```

``` yaml
单元 42 → 编码:
字节 9 – 位 2 (rear_window_heater_trigger): 激活
```

将后视镜加热作为单独项显示在舒适系统用电设备菜单中：

=== "在 ODIS 中编码"
    ``` yaml
    单元 19 → 适配:
    Efficiency_display:  
    - Convenience_consumption_mirror_heating_dependency → Independent_of_outside_temperature_without_switch
    Range_gain
    - Consumption_mirror_heating_in_heated_rear_window: 激活
    → 应用 
    ```
=== "在 OBD11 中编码"
    ``` yaml
    单元 19 → 适配:
    效率程序显示:  
    - 舒适系统用电、外后视镜加热、依赖关系 → 不依赖车外温度、无开关  
    增加续航:  
    - 后窗加热中的外后视镜加热用电: 激活
    ```

### 提高前后挡风玻璃加热的温度和时间

!!! note ""
	输入值以秒为单位，例如 1200 / 60 = 20（分钟）

更改后窗加热的温度和时间
``` yaml title="登录密码: 31347"
单元 09 → 适配:
玻璃加热:
- Heckscheibenheizung Zeitwert: 从「320 с」改为「640 с」
- Abschalttemperatur fuer Heckscheibenheizung: 从「35.0 °C」改为「38.0 °C」
→ 应用
```

更改前风窗加热的温度和时间
``` yaml title="登录密码: 31347"
单元 09 → 适配:
玻璃加热:
- Frontscheibenheizung Zeitwert: 「320 с」改为「640 с」
- Abschalttemperatur fuer Frontscheibenheizung: 「35.0 °C」改为「38.0 °C」
→ 应用
```

### 激活 Air Care Climatronic

!!! note ""
    AirCare 激活后，Climatronic 系统开始在内循环模式下让空气通过空调滤芯，同时引入车外新鲜空气。这样能最有效地净化车内空气，并通过强力过滤细微颗粒来改善空气质量。  
    为使该选项正常工作，建议使用防过敏空调滤芯。它能有效分离固体粉尘和花粉颗粒 —— 这在城市环境中是个大问题，尤其在春秋季节。

!!! warning ""
    激活此功能需要：  
    - Climatronic 单元 SW 不低于 1403；  
    - Gateway 单元 SW 不低于 1244/2244；  
    - 2016 年起（2017 车型年起）的 MIB Infotainment 单元 (STD2/HIGH2)；  

=== "在 ODIS 中编码"
    ``` yaml
    单元 08 → 编码:
    filtering_interior_air: installed
    → 应用（需重启单元）
    ```
  
=== "在 VCDS 中编码" 
    ```yaml
    08 – 空调控制  
    编码 - 07 → 长编码:
    字节 15 – 位 5-6 (20 – 车内空气过滤): 激活
    退出 → 保存  
    ```
  
### 下雨时自动关闭天窗
:octicons-verified-24: VW Atlas

``` yaml title="登录密码: 31347"
单元 09 → 适配:
Access control 2:
- RegenschlieRen: permanently
- RegenschlieRen: 激活
→ 应用
```

``` yaml title="登录密码: 31347"
单元 09 → 编码 → 子块 RLHS:
字节 00 – 位 1-2: 激活
→ 应用
```
