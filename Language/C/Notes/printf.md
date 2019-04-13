---
title: printf
date: 2019-04-13 16:49:22	
modify: 
tag: [basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# printf

## 概述

- printf: print format 格式化输出内容
	- d%: 输出十进制
	- c%: 输出一个字符
	- %s: 输出一个字符串
	- %f: 输出一个float
	- %hd: 输出short int 类型
	- %ld: 输出long int类型
- 打印时候，尤其是数值，一定要用对应的字符打印自己的数据类型，否则可能会出现数据溢出
- 对于数据溢出，编译器通常不会打印告警，因为通常编译器的告警级别设置的较高

## 范例
- 数据溢出
```c
#include<stdio.h>

int main()
{
    int m = 306587;
    printf("int num is %hd", m);

    return 0;

}
# int num is -21093
```

## 参考
- [printf](http://c.biancheng.net/cpp/html/3092.html)
