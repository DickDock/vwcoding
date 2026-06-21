# 行驶与操控

### 转向机重新调校

!!! tip ""
     方向盘变得更有路感。  
     如果设为 "Direct" 配置 —— 从极低速起方向盘就很沉。  
     如果设为 "Incremental" 配置 —— 方向盘随车速升高逐渐变沉。

``` yaml title="登录密码: 19249"
单元 44 (转向助力) → 编码:
选择活动驾驶模式: 激活
→ 应用
	
单元 44 (转向助力) → 适配:
转向助力特性: "Dynamik"
驾驶模式切换: "Incremental"
→ 应用
```

### 关闭挂车稳定

=== "在 ODIS 中编码"
    ``` yaml
    单元 03 → 编码:  
    - Trailer Stabilization: 停用
    → 应用（需重启单元）
    ```

=== "在 VCDS 中编码" 
    ``` yaml
    单元 03 — ABS → 适配:  
    - 适配通道 № 56: 1 – 开启, 0 – 关闭  
    退出 → 保存  
    ```
    
  
### 用 Autohold 平顺起步

!!! tip ""
    有时在开启 AutoHold 起步时会感到轻微顿挫。效果明显，现在车辆起步非常平顺。

=== "在 ODIS 中编码"
    ``` yaml title="登录密码: 20103"
    单元 3-ABS/ESP → 适配:
    Drive_away_assist_control (Anpassung des Dynamischen Anfahrassistenten): 提前 (Früh)
    Hill_hold_assist_control (Dynamischer Anfahrassistent): 提前 (Früh)
    → 应用
    ```

=== "在 OBD11 中编码" 
    ``` yaml title="登录密码: 20103"
    单元 03 制动系统电子模块 → 适配:
    动态起步辅助: 提前
    坡道起步辅助: 提前
    ```
  
### 油门踏板响应时间
``` yaml title="登录密码: 27971 或 19249"
单元 44 → 适配:
驾驶模式切换 (Switching Driving Profile): 直接，按阈值控制
→ 应用
```

### DSG-7 适配

1. 预热发动机和变速箱 —— 约一小时行驶  
2. 发动机熄火，点火开启
    ``` yaml
    单元 02 → 变速箱电子模块 → 基本设置:
    启动双离合器快速适配 
    等待完成提示 
    ```
3. 关闭点火  
4. 启动发动机 —— 拉手刹（不踩刹车）  
5. 挂入 P 挡
    ``` yaml
    单元 02 → 变速箱电子模块 → 基本设置:
    变速箱基本设置 
    等待完成提示，会听到变速箱令人不安的摩擦声和顿挫
    ```
