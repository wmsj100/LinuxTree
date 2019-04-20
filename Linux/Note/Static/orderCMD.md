---
title: 命令执行顺序
date: Tue 20 Feb 2018 07:48:05 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 系统内部有多个ls的命令，那么执行`ls`命令时候，到底触发的是哪个？
- 命令的执行顺序如下：
    - 以相对路径或绝对路径执行的命令， /bin/ls ./ls 
    - 由alias找到该命令来执行
    - 由bash内置的（buitin）命令来执行
    - 通过$PATH这个变量的顺序找到的第一个命令来执行
- 所以‘ls’其实是由alias定义的命令
- type -a ls 可以查看ls的定义位置
