
# 仪表盘

### 油箱剩余量

``` yaml title="登录密码: 20103"
单元 17 → 编码:
字节 10 – 位 4 (refuel_volume): 激活
→ 应用（需重启单元）
```

### 关闭发动机运行时钥匙不在车内的声音与视觉警告
``` 
单元 17 → 编码:
Leaving_warning → no
→ 应用（需重启单元）
```

### 在车速表上添加中间刻度
:octicons-verified-24: Audi
``` 
单元 17 → 编码:
Tachometer_erweiterte_Skalenteilung: yes
→ 应用（需重启单元）
```

### 显示 lap timer 与机油温度
:octicons-verified-24: Audi + e-tron
``` 
单元 17 → 编码:
字节 1 – 位 3 (lap timer active): yes
→ 应用（需重启单元）
```
在某些车型上该编码可能名为 "Lap counter"

### "运动"菜单
:octicons-verified-24: Audi e-tron
``` 
单元 17 → 编码:
Acceleration display: on
→ 应用
```

### 显示加速度测量
:octicons-verified-24: Audi
``` 
单元 17 → 适配:
Displayable_content_configuration:
- Drag_indicator: no_display → readout
- Acceleration measurement: Display # (1)!
→ 应用
```

1. 某些车辆可能需要此选项

![Screenshot](../images/MLB/drag_info.jpeg) 

### 设置当前挡位显示（在普通模式、S 挡或两者中）
:octicons-verified-24: Audi
``` yaml
单元 02 → 编码:
Block 3 – Functions: → 选择所需项
```
或
``` yaml
单元 02 → 适配:
Activate_gear_information_display:
- Activate_gear_information_display: → 选择所需项
```

### 在抬头显示上显示
:octicons-verified-24: Audi
``` yaml
单元 82 → 编码:
Navigation System: not available → available (显示导航系统提示)
Laptimer_activated: not available → available (显示已启动的圈速计时)
clock: not available → available (显示当前时间)
Telephone: not available → available (显示来电)
speedlimiter: not available → available (显示已开启的限速器)
predictive_efficiency_assistant: not available → available (显示生态辅助提示)
→ 应用
```

### 指针自检

``` yaml title="登录密码: 20103"
单元 17 → 编码:
字节 01 – 位 0 (Демонстрация/Staging/Gauge Test/Needle Sweep active): 激活
→ 应用（需重启单元）
```

### 升挡提示（在"手动"模式驾驶时）
:octicons-verified-24: Audi
``` yaml title="登录密码: 20103"
单元 17 → 适配:
Upshift_indicator_in_the_centre_display: no_display 改为 display
→ 应用
```
