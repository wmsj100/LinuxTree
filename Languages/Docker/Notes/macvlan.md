---
title: macvlan
date: 2020-03-09 12:13:17
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# macvlan

## 概要

- 这个是docker实现的一个自动模拟容器一个ip和mac地址,可以把虚拟机创建在不同子网段,然后让容器进行沟通
- 这个实现的前提是在本地,共有云是不能这样配置的.
- 因为这个前提是配置网卡模式为混杂模式,即所有途经自己的流量都继续转发,不再判断是否是请求自己的流量.
- 现在都使用overlay覆盖网络来实现跨网段访问,也不需要特意去创建一些网段出来.
- 所以那天为了测试macvlan的效果花费了很长时间去创建容器,最后都无法ping通,有虚拟机防火墙设置的原因,也有可能本身配置有问题.

## 参考
