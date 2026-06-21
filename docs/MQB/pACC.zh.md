
# 激活 ACC 与 pACC (SWaP)

!!! warning ""
    所有操作你自行承担风险！我们不对损坏的设备负责。  
    刷写需要 ODIS Engineering 12 版。更早的版本刷写时可能报错 —— "未识别变体"。  

SWaP – 一段基于车辆 VIN 码、所应用 SWaP 的车辆单元的专属个性化识别码 VCRN (Vehicle Component Registration Number)，以及功能清单 FEC (Function Enabling Codes) 或 FSC (FreiSchaltungsCode) 的码。  
SWaP 由私钥签名 (RSA1024)。  

pACC (Predictive ACC) —— 一种自适应巡航控制，可借助地图数据（预测数据 PSD）和识别到的交通标志自动设定车速。  

含 SWaP 生成器、固件和参数集的压缩包：
[下载（2022.02.02 版本）:material-download:](../firmwares/accGenerator.zip){ .md-button .md-button--primary }

=== "适用于 2Q0/3QF/5Q0/5QF radar 的功能 FEC 码"
    10009001	MRR-Paket 1: ACClow (Basis-ACC) + FrontAssist inkl. CityANB  
    10009002	MRR-Paket 2: ACClow (ACC FTS) + FrontAssist inkl. CityANB  
    10009003	MRR-Paket 3: ACClow (ACC S&G) + FrontAssist inkl. CityANB  
    10009004	MRR-Paket 4: FrontAssist inkl. CityANB (без ACC)  
    10009005	MRR-Paket 5: CityANB (без ACC)  
    10009006	MRR-Paket 6: ACChigh (Basis-ACC) + FrontAssist inkl. CityANB  
    10009007	MRR-Paket 7: ACChigh (ACC FTS) + FrontAssist inkl. CityANB  
    10009008	MRR-Paket 8: ACChigh (ACC S&G) + FrontAssist inkl. CityANB  
    10009101	ACC-Funktionserweiterungs-Paket "predictiveACC"  
    10009102	ACC-Funktionserweiterungs-Paket "StauAssistent" (拥堵辅助)  
    10009103	ACC-Funktionserweiterungs-Paket "predictiveACC & StauAssistent"  
    10009201	AWV-Auspraegung "AWV1,2 – Warnung nur visuell & auditiv" (仅视觉与听觉预警)  
    10009202	AWV-Auspraegung "AWV1,2"  
    10009203	AWV-Auspraegung "AWV1,2,3"  
    10009204	AWV-Auspraegung "AWV1,2,3, vFGS  
    10009205	AWV-Auspraegung "AWV1,2,3, vFGS, vRFS“  
    10009300	AWV-Funktionserweiterungs-Paket "Elektronische Parkbremse"  
    10009301	AWV-Funktionserweiterungs-Paket "EmergencyAssist"  
    10009302	AWV-Funktionserweiterungs-Paket "Abbiegeassistent"  
    10009303	AWV-Funktionserweiterungs-Paket "AWV-Gegenverkehr"  
    10009304	AWV-Funktionserweiterungs-Paket "Abbiegeassistent & AWV-Gegenverkehr"  
    10009305	AWV-Funktionserweiterungs-Paket "EmergencyAssist & AWV-Gegenverkehr"  
    10009306	AWV-Funktionserweiterungs-Paket "EmergencyAssist & Abbiegeassistent"  
    10009307	AWV-Funktionserweiterungs-Paket "EmergencyAssist & Abbiegeassistent & AWV-Gegenverkehr"  
    10009500	Verkehrszeichenerkennung (VZE)  
    10009600	Vorrausschauender Fussgaengerschutz (VFS) - FCWP  
  
    FGS = Fußgängerschutz (Pedestrian Protection)  
    RFS = Radfahrer-Schutz (Bicycle Protection)  

