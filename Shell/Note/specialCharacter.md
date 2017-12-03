---
title: 特殊字符
date: Sun 03 Dec 2017 07:17:47 PM CST
tag: [Shell]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 符号
- # 注释， “#!除外，它用于指定当前脚本的解释器”
- ; 命令分隔符，可以在同一行写俩个或俩个以上的命令
	- 实例
	'''bash
	#!/bin/bash
	echo hello; echo there
	filename=ttt.sh
	if [ -e "$filename" ]; then
		echo "File $filename exists."; cp $filename $filename.bak
	else
		echo "File $filename not found."; touch $filename
	fi; echo "File test complete."
	'''
- ;; 双分号，终止'case'选项
	- 实例
	'''bash
	#!/bin/bash
	varname=b

	case "$varname" in
		[a-z]) echo "abc";;
		[0-9]) echo "123";;
	esac
	'''
- . 等价于source 用于在当前bash环境下读取并执行目标脚本的命令。
- 引号，区分单引号和双引号
	- 单引号，会阻止解释所有的特殊字符，包括变量； echo '$name' >> '$name'
	- 双引号， 会阻止大部分的特殊字符，但变量可以被执行。 echo "$name" >> 'wmsj100'
- / 文件名路径分隔符
- \ 反斜线，一种对单字符的引用机制
	- \n 表示新的一行
	- \r 回车
	- \t 水平制表符
	- \v 垂直制表符
	- \b 后退符
- ` 反引号 命令替换，反引号中的命令会优先执行
	- cp `mkdir test` test.sh test;
	- 先创建'test'目录，然后复制'test.sh'到'test’目录
- : 冒号
	- 空命令，等价于'true'，退出码是'0'
		- while : == while true
		- 可以在if/then中作占位符
		- if [ $val -gt 0 ] then :
	- 变量扩展
		- 在与'>'重定向操作符结合使用时，将会把一个文件清空，但是并不会修改这个文件的权限，如果这个文件之前不存在，那么会创建这个文件。
- ? 三元操作符
	'''bash
	#!/bin/bash
	a=10
	(( t=a<50?8:9 ))
	echo $t // 8
	'''
- $ 变量替换，可以读取变量值
		- : > test.sh 

