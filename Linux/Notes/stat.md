---
title: stat
date: 2020-06-17 14:32:32
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# stat

## 概要

- 获取文件的时间

## 使用

- `stat a`
```
[root@22e22f866423 ~]# stat a
  File: ‘a’
  Size: 9               Blocks: 8          IO Block: 4096   regular file
Device: 100036h/1048630d        Inode: 660840      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2020-06-17 06:34:03.672453356 +0000
Modify: 2020-06-17 06:37:18.174551177 +0000
Change: 2020-06-17 06:37:18.174551177 +0000
 Birth: -
```
- `stat -c %y a` `2020-06-17 06:37:18.174551177 +0000` 按照可读的方式打印文件的最后修改时间

## 参考

- [linux stat](https://blog.csdn.net/qq_31828515/article/details/62886112)