=== "适用于 3Q0 radar 的功能 FEC 码"
    10003100	MRR-Paket 1: ACClow (Basis-ACC) + FrontAssist inkl. CityANB  
    10003200	MRR-Paket 2: ACClow (ACC FTS) + FrontAssist inkl. CityANB  
    10003300	MRR-Paket 3: ACClow (ACC S&G) + FrontAssist inkl. CityANB  
    10003400	MRR-Paket 4: FrontAssist inkl. CityANB (ohne ACC)  
    10003500	MRR-Paket 5: CityANB (ohne ACC)  
    10003600	MRR-Paket 6: ACChigh (Basis-ACC) + FrontAssist inkl. CityANB  
    10003700	MRR-Paket 7: ACChigh (ACC FTS) + FrontAssist inkl. CityANB  
    10003800	MRR-Paket 8: ACChigh (ACC S&G) + FrontAssist inkl. CityANB  
    10003900	MRR-Paket 9: ACChigh konservativ (Basis-ACC) + FrontAssist inkl. CityANB  
    10003A00	MRR-Paket 10: ACChigh konservativ (ACC FTS) + FrontAssist inkl. CityANB  
    10003B00	MRR-Paket 11: ACChigh konservativ (ACC S&G) + FrontAssist inkl. CityANB  
    10004000	zFAS AreaView3  
    10004100	zFAS Bildverarbeitung AV3/IPA  
    10004200	zFAS Anhaenger-Rangier-Assistent  
    10004300	zFAS Aktionsgenerierung Warnen  
    10004600	zFAS AWC Ladeplattenerkennung  
    10005000	Personalisierung  
    10006100	ACC-Funktionserweiterungs-Paket "predictiveACC"  
    10006200	ACC-Funktionserweiterungs-Paket "StauAssistent"  
    10006300	ACC-Funktionserweiterungs-Paket "predictiveACC&StauAssistent"  
    10007100	AWV-Auspraegung "AWV1,2 – Warnung nur visuell&auditiv"  
    10007200	AWV-Auspraegung "AWV1,2"  
    10007300	AWV-Auspraegung "AWV1,2,3"  
    10007400	AWV-Auspraegung "AWV1,2,3, vFGS  
    10008100	AWV-Funktionserweiterungs-Paket "EmergencyAssist"  
    10008200	AWV-Funktionserweiterungs-Paket "Abbiegeassistent"  
    10008300	AWV-Funktionserweiterungs-Paket "AWV-Gegenverkehr"  
    10008400	AWV-Funktionserweiterungs-Paket "Abbiegeassistent&AWV-Gegenverkehr"  
    10008500	AWV-Funktionserweiterungs-Paket "EmergencyAssist&AWV-Gegenverkehr"  
    10008600	AWV-Funktionserweiterungs-Paket "EmergencyAssist&Abbiegeassistent"  
    10008700	AWV-Funktionserweiterungs-Paket "EmergencyAssist&Abbiegeassistent&AWV-Gegenverkehr"  

### 以 5Q0 radar 为例的参数集结构

![Screenshot](../images/MQB/swap_info.jpeg)  

### radar 与固件对应关系  

| 硬件 ID |     固件 X     |            固件 | 参数集<br/>(ODIS XML)                              |
|----------------:|:------------------:|--------------------:|:-------------------------------------------------------|
|       2Q0907572 | FL_2Q0907572T_X383 | FL_2Q0907572AB_0397 | ARBEITS_DATEI_DSDL2.xml（有 VW 和 Škoda 变体） |
|   3QF_5QF907572 | FL_5Q0907572M_X720 |  FL_5Q0907572S_0780 | 13_5Q0907572R_EU_RDW.xml                               |
|       3Q0907572 | FL_3Q0907572A_X180 |  FL_3Q0907572C_0196 | DA_013_7200_3H0_V002_VW483A2RDW.xml                    |
|       5Q0907572 | FL_5Q0907572E_X312 |  FL_5Q0907572K_0402 | 13_5Q0907572K.xml                                      |

要激活自适应巡航，首先需要了解所装 radar 的当前版本：  
```
系统标识: ACCCONTIMQB  
软件版本: 0372  
硬件版本: H01  
VW/Audi 零件号: 2Q0907572R  
硬件零件号: 2Q0907572B  
```

