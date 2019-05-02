---
title: source or .
date: 2019-05-02 09:18:01	
modify: 
tag: [source,dot]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# source or .

## 概述
- 通常在shell中执行外部命令或脚本程序，会创建一个新的环境(一个子shell)，
- 命令将在这个新环境中执行，命令执行完毕后，环境就丢弃，留下退出码给父Shell
- 所以在子shell中对父shell做出的任何修改都会丢失
- `source` or `.`在执行脚本程序时，使用的是调用该脚本程序的同一个shell，即父shell
- 所以通过脚本引入的变量或者对父shell做出的修改都会保留

## 参考
- []()
