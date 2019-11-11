---
title: README
date: 2019-09-15 18:30:03 Sunday
modify:
tag: [README]
categories: Docker
author: wmsj100
mail: wmsj100@hotmail.com
---

# README

## 概述
- 容器的概念

## 安装
- sudo curl -sSL https://get.docker.com | sh

## 配置源
- `vi /etc/docker/daemon.json`
	```json
	{ 
	"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"] 
	}
	```
- sudo systemctl daemon-reload
- sudo systemctl restart docker

## 参考
- [树莓派安装docker](http://shumeipai.nxez.com/2019/05/20/how-to-install-docker-on-your-raspberry-pi.html)
- [阮一峰docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [docker源网站](https://www.daocloud.io/dce)

