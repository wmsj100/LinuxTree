---
title: resourceOccupy
date: 2020-04-17 09:56:50
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# resourceOccupy

## 概要

- 再docker中查看top发现cpu占用率非常高，几乎100%，但是查看自己的活动进程，发现没有资源去占用cpu，所以此时就可以想到是其他的docker占用了资源，因为我当前的docker和其他docker是共享当前主机资源的
- 如此看来，通过docker启动的容器也是无法实现虚拟机的优势，就是对于资源的使用不可控

## 参考

