---
title: decompile3
date: 2020-11-20 10:40:22
modify: 
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# decompile3

## 概要

- `py`文件可以编译为`pyc`文件，同时也可以反过来执行这个流程
- 这个过程可以借助于`decompyle`来实现

## 使用

- `git clone https://github.com/rocky/python-decompile3.git`
- `pip install -e .`
- `decompyle3 xxx.pyc` 这样就可以输出编译前的文件内容
- 这样操作的前提是`pyc`文件和当前的python版本一致，至少大版本是一致的，

## 总结

- 如果`pyc`文件是`py36`编译的，这样的文件是无法通过`decompyle3`来反编译的

## 参考

- [decompyle3](https://github.com/rocky/python-decompile3)