### 在不更改 SWaP 码的情况下更换 radar 固件

1. 备份当前的编码和适配  

2. 对于 2Q0 radar，需先安装固件 FL_2Q0907572T_0383_BOOTLOADER_V001_S  

3. 按表格安装普通固件（非 X）  

4. 按表格刷入所需参数集  

5. 恢复编码和适配  

### 刷写与生成 SWaP 码

1. 首先应检查公钥是否与所需值不同。  
可在 13 单元的测量值中查看：
    ```
    для 2Q0.. - A6 2C 69 ...  
    для 5Q0/3QF.. - 9C 47 73...  
    для 3Q0.. - D2 C3 3E...  
    для 5Q0.. - "8F 51 4A...  
    ```
    **如果公钥与列表中某一项一致，可放心跳到第 5 步！**  
  
2. 用 ODIS Service 在线账号强制在 radar 上激活组件保护。  
   需要开始解除组件保护的流程（在保护已解除的状态下），并在过程中断开 VAS5054A。若运气好，现有的配对码会被擦除，而新码还来得及刷入单元，单元重启后会进入 CP。若不成功，再重复一次。  

3. 安装 X 固件，例如 FL_2Q0907572AA_X390___S.odx  
    ```
    对于 2Q0 radar —— 如果版本低于 0380，则需先安装固件 FL_2Q0907572T_0383_BOOTLOADER_V001_S，然后再安装 FL_2Q0907572AA_X390___S.odx  
    ```

4. 解除组件保护
解除保护后需确认公钥已变为所需值。  
可在 13 单元的测量值中查看。
    ```
    для 2Q0.. - A6 2C 69 ...  
    для 5Q0/3QF.. - 9C 47 73...  
    для 3Q0.. - D2 C3 3E...  
    для 5Q0.. - "8F 51 4A...  
    ```
    如一切正常，进入 SWaP 生成  
5. 生成 SWaP 码需要 VCRN (Vehicle Component Registration Number)。  
该码可从 13 单元的测量值中提取：
    ``` yaml
    单元 003 — 测量值 → 个性化识别码 (VCRN) 
    ``` 
  
6. 选择所需 FEC 码  
最多 4 个。取决于 radar 本身支持哪些 swap。  
    ``` yaml
    单元 003 — 测量值 → 所有 SWaP 功能列表
    ```
    ![Screenshot](../images/MQB/swap_avail.jpeg)  
例如，radar 3qf907561d 支持：10009000 10009100 10009200 10009300  
    ```
    10009008 — ACC High 210 & stop and go & fts  
    10009204 — front assist  
    10009101 — pre acc  
    10009307 (doesn't work for 3QF Bosch sensors
    ```

7. 用 afcg.exe 工具生成 SWaP 码。生成需输入：VIN、VCRN（第 5 步获取）以及用空格分隔的 FEC 码集  

8. 生成的 SWaP 码需输入到 13 单元的适配中（传输 SWaP 功能解锁码）：  
    ``` yaml
    单元 009 — 诊断会话 → 下线模式 (EOL)  
    单元 008 — 访问权限 → 码 20103  
    单元 007 — 适配 – 传输 SWaP 功能解锁码 → 在「数据输入」字段输入生成的码  
    单元 005 — 基本设置 UDS → 解锁 SWaP 功能  
    单元 003 — 测量值 → 所有 SWaP 功能的状态
    ```
    可在测量值中检查是否一切正确 (003 测量值 → 所有 SWaP 功能的状态)。  
    如一切正常，你会看到你的 FEC 码清单，每个都标注 available、valid、condition met（可用、有效、条件满足）。  

9. 按表格安装普通固件（非 X）  

10. 按表格刷入所需参数集  

11. 恢复编码和适配，或从零设置（见下）  
  
### 为首次激活 ACC 进行编码和适配

**发动机电子模块设置**  
``` yaml
单元 01 → 编码:
字节 5 – 位 6: 激活
→ 应用（需重启单元）
```
**制动系统设置**  
``` yaml
单元 03 → 编码:
字节 24 – 位 3: 激活
→ 应用（需重启单元）
```

