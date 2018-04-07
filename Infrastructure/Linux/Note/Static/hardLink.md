---
title: 硬连接
date: Sat 17 Feb 2018 07:39:32 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- ln不添加参数，创建的默认就是硬连接文件，硬链接文件不会新增inode, block数量，只是在目录内新增了一个文件名，
- ln -s /etc/passwd ./passwd 创建一个软连接，这个软连接是一个单独的文件，文件的内容就是链接文件名，会新增inode,block;
- 如果删除源文件，软链接会出现打开异常，硬链接文件不会受到影响，
- 创建目录会新增目录的硬链接数量，
- 在目录内创建文件不会影响目录的硬链接数量

## 限制条件
- 硬链接不允许给目录创建
- 只有在同一个文件系统中的文件才能创建硬链接
