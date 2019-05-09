---
title: proc_fd
date: 2019-05-09 19:41:13	
modify: 
tag: [proc,linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# proc_fd

## 概述
- 每个进程的所有信息都在`/proc`目录下自己的`PID`文件夹内
- `cmdline` 说明当前进程的名称
- `fd` 文件描述符目录

```
lrwx------ 1 pi pi 64 May  9 00:00 0 -> /dev/pts/1
lrwx------ 1 pi pi 64 May  9 00:00 1 -> /dev/pts/1
lrwx------ 1 pi pi 64 May  9 00:00 2 -> /dev/pts/1
lrwx------ 1 pi pi 64 May  9 19:36 255 -> /dev/pts/1
```

## 范例
- `echo "hello pts1" > /dev/pts/1` 在`pts1`终端可以受到这条消息，通过这个方法可以给特定终端发送信息

## 参考
- []()
