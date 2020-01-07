---
title: 树莓派安装node和npm
date: 2020-01-07 13:44:59
modify: 
tags: [Notes]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# 树莓派安装node和npm

## 概要

- 树莓派配置好apt源之后如果要使用node，直接通过`sudo apt install nodejs`这样安装的node版本太低，看版本只有`v8`，这个版本还没有集成`npm`，所以无法直接使用npm，但又不知道该怎么安装。
- 树莓派本身是基于arm架构的，还得选择适合自己架构的安装包进行安装。
- 所以网上找了一个比较靠谱的方法

## 安装流程

- `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash` 安装`nvm`
	- `nvm`: macos上开发的一个用来管理node版本的集成工具，可以同时安装多个版本的nodejs
- `source ~/.bashrc`
- `nvm --version` 查看版本0.33.11
- `nvm ls-remote` 查看远端nodejs的版本，默认是最新版本再最下面，找到最新的·LTS版本安装
- `nvm install v12.14.0` 当前最新的版本安装
- `node -v` v12.14.0
- `npm -v` 6.13.4

## 安装cnpm

- `npm install -g cnpm --registry=https://registry.npm.taobao.org` 安装淘宝镜像

## 参考

- [树莓派安装nodejs和npm](https://www.jianshu.com/p/66a8de714c85)
