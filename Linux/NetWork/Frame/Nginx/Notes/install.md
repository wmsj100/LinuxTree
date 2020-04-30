---
title: install
date: 2020-04-30 14:27:28
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# install

## 概要

- 可以通过系统包管理器直接安装，但也可以手动安装版本

## 安装

- `yum install gcc-c++` 
- `yum install -y pcre pcre-devel` Nginx的Rewrite模块和HTTP核心模块会使用到PCRE正则表达式语法。这里需要安装两个安装包pcre和pcre-devel。第一个安装包提供编译版本的库，而第二个提供开发阶段的头文件和编译项目的源代码
- `yum install -y zlib zlib-devel` zlib库提供了开发人员的压缩算法，在Nginx的各种模块中需要使用gzip压缩
- `yum install -y openssl openssl-devel` nginx不仅支持 http协议，还支持 https（即在 ssl 协议上传输 http），如果使用了 https，需要安装 OpenSSL 库
- `wget http://nginx.org/download/nginx-1.16.1.tar.gz` 下载并解压
- `./configure` 开始配置
- `make`
- `make install` 默认安装到`/usr/local/nginx`
- `cd /usr/local/nginx/sbin`
- `./nginx` 启动服务
- `./nginx -s stop` 停止服务
- `vi /etc/rc.local`最后添加`/usr/local/nginx/sbin/nginx`
- 手动添加环境变量， 执行`nginx`来启动服务
- `nginx -t`
- `nginx -s reload`

## 参考

- [nginx install](https://blog.csdn.net/qq_42815754/article/details/82980326)
