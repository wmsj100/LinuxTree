---
title: 虚拟机没有公网IP
date: 2020-05-27 15:21:30
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 虚拟机没有公网IP

## 概要

- 之前认为一台虚拟机就需要一个公网IP，这样才可以直接通过公网来登录到虚拟机，
- 但昨天登录ambari的虚拟机时候发现只有一台虚拟机有公网ip，其他俩台虚拟机是通过局域网来通信的。
- 这样最大的好处就是对于虚拟机的保护，而且网络通过局域网传输文件时候可以达到惊人的140M/s,这个速度是无法通过公网IP达到的。
- 通常一台虚拟机,公有云的虚拟机只有一张网卡，也就是只有一个局域网ip地址，那么如何通过局域网地址来实现网络访问呢,关键技术就是NAT
- 那么公网IP是什么，怎么确定的，一个ip地址可以拆分为网络地址和主机地址，通过网络地址可以确定到网络地址的路由器，主机地址可以通过计算来来确定到是内网中的哪一个虚拟机。

## 参考

- [公网ip](https://blog.csdn.net/u011314442/article/details/82182265)
