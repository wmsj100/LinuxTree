---
title: logging
date: 2019-04-10 11:09:54	
modify: 
tag: [model]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 日志

## 概述
- 日志模块也是python的标准库，通常用于输出日志

## 使用

- basicConfig: 在该函数中设置日志的具体参数来修改默认行为，拥有的参数如下：
	- level: 设置日志级别，默认是`warning`级别的，
		- debug/info/warning/error/critical 级别依次提升
		- level=logging.ERROR
	- filename='./error.log' 设置日志文件的名称
	- filemode: 文件打开方式，默认值为`a`追加，也可以用`w`覆盖写
	- datafmt: 指定日期格式
	- format: 指定handler使用的日志显示格式
		- '%(asctime)s - %(name)s - [line:%(lineno)d] - %(message)s'
- logging.basicConfig(filename='./error_emp_log.log',level=logging.INFO,format="%(asctime)s [line:%(lineno)d] %(message)s")


## 参考
- [logging解析](https://www.cnblogs.com/darkpig/p/5924820.html)
