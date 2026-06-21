# 支持与项目发展

## 支持项目

如果你喜欢这个项目并愿意支持它持续发展，
可以通过 Yandex 转账（卢布）或比特币进行捐助：

<div class="grid cards" markdown>

-   :fontawesome-solid-money-bill:{ .lg .middle } __从俄罗斯银行卡转账__

    ---
    通过银行卡或 Yandex 钱包以卢布转账  

    [支持 :fontawesome-solid-paper-plane:](https://yoomoney.ru/to/4100110582992748/100){ .md-button }

-   :fontawesome-brands-btc:{ .lg .middle } __加密货币__

    ---
    ![BTC wallet](./images/btc.png){ width="100" align=left }  
  
    转账到 BTC 钱包：`1BKR5d91YUic3aqwc6nTGTMLkGBBrZkkcj`

</div>

## 添加新材料

### 站点结构

图片存放路径：`/docs/images`  
固件路径：`/docs/firmwares`  
参数集路径：`/docs/parameters`  

### 添加新的编码

本站使用 Markdown 标记语言构建。  

页面模板：

```
    # 页面标题
    ### 编码/适配名称

    !!! tip ""
        说明/目的（如有）

    !!! warning ""
        某些警告（如有）

    ``` yaml title="登录密码: XXXXX（如有）"
    单元 XX → 适配/编码:
    字节 XX – 位 X (位名称): 激活
    分区名称:
    - 适配名称: 激活
    → 应用
    ```

    ??? note "折叠列表名称"
        这里是默认在站点上折叠显示的信息
```

向站点页面插入图片的示例：  
```
![Screenshot](../images/MQB/odis-e-tires.png)```

向站点页面插入文件的示例：  
```
[(Škoda 用固件)](../firmwares/TMC-zz.rar)```

### 双语内容

本站支持俄语和英语。每个页面以两个文件存在：

- `page.md` —— 俄语版本（默认语言）
- `page.en.md` —— 英语版本

**在添加或修改编码与适配时，必须同时改动这两个文件**，并提交一个 pull request。

1. 在 `/docs` 中找到对应页面，例如 `docs/MQB/drive.md`。
2. 在俄语版本中做出修改。
3. 在 `docs/MQB/drive.en.md` 中做出等效修改。
4. 如果是新建页面 —— 添加两个文件，并在 `mkdocs.yml` 的 `nav` 中加入条目。
5. 对于新的菜单项，在 `nav_translations`（`locale: en` 段）中添加翻译。
6. 检查构建：`mkdocs build`。
7. 创建 pull request。

更多内容 —— 见 [README.md](https://github.com/Kanaduchi/vwcoding/blob/master/README.md) 与 [CONTRIBUTING.md](https://github.com/Kanaduchi/vwcoding/blob/master/CONTRIBUTING.md)。
