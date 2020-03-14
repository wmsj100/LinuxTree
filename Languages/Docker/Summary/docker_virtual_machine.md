---
title: docker_virtual_machine
date: 2020-03-14 16:22:13
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker_virtual_machine

## 概要

- 关于docker的虚拟机,要理解它的运行机制,它和虚拟机的本质区别在于,它是运行于宿主系统上面的.
- 共享宿主资源,
- 在docker的虚拟机上面执行一些命令和在宿主机上面执行结果是一样的
```
/ # uname -a
Linux c33613301f28 5.3.0-42-generic #34~18.04.1-Ubuntu SMP Fri Feb 28 13:42:26 UTC 2020 x86_64 Linux
/ # Linux Ubuntu 5.3.0-42-generic #34~18.04.1-Ubuntu SMP Fri Feb 28 13:42:26 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux^C
```
- 获取的内核版本信息完全一样.因为它读取的就是主机的信息
- 关于虚拟机的虚拟网卡是通过Docker的虚拟网卡来管理的,而docker和本机的物理网卡是可以互通的.
- 所以docker上面创建的虚拟机是可以直接访问互联网的,也就是这样是没有达到网络隔离的目的

## 参考

