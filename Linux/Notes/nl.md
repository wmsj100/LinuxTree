---
title: nl
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---
# nl 计算文件中行号

- number of lines
- 可以将文件内容自动加上行号
	- b 指定行号指定的方式
		- b a 表示不论是否为空行，都列出行号
		- b t 如果有空行，空的那一行不要列出行号（默认值）
	- n 列出行号的表示方法，有三种
		- n ln 行号在屏幕的最左方显示
		- n rn 行号在自己栏位的最右方显示，且不加零
		- n rz 行号在自己栏位的最右方显示，且加零
	- w 行号占用的位数

