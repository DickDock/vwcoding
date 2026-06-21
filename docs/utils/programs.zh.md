
# 功能编码工具

VAG 车辆控制单元的设置、编码与刷写有多种不同的适配器和程序。

## ODIS

最通用的工具之一。 

功能：  

* 向控制单元刷写并加载参数集  
* 编码与适配

由两个应用组成：

* ODIS S (Service) – 用于编码和适配的基础程序。能读取日志、清除故障码
* ODIS E (Engineering) – 更高级的工具，用于刷写、控制单元参数化

当前版本：ODIS E 12.2 与 ODIS S 6.2  

工作需要 VAS5054 适配器。该适配器可在 AliExpress 购买

## VCTools

VCTool – 是一款一键激活隐藏功能的软件。  
车辆诊断与控制单元手动设置。完整支持 SFD 保护系统。  
可激活 170 多项隐藏功能。

功能：  

* 向控制单元刷写并加载参数集  
* 编码与适配

该程序可与任何 J2534 适配器（包括 VAS5054A）配合使用。

* [程序官网](https://vctool.app/)

## ELM327 与 CarScanner

推荐软件：CarScanner  

* [程序官网](https://www.carscanner.info/)
* [如何选择适配器](https://www.carscanner.info/ru/choosing-obdii-adapter/)

CarScanner 应用能向控制单元加载参数集！目前提供用于激活 TJA 的参数集。

## VCDS

用于编码和适配的工具。不能刷写控制单元

!!! warning "注意"
    推荐版本：25.3  
    21.1.1 之前的版本不支持 2021 车型系列  

     不能读取以下单元：  
        - 29、39、D6、D7 – 因为读不到 4B  
        - 76 单元在 VCDS 中显示为 10  
        - CA

有两个变体： 

* [car2diag](https://car2diag.ru/)（原版的俄文复制版 - Вася диагност）
* [Ross-tech](https://www.ross-tech.com/)（原版 VCDS）

工作需要 VAG COM 适配器

## ODBELEVEN (OBD11)

[OBD11](https://obdeleven.com/) – 用于控制单元编码和适配的便捷工具。  
不能刷写控制单元。包含需用积分付费的功能。  

能加载有限的一组参数集，例如用于激活行车视频的参数集。  

仅在移动设备上运行。

!!! warning ""
    对于 2021 年生产的车辆，应用编码时需打开机盖并拉起手刹

## ELM327

也可以用便宜的中国产 OBDII 适配器对控制单元进行编码和设置。  

推荐软件：

* [Car Scanner](https://www.carscanner.info/)

## VCP

[VCPSYSTEM](http://vcpsystem.ru/) – 用于电子部件的诊断与编程。  
可对各类控制单元进行编码、设置和刷写。数据库中包含大量参数集。  

推荐版本：VAG CAN PRO 8.7 及以上
