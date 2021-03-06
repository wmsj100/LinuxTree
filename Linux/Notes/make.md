---
title: make
date: 2020-03-28 22:13:20
modify: 2020-04-01 11:36:01  
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# make

## 概要

- 在软件开发中,make是一个工具程式,经由读取叫做"makefile"的文件,自动化构建软件.
- 它是一种转化文件形式的工具,转换的目标称为"target";与此同时,它也检查文件的依赖关系,如果需要的话,它会调用一些外部软件来完成任务.
- 它的依赖关系检查系统非常简单,主要根据依赖文件的修改时间进行判断.
- 大多数情况下,它被用来编译源代码,生成结果代码,然后把结果代码连接起来生成可执行文件或者库文件.
- 它使用叫做"makefile"的文件来确定一个target文件的依赖关系,然后把生成这个target的相关命令传给shell去执行.
- 虽然目前由众多依赖关系检查工具,但是make是应用最广泛的一个.这要归功于它被包含在Unix系统中.
- make程序已经被使用者多次重写/改写,其中包括几次用相同的文件格式和算法原理重新编写,并且依照不同需要添加了一些不常见的改良.
	- GNU make: 仿照make的标准功能(透过clean-room工程)重新改写,并加入作者觉得值得加入的新功能,常和GNU编译系统一起被使用,是大多数GNU Linux安装的一部分.
	- BSD make: 编译目标的时候由并行计算的能力.
	- Microsoft nmake: 微软的工具

## 优点和缺点

- 就像其他和make有着悠久历史的软件一样,make有着很多的拥护者和反对者.
- 它的很多问题因现代大型的软件项目的出现而暴露出来.
- 但很多人争论说它在常见的情况下可以很好的工作,而且使用非常简单,功能强大,表达清楚.
- 无论如何,make仍然被用来编译很多完整的操作系统,而且现在替代品们在基本的操作上与它没有太大的差别.

## 编译报错

- 下面是一个执行gcc编译的报错
```
checking for suffix of object files... configure: error: in `/root/Downloads/gcc-5.4.0/aarch64-unknown-linux-gnu/libgcc':
configure: error: cannot compute suffix of object files: cannot compile
See `config.log' for more details.
make[2]: *** [configure-stage1-target-libgcc] Error 1
make[2]: Leaving directory `/root/Downloads/gcc-5.4.0'
make[1]: *** [stage1-bubble] Error 2
make[1]: Leaving directory `/root/Downloads/gcc-5.4.0'
make: *** [all] Error 2
```
- 编包的报错会在每个包内部生成config.log，即可以进入/root/Downloads/gcc-5.4.0/aarch64-unknown-linux-gnu/libgcc,然后查看config.log

## 参考

- [wikipedia make](https://zh.wikipedia.org/wiki/Make)
