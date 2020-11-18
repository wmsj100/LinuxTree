---
title: progress
date: 2020-11-18 17:34:13
modify: 
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# progress

## 概要

- progress是一个进度条库

## 使用

```python
from progress.bar import Bar
bar = Bar('progressing', max=10)
for i in range(10):
	bar.next()
	pass
Setting up   |================================| 100%
```

## 参考

