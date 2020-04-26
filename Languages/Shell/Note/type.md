---
title: type
date: 2020-04-26 15:10:17
modify: 
tags: [Note]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# type

## 概要

- 通过用于判断类型

## 范例

```shell
if [ $(type -t $funcName) = "function" ];then
	echo "$funcName has defined and is function"
	return 0
else
	return 1
fi
```

## 参考

