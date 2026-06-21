
# 仪表盘设置

### 指针自检

!!! info ""
    仅适用于第一类 Active Info Display (5NA920790A/B/C, 5NA920791A/B/C)  
    第二类仪表盘 (5NA920790D) 不支持

!!! warning ""
    编码仅在点火开启、发动机未启动时进行
  
=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    Демонстрация: 激活
    → 应用（需重启单元）
    ```

=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 – 组合仪表 → 长编码:
    Демонстрация: 是
    ```

=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 仪表盘 → 编码 → 长编码:
    字节 1 – 位 0 (Gauge test/ Needle Sweep / Staging): 激活
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/AID/staging.jpg)

### 关闭发动机运行时钥匙不在车内的声音与视觉警告
``` yaml
单元 17 → 编码:
Leaving_warning: no
→ 应用（需重启单元）
```

### 在仪表盘上显示来电照片、专辑封面、电台 logo

``` yaml title="登录密码: 20103 或 47115"
单元 17 → 适配:
Picture_Upload_Download: 激活
→ 应用
```
  
### 油箱剩余量

!!! warning ""
    编码仅在点火开启、发动机未启动时进行

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    需加注的油量: 激活
    → 应用（需重启单元）
    ```
  
=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 组合仪表 → 长编码:
    需加注的油量: 是
    ```
  
=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    17 仪表盘 → 编码 → 长编码:
    字节 10 – 位 4 (Volume to be Replenished): 激活  
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/AID/refill.jpg)

!!! tip ""
    加油量读数的步进为 5 升的整数倍，即 5-10-15-20 等  
    （已验证，实际能比显示的稍多 —— 显示 30 时，轻松加进了 32 升）
  
### 圈速计时器

!!! warning ""
    编码仅在点火开启、发动机未启动时进行

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    圈速计时器: 激活
    → 应用（需重启单元）
    ```

=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 仪表盘 → 编码 → 长编码:
    字节 1 – 位 3 (Lap Timer active): 激活  
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/AID/staging.jpg)

### 显示瞬时油耗

``` yaml title="登录密码: 20103"
单元 17 → 适配:
Instantaneous Consumption Display: Display
→ 应用
```

### 关闭开门时点火已开启的声音提示

``` yaml title="登录密码: 20103"
单元 17 → 适配:
Ignition active message; trigger (点火激活提示, 气体发生器): «No display (tbd)»
→ 应用
```

!!! tip
    有 3 个值：No display (tbd), Driver door, All doors.  

### 关闭安全带未系警告

!!! tip ""
    关闭它是为了在偶尔需要短距离移动时不被打扰

``` yaml title="登录密码: 20103"
单元 17 → 适配:
关闭安全带未系警告: 是
→ 应用
```
  
### 激活车速表的中间刻度值

!!! note ""
    仅在 2019 年起的新款 AID 仪表盘上有效。  
    无论哪种方案，100 km/h 始终在顶部。

??? Variants
    Variant_0
    ![Screenshot](../images/MQB/AID/speed_variant_0.png)
    Variant_1
    ![Screenshot](../images/MQB/AID/speed_variant_1.png)
    Variant_2
    ![Screenshot](../images/MQB/AID/speed_variant_2.png)
    Variant_3
    ![Screenshot](../images/MQB/AID/speed_variant_3.png)
    Variant_4
    ![Screenshot](../images/MQB/AID/speed_variant_4.png)
    Variant_5
    ![Screenshot](../images/MQB/AID/speed_variant_5.png)
    Variant_6
    ![Screenshot](../images/MQB/AID/speed_variant_6.png)
    Variant_7
    ![Screenshot](../images/MQB/AID/speed_variant_7.png)
    Variant_8
    ![Screenshot](../images/MQB/AID/speed_variant_8.png)    
    Variant_9
    ![Screenshot](../images/MQB/AID/speed_variant_9.png)  

``` yaml title="登录密码: 20103"
单元 17 → 适配:
车速表最终值 / Speedometer_final_value / Tachometer end value: 执行方案_4 (原为 执行方案_1)
→ 应用
```

### 更改仪表盘中央区的动画/显示

!!! info "可选方案"
    执行方案_1 – 经典
    执行方案_3 – 点阵/碳纤维主题

``` yaml title="登录密码: 20103"
单元 17 → 适配:
显示内容: 执行方案_3 (原为 执行方案_1)
→ 应用
```

### R-line logo（用于新款仪表盘 5NA920790D）

!!! tip "可选项"
    无 R logo  
    带 R logo  
    带 R-Line logo  
    25/19 改款的 R logo  
    25/19 改款的 R-Line logo  

``` yaml title="登录密码: 20103"
单元 17 → 适配:
R_Logo: 选择所需项
→ 应用
```

### 修正车速表读数

!!! tip ""
    每种轮胎规格都需要选取自己的值

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    车轮周长 / Tire Circumference: 执行方案 3
    → 应用
    ```
  
