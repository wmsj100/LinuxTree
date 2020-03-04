---
title: virtualbox
date: 2020-03-04 18:42:23
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# virtualbox

## 概要

- virtualbox是一款开源虚拟机软件，现在有甲骨文发行

## 安装

- 添加sources.list
	- 查看自己的发现版本
	- `cat /etc/lsb-release`
```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.4 LTS"
```
	- 或者直接输入lsb_release
- `deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian bionic contrib` 写入`/etc/apt/sources.list`
- `wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -`
- `sudo apt-get update`
- `sudo apt-get install virtualbox-6.1`

## 参考

- [virtualbox install](https://www.virtualbox.org/wiki/Linux_Downloads)
