---
title: npm
date: 2019-10-10 10:45:33 Thursday
modify:
tag: [npm]
categories: Nodejs
author: wmsj100
mail: wmsj100@hotmail.com
---

# npm

## 概述
- sudo apt install npm
- sudo npm install -g npm 升级npm
- npm install -g cnpm --registry=https://registry.npm.taobao.org  安装cnpm
- npm cache clean --force清除缓存

## 安装新版本node

- npm update -g
- npm install -g n 
- n latest

## npm install error

- 这几天一直弄node都是失败的，npm无法安装成功，其实就是方法错误，不是虚拟机本身有什么限制。
- 先升级node，按照上面的方法
- 安装cnpm
- sudo cnpm install -g vue 所有的资源都按照这样安装。

## 参考

- [安装新版包nodejs](https://cloud.tencent.com/developer/article/1436906)