=== "在 VCDS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 17 仪表盘 → 编码 → 长编码:  
    字节 3 – 位 0-2: 执行方案 3
    退出 → 保存  
    ```
    ![Screenshot](../images/MQB/AID/speed.png)

### 更改所显示车辆的外观

!!! warning
    若开启了氛围灯则不工作

### 更换仪表盘皮肤

=== "VW 仪表盘 5NA920790A/B/C, 5NA920791A/B/C"

    主题通过改变 2 个参数的组合来设定
    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    Tube_version: 0..9
    Vehicle variant: 0..9
    → 应用
    ```

    方案 1 – 标准样式  
    ![Screenshot](../images/MQB/AID/themes/StandartTheme.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配:
    Tube_version: 方案 0, 5, 6, 7, 8, 9
    → 应用
    ```

    方案 2 – 点更多的标准样式  
    ![Screenshot](../images/MQB/AID/themes/StandartThemeMoreDots.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配:
    Tube_version: 方案 1
    → 应用
    ```

    方案 3 – Alltrack 主题  
    ![Screenshot](../images/MQB/AID/themes/AllTrackTheme.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配:
    Tube_version: 方案 2
    → 应用
    ```

    方案 4 – GTI / GTD 主题  
    ![Screenshot](../images/MQB/AID/themes/GTITheme.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配:
    Tube_version: 方案 3
    → 应用
    ```

    方案 5 – R-line 主题  
    ![Screenshot](../images/MQB/AID/themes/RTheme.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配: 
    Tube_version: 方案 4
    → 应用
    ---
    Vehicle variant: 方案 2, 4
    → 应用
    ```

    方案 6 – 仪表盘底部带 R-line logo 的 R-line 主题  
    ![Screenshot](../images/MQB/AID/themes/RThemeWithLogo.jpg)
    ``` yaml title="登录密码: 20103"
    单元 17 → 适配:
    Tube_version: 方案 4
    → 应用
    ---
    Vehicle variant: 方案 6, 8
    → 应用
    ```

=== "VW 仪表盘 5NA920790D"

    ``` yaml title="登录密码: 20103"
    单元 17 → 编码:
    Tube_version
    - Skinning: 0..9
    → 应用
    ```

    variant 0  
    ![Screenshot](../images/MQB/AID/themes_D/variant_0.png)  
    variant 1  
    ![Screenshot](../images/MQB/AID/themes_D/variant_1.png)  
    variant 2  
    ![Screenshot](../images/MQB/AID/themes_D/variant_2.png)  
    variant 3  
    ![Screenshot](../images/MQB/AID/themes_D/variant_3.png)  
    variant 4  
    ![Screenshot](../images/MQB/AID/themes_D/variant_4.png)  
    variant 5  
    ![Screenshot](../images/MQB/AID/themes_D/variant_5.png)  
    variant 6  
    ![Screenshot](../images/MQB/AID/themes_D/variant_6.png)  
    variant 7  
    ![Screenshot](../images/MQB/AID/themes_D/variant_7.png)  
    variant 8  
    ![Screenshot](../images/MQB/AID/themes_D/variant_8.png)  
    variant 9  
    ![Screenshot](../images/MQB/AID/themes_D/variant_9.png)

=== "Seat 仪表盘"

### 复位保养间隔

``` yaml title="登录密码: 20103"
单元 17 → 适配:
复位扩展保养间隔计数器: 复位
→ 应用
```
