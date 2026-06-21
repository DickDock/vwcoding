
# 行驶与操控

### 自适应巡航开启时关闭右侧超车限制
``` yaml
单元 03 → 编码:
Overtaking_right_prevention: 停用
```

### 减小 autohold 起步时的顿挫
``` yaml
单元 03 → 适配:
Treshold_for_drive_away_assist:
- Data: normal → early
→ 应用
```

### 设置制动盘烘干系统
``` yaml
单元 03 → 适配:
brake disk wiper:
- Param to DOP: normal → strong
→ 应用
```

### 开启加速时的侧向跑偏补偿系统
``` yaml
单元 03 → 适配:
Straigt_line_control:
- Data: 激活
→ 应用
```
