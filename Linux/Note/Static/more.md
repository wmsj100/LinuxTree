---
title: more
date: Mon 19 Feb 2018 09:29:02 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---
 more 一页一页显示内容

- +n 从第n行开始
- -n 定义最开始的屏幕大小为n行
- +/pattern 在每个档案显示前搜寻该字符串（pattern），然后从该字符串前俩行之后开始显示
- c 从顶部清屏，然后显示

- 在more界面可以执行的操作
	- = 输出当前的行号
	- q 推出more
	- 空格键 向下滚动一屏
	- b 返回上一屏

- ll ./ | more -5 搭配more来展示文件内容
