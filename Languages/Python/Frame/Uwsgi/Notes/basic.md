---
title: basic
date: 2020-01-11 10:05:29
modify: 2020-07-20 09:27:42  
tags: [Notes]
categories: Uwsgi
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- uwsgi是一套实现了wsgi(web server gateway interfacce)协议的一个框架，它以自己专有的uwsgi协议和python应用程序进行交互
- 它可以和nginx和apache通过wsgi协议进行交互
- 它是web服务器和python应用程序的桥梁
- 只要配置好配置文件，使用很简单，
- 它也可以单独作为服务器对外提供服务的能力，就是客户端之间通过uwsgi和python应用程序交互，但这样的风险高，性能也没有nginx好。

## 使用

- `sudo apt install uwsgi`
- `pip install uwsgi` 如果使用pip来安装时候需要依赖gcc来执行编译操作，
	- `yum install gcc`
- `uwsgi --socket :8083 --wsgi-file /home/pi/Documents/mydjango/test.py` 这样可以启动一个端口为8083的web服务器，
- `uwsgi --http :8084 --wsgi-file /test.py` 这样可以开启一个http的端口服务器
- test.py的内容如下
```python
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello World']
```
- `uwsgi --ini /home/pi/Documents/mydjango/uwsgi.ini` 也可以通过配置文件的形式来启动uwsgi
- uwsgi.ini的内容如下
```ini
[uwsgi]

chdir=/home/pi/Documents/mydjango
module	= mydjango.wsgi:application
wsgi-file=mydjango/wsgi.py
home=/home/pi/Software/virtualenv
uid=www-data
gid=www-data
master=true
processes=4
#socket=/home/pi/Documents/mydjango/mydjango.sock
socket=:8083
#chmod-socket=664
vacuum	= true
```


## 参考

- [nginx+uwsgi+flask](https://www.missshi.cn/api/view/blog/5b1511a213d85b1251000000)
