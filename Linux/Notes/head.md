---
title: head
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---
# head 显示文档头部

- q 隐藏文件名
- v 显示文件名
- c 显示字节数
- n 显示行数

- head -n 5 xxx.log  显示前5行
- head -n 5 xxx.log aaa.log 显示俩个文件的前5行
- head -n -5 xxx.log 显示文件除了最后5行的内容
