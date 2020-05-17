---
title: rsync
date: 2020-03-19 17:27:35
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# rsync

## 概要

- 这是一个可以进行远程备份和复制的工具,在本地使用也很好用,类似cp/scp,但是区别在于rsync会比对俩处文件是否相同,只拷贝差异文件
- rsync和cp都是异步复制的，就是说同时有多个cpu进行磁盘写操作，但是cp是单进程异步，而rsync是多进程的异步，
- rsync可以断点传输，传输会比对文件，如果文件的时间一致，就不会传输。

## 使用

- `rsync -a ~/.ssh /tmp` 拷贝文件到/tmp,在本地使用
- `rsync -av -e ssh ./* pi@192.168.20.2:/tmp` 把当前目录的所有内容拷贝到pi主机的tmp目录,如果再次执行这个操作会发现没有执行,因为没有文件差异

## 参考

