---
title: sizeof
date: 2019-04-13 16:45:27	
modify: 
tag: [func,basic]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# sizeof

## 概述
- 获取变量占用的位数
- 调用时候有俩种方式：
	- sizeof a
	- sizeof(a)

## 范例
```c
#include<stdio.h>
int main()
{
    short a=10;
    int b=10;

    int short_length=sizeof a;
    int int_length = sizeof(b);
    int long_length=sizeof(long);
    int str_length = sizeof(char);

    printf("short=%d, int=%d, long=%d, char=%d\n", short_length, int_length, long_length, str_length);

    return 0;
}
```

## 参考
- [sizeof](http://c.biancheng.net/cpp/html/3092.html)
