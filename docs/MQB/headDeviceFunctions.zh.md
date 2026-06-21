
# Composition Media 与 Discover Media 的 SWaP 码与参数集

!!! warning 
    你所做的一切，全部由你自行承担责任！如果没有把握 —— 不要开始！

## Delphi 设备的语音助手、MirrorLink、Bluetooth 与运动监视器

### 需要准备什么

1. USB-Ethernet 适配器：  
首选：d-link dub e 100 修订版 b1（银色）、c1、d1  
或 https://aliexpress.ru/item/32969701309.html?spm=a2g0s.9042311.0.0.3b9d33edZKppDb&sku_id=12000018080745527  
可谓开箱即用、无需折腾，或其他采用 ASIX 88772 芯片的设备
2. 车机固件  
3. 车机 SWaP

### 关于车机的信息

如何识别 Delphi 模块？  
Delphi 模块始终是标准设备，而非高端设备。  
因此 Delphi Unit 始终是 Discover Media，而非 Discover Pro。  
所有 Delphi 模块都是 Discover Media 设备，但并非所有 Discover Media 设备都是 Delphi 模块！
Discover Media 也可能是 Technisat Preh 设备 —— 仅供参考。  
要在不拆机的情况下识别设备，需长按收音机上的「MENU」键，直到打开另一个菜单。 
  
![Screenshot](../images/MQB/MIBII/1.png)

在该菜单的「更新 / 软件版本」项中可以看到软件版本。  

![Screenshot](../images/MQB/MIBII/2.png)

(Delphi) SW Train Version (MST2_EC_VW_P0891D) – 构成如下：  

```
MST2 = MIB2 标准设备  
ЕС = 欧洲版本（美版与之对应）  
VW = 汽车品牌  
0891 = Firmware 0891  
D = Delphi 模块的简短版本  
```

如果 SW Train 版本末尾是字母 D，说明你有一个 Delphi 模块。  
如果在品牌后看到 PQ 或 ZR、或 SW Train 版本末尾是字母 T，说明你的是 Technisat Preh 设备。  

### 设备刷机 

!!! note ""
    据我们所知，只有 0891 固件才能通过 Ethernet-USB 连接 MIBII

刷写车机需要准备：

