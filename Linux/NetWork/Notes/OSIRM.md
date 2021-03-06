---
title: OSIRM
date: 2018-04-07 22:35:48 Sat
modify: 2018-04-07 22:35:48 Sat
tag: [net]
categories: NetWork
author: wmsj100
mail: wmsj100@hotmail.com
---

# OSI/RM 网络标准

## 概述
- OSI/RM低四层(物理层，数据链路层，网络层，传输层)定义了如何进行端到端的数据传输，也就是定义了如何通过网卡，物理电缆，交换机和路由器进行数据传输
- 高三层(会话层，表示层，应用层)定义了终端系统的应用程序和用户如何彼此通信

- 现在更多的划分为低三层和高四层
- 低三层：负责创建网络通信所需的网络连接(面向网络)，属于通信子网部分
	- 首先通过它们自己对应层的信息交换构建数据通信所需的网络平台
	- 为上层的数据提供物理的传输通道
	- 第三层不能时别和处理来自应用层的网络应用数据，
- 高四层：具体负责端到端的用户数据通信(面向用户)，属于资源子网部分
	- 高四层进行的才是真正面向用户的网络应用，

## 总结
- 每一层所代表的都是一组网络功能，而实现功能可以有许多不同的软/硬件方案。
- 同一层中的各网络节点都有相同的层次结构，具有同样的功能
- 同一节点内相邻层之间通过接口进行通信
- 每一层使用下一层提供的服务，并向上层提供服务
- 不同节点的同等层按照协议实现对等层之间的通信
- 网络设备间的通信仅需要低三层，用来构建数据通信平台，网络平台构建好后，用户应用数据就可以利用这个平台进行各种网络应用通信。

## 现状
- OSI/RM现在被TCP/IP协议(非正式标准，事实标准)替代
- 层次划分过多
