----
title: ln
date: Mon 19 Feb 2018 09:29:02 AM CST
modify: 2020-03-10 16:05:06 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# ln

## 概览

- ln -s /var/tmp   ./tmp   在当前目录内创建一个快捷方式，指向/var/tmp
- ln  是创建软连接的意思。
- 虽然软连接指向的是一个目录，但是通过 rmdir 来删除软连接会报错，所以知道软连接本身是一个连接文件，

## 想法

- 安装vim之后,无法使用vi来调用vim,想到一个折中的方法是
- `vi /etc/bash.bashrc`
- `alias vi='vim'
- 这样可以实现那样的功能,但是感觉很可笑,明明就是一个可执行命令,最好的方式是ln
- `cd /usr/local/bin`
- `ln -s /usr/bin/vim vi`
