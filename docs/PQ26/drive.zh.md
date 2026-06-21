# 动力与操控

### 6 速自动变速箱 (Aisin) 重新设定
``` yaml
单元 02 → 长编码: 
字节 00 – 位 00-23 – 000348 (标准) 或输入其他值 (000852)
→ 应用
```

也可以不进入长编码，把当前编码复制到「新编码」字段，再把其中前 6 位「000348」替换为「000852」。  
也有 7 位编码的单元，例如：「0101000」，相应地把前 7 位由「0101000」改为「0000008」。  

该自动变速箱可改成的值：  
— 0000328 — Škoda Rapid 及部分 VW 车型的出厂编码  
— 0000072 — Škoda Octavia A5FL 的出厂编码  
— 0000008 — Audi A3、Škoda Octavia A5、VW Touran（2005 MY 之前）的编码  
— 0008201 — Audi TT 的编码  
— 0008264 — Audi A3、VW Jetta 的编码  
— 0008520 — VW Tiguan 的编码 – 备选编码  

2015-2016 单元 09G 927 749xx（6 位编码）：  
— 000348 – 原厂  

自 2016 款起，单元 09G 927 749xx，自 2017 年起还有 09G 927 158 AL（已是 20 字节编码）。  
Octavia、Rapid 和 Polo 三厢最常见且唯一的编码是：– 010100000C000000000000000000000000000000。  
这类单元也可能有其他编码：  
— 010200000C000000000000000000000000000000 — 用于 1.4TFSI 和 1.8TFSI 发动机  
— 010500000C000000000000000000000000000000 — 用于 1.6 CPDA 发动机。  
相应地，对 20 字节编码 010100000C0 … 之后全为零，把前 7 位 — 例如改为 00000080C … 之后全为零（Audi A3）— 保存！

### 油门踏板重新编码（减小踩踏响应）
``` yaml
单元 01 → 长编码:  
字节 00 – 位 0-2 – 选择值 02 (制造商: Audi) – 执行。* 带定速巡航的车辆不推荐 — 巡航会出问题
→ 应用
```

### 更改 RAPID 电动助力转向设定（驾驶模式设定）
``` yaml
单元 44 → 长编码:  
字节 00 – 位 7: 激活。值由 00 改为 80。
→ 应用
```

``` yaml title="登录密码: 17580"
单元 44 → 适配
Characteristic curve of steering assistance → 选择所需值 (Driving profile selection button, Comfort, Automatic, Dynamic, Default)
→ 应用
* 推荐值 – Dynamic
Driving Profile switchover (驾驶模式切换) → 选择所需值 (Incremental controlled over time (随时间递增), direct…(直接…)) → 保存。
* 推荐值 – Direct
→ 应用
```

### 激活 TSC 功能 

!!! note ""
    侧向跑偏补偿、急加速时驱动轮扭矩差补偿 — 仅限 1.4TSI

``` yaml title="登录密码: 17580"
单元 44 → 长编码:  
字节 00 – 位 2-3: 激活。字节值由 00 改为 04
→ 应用
```

### 停用启停功能
``` yaml title="登录密码: 20103"
单元 19 → 适配:
EM_start_stop_requirement_ambient_temperature:
- Minimum_temperature → -50.0 °C 把值改为 50。
或按电压：
- Start Stop voltage limit → 7,6В 改为 12,1В
→ 应用
```
