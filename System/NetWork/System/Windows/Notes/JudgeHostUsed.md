---
title: 判断域名是否被占用
date:  2018-07-03 09:19:00
modify:
tag: [cmd]
categories: Windows
author: wmsj100
mail: wmsj100@hotmail.com
---

# 判断域名是否被占用

## 问题
- 如何判断域名是否被占用？
- 如何从域名解析到IP

## 解决
- 直接用`cmd`工具的`ping`命令来获取，如果能`ping`通则说明域名已经被占用，并且会返回域名的`ip`；
- 如果域名没有解析到，则说明域名没有被占用
