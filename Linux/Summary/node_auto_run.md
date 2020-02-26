---
title: node后台占用大量cpu
date: 2020-02-26 10:33:31
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# node后台占用大量cpu

## 概要

- 虚拟机使用时候忽然觉得卡吨，然后查看top发现node占用了30%的cpu资源
- 查看ps -ef | grep nodepid 发现是typescript触发的更新，
- 然后就强制kill了进程，可是过了一会儿又自动启动了
- 然后就意识到自己之前在sudo npm install方式安装了很多node包，所以觉得卸载安装在全局的包
- `sudo npm uninstall -g ...` 这样进行卸载

