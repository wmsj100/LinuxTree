---
title: 修改apt源
date: 2020-01-05 20:58:57
modify: 2020-01-08 14:18:50
tags: [Notes]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# 修改apt源

## 概要

- 树莓派安装完成后需要修改默认的源，
- `sudo vi /etc/apt/source.list`，用下面的源替换软件更新源
- `deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ stretch main contrib non-free rpi`
- `sudo vi /etc/apt/sources.list.d/raspi.list`,替换系统更新源
- `deb http://mirrors.ustc.edu.cn/archive.raspberrypi.org/debian/ stretch main ui`
- `sudo apt update`
- `sudo apt upgrade`

## 推荐

```
deb http://mirrors.ustc.edu.cn/raspbian/raspbian/ buster main contrib non-free rpi
deb http://mirrors.aliyun.com/raspbian/raspbian/ buster main contrib non-free rpi
```
- `deb-src http://mirrors.aliyun.com/raspbian/raspbian/ buster main` for /etc/apt/source.list
- `deb http://mirrors.aliyun.com/raspbian/raspbian/ buster main contrib non-free rpi` for /etc/apt/source.list.d/raspi.list

## 参考

- [树莓派更好源](https://www.jianshu.com/p/768f0181672b)
