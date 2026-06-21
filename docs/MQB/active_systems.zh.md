
# 主动驾驶辅助系统

### 设置 BDW (Brake Disc Wiper / 制动盘烘干)

``` yaml title="登录密码: 40304"
单元 3-ABS/ESP → 适配:
Disk drying:
- 默认: 默认为弱 (weak)
- 新值: 强 (strong)
→ 应用
```

### 设置 ASR (Starting vibration reduction / 减小起步抖动)

!!! tip ""
    Normal（较少切割动力）  
    Strong（默认）  
    Maximum（适合不想磨胎的人，但系统会压制发动机）  
  
``` yaml title="登录密码: 20103"
单元 3-ABS/ESP → 适配:
减小起步抖动 / Starting vibration reduction: 输入所需的档位值
→ 应用
```

### TSC (Traction Control System / 侧向跑偏补偿)

急加速时会自动补偿车辆向右的跑偏。  

!!! tip
    可选值如下：  
    - inactive  
    - with learned Value active / 带自适应值（2 位）  
    - without learned Value active（3 位）  

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 19249"
    单元 44 (转向助力) → 编码:
    torque_steer_function / 侧向跑偏补偿: 所需值
    → 应用
    ```

=== "在 VCDS 中编码"  
    ``` yaml title="登录密码: 19249"
    单元 44 转向助力 → 编码 → 长编码:
    字节 0 – 激活值
    退出 → 保存
    ```

### 坡道起步/驻坡辅助 Hill Hold Control (HHC)

!!! note ""
    HHC 在上坡或下坡时驻住车辆，防止其自行溜车，直到驾驶员踩下油门踏板。

``` yaml
单元 3-ABS/ESP → 编码 → 长编码:
字节 25 – 位 0: 激活
```

!!! note "适配值"
    HHC 有 3 个级别：early、normal、late
  
``` yaml title="登录密码: 20103"
单元 3-ABS/ESP → 适配:
HHC (Berganfahrassistent, Hill_hold_assist_control): 提前 (early)
→ 应用
```

!!! warning ""
    如果激活后 ABS 错误未消失，说明你的单元不支持 HHC。

### 通过菜单关闭 ESC

!!! warning
    2016-17 年的车上可能安装 31 字节的 ABS 单元。  
    其中还有最后 1 个字节，通常值为 03 —— 不要动它！
  
!!! tip
    可选值如下：  
    01 = ESC & ASR On  
    02 = ESC & ASR On/Off  
    03 = ESC & ASR On + ESC SPORT  
    04 = ESC & ASR On + ESC Off  
    05 = ESC On/Off + ASR Off  
    06 = ESC On/Off + ESC Sport  
    07 = ESC On/Off + ASR Off  
    08 = ESC On/Off + ESC Sport  
    09 = ESC On + ASR Off + ESC Sport  

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 3-ABS/ESP → 编码:
    字节 29 – 改为「05」（提供 ESC 开、ASR 关、ESC 关菜单） 
    → 应用
    ```
  
    为使 ESP 在 100km/h 以上不再自动开启： 
    ``` yaml title="登录密码: 20103"
    单元 3-ABS/ESP → 适配:
    ESP activation depending on speed (Electronic stabilitin program): 停用
    → 应用
    ```

=== "在 VCDS 中编码"  
    ``` yaml title="登录密码: 20103"
    01 — ABS/ESP → 编码 → 长编码:
    字节 29: 改为「05」（提供 ESC 开、ASR 关、ESC 关菜单）  
    退出 → 保存
    ``` 
    ![Screenshot](../images/MQB/esc.png)

### 设置 XDS（弯道内侧车轮制动以更好地切入弯道）

!!! tip
    设为 max 与 strong 对比试了一下，感觉 strong 模式下内侧（弯道）车轮的制动发生在更高车速、更大转向角时，相比 maximum 模式。  
    maximum 模式下转弯半径明显更小。  
  
=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 03 → 编码:
    字节 17 – 位 3: 激活
    ```
=== "在 VCDS 中编码" 
    ``` yaml title="登录密码: 20103"
    03 单元 ABS → 编码 → 长编码:  
    字节 17 – 位 3 (电子差速锁（扩展）): 激活
    退出 → 保存
    ``` 
    ![Screenshot](../images/MQB/xds1.gif)

### BAS (Brake Assist System / 紧急制动系统) 适配
紧急制动系统 —— 一种对制动液压系统压力进行电子控制的系统，在需要紧急制动而踏板力不足时，自行提高制动管路压力。  

``` yaml title="登录密码: 20103"
单元 03 (ABS) → 适配:
brake assist: (0-中, 1-低, 2-高)
→ 应用
```

### 激活 CBC (Corner Brake Control / 弯道制动稳定系统)

!!! note ""
    该系统通常已激活。是 ABS、ESP 或其他安全系统的一部分  
  
弯道制动稳定系统 —— CBC (Corner Brake Control)，在弯道制动时触发，用制动力产生一个纠正性的「反向转矩」，从而修正弯道制动时的「甩尾」表现。  

``` yaml
单元 03 (ABS) → 编码:
字节 15 – 第 4 位: 激活
→ 应用
```
