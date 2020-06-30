---
title: 基础知识 
date: 2018-07-08 16:02:16	
modify: 2020-06-30 10:28:06 
tag: [sed]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 基础知识

## 概述

- 用于批量匹配和修改行

## 常用命令

- `cat *.file | sed '/^$/d' > out.file` 删除文件的空行
- `cat *.file | sed 's/^/- &/g' > out.file` 在文件的每一行插入`- `
- `sed -i "s/wmsj100/WMSJ100/g" `grep -nrw "wmsj100" | awk -F : '{print $1}'`
- `set -i "s|\<Arch\>|ArchLinux|g" `grep -rw "Arch" | awk -F ':' '{print $1}' | sort | uniq` 修改当前目录下的所有文件,把Arch替换为ArchLinux
	- `\<` 匹配单词的开头
	- `\>` 匹配单词的结尾

## 批量插入文件

- `sed -i '3 r b.txt' a.txt` 在文件a.txt中的第3行后面插入b.txt文件，这个命令也可以适用于在批量文件中插入一个文件

## 参考

- [set常用法](https://blog.csdn.net/gua___gua/article/details/49304699)
