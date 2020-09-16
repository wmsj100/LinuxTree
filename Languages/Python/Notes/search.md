---
title: search
date: 2020-09-16 10:14:16
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# search

## 概要

- search是re模块的方法，正则匹配

## 使用

```python
import re
a=""count='asdf'"
b=re.search("count='\w*'", a).group()
print(b)
```

## 参考

