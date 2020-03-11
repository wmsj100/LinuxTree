---
title: go项目的结构
date: 2020-03-11 16:37:18
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# go项目的结构

## 概要

- 说明go项目的目录结构

## 目录说明

- src目录: 用于以包的形式组织并存放Go源文件,这里的包与src下的每个子目录是一一对应.
	- 通常通过`go get`命令获取的库源文件下载到src目录下对应的文件夹中
- pkg: 用于存放通过`go install`命令安装某个包后的归档文件.
	- 归档文件是指那些名称以`.a`结尾的文件
	- 该目录与`GOROOT`目录下的pkg目录功能类似,区别在于这里的pkg目录专门用来存放项目代码的归档文件
	- 编译和安装项目代码的过程一般会以代码包为单位进行,比如log包被编译安装后,将生成一个名为`log.a`的归档文件,并存放在当前项目的`pkg`目录下
- bin: 通过`go install`命令安装后,保存有Go命令源文件生成的可执行文件.

## 参考

- [go 工程结构说明](http://c.biancheng.net/view/4773.html)
