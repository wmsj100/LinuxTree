---
title: uwsgi+djando+nginx
date: 2020-02-14 16:24:04
modify: 
tags: [Notes]
categories: Uwsgi
author: wmsj100
email: wmsj100@hotmail.com
---

# uwsgi+djando+nginx

## 概要

- 这个就是一直心心念djando环境搭建指南，是一个完整的流程

## uwsgi配置

- djando自带服务器但不适用于生产环境，使用uwsgi来管理django更加专业
```uwsgi.ini
[uwsgi]
#django项目目录
chdir=/home/ubuntu/Github/python_study/django/study2
# wsgi文件
module = study2.wsgi
# python虚拟环境
virtualenv=/home/ubuntu/Code/Python/virtual/py3env
# 是否以主进程启动
master = true
# 进程数量
processes = 1
# socket文件，也可以用端口，但文件更适用
socket=/home/ubuntu/Github/python_study/django/study2/study2.sock
chmod-socket=777
# 文件关闭时候删除所有临时文件
vacuum = true
# 日志文件
logto = /tmp/study2.log
```

## nginx配置

```nginx.conf
upstream Study2 {
server unix:///home/ubuntu/Github/python_study/django/study2/study2.sock;
}
server {
	listen	8004;
	server_name	myweb.com;
	charset	utf-8;
	client_max_body_size 75M;

	access_log /home/ubuntu/Github/python_study/django/study2/logs/access_log;
	error_log /home/ubuntu/Github/python_study/django/study2/logs/error_log;

	location	/media	{
		alias /home/ubuntu/Github/python_study/django/study2/media;
	}

	location	/static {
		alias /home/ubuntu/Github/python_study/django/study2/static/;
	}

	location	/ {
		uwsgi_pass Study2;
		include uwsgi_params;
	}

}
```

## 参考

- [uwsgi+django](https://www.jianshu.com/p/23762bd086e1)
