---
title: command
date: 2020-04-16 09:27:00
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# command

## 概要

- 之前判断一个命令是否存在是通过`which`来判断的，但这个是一个工具，需要单独安装`yum install which`
- 现在使用command来做这个操作

## 使用

- `command -v yum` `/usr/bin/yum` 
- 之前对于which的理解读取path定义的路径查找可执行文件，其实它还会去查找`alias`定义的别名
- `command`也会去查找别名
- 现在使用command替换which

## 问题

- 如果现在把`yum remove zip`卸载掉zip，然后通过`command -v zip` `/usr/bin/zip`发现还是给出了路径，猜测是通过查询数据库，不是实时搜索的

## 参考