**保存所选 FEC 码的编号**  
需在 FSID 组中按顺序填入所选 FEC 码的末位数字 (1 — 90, 2 — 91, 3 — 92, 4 — 93)  
例如，所选 FEC 码：10009008, 10009101, 10009204, 10009307  
``` yaml
单元 13 → 编码:
SWaP_FSID_group_1: 8
SWaP_FSID_group_2: 1
SWaP_FSID_group_3: 4
SWaP_FSID_group_4: 7
→ 应用（需重启单元）
```
**自适应巡航单元设置** 
``` yaml
单元 13 → 编码:
Front_camera: installed – 若有辅助摄像头
Control_module_for_lane_assistant: installed
Initialization_concept_front_assist:
- Initialization_1 — AID 左上角大号的 Front Assist 就绪等待图标，Front Assist 仅在开始行驶后激活，此为出厂值; 
- Initialization_2 — 小号的 Front Assist 就绪等待图标，位于之后 ACC 图标出现处，Front Assist 在点火后几秒激活并立即识别车前障碍。
Automatic_driveaway_by_pretrigger: 激活  
Automatic_driveaway_after_short_stop: 激活  
Driveaway_by_triggerleaver: 激活  
Pretriggertime_reduction: deactivated（将停车等待时间延长到 10 秒）  
FPK_functions: installed（若有 Drive Mode 按键）
Overtaking_right_prevention: deactivated（右侧超车）
Drive_pmode_selection: MMI_menu_ACC（在车机辅助菜单中选择工作模式） 
→ 应用（需重启单元）
```
``` yaml title="登录密码: 20103"
单元 13 → 适配:
Distance_Setting:
- par_Distance_Setting: on
Adjustment_mode_time_slot_adaptive_distance_control:
- Adjustment_mode_time_slot_adaptive_distance_control: on
→ 应用
```

**仪表盘设置** 
``` yaml
单元 17 → 编码:
adaptive_cruise_control: yes
→ 应用（需重启单元）
```
**网关设置（用于 VW）** 
``` yaml
单元 19 → 编码:
FPA_Funktion_ACC: 激活
→ 应用（需重启单元）
```
``` yaml
单元 19 → 适配:
Multi_function_steering_wheel_control_module Coding Value:
- variant: ACC-High
→ 应用
```

**转向机设置（用于 Škoda）**  
``` yaml
单元 16 (转向柱电子模块) → 编码:
Switch_for_cruise_control_integrated_in_turn_signal_switch: not installed
Switch_for_cruise_control: installed
Adaptive_cruise_control: installed
→ 应用（需重启单元）
```

**车机设置** 
``` yaml title="登录密码: 20103"
单元 5F → 适配:
Car_Function_Adaptations_Gen2 – menu_display_ACC: 激活
Car_Function_Adaptations_Gen2 – menu_display_ACC_over_threshold_high: 激活
Car_Function_List_BAP_Gen2 – ACC_0x05: 激活
→ 应用
```

**泊车辅助设置** 
``` yaml
单元 76 → 编码:
Adaptive_cruise_control: 激活
→ 应用（需重启单元）
```

### 为激活 pACC 进行编码和适配

![Screenshot](../images/MQB/pacc.png)  

``` yaml
单元 13 → 编码:
Traffic_sign_detection: 激活
Speed_limit_assistent: 激活
Curve_assistent: 激活
Kurvenassistent_CarMenu: 激活
→ 应用（需重启单元）
```
``` yaml title="登录密码: 20103"
单元 13 → 适配:
Predictive speed limit control:
- par_Predictive_speed_limit_control: 激活
→ 应用
```

### 5Q radar 版本的附加编码

``` yaml title="登录密码: 20103"
单元 13 → 编码:
zul_Regelabweichung_CarMenu — large
pACC_Regulation_on_priority: 激活
pACC_Reaction_to_end_of_traffic_jam: with speed adaptation
pACC_Learning_drivers_offset: 激活
pACC_Reaction_to_narrow_places: dynamic and static
→ 应用（需重启单元）
```
