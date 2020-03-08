---
title: Dockerfile
date: 2020-03-08 15:18:46
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# Dockerfile

## 概要

- 是构建docker镜像的依据

## 命令

- FROM: 制定基础镜像,必须是第一个命令,如果不以任何镜像为基础,写`FROM scratch`
- MAINTAINER: 维护者姓名
- ENV: 为容器设定环境变量
- ADD: 复制,把文件复制到镜像中,Dockfile所在目录为根目录,
	- `ADD src /src` 若src是一个目录,只会拷贝src目录的内容,目录名称不会拷贝
- COPY: 和ADD类似,只能拷贝本地文件,
- VOLUME: 挂载功能,将本地目录或者其他容器内的目录挂载到这个容器中,一般挂载数据文件
	- `VOLUME /var/log /data`
- USER: 设置容器的用户,如果设置了用户,那么RUN/CMD/ENTERPOINT都会以这个用户去执行
- WORKDIR: 指定工作目录,以后各层的当前目录就被改为指定目录,如果该目录不存在,就会创建
- EXPOSE: 声明端口,暴露容器运行时的监听端口为外部
	- 运行时候并不会因为这个声明应用就会开启这个端口的服务,
	- 为了帮助镜像使用者理解这个镜像服务的守护端口,以方便映射
	- 运行时可以通过-p进行端口映射
- RUN: 运行指定的命令,书写时候换行符是"\",多个命令要用"&&"连接
- CMD: 容器启动时候要运行的命令,只能写一个,只可以使用双引号,
	- RUN是在构建容器时就运行的命令
	- CMD是容器启动后执行的命令,在构建时候不运行
- ENTRYPOINT: 启动时候的默认命令,不可被run提供参数覆盖
- ARG: 构建参数
- ONBUILD: 后面的指令只有在以当前镜像为基础镜像镜像构建时候才会触发
- STOPSIGNAL: 容器退出时给系统发送的指令.
- HEALTHCHECK: 容器健康状况检查

## 参考

- [docker dockfile命令解析](https://www.cnblogs.com/aresxin/p/Dockfile-ji-ben-yu-fa.html)
