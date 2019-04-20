---
title: 路上学习shell
date: 2018-03-15 09:32:41 Thu
modify: 2018-03-15 09:32:41 Thu
tag: [bus,shell]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路上学习shell

## 条件判断
- 学习了关于shell的条件判断if/fi, if/elif/else/fi, case等

## 循环判断
- 学习了循环判断条件 for in, for(i=0;i<10;i++), while, utile, select;
  - 其中select比较有意思，会给列出的值按照从小到大从1开始标记，然后进行选择

## 函数
- 函数定义，使用关键字`FUNCTION`，也可以省略
  - 关于函数可以创建函数库，函数库以下划线定义
  - 在shell脚本内部引用函数库是需要使用'.'/'source'后更引用函数库的路径

## 命令
### read
- read 关于获取用户界面输入
  - read -p "input you number: " num; // 10
  - echo $num; // 10

### set 
- set可以重置参数值，

### let 
- let用于整数运算，不用输入'$'
  - a=1;b=2;
  - let "c=a+b";
  - echo $c; // 3
