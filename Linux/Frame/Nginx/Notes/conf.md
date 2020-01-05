---
title: nginx的配置文件conf
date: 2020-01-05 21:09:37
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# nginx的配置文件conf

## 概要

- nginx安装完成后直接访问报403无权限，猜测是配置问题，查看`/var/www/html`目录和文件都有可读权限，所以应该是`nginx`的配置文件不对

## 获取配置文件路径

- `which nginx` 获取`nginx`路径
- `/usr/sbin/nginx -t`  `nginx: configuration file /etc/nginx/nginx.conf test failed`
- `vi /etc/nginx/nginx.conf` 进入配置文件查看

## 参考

