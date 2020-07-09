---
title: docker-compose-app-xinde
date: 2020-07-10 01:24:35
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker-compose-app-xinde

## 概要

- 这是我第一次使用docker-compose来部署应用,因为之前的应用本身就不会涉及到应用的迁移,所以所有的应用都在一个虚拟机或者容器中,但假如现在要执行迁移动作,真的是一锅乱.
- 这样就只能使用所谓的p2v或者v2v等工具来进行迁移操作.
- 一个好的或者说逻辑清晰的应用就应该是容器化的,因为容器本身很小,代码清晰,迁移非常容易.
- 比如我把webapp从ubuntu的虚拟机之间github代码拷贝到我本地的archlinux上面,执行一个docker-compose就可以了,容器直接就运行起来了,端口监听也是ok的,而且只暴露了一个8002端口,数据库的端口是没有暴露出来的.
- 这个体验让我觉得这俩天的摸索是值得的,因为我自己体验了容器化的概念.

## 参考

