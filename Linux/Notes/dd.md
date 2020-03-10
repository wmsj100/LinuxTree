---
title: dd命令
date: Sun 18 Feb 2018 11:29:54 PM CST
modify: 2020-03-10 21:02:35 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- dd 经常用于创建一个空文件，但是作用不只是如此。
    - dd if=/dev/zero of=file bs=1M count=1000
- dd可以读取磁盘设备的内容（几乎是直接读取扇区），所以磁盘的信息，包括superblock, boot sector, meta data 等信息也会被复制，所以被写入的磁盘都不需要进行格式化的操作。
- dd if=/dev/sda1 of=/tmp/mbr.bak bs=512 count=1
- 如果想构建俩块一模一样的磁盘时，只需要执行
    - `dd if=/dev/sda1 of=/dev/sda9`
- dd可以把iso或者其他打包格式的镜像文件写入usb
- `dd if=a.iso of=/dev/sda` 输出的一定是设备本身,不能是设备下面的分区`/dev/sda1, /dev/sda2`
- `sudo dd if=ArchLinuxARM-rpi-3-latest.tar.gz of=/dev/sda`
