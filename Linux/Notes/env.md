---
title: env
date: 2020-05-27 15:07:40
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# env

## 概要

- 查看当前的环境变量，是当前client端的所有生效的环境变量或者全局变量。

## 重要参数

- `SSH_CONNECTION`: 查看当前client是从哪里被连接的，是非常重要的参数。
	- `SSH_CONNECTION=192.168.0.142 59420 192.168.0.8 22` 表示是被`192.168.0.142`的`59420`端口连接到当前主机的`22`端口

## 参考

