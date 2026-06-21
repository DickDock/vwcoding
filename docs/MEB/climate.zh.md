# 空调与高压加热

!!! warning ""
    MEB 上的 **08** 单元控制车内空调，并与 **高压加热器** 关联。写入需要 **SFD**（2024+ —— **SFD2**）。见 [SFD](../sfd.md)。

MEB 电动车上的 08 单元在功能上与 MQB-Evo 接近，但部分通道缺失或命名不同 —— 请在 ODIS 中按你的 SW 核对适配列表。

### 保存 Air Care（空气过滤）设置

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 20103"
单元 08 → 适配:
Filtering_interior_air_saving:
- Filtering_interior_air_saving: active
→ 应用
```

取值：`not_active` —— 不记忆；`active` —— 记忆；`depending_on_standing_time` —— 取决于停车时长。

### 保存内循环模式

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 20103"
单元 08 → 适配:
Save air recirculation status at terminal 15 off:
- Save air recirculation status at terminal 15 off: storing
→ 应用
```

### 保存座椅加热档位

:octicons-verified-24: SFD: yes

``` yaml title="登录码: 20103"
单元 08 → 适配:
Time for seat heating power reduction Level 3 to level 2:
- param_Time_for_seat_heating_power_reduction_Level_3_to_level_2: 0 min
Time for seat heating power reduction Level 2 to level 1:
- param_Time_for_seat_heating_power_reduction_Level_2_to_level_1: 0 min
→ 应用
```

`0 min` —— 关闭功率的自动降低（保持所选档位）。

### 车内预热（通过 App / 定时器）

原生的 **departure timer** 与通过 **We Connect / MyŠkoda** 的预热在车辆菜单和 App 中设置。通常无需在 08 中单独做适配。

关于 DC 充电前的**高压电池预热**，见 [充电与高压](charging.md) —— 那是另一个回路（单元 **8C**），不是空调 08。
