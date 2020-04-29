---
title: cpio
date: Mon 19 Feb 2018 09:29:02 AM CST
modify: 2020-04-29 14:31:04 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# cpio

## 概述

- cpio指令可以将文件复制到存档包(archives)，也可以从存档包(archives)复制出文件。
- 缺省情况下，cpio从标准输入读取输入数据，向标准输出写入输出数据。
- 归档包(archives)是一种包含其他文件和有关信息的文件。有关信息包括
	- 文件名
	- 属主
	- 时间戳
	- 访问权限
- cpio支持下列的归档格式
	- binary
	- old ASCII
	- new ASCII
	- HPUX binary
	- HPUX old ASCII
	- old tar
	- POSIX.1.tar
- 默认情况下，cpio创建二进制格式存档，以便与旧的cpio程序兼容。
- 从档案中提取时，cpio会自动识别正在读取的归档类型，并可以读取在具有不同字节顺序的计算机上创建的归档。
- cpio 也是备份命令，可以备份任何东西，包括设备文件，这个命令不会主动去找文件，需要配合find等命令通过管道或重定向来实现。
- 使用cpio打包的文件格式是cpio，通过file可以查看到，本来计划用它来修改和重新打包rpm包，发现不行，无法识别

## 参数

- m 创建文件时保留以前的文件修改时间

## 使用

- find /etc | cpio -cuBo > etc.bak
    - o 将数据输出到文件或设备上
    - B 让默认的block增加到5120，可以让处理大文件速度加快
- cpio -idvc < etc.bak 还原数据
    - i 将数据自文件或设备复制到系统中
    - d 自动新建目录
    - u 自动将较新的文件覆盖较旧的文件
    - v 在屏幕上显示存储的过程
    - c 一种较新的存储方式
