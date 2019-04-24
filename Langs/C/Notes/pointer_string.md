---
title: 字符串指针
date: 2019-04-21 16:31:52	
modify: 
tag: [string,pointer,c]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符串指针

## 概述
- 字符串中的所有字符在内存中是连续排列的，
- str指向字符串的首地址
- 有俩种表示字符串的方式
	- char str[10]="wmsj100.com" 字符数组形式，字符值可以修改，存储在全局数据区或栈区
	-` char *str="wmsj100.com"` 字符串常量，字符值不可修改，存储在常量区

## 遍历
- `str[i] == *(p+i) == p[i]`

## 取值
- `(str+1)[5]` 表示以`str+1`为起点，先后偏移5个字符，等价于`str[6]`

## 字符串数组
- 有俩种表示方法
- `char str[5][20]={....}` 这样的表示方法每个字符串都要占用20个字节，比较浪费空间
- `char *str[]={...}` 每个元素都是一个指针，指向每个字符串的首地址，比较节省内存空间

## 范例
```c
#include<stdio.h>
#include<string.h>

int main()
{
    char *str="wmsj100.com";
    char *p = str;
    int len=strlen(str);
    for(int i=0;i<len;i++){
        printf("%c %c %c\n", str[i], *(p+i), p[i]);
    }
    return 0;
}
```

## 参考
- [字符串指针](http://c.biancheng.net/cpp/html/80.html)
