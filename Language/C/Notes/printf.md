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

## 进制
- printf可以进行数值进制转换
- %d 十进制
- %o 八进制，不区分大小写
- %x 十六进制，以小写形式显示
- %X 十六进制，以大写形式显示

## 进制输出
- 默认printf只以10进制输出，即便指定了进制输出，前缀默认是不追加的，
- %#o 可以在进制字符前面添加#来显式的展示数值的进制


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

- printf 进制转换
```c
#include<stdio.h>

int main()
{
    int a = 0b101; // 这是二进制
    int b = -0B110010; // 这也是二进制
    int c = 02713; // 这是八进制
    int d = 0x1dab83; // 这是十六进制

    printf("%#o,b=%#o,c=%#o,d=%#o\n",a,b,c,d);
    printf("%#d,b=%#d,c=%#d,#d=%#d\n",a,b,c,d);
    printf("%#x,b=%#x,c=%#x,d=%#x\n",a,b,c,d);
    printf("%#X,b=%#X,c=%#X,d=%#X\n",a,b,c,d);
    return 0;

}
// 05,b=037777777716,c=02713,d=07325603
// 5,b=-50,c=1483,#d=1944451
// 0x5,b=0xffffffce,c=0x5cb,d=0x1dab83
// 0X5,b=0XFFFFFFCE,c=0X5CB,d=0X1DAB83
```

## 参考
- [printf](http://c.biancheng.net/cpp/html/3092.html)
