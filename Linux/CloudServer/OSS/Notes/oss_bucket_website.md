---
title: oss静态网站
date: 2020-02-21 22:45:40
modify: 
tags: [Notes]
categories: OSS
author: wmsj100
email: wmsj100@hotmail.com
---

# oss静态网站

## 概要

- bucket可以设置成网站托管，其实设置网站托管之后就和github的静态网站托管类似
- 而且网速要比github给力很多，
- 有多少个bucket就可以托管多少个静态网站。不知道流量是怎么算的。

## 配置

```python
import oss2
from oss2.models import BucketWebsite

bucket.put_bucket_website(BucketWebsite('index.html', 'error.html'))
```

- 上面就把一个bucket设置成静态网站托管了，
- `b.bucket.delete_bucket_website()` 删除静态网页设置

## 参考

- [oss 静态bucket](https://help.aliyun.com/document_detail/32034.html?spm=a2c4g.11186623.6.844.6c722c0398fe8K)
