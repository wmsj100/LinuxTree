---
title: container
date: 2020-03-03 09:03:31
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# container

## 概要

- 容器的基础命令
- 容器和虚拟机的区别是容器更小更更快更轻量级。
- `docker container run`来启动容器
- `-it`参数可以将当前终端连接到容器的shell终端上。
- 容器会随着其中运行的应用的推出而终止
- `docker version` 查看docker的daemon

## 命令

- `docker container ls` 查看正在运行的容器
- `docker container exec -it 6ee3d518b856 bash` 可以通过containerID来连接到容器环境。
- `docker container stop 6ee3d518b856` 停止容器
- `docker container stop $(docker container ls -q)` 这样可以批量停止容器
- `docker container start 6ee3d518b856` 启动容器
- `docker container ls -a` 默认只列出运行中的容器，通过这个命令可以列出所有容器
- `docker container rm 6ee3d518b856` 删除指定容器
	- 删除容器之前需要先stop容器
	- 删除镜像image之前需要先删除容器
- `docker container inspect --format='{{range .NetworkSettins.Networks}}{{.IPAddress}}{{end}}' 6ee3d518b856` 可以获取到当前机器的ip

## 创建容器

- `docker container run -it ubuntu:latest /bin/bash` 通过当前的/bin/bash来连接容器的shell终端
	- 上面这条命令的执行流程如下：
	- docker客户端会选择合适的API来调用Docker daemon
	- Docker daemon接收到命令并搜索Docker本地缓存，观察是否有命令请求的镜像
	- 如果本地没有镜像，Docker接下来就请求Docker Hub是否有对应镜像。
	- Docker找到该镜像后将镜像拉取到本地，存储到本地缓存中
	- daemon就开始创建容器并在其中运行指定的应用。
- 通过上面这样创建的容器，使得`bin/bash`称为容器中唯一运行的进程，`ps -efl`
```
root@d85a8c0d200e:/# ps -elf
F S UID        PID  PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
4 S root         1     0  0  80   0 -  4627 wait   04:42 pts/0    00:00:00 /bin/bash
0 R root        18     1  0  80   0 -  8601 -      04:49 pts/0    00:00:00 ps -elf
```
- 如果此时执行`exit`推出shell，则容器也会被销毁，因为杀死Bash Shell即杀死了容器中唯一运行的进程，导致这个容器也被杀死。
- 因为容器如果不能运行任何进程则无法存在。
- `docker container run --name myapp -it ubuntu:latest /bin/bash` 创建容器并且指定名称
- `docker container run -d --name always --restart always alpine sleep 1d` 这样创建的容器是直接在后台执行，不会进入交换模式

## 暂时退出容器

- `Ctrl p+q` 可以暂时退出容器而不关闭进程，通过`docker container ls`可以查询到刚刚的容器还在运行中
- `docker container exec -it 01ff9272cdf7 bash` 可以重新连回容器

## 数据持久化

- 容器中的数据也是可以持久化的，在docker中写入的文件会自动创建在docker的文件系统中，
- 此时关闭或者重启容器，然后查看创建的文件还是存在的，并没有丢失
- 停止容器运行并不会损毁容器或者其中的数据。
- 容器持久化存储首先卷。
- 即便将容器删除，如果容器数据存储在卷中，数据也会被保留下来。

## 容器的重启策略

- 在创建容器时候可以指定容器的重启策略，这是容器自己的自我修复方式
- `docker container run --name always -it --restart always alpine sh`
- 上面这样就会创建一个异常停止后会自动重启的容器，除非明确发出`docker container stop`指令

## 容器端口映射

- `docker container run -d --name webserver -p 8080:8080 alpine` 创建一个alpine的容器并且后台执行，把主机的8080端口映射到容器的8080端口
- `docker container run -d --name webserver1 -p 8081:8080 alpine` 创建一个alpine的容器并且后台执行，把主机的8081端口映射到容器的8080端口

## 容器默认启动的应用

- 容器启动后会执行默认命令来启动应用，这样可以简化容器的操作
- `docker image inspect test` 查看`CMD`可以看到执行的命令

## 参考

