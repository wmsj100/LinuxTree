---
title: 内存数据
date: 2019-04-13 10:39:56	
modify: 
tag: [basic,Linux,system,内存]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 内存数据

## 概述
- 数据由多种多样，但他们在内存中都是一样的，都是二进制存储
- 内存条是非常精密的部件，内部由上亿个电子元器件，很小，达到了纳米级别
- 这些元器件实际上就是电路，
- 电路的电压会变化，要么是0V，要么是5V，只有这俩种电压，
- 5V表示通电，用1来表示
- 0V表示断电，用0来表示
- 所以一个元器件由2种状态，1或0
- 通过电路来控制这些元器件，可以得到很多0/1组合

## 字节
- 一个元器件称为1比特(Bit)或1位，
- 8个元器件组成的组称为1字节(Byte)，16个元器件就是2字节。
- 1KB 表示1024Byte 表示由8*1024个元器件组成\*

## 单位换算
- 1Byte = 8Bit
- 1KB = 1024Byte = 2^10Byte
- 1MB = 1024KB = 2^20Byte
- 1GB = 1024MB = 2^30Byte
- 1TB = 1024GB = 2^40Byte
- 1PB = 1024TB = 2^50Byte
- 1EB = 1024PB = 2^60Byte

## 参考
- [内存数据](http://c.biancheng.net/cpp/html/3413.html)