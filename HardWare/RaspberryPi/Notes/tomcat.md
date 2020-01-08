---
title: tomcat
date: 2020-01-08 13:05:58
modify: 
tags: [Notes]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# tomcat

## 概要

- tomcat是一个服务器，可以响应动态应用，适用于中小型应用

## 安装

- 在[tomcat](https://tomcat.apache.org/)获取最新安装包，是二进制的包，`Core`包，选择`tar.gz`格式
- `wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-9/v9.0.30/bin/apache-tomcat-9.0.30.tar.gz` 进入到本地存储目录，下载压缩包
- `tar -zxvf apache-tomcat-9.0.30.tar.gz` 解压缩
- `cd /home/pi/Software/apache-tomcat-9.0.30/bin`
- `./startup.sh` 启动tomcat
- 在浏览器查看8080端口是否可以启动

## 参考

- [树莓派安装tomcat](https://www.jianshu.com/p/9e5c0e41ef24)
