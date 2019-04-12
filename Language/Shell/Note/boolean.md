---
title: 布尔值
date: 2019-04-12 14:55:43	
modify: 
tag: [boolean]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# 布尔值

## 概述
- `!` 取反
- `a` 且
- `o` 或

## 范例
```shell
#!/bin/bash
a=10
b=20

if [ $a != $b ];then
    echo "a is not eauql b"
fi

if [ $a -lt $b -a $b -gt 15 ];then
    echo "a little b and b greater then 15"
fi

if [ $a -gt $b -o $b -lt 30 ];then
    echo "a greater then b or b littel then 30"
fi
```

## 参考
- []()
