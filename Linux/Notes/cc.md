---
title: cc
date: 2020-03-29 19:55:40
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# cc

## 概要

- cc通常指向当前的编译环境,比如linux中通常cc就是gcc的软链接,
- `which cc`
- `ll /usr/bin/cc`
- `ll /etc/alternatives/cc`
- 会看到其实cc就是指向了gcc
```
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Notes$ which cc
/usr/bin/cc
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Notes$ ll /usr/bin/cc
lrwxrwxrwx 1 root root 20 Mar 16 23:20 /usr/bin/cc -> /etc/alternatives/cc
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Notes$ ll /etc/alternatives/cc
lrwxrwxrwx 1 root root 12 Mar 16 23:20 /etc/alternatives/cc -> /usr/bin/gcc
```

## 参考

- [cc gcc g++](https://stackoverflow.com/questions/1516609/difference-between-cc-gcc-and-g)
