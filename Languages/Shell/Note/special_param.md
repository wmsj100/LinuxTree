---
title: 特殊变量
date: 2019-04-12 13:26:50	
modify: 
tag: [params]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

## 特殊变量
- $$ 返回当前shell进程的ID
	- [root =:> ~]$ echo $$ #11690

- 局部变量 这种变量只有在代码块或者函数中才可见
- 环境变量
- 位置变量 从命令行传递到脚本的参数；$0, $1, $2..
	- $0 脚本文件本身的名字， $1是第一个参数，$2是第二个参数
	- $9之后的参数就必须用花括号包裹。 ${10}, ${11};
	- $# 传递到脚本的参数个数
	- $* 返回所有参数，如果用双引号包裹，以一个单字符串显示所有向脚本传递的参数。
	- $$ 脚本运行的当前进程ID号
	- $! 后台运行的最后一个进程ID号
	- $@ 返回所有参数
	- $ 与set命令功能相同
	- $? 显示最后命令的退出状态。
## 概述
- 

## 参考
- [shell特殊变量](http://c.biancheng.net/cpp/view/2739.html)
