---
title: source
date: Tue 20 Feb 2018 11:05:54 PM CST
modiry: 2020-04-15 10:14:11 
tag: [linux,sys,conf]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# source

## source 读入环境配置文件的命令

- 由于'/etc/profile', '~/.bash_profile'都是在取得'login shell'才会读取的配置文件，所以修改这些文件后通常都需要重新注销再登陆才会生效。
- 但是利用'source'或者'.'可以让配置立即生效

## source 父进程执行

- 通常shell中的命令都是在子进程中执行，子进程继承了父进程的环境变量
- 在子进程中执行`cd /tmp`命令，执行完成后实际并不会切换到/tmp目录，那是因为切换的动作是子进程来执行的
- `source test1.sh` 通过这个命令来执行，就是把脚本在当前进程执行
