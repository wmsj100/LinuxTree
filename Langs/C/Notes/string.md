---
title: 字符串
date: 2019-04-15 20:24:40	
modify: 
tag: [string]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符串

## 概述
- 使用""表示字符串
- 字符串没有专门的关键字，只能使用数组或指针来间接的存储字符串
- `char str1[]` 或者 `char *str2`  \*
- *str: 这是指针，只能读取，不能写入，所以字符串的很多写入方法(strcat)不能使用 、*
- str[30]: 这是字符数组组成的字符串，可以写入，strcat等写入方法可以使用

## 方法
- strcat(str1, str2) 把str2连接到str1，str1必须长度足够，否则发生溢出
- strcpy(str1, str2) 把str2拷贝到str1
- strcmp(str1, str2) 比较字符串大小，str1>str2:1; str1<str2:-1; str1==str2: 0

## 参考
- []()
