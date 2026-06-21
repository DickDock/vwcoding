# 附加辅助（EA、TJA、单元 44）

除基础 [Travel Assist](travelAssist.md) 之外的 **MQB-Evo** 说明。  
「硬件」加装（radar、摄像头、方向盘）—— 可类比参见 [MQB / 加装](../MQB/addons.md)；这里只讲硬件已装好情况下的**编码**。

!!! warning ""
    向 **A5**、**44**、**13** 写入需要 **SFD**；在 2024+ 车辆上，每次操作需 **SFD2**。见 [SFD](../sfd.md)。

## Emergency Assist（紧急停车辅助）

当驾驶员无反应时（无 KLR / 长时间双手离开方向盘），EA 会带双闪让车辆停下。

### 激活 EA（已安装 ACC + A5 时）

:octicons-verified-24: SFD: yes

``` yaml title="Login code: 20103"
Блок A5 → Кодирование:
- Emergency_assist_variante: EA_Variante_2
→ 应用
```

``` yaml title="Login code: 20103"
Блок 13 → Кодирование:
- Emergency_assist: activated
→ 应用
```

!!! note ""
    对于 **Travel Assist**，这些通道常一并设置 —— 见 [Travel Assist](travelAssist.md)。  
    **无 KLR** 的 workaround（关闭 EA）—— 也在那里；仅作临时使用。

## Traffic Jam Assist（拥堵辅助）

TJA = ACC + **低速**下的自适应 Lane Assist（通常到 ~60 km/h）。需要 **ACC (13)**、**摄像头 A5** 以及兼容的摄像头**固件/参数集**。

!!! warning ""
    Evo 上的 **5WA 980 653** 摄像头与经典 MQB 上的 MFK2/3 是不同的 SW 系列。来自 [MQB / camAssistFirmwares](../MQB/camAssistFirmwares.md) 的参数集**未经核实不适用**。

### 典型 A5 通道

:octicons-verified-24: SFD: yes

``` yaml title="Login code: 20103"
Блок A5 → Кодирование:
- HC_Variante: Hc_variante_2
- HC_point_of_intervention: early_setting_over_menu
- Traffic_jam_assist: activated
→ 应用
```

### 单元 13 —— 摄像头已安装

:octicons-verified-24: SFD: no (部分 SW 上)

``` yaml title="Login code: 20103"
Блок 13 → Кодирование:
- Front_camera: installed
→ 应用
```

### 单元 44 —— 与转向助力的关联 (HCA)

:octicons-verified-24: SFD: yes

``` yaml title="Login code: 19249"
Блок 44 → Кодирование:
- Heading_control_assist: activated
→ 应用
```

### 车机 (5F) 中的菜单

``` yaml title="Login code: 20103"
Блок 5F → Адаптация:
Car_Function_List_BAP_Gen2:
- LDW_HCA_0x19: activated
Car_Function_Adaptations_Gen2:
- menu_display_Lane_Departure_Warning: activated
→ 应用
```

!!! tip ""
    **经典 MQB**（3Q0 + 参数集）的完整流程 —— 见 [MQB / 3Q0_assistants](../MQB/3Q0_assistants.md)。在 Evo 上请逐一核对每个通道是否存在。

## 单元 44 —— 转向助力

用于 **Travel Assist**、**TJA**、**Auto Lane Change**：

| 通道 | 用途 |
|-------|------------|
| `Heading_control_assist` | 通过电动助力实现 Lane Assist / TJA |
| `Qfk_ma_function` | Auto Lane Change（见 [Travel Assist](travelAssist.md)） |

:octicons-verified-24: SFD: yes

``` yaml title="Login code: 19249"
Блок 44 → Кодирование:
- Heading_control_assist: activated
→ 应用
```

Login **19249** —— 单元 44 的典型登录码；请在 ODIS 中按你的 SW 确认。

## Travel Assist 2024+（V2X、Golf 8.5、T-Roc FL）

从 **~2024 MY** 起，VW 扩展了 Travel Assist：

- **V2X / swarm data** —— 当有其他车辆数据或前车时，单侧标线也能保持车道  
- 高速公路上的 **Assisted lane change**（见 [Auto Lane Change](travelAssist.md#auto-lane-change-opcionalno)）  
- **弯道预警** —— 弯前的推荐车速（取决于导航）

!!! note ""
    **ODIS 中通常没有单独的「V2X: on」** —— 该功能由 **gateway 19 + A5 + 13 + 导航 + PR IQ.DRIVE** 这一组合开启。  
    SW 更新后请检查菜单中 **Travel Assist** 和 **Side Assist** 是否激活；只有当通道处于「not coded」时才需要编码。

### OTA / 经销商更新后应检查

1. **19**、**A5**、**13** 的 SW 版本 —— 不低于你车型的推荐版本。  
2. 13 中的 `Travel_Assist`、`KLR_installed` 通道 —— 见 [Travel Assist](travelAssist.md)。  
3. 是否有 **电容式方向盘 (KLR)** 以实现完整 TA（非 workaround）。  
4. 在 **2024+** 上 —— 任何写入都需 **SFD2**。
