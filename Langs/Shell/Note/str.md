---
title: 字符串
date: 2019-04-12 15:26:45	
modify: 
tag: [string]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符串

## 概述
- 字符串是shell里最常使用的数据类型了，除了字符串和数字，也没有其他类型好用了
- 字符串可以单引号也可以双引号
- 单引号里不能再出现单引号，即便使用转义也不行
- 双引号里可以有变量
- 双引号可以进行转义
- 拼接字符串 
	- a='adf'
	- echo "hello, $a"
- `${#str}` 获取字符串`str`的长度
	- a='asdfqwer'
	- echo ${a:3:3} # fqw 从索引3开始获取长度为3的字符串切片
- 查找子字符串
	- echo `expr index "$str" as` # 查找as在字符串str中的位置

## 参考
- [字符串](http://c.biancheng.net/cpp/view/7001.html)