1. SD 卡  
2. Delphi 设备固件 [(下载)](https://yadi.sk/d/foeH0Izi_vW4_g)
3. 已激活的工程菜单 [(说明)](../headDevice/#_3)

MIBII 软件更新  
1. 将 SD 卡格式化为 FAT32  
2. 将固件更新文件复制到 SD 卡（解压压缩包后，根目录应有 3 个文件夹和一个文本文件）  
3. 将 SD 卡插入 SD 卡槽 1  
4. 移除所有其他 SD 卡和 USB 设备！  
5. 长按收音机上的 MENU 键，直到打开另一个（服务）菜单  
6. 在其中选择测试模式  
![Screenshot](../images/MQB/MIBII/3.png)  
7. 进入「SWDL」类别  
![Screenshot](../images/MQB/MIBII/4.png)  
8. 激活软件加载「手动加载」并点击「开始加载」  
![Screenshot](../images/MQB/MIBII/5.png)  
9. 选择来源（SD 卡），全选并启动固件更新  
![Screenshot](../images/MQB/MIBII/6.png)  

!!! warning ""
    固件更新时应注意什么？

    保持点火开启。  
    关闭不需要的用电设备（灯光、通风……）  
    连接充电设备（充电电流不低于 15 A，最好 20 A 及以上）  
    视设备（RAM / CPU）不同，更新需要 20 到 60 分钟  

固件更新后面板上 glonass 会闪烁 —— 这是正常的，不要害怕。  

!!! warning ""
    固件更新后可能出现"安装更改确认"错误。需要用代码确认固件更新。  
    [说明与 XOR 计算器](../../xorCalculator)

### 激活 Telnet 连接

要建立 Telnet 连接，需要在绿色菜单中激活 Ethernet。  
为此，长按收音机上的 MENU 键，直到出现（服务）菜单。然后进入测试模式  
![Screenshot](../images/MQB/MIBII/7.png)  
  
现在我们可以切换到绿色（工程）菜单  
（也可以长按 MENU 键进入）  
![Screenshot](../images/MQB/MIBII/8.png)  
  
切换到「debuggung mlp」类别。  
![Screenshot](../images/MQB/MIBII/9.png)  
  
激活 Ethernet 并重启设备  
（按住电源键至少 10 秒）。  
![Screenshot](../images/MQB/MIBII/10.png)  
  
设备重启后，需要激活「Switch to MLP」。  
![Screenshot](../images/MQB/MIBII/11.png)

现在可以把 USB-LAN 适配器插入车上的 USB 口，并用 LAN 线连接到笔记本电脑。  
如果适配器上的 LED 亮起，说明连接和 IPv4 配置成功（Ethernet 适配器 IP – 192.168.1.10）。  
  
启动 Putty 程序。MU 的 IP 地址取自绿色菜单作为 IP。  
有时某些设备上不显示 MU 的 IP 地址，但始终使用 192.168.1.4、端口用 23，然后点击「Open」。  
  
如果一切设置正确，从 QNX Neutrino 登录提示就能看出它在工作。  

Delphi 单元登录 Login:root。无需密码。直接按回车……
![Screenshot](../images/MQB/MIBII/12.jpg)
  
出现欢迎信息后，就可以输入命令了。  
![Screenshot](../images/MQB/MIBII/13.jpg)

命令：  
```
cp – 复制  
rm – 删除  
chmod – 修改权限（例如 chmod 777= 完整读/写权限）  
mkdir – 创建目录（文件夹）  
mount – 挂载路径  
umount – 卸载挂载路径  
```

属性：  
```
-f – 强制（覆盖 / 强制）  
-R – 递归（例如包含内容的文件夹，复制 / 删除子文件夹）  
-t – 挂载请求 / 特定类型（例如后跟 qnx6）  
-u – 更新（重新挂载）  
-V – 进度指示  
-w – 读/写权限（挂载时）  
```

为方便起见，准备了 3 个脚本（运行它们需将其放到 U 盘根目录）  
1. 备份 [(MST2_backup.sh)](../firmwares/MST2_backup.sh)  
2. FEC 码补丁 [(MST2_fec.sh)](../firmwares/MST2_fec.sh)  
3. SWaP 补丁 [(MST2_patch.sh)](../firmwares/MST2_patch.sh)  
  
### MIBII 备份

将（空白）SD 卡插入卡槽 1，并通过 Putty 执行以下命令。 

1. 挂载 SD 卡
    ```
    cd / && mount -uw /sdc1/
    ```
2. 运行 Backup 脚本 [(MST2_backup.sh)](../firmwares/MST2_backup.sh)
    ```
    cd / && /sdc1/MST2_backup.sh
    ```
3. 应当看到：
    ```
    # MST2_backup.sh  
    ROOT access — OK  
    Making backup dir on SD Card — OK  
    mkdir: /sdc1/backup: File exists  
    SWaP *.fec files backup — OK  
    backup /ffs/etc/* — OK  
    cp: Can't create FIFO file (/sdc1/backup/script.fifo)  
    delphibin.ifs backup — OK  
    InstallationManager backup — OK  
    SWaP engine backup — OK  
    cp: Dest (/sdc1/mst2_patch.sh) must be a dir to copy dirs or multiple files to it.  
    profile backup — OK  
    MHConfig.cfg backup — OK  
    fs0 backup — OK  
    Saving unit info to file — OK  
    emmc serial numbler — SAVED  
    FINISHED — You can now remove SD Card  
    ```

### 更新 FEC 文件

执行备份后，U 盘的 pg 文件夹中会出现一个 *.fec 文件。  
用 MIB2 Delphi FEC Generator XTR3M3 [(M2DFGX16)](../firmwares/M2DFGX16.rar) 对该文件打补丁，  
即勾选你需要的所有项，并将打过补丁的 fec 文件另存。

!!! note "重要"
    如果你出厂时已激活 App Connect、MirrorLink 等，而在打 fec 文件补丁时未勾选它们，那么刷入车机后这些功能就会消失。  
    如果你的车机无导航，则勾选除导航外的所有项

??? tip "可用 FCC"
    fsc = "00030000" # AMI  
    fsc2 = "00030001" # Gracenote  
    fsc3 = "00040100" # Navigation  
    fsc4 = "00050000" # Bluetooth  
    fsc5 = "00060100" # Vehicle Data Interface  
    fsc6 = "00060200" # Škoda/Audi Connect, VW CarNet  
    fsc7 = "00060300" # Mirror Link  
    fsc8 = "00060400" # Sport HMI  
    fsc9 = "00060500" # Sport Chrono  
    fsc10 = "00060600" # LogBook  
    fsc11 = "00060700" # Online Services  
    fsc12 = "00060800" # Apple CarPlay  
    fsc13 = "00060900" # Google Android Auto  
    fsc14 = "00070100" # SDS  
    fsc15 = "00070200" # SDS for Nav  
    fsc16 = "00070400" # Digital Voice Enhancement  

### 激活 SWaP 码 

新的 SWAP 码生成器：https://mst2fecgen.mibsolution.one/

SWaP 文件。这些码包含车机所有现存的 SWaP 码  

| 类型    | 链接                                     |
|---------|------------------------------------------|
| STD2    | [(SWaP)](../../firmwares/SWAP/SWaP)      |
| PQ STD2 | [(SWaP)](../../firmwares/SWAP/STD2/SWaP) |
| NAV     | [(SWaP)](../../firmwares/SWAP/Nav/SWaP)  |
| PLUS    | [(SWaP)](../../firmwares/SWAP/Plus/SWaP) |

要加载 SWaP 码，需取所需文件以及上一步生成的 FEC 文件，放到 U 盘根目录。

将 SD 卡插入卡槽 1，并通过 Putty 执行以下命令：

1. 挂载 SD 卡  
    ```
    cd / && mount -uw /sdc1/
    ```
2. 运行脚本 [(MST2_patch.sh)](../firmwares/MST2_patch.sh)  
    ```
    cd / && /sdc1/MST2_patch.sh
    ```
3. 应当看到：  
    ```
    # mst2_patch.sh
    ROOT access — ok
    SWaP patch — ok
    cp: Copying /sdc1/SWaP to /home/mmc0t177_tmp/apps/bin/SWaP
    100.00% (xxx/xxx kbytes, xxxx kb/s)
    FINISHED — You can now remove SD Card
    ```
4. 有时脚本不执行并报错。此时需手动执行脚本中的步骤：  
    ```
    cd / && mount -uw /sdc1/
    umount -f /extbin
    mkdir /home/mmc0t177_tmp
    mount -t qnx6 /dev/mmc0t177 /home/mmc0t177_tmp
    cp -VRf /sdc1/SWaP /home/mmc0t177_tmp/apps/bin/
    chmod 777 /home/mmc0t177_tmp/apps/bin/SWaP
    umount -f /home/mmc0t177_tmp
    rm -R /home/mmc0t177_tmp
    ```
5. 长按电源键重启车机 —— 必须执行！！！！
6. 挂载 SD 卡  
    ```
    cd / && mount -uw /sdc1/
    ```
7. 运行 FEC 码补丁脚本 [(MST2_fec.sh)](../firmwares/MST2_fec.sh)  
    ```
    cd / && /sdc1/MST2_fec.sh
    ```
8. 应当看到：  
    ```
    # MST2_fec.sh
    ROOT access — ok
    *.FEC installation — ok
    mkdir: /home/mmc0t180_tmp: File exists
    FINISHED — You can now remove SD Card
    ```
9. 长按电源键重启车机 —— 必须执行！！！  

!!! note ""
    如果因某些原因没成功，说明该 SWaP 文件不适合你，请尝试其他 SWaP

!!! warning ""
    可能会出现 FEC 文件仍缓存在设备中、重启后仍然存在的情况。  
    可能需要多次删除，直到重启后它们在设备中不再可用。  
  
    rm -RVf /Persistence/SWaP/ppw/*  
    rm -RVf /Persistence/SWaP/illegal/*  
  
    之后即可导入修复后的 FEC 文件。  
  
    cp -VRf /sdc1/*.fec /Persistence/SWaP/pg/  
  
    输入命令后必须完整重启。

!!! warning 
    完成所有操作后，务必检查车机是否正常工作。  
    用扫描仪检查是否有错误，如出现则清除。

## ICC 电子语音放大器

要激活该放大器，需要加载参数集：  
[(ODIS 用参数集)](../parameters/5F_ICC_ONLY.xml.zip)

加载参数集后，必须长按电源键重启车机！
