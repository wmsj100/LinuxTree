---
title: blkid
date: 2020-03-21 08:37:56
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# blkid

## 概要

- 查看磁盘的UUID,或者磁盘文件系统类型
- 使用这个命令必须安装“e2fsprogs”软件包

## 使用

- `blkid`
- `blkid /dev/sda1`
```
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Notes$ blkid
/dev/loop0: TYPE="squashfs"
/dev/loop1: TYPE="squashfs"
/dev/loop2: TYPE="squashfs"
/dev/loop3: TYPE="squashfs"
/dev/loop4: TYPE="squashfs"
/dev/loop5: TYPE="squashfs"
/dev/loop6: TYPE="squashfs"
/dev/loop7: TYPE="squashfs"
/dev/nvme0n1p1: UUID="6569-B76F" TYPE="vfat" PARTUUID="cd841bf8-0aa3-4d5e-8c2b-be60066f93f4"
/dev/nvme0n1p2: UUID="0413c994-ad39-48bd-b836-9a744797a2b6" TYPE="ext4" PARTUUID="9b787376-07b8-49bb-bfb9-a8e5a5e394dc"
/dev/nvme0n1p3: UUID="1144df6c-79dc-4d92-b937-4c7bd2bd04f9" TYPE="ext4" PARTUUID="0283998d-8160-4b84-ab83-599c8fbfb075"
/dev/nvme0n1p4: UUID="8c89f5ff-e757-4b52-983f-93a2aee22533" TYPE="swap" PARTUUID="6af4b390-ff7a-4fb1-9849-344bc94ce68b"
/dev/nvme0n1p5: UUID="40b721b7-773c-4d0f-801b-6398dafe8b8d" TYPE="xfs" PARTUUID="dd47e5f3-879a-439d-85e1-b1b11b6235b4"
```

## 参考

- [blkid](https://man.linuxde.net/blkid)
