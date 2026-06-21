# 行驶辅助

### 制动盘烘干调节

:octicons-verified-24: SFD: yes :octicons-verified-24: Tested SW: 0136

!!! note ""
    并非每个编码 dongle 都会显示该适配通道。请用 OBD11、ODIS 操作
  
``` yaml 
Control unit 03 → Adjustments:
Break disk drying:
- Break disk drying: medium (light, medium, strong)
→ Apply
```

### 在不选择驾驶模式的情况下更改转向特性

:octicons-verified-24: SFD: no :octicons-verified-24: Tested SW: 1040

``` yaml 
Control unit 44 → Adjustments:
- Steering_support_characteristic_line: dynamic
→ Apply
```
