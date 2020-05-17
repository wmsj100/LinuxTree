---
title: lsblk
date: 2020-03-21 08:35:42
modify: 2020-05-17 15:06:36 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# lsblk

## 概要

- 列出磁盘的简单信息,包括挂载点,磁盘容量
- 该工具用于列出所有可用块设备的信息，而且还能显示他们之间的依赖关系。
- lsblk包含于`util-linux`工具包中

## 使用

- `lsblk`
- `lsblk /dev/nvme0n1p5` 查看单块磁盘信息

```
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0   956K  1 loop /snap/gnome-logs/81
loop1         7:1    0  14.8M  1 loop /snap/gnome-characters/399
loop2         7:2    0  44.9M  1 loop /snap/gtk-common-themes/1440
loop3         7:3    0  89.1M  1 loop /snap/core/8268
loop4         7:4    0   3.7M  1 loop /snap/gnome-system-monitor/127
loop5         7:5    0  54.7M  1 loop /snap/core18/1668
loop6         7:6    0 160.2M  1 loop /snap/gnome-3-28-1804/116
loop7         7:7    0   4.2M  1 loop /snap/gnome-calculator/544
nvme0n1     259:0    0 119.2G  0 disk
├─nvme0n1p1 259:1    0    94M  0 part /boot/efi
├─nvme0n1p2 259:2    0  28.6G  0 part /
├─nvme0n1p3 259:3    0  19.1G  0 part /var
├─nvme0n1p4 259:4    0   3.8G  0 part [SWAP]
└─nvme0n1p5 259:5    0  67.7G  0 part /home
```

## 参考

