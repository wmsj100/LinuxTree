---
title: 流程控制 
date: Mon 04 Dec 2017 11:27:30 PM CST
tag: [shell]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- else分支没有语句就不写，不能为空；
- if then; elif then; else fi;
- for循环
	- for loop in item1 item2 ... itemn
	  do
		echo "the value is: $loop"
	done
- while 
	'''bash
	#!/bin/bash
	int=1
	while (( $int <=5 ))
	do
		echo $int
		let "int++"
	done
	'''
	- let 变量不需要添加“$”
- until 循环执行一系列命令，直至条件为真停止。一般while循环优于until。
	'''bash
	do
		command
	done
	'''

