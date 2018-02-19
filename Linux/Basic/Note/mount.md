---
title: mount
date: Sun 18 Feb 2018 10:55:44 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 设备自动挂载是在文件'/etc/fstab' 文件中设置
- mount -l 查看所有已经挂载的设备
- dumpe2fs /dev/sda8  查看当前设备的文件系统信息
- tune2fs -l /dev/sda8  查看设备的文件系统详情 等效于 dumpe2fs
- mount -a 自动加载 ‘/dev/fstab' 文件中写入的设备
