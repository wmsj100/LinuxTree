---
title: lrzsz
date: 2020-04-08 16:53:21
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# lrzsz

## 概要

- 是一个可以在windows和linux之间传输文件的工具
- 体积小，且速度快，比ftp速度快，且带有可视界面。
- 可视窗口是通过当前的终端软件来实现的，比如xshell/mobaxterm

## 使用

- rz: receive file use Z-modem
- sz: send file use Z-modem
- `yum install lrzsz`
- `rz` 从windows上传文件，执行这个命令后会弹出一个可视弹框，选择要上传到当前路径的文件
- `sz a.txt` 会弹出可视弹框，选择要存储到windows的路径

## mobaxterm无法使用rz

- 终端软件是用的mobaxterm，在容器里面下载了lrzsz工具套件
- `rz` 在命令行执行这个命令，然后就卡死了，没有后续操作了，也没有直接弹出可视窗口，
```
[root@87283aa8325b ~]# rz
▒z waiting to receive.**B0100000023be50
```
- 其实mobaxterm没有xshell那样方便，直接就会弹出可视窗口，需要在界面右击，选择`send file use Z-modem`然后就会弹出可视窗口

## 参考

