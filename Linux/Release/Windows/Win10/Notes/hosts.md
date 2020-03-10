---
title: hosts
date: 2020-01-08 22:29:35
modify: 
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# hosts

## 概要

- 域名解析的配置文件

## win10无权限修改文件

- 碰都的情况是在win10上没有权限修改这个文件
- 解决办法是以管理者权限启动powershell,进入到hosts目录，然后执行命令`notepad hosts`，然后修改文件再保存，这样就可以了。

## 参考

