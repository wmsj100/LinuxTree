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

## 包

- Go语言以包作为管理单位,每个Go源文件必须想声明它所属的包,所以每个go源文件的开头都是一个package的声明
- Go语言的包和文件夹是一一对应的,
	- 一个目下的同级文件属于一个包
	- 包名可以与其目录名不同
	- main包是Go语言程序的入口包,一个Go语言必须有且仅有一个main包.
	- 如果一个程序没有main包,编译时候会出错,无法生成可执行文件.

## import

- 用于导入程序依赖的包,导入的包名使用双引号包裹
- 如果需要导入多个包,需要用括号包裹,且每个包占用一行
```go
import (
	"name1"
	"name2"
)
```

## main函数

- Go语言的入口函数,即程序启动后运行的第一个函数
- main函数只能声明在main包中,不能声明在其他包中
- 一个main包也必须有且仅有一个main函数.

## go build

- 将Go语言程序代码编译成二进制可执行文件

## go run

- 会在编译后直接运行Go语言程序,编译过程中会产生一个临时文件,但不会生成可执行文件夹适合调试程序

## 参考

- [go 编译](http://c.biancheng.net/view/6046.html)