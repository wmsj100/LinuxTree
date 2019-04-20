---
title: linux基础知识
date: Tue 20 Feb 2018 10:39:17 AM CST
tag: [linux,basic]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 每个linux都能够拥有多个内核版本，且几乎发行版的所有内核版本都不相同。
- uname -r 查看当前系统的内核版本

- 反单引号 在一串命令中，反单引号内的命令会被先执行，而其执行出来的结果会作为外部的输入信息。
    - ll `locate crontab` 先用locate将文件名数据列出来，在用ll命令展示
