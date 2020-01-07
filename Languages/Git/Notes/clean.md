---
title: clean 
date: 2018-06-29 23:13:22	
modify: 
tag: [clean]
categories: Git 
author: wmsj100
mail: wmsj100@hotmail.com
---

# clean

## 概述
- 怎么处理本地的没有跟踪的文件
- 怎么处理本地修改的但是不想通过`git checkout --file ..`这样一个一个撤销操作
- 这时候就可以通过`clean`命令来处理

## 使用
- `git clean -f` 强制删除本地所有文件,不包括文件夹
- `git clean -fd` 强制删除本地所有文件,包括文件夹

## 参考
- []()
