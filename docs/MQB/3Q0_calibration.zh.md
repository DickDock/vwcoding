
# 3Q0/3QD* (MFK 2.0) 辅助摄像头标定

为使 Lane Assist 摄像头成功、正确地工作，需要：
1. 已刷入正确的参数集
2. 正确安装的 Lane Assist 摄像头
3. 正确的摄像头编码
4. 正确执行的摄像头标定流程

## 适配

Calibration target position 适配通道不影响摄像头标定，但可能影响其工作
``` yaml
单元 A5 (辅助摄像头) → 适配:
Calibration target position-Target 1: calibration mark 1: x-coordinate, Passat 2400 mm (Tiguan 2541 mm)
Calibration target position-Target 1: calibration mark 1: y-coordinate, Passat 745 mm (Tiguan 735 mm)
Calibration target position-Target 1: calibration mark 1: z-coordinate, Passat 1506 mm (Tiguan 1694 mm)
Calibration target position-Target 1: calibration mark 2: x-coordinate, Passat 2400 mm (Tiguan 2541 mm)
Calibration target position-Target 1: calibration mark 2: y-coordinate, Passat -745 mm (Tiguan -735 mm)
Calibration target position-Target 1: calibration mark 2: z-coordinate, Passat 1506 mm (Tiguan 1694 mm)
Calibration target position-Target 1: calibration mark 3: x-coordinate, Passat 2400 mm (Tiguan 2541 mm)
Calibration target position-Target 1: calibration mark 3: y-coordinate, Passat 745 mm (Tiguan 735 mm)
Calibration target position-Target 1: calibration mark 3: z-coordinate, Passat 846 mm (Tiguan 1106 mm)
Calibration target position-Target 1: calibration mark 4: x-coordinate, Passat 2400 mm (Tiguan 2541 mm)
Calibration target position-Target 1: calibration mark 4: y-coordinate, Passat -745 mm (Tiguan -735 mm)
Calibration target position-Target 1: calibration mark 4: z-coordinate, Passat 846 mm (Tiguan 1106 mm)
```
坐标 X —— 从摄像头镜孔到标定板的距离（纵轴），  
Y —— 沿水平横轴的标定点，  
Z —— 沿垂直轴的标定点（随不同车辆摄像头高度而变化）。 

## 安装标定板

标定用样板  
![Screenshot](../images/MQB/addons/Front_maket.jpg)  

标定板应居中置于车辆正前方，距前轮中心轴 1500 mm，安装高度为从车辆所在平面到标定板上边缘 1570 mm。  

第 1 步 —— 将标定板置于距车辆前轮中心轴 1500 mm ± 20 mm 处。安装高度为从车辆所在平面到标定板上边缘 1570 mm。标定板必须严格水平（垂直和水平方向都要），标定板的垂直中心必须与车辆纵向中心重合，且标定板平面必须严格垂直于车辆纵轴。  
第 2 步 —— 执行标定（标定流程见下）。标定时输入轮拱的**真实**高度值！

标定板安装高度计算：

=== "Sedan 车身"
    1200 —— 摄像头高度  
    535 —— 从标定板下缘到白色矩形的距离  
    110/2=55 —— 从矩形下部到其中心的距离  
    960 —— 从下缘到样板上缘的距离  
    合计：1200-535-55+960=1570（到样板上缘）

=== "Crossover 车身"
    1480 —— 摄像头高度  
    535 —— 从标定板下缘到白色矩形的距离  
    110/2=55 —— 从矩形下部到其中心的距离  
    960 —— 从下缘到样板上缘的距离  
    合计：1480-535-55+960=1850（到样板上缘）

## 标定流程

1. Odis Service –「数据总线拓扑」，单元 A5，右键点击「单元识别」，单元列表中 A5 会变为可用。 
2. 选择「驾驶员前部辅助系统传感器 (BOSCH)」项
3. 在 A5 单元上右键 – 测量技术
4. 选择 A5 – 标定
5. 在接下来的 4 步中输入轮拱的**真实**高度值。

标定流程持续最多 10 秒，之后系统会要求关闭点火、等待、再重新打开。  
结果中的角度应尽可能接近 0。 
3 度是摄像头无法标定的临界值。实践中 1 度以内的角度属正常。
![Screenshot](../images/MQB/Initial%20calibration.png)  

以 65 km/h 以上的速度在有标线的道路上行驶 10 分钟做一次测试行驶，检查动态标定（行驶中标定）的值。  
动态标定角度的最大值为 3 度。  
一旦该角度更大，摄像头就会报错、辅助系统将关闭。  
如果动态标定（即纵向倾角）高于 1.5 度，说明标定时标定板安装不正确或刷入了错误的参数集。
![Screenshot](../images/MQB/Dynamic%20calibration.png)  
