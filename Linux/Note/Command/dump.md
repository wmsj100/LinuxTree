---
title: dump.md
date: Sun 18 Feb 2018 10:37:15 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- dump 是一个文件系统备份的方便的方法，
    - yum install dump
- dump -0u -f /mnt/img/img.dump.0 /mnt/img  这样就创建了一个0级备份文件。
- dump -W 查看dump备份情况，会显示出文件系统有备份的情况。

## restore
- restore 是恢复通过dump备份的文件系统，这个恢复需要在一个新的空白文件系统进行
- restore -r -f /mnt/img/img.dump.0 把工作目录切换到要恢复的目录，执行这个命令
- restore -i -f /mnt/img/img.dump.0 会进入restore的交互模式。在这个模式可以进行选择性的恢复。

