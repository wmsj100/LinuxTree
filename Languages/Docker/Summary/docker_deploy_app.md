---
title: 容器化部署
date: 2020-07-07 10:06:57
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker_deploy_app

## 概要

- 当前应用通常都是混合部署在一台服务器上面，这样面临的窘境是当服务器需要扩容的时候会非常麻烦，尤其是面临负载问题的时候，如何扩容，只能复制一台虚拟机出来，然后借助公有云厂商的LVS等服务来实现负载均衡。
- 但假如一开始应用就是用docker来部署，然后通过docker-compose来管理，这样实现横向扩展就变得非常容易。
- 所以容器化绝对是大势所趋，当前阿里云的所以应用都是跑在容器上面的。

## 参考

