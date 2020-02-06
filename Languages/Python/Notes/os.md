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

## 系统

- `os.system(command)` 函数用来运行shell命令
	- `os.system("ping -c 1 google.com")` ping谷歌
- `os.sep` 获取操作系统特定路径分隔符
- `os.environ` 获取系统环境变量

## 操作目录

- `os.listdir()` 返回指定目录的文件或目录信息
- `os.mkdir()` 创建一个目录，
- `os.rmdir()` 删除一个目录
- `os.makedirs()` 可以创建嵌套的目录层级
- `os.removedirs()` 可以删除嵌套的目录层级
- `os.chdir()` 改变工作目录
- `os.rename()` 重命名目录或文件

- `os.walk(dirname)` 便利文件夹下的所有文件，返回三个参数: root: 当前便利目录；dir: 当前目录下的文件夹；files: 当前目录下的文件
```python
for root, dirs, files in os.walk('.'):
	print('root is ',root)
	print('dirs is ',dirs)
	print('files is ', files)
# root is  .
# dirs is  ['dir1']
# files is  ['DSC_0970.JPG', 'file1.py', 'test.txt', 'test1.py']
# root is  .\dir1
# dirs is  ['a']
# files is  []
# root is  .\dir1\a
# dirs is  ['bdir']
# files is  []
# root is  .\dir1\a\bdir
# dirs is  ['c']
# files is  []
# root is  .\dir1\a\bdir\c
# dirs is  ['d']
# files is  []
# root is  .\dir1\a\bdir\c\d
# dirs is  []
# files is  []
```

## 参考

- [python的os模块](https://blog.csdn.net/xxlovesht/article/details/80913193)
