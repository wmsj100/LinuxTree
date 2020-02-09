---
title: nginx_uwsgi_flask
date: 2020-02-09 16:21:02
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# nginx_uwsgi_flask

## 概要

- 配置python的服务框架，以nginx为代理，uwsgi为python服务导流，flask为轻量级框架
- 其实这套框架早在18年6月份参与的项目就知道了，当时为什么没有兴趣去深入研究呢，区别只是当时选择了django。

## uwsgi配置

```uwsgi
[uwsgi]
socket = 127.0.0.1:5051
pythonpath = /home/ubuntu/Github/python_study/flask/study3
module = run
wsgi-file = /home/ubuntu/Github/python_study/flask/study3/uwsgi.ini
callable = app
processes = 1
threads = 1
daemonize = /home/ubuntu/Github/python_study/flask/study3/server.log
pidfile=/home/ubuntu/Github/python_study/flask/study3/uwsgi.pid
```
- `socket`: 一个套接字，相当于为外界留出一个uwsgi服务器的接口。
	- `socket`不等于http，换句话说用这个配置起来的uwsgi服务器是无法直接通过http请求成功访问的，
- `pythonpath`: 指出了项目的目录
- `module`: 指出类项目启动脚本的名字
- `wsgi-file`: 指出了uwsgi的配置文件路径
- `callable`: 指出了具体执行run方法的那个实体的名字，一般都是`app=Flask(__name__)`
- `processes`和`threads`: 指出了启动uwsgi服务器之后，服务器会打开几个并行的进程，每个进程会开几个线程来等待处理请求。
- `daemonize`: 表示把uwsgi服务器作为后台进程启动，项的值指向一个文件表明后台中的所有的输出都重定向到这个日志文件。
- `pidfile`: uwsgi服务启动之后会自动放到后台执行，这个文件存储uwsgi的pid的值。

### socket和http

- socket本身不是协议而是一种具体的`TCP/IP`实现方式，而`HTTP`是一种协议且基于`TCP/IP`。
- 具体到这个配置，如果只配置类`socket=127.0.0.1:5051`，通过浏览器或者其他HTTP手段是无法成功访问的。
- 而在uwsgi这边的日志里会提示请求包的长度超过了最大固定长度。
- 另一方面，如果配置的是`http = 127.0.0.1:5051`那么就可以直接通过一般的http手段来访问到目标。
- 但这会引起nginx无法正常工作。
- 正确的做法应该是nginx在uwsgi之前作为啦代理，配置socket来和uwsgi通信

### 启动uwsgi

- 配置完成后就可以执行`uwsgi uwsgi.ini`来启动uwsgi，再查看日志，如果没有报错，`ps -ef | grep uwsgi`也能查询到uwsgi的进程，则说明启动成功。
- `kill -9 uwsgi.pid` 停止uwsgi需要先找到uwsgi的pid，然后手动执行kill来杀死进程

## nginx配置

```nginx.conf
server {
	listen 80;
	server_name myweb.com;
	access_log /home/ubuntu/Github/python_study/flask/study3/logs/access.log;
	error_log /home/ubuntu/Github/python_study/flask/study3/logs/error.log;

	location / {
		include uwsgi_params;
		uwsgi_pass 127.0.0.1:5051;
		uwsgi_param UWSGI_CHDIR /home/ubuntu/Github/python_study/flask/study3;
		uwsgi_param  UWSGI_SCRIPT run:app;
	}
}
```
- `listen`: 监听80端口
- `server_name`: 只有来自`myweb.com`的请求才处理
- `access_log/error_log`: nginx的成功和错误日志
- `include uwsgi_params`: 导入uwsgi配置
- `uwsgi_pass`: 进行反向代理的地址和端口，需要和uwsgi的配置一致
- `uwsgi_param`: 
	- `UWSGI_CHDIR`: 项目根目录
	- `UWSGI_SCRIPT`: 启动项目的主程序

- 这样配置完成后来自80端口的请求先到达nginx，然后nginx通过socket方式转发给uwsgi，uwsgi通过入口文件run:app方式来启动程序并进行处理，然后把结果返回给nginx。

## 程序入口文件代码

- main.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello wmsj100"

@app.route('/name')
def name():
    return "Your name is wanghao"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

- run.py
```python
from main import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

## 参考

- [nginx_uwsig_flask](https://www.cnblogs.com/lfxiao/p/10103490.html)
