---
title: source读入环境配置文件
date: Tue 20 Feb 2018 11:05:54 PM CST
tag: [linux,sys,conf]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## source 读入环境配置文件的命令
- 由于'/etc/profile', '~/.bash_profile'都是在取得'login shell'才会读取的配置文件，所以修改这些文件后通常都需要重新注销再登陆才会生效。
- 但是利用'source'或者'.'可以让配置立即生效
