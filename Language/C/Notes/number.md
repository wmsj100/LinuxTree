---
title: 数值
date: 2019-04-13 16:31:31	
modify: 
tag: [int,lint,float]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数值

## 概述
- int: 占用4个字节，即4*8=32位Byte，即2^32-1~~43亿 \*
- short: 占用2个字节，short可以节省内存
- long: 占用8个字节

## 占位
- 只有short的占位是确定的，至少占用2个字节，int/long和机器的字长有关系
- 16位环境下： short: 2Bit，int: 2Bit, long: 4Bit
- 32位环境： short: 2Bit, int: 4Bit, long: 4Bit
- 64位环境： short: 2Bit, int: 4Bit, long: 8Bit

## 进制
- 0b/0B 二进制
- 0	八进制
- 0x/0X 十六进制

## 符号位
- 数值是由正负区分的，默认是拿最高位来区分的，0表示正数，1表示负数
- 比如int类型的是32位，从0位到30位是数值位，31位为符号位，
- `unsigned` 通过这个关键字可以取消符号位，所有位数都可以用来存储数值，这个只能存储正数。

## 参考
- [进制](http://c.biancheng.net/cpp/html/3421.html)
