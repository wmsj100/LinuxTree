---
title: version
date: 2019-10-11 07:02:04 Friday
modify:
tag: [basic]
categories: RaspberryPi
author: wmsj100
mail: wmsj100@hotmail.com
---

# version

## 概述

- 查看树莓派信息

## 用法

- `cat /proc/device-tree/model` 查看树莓派型号
- `cat /proc/version` 查看kernel版本
- `cat /etc/os-release` 查看os版本信息
- `cat /etc/issue` 查看Linux distro版本
- `cat /etc/debian_version` 查看Debian版本
- `getconf LONG_BIT` 查看系统位数
- `uname -a` 查看kernel版本

## 参考
- [树莓派版本信息](https://www.cnblogs.com/ahuo/p/11039451.html)
