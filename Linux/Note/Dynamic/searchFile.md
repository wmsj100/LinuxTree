---
title: 搜索文件
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 搜索文件

## which
- which 在PATH路径内搜索可执行文件，它一般用来确认系统中是否安装了某个软件
- which 是Shell内建的一个命令，通常用which来确定时候安装了某个软件，因为它只从PATH指定的路径中去搜索命令；
	- which gcc ; which cd 一般都在 /usr/bin/ 目录中

## whereis 
- whereis 搜索数据库中，快速 ,和which类似，都是找寻二进制，但会找到man帮助文档

- locate 通过/var/lib/mlocate/mlocate.db 数据库查找，这个数据库是使用定时任务每天自动执行updatedb命令来更新一次，所以如果是刚刚添加的文件，需要手动执行一次updatedb. 这个查询可以用通配符。  locate /home/wmsj100/Documents/git/*.jpeg
	- b 定位可执行文件
	- m 定位帮助文件
	- s 定位源代码文件
	- u 搜索默认路径下除可执行文件/源代码文件/帮助文件之外的其他文件
	- B 指定搜索可执行文件的路径
	- M 指定搜索帮助文件的路径
	- S 指定搜索源代码文件的路径

## locate 
- 和whereis 命令类似，且使用相同的数据库，whereis只可以搜索可执行文件/帮助文件/源代码文件，但是locate可以搜索更全面的文件
- locate /etc/sh 搜索etc目录下以sh开头的文件
- locate /etc/*msj10* 搜索etc目录下包含msj10的所有文件

## find
- find 最强大的搜索命令，它会直接搜索硬盘，通过文件类型/文件名/时间戳/文件权限进行搜索。  find /home/wmsj100 -name hello*  

## 时间相关的命令参数
- -atime 最后访问时间
- ctime 最后修改文件内容的时间
- mtime 最后修改文件属性的时间
- mtime n : n为数字，表示n天之前一天之内修改的文件
- mtime +n: 列出n天之前（不包括n天本身）被修改过的文件
- mtime -n: 列出n天之内（不包括n天本身）被修改过的文件
- newer file: file为一个已存在的文件，列出比file还要新的文件 


- summary:
	介绍了文件的查找命令whereis 查找具体的文件名，查找数据库，快速简单； locate 查找数据库，可以配额通配符 locate /home *.jpg; which 查找PATH路径下的可执行文件； find是查找磁盘，速度最慢但是最强大。
