---
title: python版本升级
date: 2018-04-29 11:11:43 Sun
modify: 2018-04-29 11:11:43 Sun
tag: [python]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# Python 升级

## 目标
- 系统使用`centOS`，系统默认安装的是`python2.7`，
- 为了使用`Django`，需要使用`python3`，

## 操作
- `yum remove python`
- sudo `yum remove python`
- sudo `yum remove python2`
- 上面这些操作都会出现一大堆的依赖，然后提示卸载失败，因为python内嵌到系统，很多组建有依赖，所以不能简单粗暴的先把旧版本卸载，
- 其实如果能想到系统运行有依赖python，那么如果卸载成功了，在新版本python没有安装的这段空白时间系统要怎么正常运行
- 所以不能卸载旧版本，而是直接安装新版本，然后把运行的`python`链接指到新版本的python

## 步骤
- tar -zxvf Python.tgz
- cd Python
- sudo ./configure
- sudo make
- sudo make install
- mv /usr/bin/python /usr/bin/python1 # 备份旧版本链接
- ln -fs /usr/local/bin/python3 /usr/bin/python # 创建新版本链接
- python -V # Python 3.6.5
