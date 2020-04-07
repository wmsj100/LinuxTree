---
title:  文件格式化为文件系统创建分区并进行挂载
date: Tue 20 Sep 2017 10:35:46 PM CST
modify: 2020-04-07 19:40:06 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 文件格式化为文件系统创建分区并进行挂载

## 概述

- dd if=/dev/zero of=mirror.img bs=1M count=256M
- mkfs.ext4 mirror.img
- losetup /dev/loop0 mirror.img 通过losetup命令创建镜像与回环设备的关联
- fdisk mirror.img 给mirror.img创建一个主分区和俩个逻辑分区
- kpartx -av /dev/loop0 给各分区创建虚拟设备的影射
- mkdir -p /media/mirror_{1..3} 在meida创建3个文件夹
- mount /dev/mapper/loopimg1 /media/mirror_1 加载分区。

## 卸载

- `umount /home` 卸载分区
- `umount: /home: device is busy` 有可能当前分区有进程在使用导致卸载失败
- `fuser -m /home` `/home: 10278c 10279c 10280c 10281c 10282c 10295 10365 18222c`
- 可以通过fuser来查看占用当前分区的进程，
- `ps aux | grep -E "10278|10279"` 可以查看具体进程详情
- `kill -9 10278`

## 注意

- mount -a 在不重启电脑的情况下重新挂载/etc/fstab分区设置，修改分区挂载后建议先这样设置，防止设置错误直接重启导致电脑无法重启
