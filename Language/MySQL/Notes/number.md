---
title: 数值类型
date: 2019-04-09 14:03:59	
modify: 
tags: [number]
categories: MySql
---

# 数值类型

- int(m) m指的是数据的最大显示宽度，且最大有效显示宽度是255，显示宽度和存储大小或类型包含的值的范围无关。
- 如果为一个数值列指定“zerofill”，mysql将自动为该列添加“unsigned” 非负数属性，
- 数值类型的数据类型默认为“signed”， 
- serial 是别名，代表“bigint unsigned not null auto_increment unique;

- float[(m,d)] 
	- m 浮点数的总位数
	- d 小数点后面的位数
	- score float(5,1) 总位数5，小数位1
