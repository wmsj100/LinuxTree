---
title: kernel
date: 2020-03-14 16:43:56
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# kernel

## 概要

- 关于内核的理解是,
- 内核是系统最重要最核心也最先启动的模块
- 先运行内核,然后挂载根目录,然后在挂载其他分区,然后再启动开机要运行的服务
- 内核是需要全部加载到内存中来运行的
- 对内核的修改是需要重启电脑才可以实现的
- 无法对内存中的内核作出修改,
- root也无法修改内存中的内核,是一个隔离区,有写保护措施,还有自我修复,
- 内核panic之后会自动拉起,这是通过看门狗机制来实现的,只要喂狗和咬狗机制

## 参考

