
# 驾驶模式选择设置 (FPA 参数集)

修改 FPA 参数集需安装：  
- 010 Editor 编辑器 (https://www.sweetscape.com/010editor/)  
- fpa_dataset.bt 模板 (https://github.com/jilleb/MQB-FPA/)  
- fpa_dataset_save.1sc 脚本 (https://github.com/jilleb/MQB-FPA/)

## 参数集

我们关注的是 19 单元的参数集，位于地址 0x0000B80。  
参数集的前 4 字节是版本。例如，0x4E, 0x43,0x30,0x30 = NC00。

只能通过 ODIS online 获取参数集。  

## 在 010 Editor 中编辑参数集

1. 打开下载好的 FPA 参数集文件，复制 <PARAMETER_DATA> 区段中的所有位。  
2. 进入 010 editor，新建文档并切换到 hex-mode (View → Edit as → HEX)。  
3. 将复制的字节粘贴到编辑器中 (Edit → Paste from → Paste from HEX text)。
4. 然后运行 fpa_dataset 模板 (Run template)。编辑器中的值会被标成不同颜色：  
   1. 绿色 = 已知且已验证的值，  
   2. 黄色 = 可能的值，  
   3. 红色 = 未知，  
   4. 浅蓝 = 用于 hybrid cars。

![Screenshot](../images/MQB/fpa_editor.jpeg)  

## 可以做什么

1. 关闭标准模式下旋钮上常亮的 Mode 指示灯 (mode_light_on = 00)。  
2. 让 DSG 在熄火后保留所选模式（值 FFFE）。  
3. 四驱设置：Eco、Normal、Offroad。  
4. 可开启/关闭 DSG 滑行模式。  
5. 发动机设置。  
6. 模式的精细设置。  
7. 开启 DCC（如已安装）。  

## 保存参数集

脚本 "fpa_dataset_save.1sc" 用于生成 ODIS 或 VCP 格式的参数集。  
  
在脚本文件中可设置：  
```
saveFormat = 0; // VCP format  
saveFormat = 1; // ODIS format  
```
```
saveAddress = 0; // This will use 0x0B80 as flashing address (newer gateway firmware versions)  
saveAddress = 1; // This will use 0x2388 as flashing address (older gateway firmware versions)  
```

之后用脚本下载修正后的参数集并将其刷入 19 单元。
