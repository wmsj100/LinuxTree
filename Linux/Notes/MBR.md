---
title: MBR
date: 2020-03-15 11:12:49
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# MBR

## 概要

- MBR: Master Boot Record
- 是存储设备最开始的512字节,包含操作系统启动加载器和分区表,再BIOS系统的启动流程中扮演重要角色.
- MBR并不位于某个分区中,而是分区前,设备的最开始部分.
- 无分区设备的启动扇区或分区中的启动扇区被称为Volumn boot record
- MBR前面的446字节是启动代码区域,在BIOS系统中通常包含启动加载器的第一部分.

## 分区类型

- 目前只有三种分区类型
	- 主分区
	- 扩展分区
		- 逻辑分区
- 主分区: 每个磁盘或RAID卷上只能有4个,可设置启动状态.
- 扩展分区: 如果分区方案要求使用4个以上的分区,就需要将至少一个分区设置为扩展分区,并在上面创建逻辑分区
	- 扩展分区可以被看作是容纳逻辑分区的容器
	- 硬盘上最多有一个扩展分区.
	- 如果磁盘上有一个扩展分区,它也被看作是一个主分区.因此只能另外再建立3个主分区
	- 扩展分区内所包含的逻辑分区数量没有限制.

## GUID分区表

- GPT方案中只有一种分区类型,主分区,磁盘和RAID卷中包含的分区数量没有限制.
- GPT: GUID Partition Table
- UEFI: Unified Extensible Firmware Interface 是EFI的标准组织
- UEFI指定了GPT的分区规范,使用globally unique identifiers(GUIDs)或linux中的UUID定义分区和分区类型,设计上是为了替换MBR
- GUID分区表的磁盘开始位置有一个PMBR(protective Master Boot Record),用以处理不支持GPT软件的访问,这段MBR和真正的MBR一样,可以用以支持BIOS/GPT启动的启动管理器.

## 参考

- [启动流程](https://wiki.archlinux.org/index.php/Partitioning_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
