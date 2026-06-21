
# 声音

### 改善音质

!!! tip ""
    此设置对车机音质的改变非常有限。  
    要获得更好的音质，需向单元加载参数集。

=== "在 ODIS 中编码"  
    ``` yaml title="登录密码: 20103"
    单元 5F → 编码:
    byte_11_Sound_System: Sound_System_no_Allocation 或 Sound_System_Internal 
    → 应用（需重启单元）
    ```

=== "在 OBD11 中编码"
    ``` yaml title="登录密码: 20103"
    5F – MMI / RNS → 编码 - 07 → 长编码:
    字节 11 – 选择 01 – Sound_System_no_Allocation 或 04 – Sound_System_Internal
    退出 → 保存  
    ```

### 提高麦克风灵敏度

!!! tip ""
    车内通话时驾驶员的声音更清晰了。调节范围从 -10 到 10。最佳值从 2 起。

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 5F → 适配:
    Microfone sensivity (Mikrofonempfindlichtkeit)
    - 从 2 到 10Db
    → 应用 
    ```

=== "在 OBD11 中编码" 
    ``` yaml title="登录密码: 20103"
    单元 5F 电子信息系统 → 适配:
    麦克风灵敏度: 2-10 Дб
    ``` 