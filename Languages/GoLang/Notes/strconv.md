---
title: strconv
date: 2020-03-13 20:11:59
modify: 
tags: [Notes]
categories: GoLang
author: wmsj100
email: wmsj100@hotmail.com
---

# strconv

## 概要

- 这个包主要用来执行go的数值转换

## 常用方法

- `strconv.Itoa` 把int转换为字符串
- `strconv.Atoi` 把字符串转换为int
- `Parse`系列函数都有俩个返回值,所以需要俩个变量来接收
	- `strconv.ParseBool` 字符串转换为布尔值,只能接受`1/0/t/f/T/F/true/false/True/False/TRUE/FALSE/`其他值都返回错误
	- `strconv.ParseInt(str, base, bitSize)` 字符串转换为int,
		- base: 指定进制,如果base是0,会从字符串前缀判断,0x:16, 0: 8, 否则是10进制
		- bitSize: 指定结果必须能无溢出赋值的整数类型,0/8/16/32/64分别代表int/int8/int16/int32/int64
	- `strconv.ParseUnit(str, base , bitSize)`
	- `strconv.ParseFload(str, bitSize)`
- `Format`系列函数实现了给定数据格式转换为字符串功能
	- `strconv.FormatBool(true)` 'true'
	- `strconv.FormatInt(i int64, base int)` 把int64的数值转换为对应进制base的字符串
		- i值必须为int64格式
		- base: 2/8/16
	- `strconv.FormatUnit(i uint64, base)` 把uint64位数值转换为base字符村
	- `strconv.FormatFloat(i float64, fmt byte, prec, bitSize int)string`
		- i 必须是float64
		- fmt f/b/e/E, g表示指数很大时用e,否则f
		- prec: 控制小数精度
		- base 

## 参考

