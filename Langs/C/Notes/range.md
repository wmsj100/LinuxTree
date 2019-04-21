---
title: 获取随机数
date: 2019-04-21 10:58:44	
modify: 
tag: [range,c,basic,func]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 获取随机数

## 概述
- range在标准库`<stdlib.h>`中，需要引入这个库
- range() 返回一个随机数，这个随机数是按照某个公式计算出来的，
- range产生的随机数是伪随机，这个数是种子
- 在系统启动之后这个种子就是一个定值
- srand(): 可以进行播种，重新生成种子
- srand((unsigned)time(NULL)) 使用time进行播种，这样每次再执行就会都是随机数，这个随机数是逐渐变大的，因为时间是再变大。

## 范围随机
- range()%13+10 13~22之间的随机数

## 参考
- [range](http://c.biancheng.net/cpp/html/2758.html)
