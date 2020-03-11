---
title: submodule
date: 2020-03-11 21:17:13
modify: 
tags: [Notes]
categories: Git
author: wmsj100
email: wmsj100@hotmail.com
---

# submodule

## 概要

- 使用这个是想要在本地配置vim的环境`YouCompleteMe`插件时候发现需要下载很多
- 主软件包可以在码云上面加速下载,但是它里面包含了数十个子仓库,每次都是执行安装程序,然后自动触发报错,找到报错开始安装
- 原来git本来就支持这种父子项目

## 概念解释

- `git submodule`是一个很好的多项目使用共同类的工具,他允许库项目作为repository,子项目作为一个单独的git项目存在于父项目中,子项目可以有自己独立的commit/push/pull
- 父项目以`submodule`的形式包含子项目
- 父项目可以指定子项目header,提交时候会包含submodule信息
- 克隆父项目时候时候可以把submodule初始化

## 项目中添加submodule

- `git submodule add git@github.com:wmsj100/test1.git`

## 操作

- 在当前项目添加依赖项目
- `git submodule add 

## 参考

