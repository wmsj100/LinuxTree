---
title: 负载均衡
date: 2020-01-08 22:17:22
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# 负载均衡

## 概要

- 负载均衡其实就是在反向代理的基础上实现的，或者说反向代理大概率会和负载均衡集成使用
- 负载均衡通过一定的策略来实现访问不同的服务器

## 模拟负载均衡

- 一个tomcat可以实现一个应用，
- 可以同时启动多个tomcat来模拟多台服务器
- 通常一台服务器会启动一个tomcat
- 修改不同tomcat的配置文件`/tomcat/conf/server.xml` ，tomcat的端口不能重复，所以修改`shutdonw/Connector port`总共3个端口，必须保证端口不能重复，否则会因为端口冲突导致`tomcat`启动失败
- `netstat -ntpl | grep 8081`来查看端口是否启动成功
- 修改`nginx`的配置文件，在`upstream`中写入多个服务器IP或者同一个服务器的不同端口
- `upstream`后面的标识只能是`domain`，如果写自定义会导致反向代理或者负载均衡不生效。
- `sudo nginx -s reload`
- `sudo service nginx restart` 如果这样还不生效，可以指向重启虚拟机来查看。我的树莓派就出现这样的问题，重启后还是不生效，结果定位的原因是因为`upstream`后面的值不是`domain`。

## 范例

```nginx
upstream domain{
	server 192.168.0.102:8081;
	server 192.168.0.102:8082;
}

server {
	listen 80;
	server_name www.taobao.com;
	location / {
		proxy_pass http://domain;
	}

}
```

## 参考

