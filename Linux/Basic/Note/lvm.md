---
title: lvm逻辑卷
date: Mon 26 Feb 2018 10:30:51 PM CST
tag: [linux,sys]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 逻辑卷

## lvm逻辑卷管理
- 就是使用逻辑卷组管理（logic volume manager）创建出来的设备
- lvm介于硬盘裸设备和文件系统的中间层

## 基本概念
### PV(Physical Volume) 物理卷
- 物理磁盘分区，如果想要通过LVM管理这个物理卷，可使用fdisk工具将其ID改为8e

### VG(Volume Group) 卷组
- 是物理卷的集合

### LV(Logic Volume) 逻辑卷
- PV（物理卷）中划分出来的一块逻辑磁盘

---

- 首先创建一个或多个物理卷，物理卷按照相同的组名聚集形成一个物理卷组，而逻辑卷就是从物理卷组中抽象出来的一块磁盘空间

## 逻辑卷制作过程
- pvcreate 创建物理卷（PV ）
- pvscan 简单查看物理卷信息
- pvdisplay 查看物理卷的详细信息

### 範例
- 创建多个可用分区，修改分区id为8e
- pvcreate /dev/sda8 
- pvcreate /dev/sda9 
- pvcreate /dev/sda10 
- pvdisplay 查看pv的详细信息

## 物理卷组（VG）制作过程
- 有了物理卷就可以制作物理卷组了
- vgcreate vgname /dev/sda8 /dev/sda9 /dev/sda10 创建物理卷组 组名为vgname，使用的卷为/sda8-10 
- vgscan 简单查看物理卷组信息
- vgdisplay 查看物理卷组的详细信息
- vgextend first_vg /dev/sda11 通过这个命令可以把已经通过pvcreate命令处理的pv添加到vg物理卷组中进行VG扩容

## 逻辑卷组制作过程
- 有了物理卷组就可以创建逻辑卷了
- lvcreate -L 100M -n first_lv first_vg 基于物理卷组first_vg创建逻辑卷first_lv 大小为100M
- lvscan 简单查看 
- lvdisplay 查看lv详情

## 创建文件系统并挂载
- 到现在已经创建了一个逻辑卷，但是还无法使用，和物理卷一样，需要格式化创建文件系统，
- 逻辑卷的全路径为 /dev/卷组名/逻辑卷名
- mkfs.ext4 /dev/first_vg/first_LV 
- mount /dev/first_vg/first_LV /mnt/sda8/ 这样就把逻辑卷挂载到目录了

- linux采用 文件系统+虚拟文件系统的形式

