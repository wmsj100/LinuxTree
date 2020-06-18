---
title: disk2vhd
date: 2020-06-18 10:17:49
modify: 
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# disk2vhd

## 概要

- disk2vhd是一个可以直接用来将当前系统备份为vhd的工具，只能在windows上使用。
- 如果是其他工具，需要先将当前系统制作为iso镜像，然后通过虚拟机来导入镜像，在用virtualbox或者vmware等工具把虚拟机镜像导出为vhd镜像格式，然后上传到公有云的obs，然后通过vhd来创建私有镜像，再利用该镜像来安装虚拟机。
- Clonezilla:再生龙，是用来克隆linux的，可以克隆ubuntu或者debine等系统。

## 参考

