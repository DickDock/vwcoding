# 仪表盘

### 「油箱口方向」标记
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 10 – 位 4: 激活
→ 应用
```

### 指针自检
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 01 – 位 0: 激活
→ 应用
```

### 单圈计时
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 01 – 位 3: 激活
→ 应用
```

### 开启「请拔出钥匙」提醒
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 01 – 位 4: 激活
→ 应用
```

### 超过设定车速时提醒后雾灯已开启
``` yaml title="登录密码: 31347（旧款为 20103）"
单元 09 → 适配:
Driving light and parking light – Nebelschlusslicht Warngeschwindigkeit: 
- 0 — 关闭提醒。
- 1 … 255 — 触发提醒的车速上限（推荐 60）
→ 应用
```

### 校正车速表读数

!!! note ""
    仅在 03 以内有效，再高里程就会明显偏离真实值。  
    值为 03 时，里程每 10 km 约增加 300 米。  
    出厂编码 00 时，每 40 km 增加 200 米。  
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
03 字节:
- 00, 轮胎周长: 标准
- 01, 轮胎周长: 变体1
…
- 07, 轮胎周长: 变体7
→ 应用
```

### 重置保养提醒
``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
SIE – time from inspection → 把按天计的里程值设为 0
SIE – distance from inspection → 把按 km 计的里程值设为 0
→ 应用
ESI – Resetting ESI → 选择 Reset
→ 应用
```

### 更改保养间隔（按里程和按时间）
``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
ESI – maximum value km-driving distance/inspection → 30000 km – 改为所需值, 例如 15000
ESI – minimum value km-driving distance/inspection → 15000 km – 改为所需值, 例如 7500
ESI – maximum value of time between inspections → 730 d – 改为所需值
ESI – minimum value of time between inspections → 365 d – 改为所需值
→ 应用
```

### 12 小时制时钟
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 06 – 位 7: 激活 (12 小时制) / 停用 (24 小时制)
→ 应用
```

### 节能建议
``` yaml
单元 17 (5JA 920 7XX) → 长编码:
字节 01 – 位 7: 激活
→ 应用
```

``` yaml
单元 19 → 长编码:
字节 13 – 位 0: 激活
→ 应用
```
在 19 单元的适配中按自己的需要关闭不需要的项（出厂默认全部激活）
``` yaml
单元 19 → 适配:
能效程序显示 – 建议 → 空气动力学阻力: 关闭车窗/天窗。
能效程序显示 – 建议 → 发动机制动: 仅在转速低于 1300 时踩离合。
能效程序显示 – 建议 → 启动发动机时不要踩油门踏板。
能效程序显示 – 建议 → 使用推荐挡位（仅 MT）。
能效程序显示 – 建议 → 使用启停系统。
能效程序显示 – 建议 → 开启启停系统。
能效程序显示 – 建议 → 空调系统: 关闭车窗/天窗。
能效程序显示 – 建议 → 使用 D 挡位。
能效程序显示 – 建议 → 车辆静止时不要踩油门踏板。
能效程序显示 – 建议 → 天窗已开: 关闭空调系统（AC 键）
→ 应用
```

!!! note ""
    编码后需进入车机的仪表显示信息设置菜单，开启「节能建议」项。

### 校正油耗读数

!!! info "计算示例"
    取仪表上显示的行车电脑油耗 - 6,3 л/100km。  
    取实际观测油耗 – 例如 6,8 л/100km。  
    然后做比例计算。  
    把行车电脑读数当作 100%  
    6,3 – 100%  
    6,8 – Х  
    Х = 6,8 * 100 /6,3  
    Х = 107,9%, 四舍五入后 108%  
    在适配值字段填入该值。平均而言，行车电脑读数偏低 0,4 升。

默认 – 100%，步长 1%，最小 — 85%，最大 — 115%

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
Display correction of consumptions and operating range: 100%
→ 应用
```

### 燃油液位指示 – 调整 / 标定

出厂设置：-12,8；取值范围：-8,0 到 8,0  
负值让油针下降，正值让油针上升。这也会影响剩余油量的计算。

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
Offset for tank calibration values:
- Complete tank calibration: -12.8 l 改为所需值
→ 应用
```

### 设定时钟同步源

- internal clock – 内部时钟  
- GPS – 从 GPS 单元获取。时间按格林尼治时间 (GMT+0) 
- 无线电控制器 – 来自 5F 单元的时间  
- 不激活 – 不进行同步

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
Source for synchronization of time: internal clock
→ 应用
```

### 更改路面湿滑预警温度（「雪花」）

按迟滞回路原理工作：达到下限时触发，达到上限时关闭。

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
outside_temperature:
- outside_temperature: 4 # 输出预警的温度
- p_ice_warning_exit_temperature: 6 # 关闭预警输出的温度
- Source for synchronization of time: internal clock
→ 应用
```

### 在驻车灯模式下开启仪表盘背光

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
Illumination_algorithm:
- Scale_switching_algorithm: lds (原为 parking_light)
→ 应用
```

### 更改仪表盘语言

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
Language version: 改为所需语言
→ 应用
```

### 保养提醒的显示时长

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
time_parameter_display:
- hmi_t_NextServiceAnz_ms: 5s 改为所需值
→ 应用
```

### 警告消息的显示时长

``` yaml title="登录密码: 25327（旧款为 20103）"
单元 17 (5JA 920 7XX) → 适配:
time_parameter_display:
- hmi_t_NextWarning_ms: 6s 改为所需值
→ 应用
```
