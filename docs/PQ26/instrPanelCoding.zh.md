# 仪表盘背光曲线 

![Screenshot](../images/PQ26/instr_main.png)  
好，我们都在 17 单元里见过这些通道（下面以 5JA-920-740-A 为例讲解，可推广到 5JA 920 7XX）：  
ENG105831-ENG101574-dimming_characteristic_curve_adjustment_clock_dial_day-X1,00 …  
ENG105831-ENG99777-dimming_characteristic_curve_adjustment_clock_dial_day-Y1,00 …  
ENG105832-ENG101574-dimming_characteristic_curve_adjustment_clock_dial_night-X1,00 …  
ENG105832-ENG99777-dimming_characteristic_curve_adjustment_clock_dial_night-Y1,02 …  
ENG105834-ENG101574-dimming_characteristic_curve_adjustment_gauge-X1,00 …  
ENG105834-ENG99777-dimming_characteristic_curve_adjustment_gauge-Y1,03 …  
ENG105835-ENG101574-dimming_characteristic_curve_adjustment_indicator_lights-X1,00 …  
ENG105835-ENG99777-dimming_characteristic_curve_adjustment_indicator_lights-Y1,05 …  
ENG119878-ENG101574-dimming_characteristic_curve_adjustment_internal_phototransistor-X1,00 00 …  
ENG119878-ENG99777-dimming_characteristic_curve_adjustment_internal_phototransistor-Y1,00 00 …  
ENG105836-ENG101574-dimming_characteristic_curve_adjustment_middle_display_main_field-X1,00 …  
ENG105836-ENG99777-dimming_characteristic_curve_adjustment_middle_display_main_field-Y1,01 …  

通道有很多，每个位置有 5–6 个 X 和 Y 值。一对 X 与 Y 的设定称为一条曲线。  
这样就有 6 条曲线：  

* dimming_characteristic_curve_adjustment_clock_dial_day — 日间模式刻度盘背光亮度  
* dimming_characteristic_curve_adjustment_clock_dial_night — 夜间模式刻度盘背光亮度  
* dimming_characteristic_curve_adjustment_gauge — 仪表指针背光亮度  
* dimming_characteristic_curve_adjustment_indicator_lights — 仪表盘附加指示灯亮度  
* dimming_characteristic_curve_adjustment_internal_phototransistor — 仪表光照传感器读数归一化曲线  
* dimming_characteristic_curve_adjustment_middle_display_main_field — 仪表盘中部显示屏亮度  

日间模式与夜间模式的区别在于是否开启近光。近光点亮 — 即夜间模式。  

我们来尝试适配日间/夜间模式刻度盘背光亮度曲线，以及仪表光照传感器读数归一化曲线。  
通道值以 16 进制 (HEX) 给出。把 X 和 Y 值画在图上，得到以下图形：  
![Screenshot](../images/PQ26/chart1.png)  
刻度盘背光亮度

![Screenshot](../images/PQ26/chart2.png)  
仪表光照传感器读数归一化曲线  

只处理 16 进制数。换算成 10 进制只是为了画图。  
亮度设定的修改方案：  

* dimming_characteristic_curve_adjustment_clock_dial_day,  
* dimming_characteristic_curve_adjustment_clock_dial_night  
日间和夜间模式刻度盘背光亮度设定曲线。只处理 Y 值。0 — 关闭背光。253 — 最大亮度。为了避免黄昏时刻度盘背光被关闭，需要去掉日间背光曲线中的 0 值（表中以黄色标出）。绿色列中的值可按喜好调整。日间模式取消了黄昏时刻度盘的完全熄灭。夜间模式给出一条在传感器读数较高时光线更暗的曲线。

![Screenshot](../images/PQ26/chart3.png)  
![Screenshot](../images/PQ26/chart_table3.png)  
dimming_characteristic_curve_adjustment_internal_phototransistor  

把光照传感器读数归一化到 0.253 区间的曲线。0 — 暗，253 — 最亮。可以让曲线更陡地到达最大值。只处理 X 坐标。

![Screenshot](../images/PQ26/chart4.png)  
![Screenshot](../images/PQ26/chart_table4.png)  
众所周知，仪表盘被设定为通过关闭刻度盘背光，在黄昏时提醒你忘关近光。  
许多人不喜欢这种工作逻辑 — 解决办法：  
ENG105831-ENG99777-dimming_characteristic_curve_adjustment_clock_dial_day-Y1,03  
ENG105831-ENG100480-dimming_characteristic_curve_adjustment_clock_dial_day-Y2,05  
ENG105831-ENG100773-dimming_characteristic_curve_adjustment_clock_dial_day-Y3,08  

更改这三个通道的值 — 即可让黄昏时仪表刻度盘背光不被关闭。这些通道原本为 0 值。  

不建议改变亮度变化方向，也不建议把值拉到最大。
我自己没有设置黄昏时关闭背光 — 现状就很满意。  

访问码需要自行尝试。可试 47115。
