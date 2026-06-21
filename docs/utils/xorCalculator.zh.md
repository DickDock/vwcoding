---
hide:
  - toc
---
# XOR 计算器

本计算器用于确认 VW 车辆的车机固件。 
在 5F 单元更换固件后，可能出现错误 `1555 / B201A – 安装更改确认`。

确认固件更改需要：  
1. 从适配中读取代码：
    ``` yaml
    单元 5F → 适配:
    安装更改确认 (Confirmation of installation change)  
    ```
2. 将代码输入计算器并生成确认代码
3. 将代码写回适配：
    ``` yaml
    单元 5F → 适配:
    安装更改确认 (Confirmation of installation change): 生成的代码
    → 应用
    ```

--8<-- "overrides/pages/xorCoding.zh.html"
