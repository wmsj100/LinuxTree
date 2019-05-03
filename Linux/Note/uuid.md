---
title: UUID
date: 2019-04-19 22:37:56	
modify: 
tag: [basic]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 查看UULD

## 概述
- blkid: 查看磁盘的详情
root@raspberrypi:/home/pi# blkid
/dev/mmcblk0p1: LABEL="boot" UUID="27D9-A951" TYPE="vfat" PARTUUID="73fafd5c-01"
/dev/mmcblk0p2: LABEL="rootfs" UUID="db9fbdec-9f10-4008-95da-5062491e0659" TYPE="ext4" PARTUUID="73fafd5c-02"
/dev/mmcblk0: PTUUID="73fafd5c" PTTYPE="dos"
/dev/sda: UUID="9ac9d3cf-e649-4b17-82ed-5687a890dc8d" TYPE="ext4"

## 参考
- []()
