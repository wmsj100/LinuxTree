---
title: df
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---
# df

- 检查linux服务器的文件系统的磁盘使用情况。

## 参数
- a 全部文件系统列表
- h 方便阅读方式
- i 显示inode信息
- T 文件系统类型
- t 只显示选定文件系统的磁盘信息
- x 不显示选定文件系统的磁盘信息

## 实例
- df -h 以方便阅读的形式显示文件系统磁盘信息
- df -i 以inode模式显示磁盘使用情况
- df -T 显示磁盘的文件系统类型
- df -t ext4 只显示ext4类型的文件系统
- df -x ext4 不显示ext4类型的文件系统
