---
title: install
date: 2020-03-09 16:04:25
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# install

## 概要

- go语言是通过二进制方式安装的

## 安装

- amd64位架构
	- `wget https://studygolang.com/dl/golang/go1.14.linux-amd64.tar.gz`
- armv6l
	- `wget https://studygolang.com/dl/golang/go1.14.linux-armv6l.tar.gz`
- `sudo tar -xcvf go1.14.linux-amd64.tar.gz -C /usr/local`
- `mkdir -p ~/GoLang/{src,bin,pkg}`
- `vi ~/.bashrc`
```~/.bashrc
# go config
export GOPATH=/home/ubuntu/GoLang
export PATH=$PATH:/usr/local/go/bin
export GOPROXY=https://goproxy.cn
export GO111MODULE=auto
```
- `source ~/.bashrc`
- `go version` 查看go的版本
- `go env` 查看go的环境变量

## 系统发行版

- `sudo apt install golang-go` 这样会自动安装go以及依赖,但是安装版本太低,1.10,现在都是1.14了.

## 参考

