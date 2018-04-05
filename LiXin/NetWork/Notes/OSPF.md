---
title: OSPF
date: 2018-04-05 10:23:46 Thu
modify: 2018-04-05 10:23:46 Thu
tag: [basic,net]
categories: NetWork
author: wmsj100
mail: wmsj100@hotmail.com
---

# OSPF
- open shortest path first 开放最短路径优先

## 概念
- 所有在自治系统内部使用的路由选择协议都是要寻找一条最短路径
- OSPF最主要的特征就是使用分布式的链路状态协议
- OSPF特点：
	- 向本自治系统中所有路由器发送信息
	- 发送的信息就是与本路由器相邻的所有路由器的链路状态
	- 只有当链路状态发生变化时，路由器才向所有路由器发送此信息
- 为了使OSPF能够适用与大规模网络，将一个自治系统再划分位若干个更小的范围，叫做区域。
- 一个区域的路由器最好不要超过200个	
