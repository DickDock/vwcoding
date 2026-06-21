# 充电与高压电池

!!! warning ""
    MEB 上的 **C5**、**8C**、**8B**（BMS）单元受 **SFD** / **SFD2** 保护。DC/AC 限值**由 BMS 决定**，而非某一项「最大电流」适配。

## 原生可设置项（无需 ODIS）

在 ID.3/ID.4/Enyaq 的**充电**菜单中：

- **降低 AC 电流**（例如 8 A 而非 16 A）—— 适用于较弱的家庭电网  
- **Departure time** —— 按电价延迟充电  
- **最低 SOC**（0–50%）—— 「不低于此」放电阈值  
- **DC 优化** —— 按含充电站的路线自动预热电池（preconditioning）

这些功能无需编码。

## 充电慢的诊断（ODIS / OBD）

有用的**测量值**（名称可能因 SW 而异）：

| 单元 | 看什么 | 为什么 |
|------|-------------|-------|
| **C5 / 8B** | Dynamic limit for charging (A) | BMS 当前的真实限值 |
| **C5 / 8B** | HV battery min/max temperature | 电池冷 = DC 低 |
| **8E** | AC charge power / phases | 车载充电机限制 |
| **19** | Charging mode | AC / DC / 电缆错误 |

!!! tip ""
    如果 **Dynamic limit** 很高但充电桩给的更少 —— 限制在**充电桩**一侧。如果电池温暖时 BMS 限值仍很低 —— 排查 BMS 故障、绝缘、SW 更新。

## 手动预热高压电池（8C，仅诊断）

!!! danger ""
    **非原生功能。**爱好者在寒冷天 DC 充电前使用。有拒保、HV 故障、测试异常终止的风险。仅在停车时、且可访问 ODIS 的情况下进行。

在部分 ID.3/ID.4 上（单元 **8C** Battery Energy Module）：

1. ODIS online，对 8C 解锁 **SFD**。  
2. **Change Service → Development Mode**（否则 output test 可能无法启动）。  
3. **Output test** —— HV battery heater（名称取决于 SW），约 300 秒。  
4. 点火 ON，首次启动时可微开机盖。  
5. 监控：live data 中预热功率约 5–6 kW；pack 温度上升。

原生的**导航预热（preconditioning）**更安全，且无需 development mode。

## 单元 C5 —— 通常**不**编码的项

- DC 最大功率（135 kW 等）—— 由 BMS 和温度决定  
- 电池容量（58 / 77 / 82 kWh）—— 硬件决定，无法用代码「开启」  
- 双向充电（V2H）—— 取决于 PR、SW 和市场，不是通用适配

当充电功率「丢失」时，先检查 **C5/8C 的故障**、**12V**（弱 AUX → 频繁唤醒）、通过 ODIS 的 **SW 更新**。
