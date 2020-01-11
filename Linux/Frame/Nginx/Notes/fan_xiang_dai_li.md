---
title: 反向代理
date: 2020-01-08 20:47:32
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# 反向代理

## 概要

- 反向代理多用于进行负载均衡/集群，
- 可以通过指定的域名访问固定端口的页面。

## 范例
```nginx
upstream domain{
	server 192.168.0.102:8080;
}

server {
	listen 80;
	server_name www.tomcat.com;
	
	location / {
		proxy_pass http://domain;
	}
}
```

- 通过上面的配置，就可以通过直接访问域名`www.tomcat.com`来访问`192.168.0.102:8080`，使访问更加简便。

## 参考

- [反向代理](https://www.w3cschool.cn/minicourse/play/nginx_my?cp=5091&gid=0)
