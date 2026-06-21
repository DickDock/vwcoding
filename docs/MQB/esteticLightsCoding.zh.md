
# 车内照明区域编码

## 通用信息

!!! note ""
感谢 [Вячеслав](https://www.drive2.ru/users/slavian116) 协助制作本说明

??? tip "亮度调节区域标识列表"  
innenlicht – 车内照明  
fussraum – 脚部  
tueren – 车门  
cockpit – 前面板（无线充电凹槽）
miko – 中控台  
dach – 顶部

??? tip "现有灯具列表"
Ambiente_Applikationsleisten_in_Tuertafel – 车门饰板照明 Ambiente_Lautsprecher – 扬声器照明  
Ambiente_Applikationsleisten_in_Instrumententafel – 无线充电凹槽照明  
Cockpitbeleuchtung – 前控制台照明  
Mittelkonsolenbeleuchtung – 无线充电凹槽照明  
Dachbeleuchtung – 顶部照明  
Panoramaschiebedachbeleuchtung – 全景天窗照明  
Fussraumbeleuchtung – 脚部照明

!!! note ""
这些编码只能通过 OBD11 或 ODIS 进行

    要加装额外的车内照明灯具，需执行几个步骤：  
    - 安装灯具，挂接到一个空闲灯具上
    - 激活灯具  
    - 设置亮度  

### 在氛围灯菜单中绘制"小太阳"

!!! note ""
在 composition color 上不工作（它没有区域可视化，区域以列表形式呈现）。  
此编码只能通过 OBD11 或 ODIS 进行

此编码适用于出厂只有脚部照明、没有氛围灯的人。  
这种情况下，激活氛围灯后常常会失去对脚部照明区域的调节能力，即那个小太阳及其可视化。

此外，这些信息对已经加装或打算加装额外照明灯的人也有用。

在 9 单元中，氛围灯菜单中附加区域的激活由 3 个适配参数负责 *车内照明, 参数 / Interior_light_parameter*

```
- p_ambientelicht_verbauinformation_HMI
```

| 位 | 说明                                            |
|-----|-----------------------------------------------------|
| 0   | 脚部照明（脚部照明灯可视化）* |
| 1   | 脚部照明（无可视化）                    |
| 2   | 前面板照明（条状可视化）*        |
| 3   | 空                                               |
| 4   | 中控台（无可视化）              |
| 5   | 前面板照明（无可视化）             |
| 6   | 前面板照明（无可视化）             |
| 7   | 前面板照明（无可视化）             |

```
- p_ambientelicht_verbauinformation_HMI2
```

| 位 | 说明                                                |
|-----|---------------------------------------------------------|
| 0   | 中控台（无可视化）                  |
| 1   | 中控台（无可视化）                  |
| 2   | 车门照明（把手照明灯可视化）* |
| 3   | 车门照明（无可视化）                      |
| 4   | 车门照明（条状可视化）*                 |
| 5   | 车门照明（无可视化）                      |
| 6   | 车门照明（无可视化）                      |
| 7   | 车门照明（无可视化）                      |

```
- p_ambientelicht_verbauinformation_HMI3
```

| 位 | 说明                                           |
|-----|----------------------------------------------------|
| 0   | 车门照明（无可视化）                 |
| 1   | 顶部照明（无可视化）               |
| 2   | 顶部照明（灯具照明可视化）* |
| 3   | 顶部照明（无可视化）               |
| 4   | 空                                              |
| 5   | 空                                              |
| 6   | 空                                              |
| 7   | 空                                              |

编码示例 – 激活顶部照明的"小太阳"和可视化  
![Screenshot](../images/MQB/dach.png)

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_ambientelicht_verbauinformation_HMI3: 110
→ 应用
```

编码示例 – 激活把手照明的可视化  
![Screenshot](../images/MQB/door.png)

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_ambientelicht_verbauinformation_HMI2: 100
→ 应用
```

### 在空闲通道上安装灯具

要连接 LED，需在 BCM 上找到空闲引脚。这取决于配置。  
然后找到相应的空闲通道，例如 MID LED 的车主可以把灯接到引脚 36，  
然后在编码 Leuchte0BLK VLB36 中设置该空闲通道，并在其中写入 LED 和功能。

可能的功能：

| 功能         | 说明               |
|-----------------|------------------------|
| Ambientelicht 1 | 杂物箱上方的小太阳 |
| Ambientelicht 2 | 杂物箱上方的小太阳 |
| Ambientelicht 3 | 车门小太阳         |
| Ambientelicht 4 | 空                  |
| Ambientelicht 5 | 空                  |

``` yaml
Lasttyp 0 — LED Kleinleistung
Lichtfunktion A 0 – Ambientelicht 1
Dimmwert AB 0 — 99
``` 

### 激活灯具

如果某个"小太阳"开启后没有出现，则需要激活灯具本身。  
例如，激活脚部照明灯具：

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 灯具配置 / Interior_light_lamp_configuration
- Fussraumbeleuchtung: installed
```

### 设置照明亮度

9 单元中负责特定灯具亮度值的参数如下：

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
p_adaption_kundenwunsch_
p_helligkeit_entriegelt_
p_helligkeit_max_
p_helligkeit_HD_auf_zuendung_ein_
p_helligkeit_HD_auf_zuendung_aus_
p_helligkeit_dieseTuer_auf_zuendung_ein_
p_helligkeit_andereTuer_auf_zuendung_ein_
p_helligkeit_Fzg_geschlossen_zuendung_ein_
p_helligkeit_dieseTuer_auf_zuendung_aus_
p_helligkeit_andereTuer_auf_zuendung_aus_
p_helligkeit_einausstieg_
p_helligkeit_Fzg_geschlossen_zuendung_aus_
p_helligkeit_Tueren_geschlossen_HD_auf_zuendung_aus_
p_helligkeit_Tueren_geschlossen_HD_zu_zuendung_aus_
p_helligkeit_Tueren_geschlossen_schluessel_ab_
p_helligkeit_Fzg_geschlossen_schluessel_ab_
```

所有值都可以例如从已有通道中获取，例如脚部照明：fussraum

灯罩默认亮度

``` yaml title="登录密码: 31347"
单元 09 → 适配:
第 2 代车内照明 / Interior_light_2nd_generation
- Defaultwert Ambienteprofil Mittelkonsole: 80
- Defaultwert Ambienteprofil Dach: 80
- Defaultwert Ambienteprofil Farbe: 80
- Defaultwert Ambienteprofil Fussraum: 80
- Defaultwert Ambienteprofil Tuer: 80
```

亮度调节

``` yaml title="登录密码: 31347"
单元 09 → 适配:
第 2 代车内照明 / Interior_light_2nd_generation
- Helligkeit Mittelkonsolenbeleuchtung nicht berechnen — 未激活（禁止调节）
- Farbausgabe Mittelkonsolenbeleuchtung nicht berechnen — 激活（亮度调节）
```

## 车内照明的开启延迟

9 单元中的编码可实现车内灯光的顺序开启。

由以下参数负责：

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_t verzoegerung einstieg innenlicht — 入车时车内照明的开启延迟, 点火关闭
- p_t verzoegerung ausstieg innenlicht — 出车时车内照明的开启延迟, 点火关闭
- p_t verzoegerung oeffnen innenlicht — 开门时车内照明的开启延迟, 点火开启
- p_t verzoegerung entriegelt innenlicht — 解开中控锁时车内照明的开启延迟
- p_t verzoegerung schliessen innenlicht — 关门时车内照明的关闭延迟, 点火开启
- p_t verzoegerung schluessel ab innenlicht — 打开点火时车内照明的关闭延迟
- p_t verzoegerung verriegelt innenlicht — 锁中控锁时车内照明的关闭延迟
```

每个灯具共 7 个功能。其余所有灯具与车内照明（顶灯）类似。

例如，  
车门灯设为 0.8 秒，车内照明设为 1.6 秒。  
脚部照明保持不变并最先点亮，然后是车门，再是顶部。

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_t_verzoegerung_einstieg_fussraum: 0,0 s
- p_t_verzoegerung_einstieg_tueren: 0.8 s
- p_t_verzoegerung_einstieg_innenlicht: 1,6 s
→ 应用
```

车门关闭同样设为 0.8 秒，脚部设为 1.6 秒。  
车内照明最先熄灭。然后是车门，最后才是脚部。

``` yaml title="登录密码: 31347"
单元 09 → 适配:
车内照明, 参数 / Interior_light_parameter:
- p_t_verzoegerung_ausstieg_fussraum: 1,6 s
- p_t_verzoegerung_ausstieg_tueren: 0.8 s
- p_t_verzoegerung_ausstieg_innenlicht: 0,0 s
→ 应用
```
