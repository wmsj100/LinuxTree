---
title: basic
date: 2020-01-08 20:48:54
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- nginx很重要的一个作用是可以在一台服务器上同时部署多个网站
- 这个功能是通过配置文件来实现的
- 每个网站可以添加一个配置文件
- 在访问的电脑上配置`hosts`文件，把域名指向目标虚拟机，然后直接访问域名就可以访问网站

## 范例

```nginx
server {
	listen 80; #监听端口
	server_name www.test1.com; #服务域名

	location / {
		root /home/pi/Documents/www/test1;  #网站根目录
		index index.html index.htm index.nginx-debian.html; #根目录引导页
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files $uri $uri/ =404;
	}

}
```

## 参考

