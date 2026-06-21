# MQB EEPROM

在 MQB 平台上，与 PQ 一样，部分设置可以直接在 EEPROM 存储中进行

## 已知的 BCM 存储地址

这些由 BCM 单元 (09) 中的适配负责： 
``` yaml
Parameter Write Adaptation:
- parameter address: FExxxx # (1)!
- parameter value: yyy # (2)!

Parameter Read Adaptation:
- parameter address: FExxxx
```

1. 参数地址
2. HEX 制的值。例如，`05h = 5 = 0.5 秒`、`0Ah = 10 = 1 秒`、`14h = 20 = 2 秒`

| 存储地址     | 旧值            | 新值           | 说明                                                                            |
|:-------------|:---------------:|:--------------:|:--------------------------------------------------------------------------------|
| FE0207       |       40        |       20       | 按键降窗的按住时间                                                              |
| FE0208       |       40        |       20       | 按键升窗和折叠后视镜的按住时间                                                  |
