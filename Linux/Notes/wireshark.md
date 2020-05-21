---
title: wireshark
date: 2020-05-21 09:45:40
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# wireshark

## 概要

- wireshark是一款开源的网络分析工具
- `yum install wireshark`
- 安装完成后以`tshark`工具来提供服务

## 使用

- `tshark -i eth0 -t a port 8080` 抓取8080端口的所有请求

## 参考

