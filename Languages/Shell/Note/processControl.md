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
    ```sh
	for loop in item1 item2 ... itemn
	  do
		echo "the value is: $loop"
	  done
    ```
- while 
	```sh
	#!/bin/bash
	int=1
	while (( $int <=5 ))
	do
		echo $int
		let "int++"
	done
	```
	- let 变量不需要添加“$”
- until 循环执行一系列命令，直至条件为真停止。一般while循环优于until。
	```sh
	do
		command
	done
	```
- case 
	- 取值后面必须为单词in，每一模式必须以有括号结束，取值可以为变量或常数。
	- 每一模式以`;;`结束
- break; continue 跳出循环
	- break 跳出循环，循环结束
	- continue 跳过当前循环，执行下一次循环
