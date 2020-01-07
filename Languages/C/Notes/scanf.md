---
title: scanf
date: 2019-04-20 22:39:05	
modify: 
tag: [scanf]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# scanf

## 概述
- 格式化输入，
- 从输入缓冲中获取数据，
- 多个数据之间使用空格来分隔，
- 如果一个数据格式匹配失败，不会跳过，当前匹配数据保持原值不变
- 多个scanf可以通过一次性输入来完成执行
- scanf读取数据时候需要的是数据地址，int/char/float等需要在前面添加`&`，字符串和数组都不需要，他们本身就会转换为地址。
- scanf函数评价不高，
	- 首先具体实现都有漏洞
	- 使用不够灵活
	- 编写的代码不易看出究竟在解析什么
- 所以应该尝试使用`fread/fgets`获取输入行

## 范例
- 对于数字/字符/布尔值等赋值操作需要通过`&`来获取值对应的内存地址
- 通过修改内存地址对应的值可以达到修改值的效果
- 这个相当于指针的操作
- 对应字符串和数组不需要使用`&`，因为本来就是内存地址
- scanf("%d", &intV);
- scanf("%s", str);

## 注意
- scanf接受字符串时候，字符串不能有空格，因为通过空格用来做间隔符，指多个值，
- scanf特殊符号

## 高级语法
- scanf("%[\n]", str) 匹配字符串到换行符为止
- scanf("%9s", str) 匹配字符串长度为9
- scanf("%[a-zA-Z0-9]", str) 匹配大小写字母数字
- scanf("%[^0-9]", str) 不匹配数字，就是匹配字符串到数字为止
- scanf("%*[^\n]");scanf("%*c"); 清空缓冲区内容，`*`表示将读取到的值直接丢弃

## 参考
- [scanf](http://c.biancheng.net/cpp/html/3425.html)
- [scanf的高级用法](http://c.biancheng.net/cpp/html/3427.html)
