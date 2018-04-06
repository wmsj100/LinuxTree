---
title: linux文件系统 ext3,ext4,xfs
date: Sat 17 Feb 2018 05:47:43 PM CST
tag: [linux,file]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

文件系统EXT3，EXT4和XFS的区别：
1. EXT3
（1）最多只能支持32TB的文件系统和2TB的文件，实际只能容纳2TB的文件系统和16GB的文件
（2）Ext3目前只支持32000个子目录
（3）Ext3文件系统使用32位空间记录块数量和i-节点数量
（4）当数据写入到Ext3文件系统中时，Ext3的数据块分配器每次只能分配一个4KB的块
2. EXT4
EXT4是Linux系统下的日志文件系统，是EXT3文件系统的后继版本。
（1）Ext4的文件系统容量达到1EB，而文件容量则达到16TB
（2）理论上支持无限数量的子目录
（3）Ext4文件系统使用64位空间记录块数量和i-节点数量
（4）Ext4的多块分配器支持一次调用分配多个数据块
3. XFS
（1）根据所记录的日志在很短的时间内迅速恢复磁盘文件内容
（2）采用优化算法，日志记录对整体文件操作影响非常小
（3） 是一个全64-bit的文件系统，它可以支持上百万T字节的存储空间
（4）能以接近裸设备I/O的性能存储数据