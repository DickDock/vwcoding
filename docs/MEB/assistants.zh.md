# 驾驶辅助

!!! warning ""
    向单元 A5 和 13 写入需要 **SFD**（在 2024+ 车辆上 —— **SFD2**）。见 [SFD](../sfd.md)。

### 关闭右侧超车限制 (ACC)

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 20103"
单元 13 → 编码:
Overtaking_right_prevention: deactivated
→ 应用
```

### Lane Assist —— 提前介入 (A5)

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 20103"
单元 A5 → 编码:
HC_point_of_intervention: early_setting_over_menu
→ 应用
```

### Travel Assist

完整说明在 MQB-Evo 平台：

→ [Travel Assist (MQB-Evo)](../MQB-Evo/travelAssist.md)  
→ [Emergency Assist、TJA、单元 44](../MQB-Evo/driverAssistExtras.md)

### Front Assist / 紧急制动

!!! note ""
    能否激活取决于已安装的 radar 与摄像头。未加装硬件时，编码不会添加该功能。

``` yaml title="登录码: 20103"
单元 A5 → 编码:
Front_Assist: activated
→ 应用
```

!!! danger ""
    只更改你的 SW 中已存在的通道。缺失的通道意味着配置不同或需要参数集。
