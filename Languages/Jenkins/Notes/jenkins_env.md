---
title: jenkins运行环境
date: 2020-03-03 08:36:55
modify: 
tags: [Notes]
categories: Jenkins
author: wmsj100
email: wmsj100@hotmail.com
---

# jenkins运行环境

## 概要

- 关于Jenkins运行非常简单，只需要执行`java -jar jenkins.war --httpPort=8080`
- 然后就可以在浏览器的8080端口查看页面了
- 但是Jenkins的运行环境可以有多种
- 通过上面那样
- 放到tomcat的webapp目录
- 通过添加apt源，`sudo apt install jenkins`这样会同时创建`jenkins`用户，并且有守护进程，默认开机启动
- 也可以通过dockers来配置Jenkins的环境

## 参考

