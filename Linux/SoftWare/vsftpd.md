---
title: vsftpd
date: 2020-01-08 15:01:02
modify: 
tags: [SoftWare]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# vsftpd

## 概要

- 这是Linux下的一款ftp软件
- 安装之后可以通过它来实现ftp功能

## 配置

- `sudo apt install vsftpd`
- `sudo vi /etc/vsftpd.conf` 
	- write_enable:yes
	- local_root:/home/pi/ftp #指定ftp的根目录
- `sudo service vsftpd restart` 重启vsftpd服务

