
# 空调系统控制

### 重新映射 ECO 按键

将 eco 模式改为把空调开到最大

``` yaml
单元 08 → 编码:
ACmax/ECO: ECO → ACmax
→ 应用（需重启单元）
```

### 开启座椅加热时分别控制坐垫加热与靠背加热
``` yaml
单元 08 → 编码:
Activation_seat_heating_and_backrest_heating: Coupled → ...
→ 应用（需重启单元）
```

### 更改 MMI 上后排乘客空调设置的显示时长
``` yaml
单元 08 → 适配:
MMI display time during rear zone adjustment:
- MMI_display_time_during_rear_zone_adjustment: 10 s → ...
→ 应用
```

### 设置预启动加热器的工作时长

``` yaml
单元 08 → 适配:
Auxiliary heating run on time:
- Auxiliary_heating_run_on_time: 10 min
→ 应用
```
