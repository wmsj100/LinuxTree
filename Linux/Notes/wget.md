---
title: wget
date: 2020-04-09 13:19:02
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# wget

## 概要

- 可以模仿页面访问url
- 通常用于下载文件

## 使用

- `wget http://prdownloads.sourceforge.net/findbugs/findbugs-3.0.1.tar.gz` 下载在当前目录
- `wget http://prdownloads.sourceforge.net/findbugs/findbugs-3.0.1.tar.gz -O /tmp/a.tar.gz`下载到指定目录
- `wget -nv http://xxx.tar.gz -O a.tar.gz` 只显示关键信息，并且了`文件另存为自定义名称

## 参考

- [wget](https://www.cnblogs.com/ftl1012/p/9265699.html)
