---
title: sys_stdin
date: 2020-03-23 10:07:44
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# sys_stdin

## 概要

- 这个是做华为的面试题时候出现的东西,之前没有碰到过,
- 我那天看到这个就整个都蒙了,本来对于sys模块的就不熟悉,
- 我下意识对它的理解类似`sys.argv`用来获取控制台输入行的参数,刚刚看一下发现不是这样的.
- 它和`input`类似,用来获取用户控制台输入的
- 为什么对这个模块不熟悉,因为好多命令是交互式的,因为在实际项目中是没有交互式的,所以没有去练习

## stdin.readline

- 获取一行的输入,全部当作字符串来处理
- `name = sys.stdin.readline().strip()` 获取用户输入,并且去掉前后空格

## stdin.readlines

- 可以进行多行输入,需要通过ctrl d来退出,全部当作字符串列表来处理
- `name = sys.stdin.readlins()` `['adfwe asdf\n', 'lll\n', '\n']`

## 参考

- [python stdin](https://blog.csdn.net/CAU_Ayao/article/details/81985103)
