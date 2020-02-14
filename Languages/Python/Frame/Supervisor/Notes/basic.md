---
title: basic
date: 2020-02-14 15:51:52
modify: 
tags: [Notes]
categories: Supervisor
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- 进程守护工具，为什么会使用到它呢，是想搭建django框架，
- 因为当前django是通过uwsgi进行管理的，但是uwsgi进程每次要关闭或者重启都需要手动查找，很麻烦
- 而且uwsgi可以启动多个实例，需要再ps中仔细区分哪个实例才是目标实例
- 然后提到了supervisor这个进程管理工具，就开始入手了，
- 使用体验是工具非常好用，尤其是对于uwsgi的进程启停，当进程出行意外被杀死时候会自动拉起，很好用
- 该工具分为服务器端和客户端
- `supervisord`： 服务器端
- `supervisorctl`: 客户端

## 操作

- `pin install supervisor` 安装
- `echo_supervisord_conf >/etc/supervisord.conf` 把系统当前的配置文件重定向到/etc，
	- 关于这个操作我因为是再虚拟环境中配置的，所以导致操作失败，没有权限，但是使用`sudo`使用又会报找不到命令。
	- 无奈之下就只能再当前用户的家目录下创建了目录来存储配置文件
	- `echo_supervisord_conf > ~/supervisord/supervisord.conf`
- 修改配置文件
	- 主要修改的是3个文件的存储，默认这些文件都放在`/tmp`目录下，这个目录的文件可能会出行被linux删除的动作，
	- `supervisor.sock, supervisord.pid, supervisord.log`
```supervisord.conf
[unix_http_server]
file=/home/ubuntu/supervisord/supervisor.sock   ; the path to the socket file
[supervisord]
logfile=/home/ubuntu/supervisord/supervisord.log ; main log file; default $CWD/supervisord.log
pidfile=/home/ubuntu/supervisord/supervisord.pid ; supervisord pidfile; default supervisord.pid
[supervisorctl]
serverurl=unix:///home/ubuntu/supervisord/supervisor.sock ; use a unix:// URL  for a unix socket
[include]
files = /home/ubuntu/supervisord/conf/*.conf
```
	- 基本需要修改的就是上面3个文件的目录
- 管理程序配置文件
	- 可以把程序的配置内容也写到`supervisord.conf`中，但那样会让这个文件不好维护，所以建议修改`include`标签
```supervisord.conf
[include]
files = /home/ubuntu/supervisord/conf/*.conf
```
	- 上面配置的意思是说自动导入再`conf`目录下的`.conf`文件，这样可以为每个程序单独定义一个配置文件，就像nginx那样
- 配置程序
	- 下面是一个django的配置内容
```django.conf
# 程序的名字，supervisor可以通过这个名字来管理程序
[program:study2]
# 指定运行用户，如果不指定用户，可能会出行没权限的告警，多出现于通过socket文件来通信
user = ubuntu
# 启动程序的命令
command=/home/ubuntu/Code/Python/virtual/py3env/bin/uwsgi --ini uwsgi.ini
# 项目的目录
directory = /home/ubuntu/Github/python_study/django/study2
# 开始的时候等待多少秒
startsecs = 0
# 停止的时候等待多少秒
stopwaitsecs = 0
# 设置该程序随着supervisor启动而启动
autorstart= true
# 程序挂了，是否需要自动拉起
autorestart = true
# 是否将程序错误信心重定向到文件
redirect_stderr = true
# 输出日志到文件
stdout_logfile = /home/ubuntu/Github/python_study/django/study2/logs/study2.log
# 输出错误到文件
stderr_logfile = /home/ubuntu/Github/python_study/django/study2/logs/study2.err
[supervisord]
# log级别
loglevel = info
```

## 管理程序

- 
- `supervisord -c /home/ubuntu/supervisord/supervisord.conf` 加载配置文件启动supervisor进程,启动服务器端就可以再客户端中对管理的程序进行操作
- `supervisorctl -c /home/ubuntu/supervisord/supervisord.conf` 进入客户端界面
	- status 
	- start app
	- stop app
	- restart app/all
- `supervisorctl`命令的操作必须加载配置文件
- 如果正好再`/home/ubuntu/supervisord/supervisord.conf`这个目录，可以不用加载，
- 可以给该文件制作快捷命令
- `alias superv='supervisorctl -c /home/ubuntu/supervisord/supervisord.conf`
- `superv status` 这样就可以使用这个短命令来管理程序了。

## 总结

- 上面就是关于这个工具的总结，之后也是可以深入了解

## 参考

- [supervisord和djando配置教程](https://www.jianshu.com/p/23762bd086e1)
