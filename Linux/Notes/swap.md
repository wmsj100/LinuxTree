---
title: swap
date: 2020-05-20 14:03:47
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# swap

## 概要

- swap是用来缓存从磁盘读取到内存的文件的空间，
- 当文件从内存使用完成不会立刻清除，而是先在内存存放，以备再次访问。
- 当物理内存容量减少了，kswapd0程序会进行内存换页操作，会把最早时间读取到内存的文件先写入到swap中
- `/proc/sys/vm/swappiness`配置文件用来设置这种策略，取值0-100，默认是60，很多虚拟机，比如华为的虚拟机centos7默认是0，即不进行内存到磁盘的缓存

## swap分区

- 可以直接在磁盘进行分区然后格式化为swap
- 也可以通过文件来进行这样
- `dd if=/dev/zero of=/root/swapfile bs=128M count=100` 创建一个12G的文件
- `mkswap /root/swapfile`
- `swapon /root/swapfile`
- `vi /etc/fstab` `/root/swapfile swap swap defaults 0 0` 写入配置文件
- `swapoff /root/swapfile`

## 参考

- [swap](https://www.cnblogs.com/kerrycode/p/5246383.html)
- [kswapd0](https://blog.csdn.net/u012129607/article/details/74993302)
