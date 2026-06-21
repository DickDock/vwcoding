# 车机 (ICAS)

!!! warning ""
    MEB 上的 **5F** 单元受 **SFD** 保护。写入请使用 ODIS online。

### Video in Motion（行车视频）

!!! note ""
    视频锁定的速度阈值在 5F 单元中设置。确切的通道名取决于 ICAS 版本（Discover Pro / Max）。

``` yaml title="登录码: 20103"
单元 5F → 适配:
Video_speed_threshold: 0 km/h
→ 应用
```

通过参数集的替代方案 —— 见 [MQB / 车机](../MQB/headDevice.md)（Video in motion 一节）以及[工具](../utils/fec.md)中的 FEC 生成器。

### 关闭启动时的音量跳变

``` yaml title="登录码: 20103"
单元 5F → 适配:
Loudness_normalization_startup: deactivated
→ 应用
```

!!! tip ""
    如果没有该通道，请在 [mibsolution.one](https://mibsolution.one) 查找适用于你 ICAS 的最新参数集。

### Developer menu / 工程菜单

与 MQB Evo 类似 —— 通过 SWaP/FEC 或 ODIS Engineering 的工程菜单。  
见 [MQB-Evo / 车机](../MQB-Evo/headControlUnit.md)。
