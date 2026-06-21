
# 解除 Component Protection 与 Discover Pro 的 SWaP 码

!!! warning 
    你所做的一切，全部由你自行承担责任！如果没有把握 —— 不要开始！  
  
所有操作仅借助 [M.I.B. bash](https://wiki.mibsolution.one/en/MHI2) 工具完成，也就是说现在激活所有选项只需一张 SD 卡。  

此补丁适用的固件列表：  
![Screenshot](../images/MQB/MIBII/mib2_vers.jpeg)  

功能激活列表：  
![Screenshot](../images/MQB/MIBII/mib2_func.jpeg)  

如果你是 MIB2 high，但固件与上表不符 —— 请做更新，更新到有补丁的版本。

激活流程：  
1. 把所有文件复制到 SD 卡 
2. 在 patches 文件夹中只保留 1 个与你当前固件版本对应的文件夹  
3. 启动软件更新。补丁已包含 GEM 激活。车机会重启几次  
4. 安装结束后进入 GEM，选择 ==>>M.I.B.-More_Incredible_Bash<<==  

![Screenshot](../images/MQB/MIBII/patch_menu.png)  

第 3 项包含所有必要的 FEC 码，以及组件保护的解除。  

!!! warning ""
    此补丁仅包含 SWaP。某些选项之后还需要在单元的编码和适配中做修改。  
    例如，要激活该放大器需加载参数集：  
    [(ODIS 用参数集)](../parameters/5F_ICC_ONLY.xml.zip)  
  
    要激活 Android Auto 或 CarPlay，需执行相应的编码。
