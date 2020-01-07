---
title: date
date: 2019-05-09 19:53:20	
modify: 
tag: [time]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# date

## 概述
- 查看系统时间

## 用法
- `%Y` 打印年份 (2019)
- `%m` 打印月份
- `%d` 打印日
- `%H` 打印小时(00-24)
- `%l` 打印小时(0-12)/小写L
- `%M` 打印分钟
- `%S` 打印秒
- `%w` 打印周数值 (0-6)
- `%a` 打印星期缩写
- `%A` 打印星期完整名称
- `%X` 以本地惯用方法打印时间 (19:57:35)

## 范例
- date +"%Y-%m-%d" #2019-05-09
- date +"%H:%M:%S %A" #19:52:24 Thursday
- date +"%Y-%m-%d %X" #2019-05-09 20:03:52
- date +"%Y-%m-%d %H:%M:%S" #2019-05-09 20:04:27

## 参考
- [linux date](https://www.cnblogs.com/asxe/p/9317811.html)
