---
title: cpu是否支持虚拟化技术
date: 2020-03-05 09:49:26
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# cpu是否支持虚拟化技术

## 概要

- 我通过virtualbox成功安装之后想要用`docker-machine`来创建docker虚拟主机，
- 创建成功了但是无法启动，网速查找资料无果
- 登录到centos8主机在可视化界面启动virtualbox，查看虚拟机的日志
- 看到一条日志
	- 'the host cpu does not support hw virtualization'
	- 意思是说我当前的笔记本的cpu不支持虚拟化
- 重启笔记本查看bios界面时候就是没有找到virtualization字眼，感觉应该是笔记本太老了，8年前笔记本还是不支持这样的技术的。
- 所以就放弃了在linux上装docker虚拟主机，只能通过树莓派和笔记本来进行交互了。

## 参考

