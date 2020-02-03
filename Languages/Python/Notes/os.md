---
title: os
date: 2020-02-03 11:38:23
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# os

## 概要

- os是python标准库中的一个用于访问操作系统功能的模块
- 通用操作：
	- 获取平台信息
	- 对目录操作
	- 判断操作

## 获取平台信息

- `os.sep`: 获取平台的分隔符
- `os.name`: 指示正在使用的工作平台
- `os.getenv('path')` 获取环境变量
- `os.getcwd()` 获取当前路径

## 操作目录

- `os.listdir()` 返回指定目录的文件或目录信息
- `os.mkdir()` 创建一个目录，
- `os.rmdir()` 删除一个目录
- `os.makedirs()` 可以创建嵌套的目录层级
- `os.removedirs()` 可以删除嵌套的目录层级
- `os.chdir()` 改变工作目录
- `os.rename()` 重命名目录或文件

## 判断操作 path

> 判断操作是在path模块

- `os.path.exists(path)` 判断文件或目录是否存在
- `os.path.isfile(path)` 判断是否为文件
- `os.path.isdir(path)` 判断是否为目录
- `os.path.basename(path)` 返回文件名
- `os.path.dirname(path)` 返回目录名
- `os.path.getsize(name)` 获取文件的size，字节单位
- `os.path.abspath(name)` 获取绝对路径
- `os.path.join(path, name)` 连接目录或文件，按照目录分隔符

## 参考

- [python的os模块](https://blog.csdn.net/xxlovesht/article/details/80913193)
