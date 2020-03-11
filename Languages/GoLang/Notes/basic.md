---
title: basic
date: 2020-03-11 16:45:37
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- go的基础知识

## 源文件

- 命令源文件: 如果一个Go源文件被声明属于main包,并且该文件中包含main函数,则它就是命令源文件.
	- 命令源文件属于程序入口,可以通过Go语言的`go run`命令运行或者通过`go build`命令生成可执行文件
- 库源文件: 库源文件指存在于某个包中的普通源文件,并且库源文件不包含main函数
- 不管是命令源文件还是库源文件,在同一个目录下的所有源文件,其所属包的名称必须一致.

## 参考

