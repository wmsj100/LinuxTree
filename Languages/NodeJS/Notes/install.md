---
title: install
date: 2020-02-07 10:35:11
modify: 
tags: [Notes]
categories: NodeJS
author: wmsj100
email: wmsj100@hotmail.com
---

# 安装nodejs

## 概要

- node是一个前后端的框架

## 安装流程

- 简单总结就是在官网下载软件源代码
- 解压并把bin目录添加到path，然后`source ~/.bashrc`
- wget https://npm.taobao.org/mirrors/node/v8.9.0/node-v8.9.0-linux-x64.tar.gz
- mv ~/Downloads/node-v8.9.0-linux-x64.tar.gz /usr/local
- sudo tar zxvf node-v8.9.0-linux-x64.tar.gz
- mv node-v8.9.0-linux-x64.tar.gz node
- 配置环境变量
- vim /etc/profile 再最后面添加：
	- # set for nodejs
	- export NODE_HOME=/usr/local/node
	- export PATH=$NODE_HOME/bin:$PATH
- 保存退出后执行更改生效 source /etc/profile
- node -v 查看node的版本号

## 安装cnpm

- `npm install -g cnpm --registry=https://registry.npm.taobao.org`

## 参考

- [centos7 安装nodejs](http://blog.csdn.net/jonatha_n/article/details/75271050)
