---
title: fsck
date: Mon 26 Feb 2018 10:19:15 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 磁盘检查

## 基础概念

- fsck 在检查磁盘的时候需要磁盘是未挂载状态，否则会造成文件系统损坏。
- 如果系统的根目录出现问题，只能重启，因为根目录无法被`umount`，重启会检测到这个问题，然后提示用户输入root密码进入单用户模式。然后就可以使用fsck修复根目录文件系统了。

## badblocks 
- 主要用于检测硬盘物理坏道，使用这个命令其实更多的只是确认磁盘是否有坏道，平时使用很少。
