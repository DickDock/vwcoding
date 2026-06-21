# Travel Assist

Travel Assist 整合了 **ACC** 与 **Lane Assist**：车辆保持车距并居中于车道内。

!!! warning "重要信息"
    - 完整的 Travel Assist 需要 **ACC**、辅助摄像头 **A5**，通常还需 **电容式方向盘 (KLR)**。
    - 在 MQB-Evo 上，几乎所有对 **A5** 和 **13** 单元的写入都需要 **SFD** —— 见 [SFD 与 SFD2](../sfd.md)。
    - 编码前请备份 A5 和 13 单元。

!!! note ""
    这些编码在 Golf 8、Octavia 4、Leon 4、Formentor 上验证过。摄像头与 radar 的 SW 必须支持该功能 —— 请核对固件版本。

## 激活 Travel Assist

### 第 1 步 —— 单元 A5（辅助摄像头）

:octicons-verified-24: SFD: yes

!!! tip ""
    通道名称可能因 SW 而异。请在 ODIS/OBD11 中查找对应项。

=== "在 ODIS 中编码"
    ``` yaml title="Login code: 20103"
    Блок A5 → Кодирование:
    - HC_point_of_intervention: early_setting_over_menu
    - HC_Variante: Hc_variante_2
    - Emergency_assist_variante: EA_Variante_2
    - Lane_Assist_off_Text: Deactivated
    - HC_advanced_takeover_request: Not_coded
    → 应用
    ```

=== "在 OBD11 中编码"
    ```yaml
    A5 Front sensor driver assist → Long coding:
    - HC point of intervention: early (via menu)
    - HC Variante: Variante 2
    - Emergency assist variante: EA Variante 2
    - Lane Assist off text: Disabled
    ```

### 第 2 步 —— 单元 13（ACC radar）

:octicons-verified-24: SFD: no (部分 SW 上对所列通道)

``` yaml title="Login code: 20103"
Блок 13 → Кодирование:
- KLR_installed: installed
- Travel_Assist: activated
- Overtaking_right_prevention: deactivated
→ 应用
```

!!! note ""
    `Overtaking_right_prevention: deactivated` —— 可选，关闭 ACC 时的右侧超车限制（另见 [ACC](acc.md)）。

### 编码之后

1. 如果 A5 和 19 (Gateway) 出现故障，清除之。
2. 关闭点火，锁车 1–2 分钟。
3. 在辅助菜单中检查 **Travel Assist** 项。

## 如果 Travel Assist「不可用」（无 KLR）

在没有电容感应条 KLR 的方向盘上，系统可能显示可用性错误。

**临时 workaround**（风险自负 —— 会关闭 Emergency Assist）：

=== "在 OBD11 中编码"
    ```yaml
    A5 → Long coding:
    - Emergency_Assist: Not_coded
    - KLR: Not_coded
    ```
    然后清除 A5 和 Gateway 中的 DTC，做一次点火循环。

!!! danger ""
    在驾驶员无反应时，Emergency Assist 将不会带双闪自动停车。仅作为安装 KLR 方向盘前的临时措施使用。

## Auto Lane Change（可选）

**并非所有**配置都可用。典型要求 (2023+)：

- ACC + Side Assist（盲区）
- 摄像头 A5 **5WA 980 653D**，SW **3403+**
- 泊车辅助 PLA (12K)
- 导航

请按 VIN 和 PR 号核对兼容性 —— 该功能取决于工厂和市场。

### 设置（若硬件支持）

:octicons-verified-24: SFD: yes

!!! warning ""
    请备份 **09**、**44**、**A5** 单元。在 2024+ 车辆上，每次写入可能需要 **SFD2**。

=== "在 ODIS 中编码"

    ``` yaml title="Login code: 20103"
    Блок 09 → Адаптация:
    转向灯辅助的 BCM 功能:
    - Travel_Assist_Blinken: active
    → 应用
    ```

    ``` yaml title="Login code: 20103"
    Блок 44 → Кодирование:
    - Qfk_ma_function: active
    → 应用
    ```

    ``` yaml title="Login code: 20103"
    Блок A5 → Кодирование:
    - HC_Variante: Hc_variante_3 (或 Hc_variante_5)
    - HC_mob_line: coded
    → 应用
    ```

!!! tip ""
    在部分车辆上，BCM 中不用适配 `Travel_Assist_Blinken`，而是用通道 **Flashing function — Travel Assist → Active**。  
    该功能通常在高速公路上 **从 ~90 km/h 起** 生效。对于 PLA **12K**，可能需要单独编码 **76** 单元 —— 请核对 SW 和 PR 码。
