---
title: cpio
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- cpio 也是备份命令，可以备份任何东西，包括设备文件，这个命令不会主动去找文件，需要配合find等命令通过管道或重定向来实现。
- find /etc | cpio -cuBo > etc.bak
    - o 将数据输出到文件或设备上
    - B 让默认的block增加到5120，可以让处理大文件速度加快
- cpio -idvc < etc.bak 还原数据
    - i 将数据自文件或设备复制到系统中
    - d 自动新建目录
    - u 自动将较新的文件覆盖较旧的文件
    - v 在屏幕上显示存储的过程
    - c 一种较新的存储方式
