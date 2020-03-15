---
title: boot
date: 2020-03-15 12:00:24
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# boot

## 概要

- boot分区包含内核/ramdisk镜像以及bootloader配置文件和bootloader stage.
- 它也可以存放内核再执行用户态程序之前所使用的其他数据.
- boot在日常系统运行中并不需要,只在启动和内核升级(包括重建initial ramdisk)的时候使用
- 如果使用软RAID0系统的话,必须有一个独立的`/boot`分区
- 不使用EFI时,`/boot`建议大小200MB,如果使用EFI,需要至少512MB.

## 参考

- [arch boot](https://wiki.archlinux.org/index.php/Partitioning_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
