---
title: 查看树莓派主板温度
date: 2019-05-11 19:52:39 Saturday
modify:
tag: [basic]
categories: RaspberryPi
author: wmsj100
mail: wmsj100@hotmail.com
---

# 查看树莓派主板温度

## 概述
- 如何查看树莓派主板温度，其实热源就是CPU，主板的温度都是被CPU加热的

## 用法
- `cat /sys/class/thermal/thermal_zone0/temp` `#>>> 62838` 通过这文件可以获取CPU的温度，需要除1000
- `vcgencmd measure_temp` #temp=41.9'C 通过这个命令可以获取cpu转换为°的温度

## 参考
- [查看树莓派温度](https://www.jianshu.com/p/b0384b667bf0)
- [查看树莓派温度](https://blog.csdn.net/wongnoubo/article/details/79770710)

