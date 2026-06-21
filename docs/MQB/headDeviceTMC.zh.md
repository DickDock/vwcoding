
# 为 MIB2/2.5 HIGH 导航系统激活 TMC

交通信息频道 (Traffic Message Channel, TMC) —— 一种传输交通拥堵和不良道路状况信息的技术。  
通常，数据以数字代码形式传输，使用无线电报警系统 (FM-RDS) 供普通 FM 接收机使用。  
支持 TMC 功能可让车辆导航系统获取交通事故路段信息，并规划绕开问题路段的备选路线。  

!!! info "有广播的城市"
    莫斯科（及周边城市）  
    圣彼得堡（及周边城市、加里宁格勒）  
    叶卡捷琳堡（及俄罗斯乌拉尔联邦区其他城市）  
    下诺夫哥罗德（及俄罗斯伏尔加联邦区其他城市）  
    克拉斯诺达尔（及俄罗斯南部联邦区其他城市）  
    新西伯利亚（及俄罗斯西伯利亚联邦区其他城市）

## 安装

安装分几个阶段，使用修改版 mib2-toolbox 工具（工具由 https://www.drive2.ru/users/kisyabrus/ 提供）  
[(Škoda 用)](../firmwares/TMC-zz.rar)  
[(Volkswagen 用)](../firmwares/TMC-vw.rar)  

安装内置区域支持脚本的 mib2-toolbox 工具：  
1. 下载压缩包  
2. 解压到 SD 卡根目录  
3. 删除之前安装的 mib2-toolbox  
4. 将卡插入车机  
5. 长按 MENU 键进入服务菜单  
6. 选择 "Software updates/versions" 项并点击右上角的 "Update" 按钮  
7. 选择 SD 卡和 MQB Coding MIB2 Toolbox  
8. 安装后系统会提示连接适配器以清除错误。选择 "Cancel"  
9. 长按 MENU 键进入服务菜单  
10. 进入 TESTMODE  
11. 进入 Green Developer Menu  
12. 菜单中会出现一个附加项 - "mqbcoding"  
  
![Screenshot](../images/MQB/MIBII/green_menu.png)  

安装所需区域  
1. 进入 "mqbcoding"，选择 customization/advanced  
2. 安装对应区域的补丁，例如 Install RussiaTMC Patch (Ekaterinburg, TMC25)
    ![Screenshot](../images/MQB/MIBII/install_patch.png)
3. 重启设备  
4. 进入 "mqbcoding"，选择 customization/adaptation/rccadaptations  
5. 在 PayTMC 适配中设值 15  
  
![Screenshot](../images/MQB/MIBII/set_TMC_region.png)  
  
用 Green Developer Menu 重启，否则适配不会生效  

![Screenshot](../images/MQB/MIBII/reboot_unit.png)  
  
重启后，车机需要一点时间从相应频率读取并接收信息。  

尽情享受拥堵显示吧！  

![Screenshot](../images/MQB/MIBII/tmc.png) 
