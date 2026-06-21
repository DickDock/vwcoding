---
hide:
  - toc
---
# 参数集编辑器

本参数集编辑器用于编辑或查看参数集文件。  

编辑器功能：  
- 查看参数集文件  
- 编辑、添加新的参数分区  
- 解码 base64 数据集  
- 将 base64 数据集转换为参数分区（简化文件）  
- 计算校验和（针对已解码的值）  
- 以简化格式保存文件  
- 识别 little-endian 字节序  

??? note "简化加密参数集的实验性功能"
    1 – 解码 `<COMPRESSED_DATA>` 对象的 base64。解码后的值包含一组以 `<SW-CNT>` 结构表示的参数  
    2 – 对每个 `<SW-CNT>` 结构中 `<DATEN>` 字段的值，截去前 8 字节（版本）和后 8 字节（CRC-32 哈希）
    3 – 将其保存到对应的 `<PARAMETER_DATA>` 并计算 CRC-16 哈希  

--8<-- "overrides/pages/datasets.zh.html"
