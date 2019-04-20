---
title:  文件格式化为文件系统创建分区并进行挂载
date: Tue 20 Sep 2017 10:35:46 PM CST
modify: 2019-04-19 22:48:32	
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 文件格式化为文件系统创建分区并进行挂载

- dd if=/dev/zero of=mirror.img bs=1M count=256M
- mkfs.ext4 mirror.img
- losetup /dev/loop0 mirror.img 通过losetup命令创建镜像与回环设备的关联
- fdisk mirror.img 给mirror.img创建一个主分区和俩个逻辑分区
- kpartx -av /dev/loop0 给各分区创建虚拟设备的影射
- mkdir -p /media/mirror_{1..3} 在meida创建3个文件夹
- mount /dev/mapper/loopimg1 /media/mirror_1 加载分区。
- mount -a 在不重启电脑的情况下重新挂载/etc/fstab分区设置，修改分区挂载后建议先这样设置，防止设置错误直接重启导致电脑无法重启
