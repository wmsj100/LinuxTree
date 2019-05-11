---
title: sscanf
date: 2019-04-23 20:34:37	
modify: 2019-05-11 19:01:08 Saturday
tag: [sscanf,func,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# sscanf

## 概述
- 将参数str字符串根据参数format字符串来转换格式化数据，转换后的结果存于对应的参数内
- scanf默认是从标准输入获取数据，而sscanf是从前面的字符串参数中解析并获取数据

## 范例
- 格式化获取数据
```c
#include<stdio.h>

int main()
{
    int a,b,c;
    char *str="+CBC: 0,90,4090";
    sscanf(str, "+CBC: %d,%d,%d",&a, &b, &c);
    printf("%d, %d, %d", a,b,c);
    return 0;
}
```
- 截取字符串长度
```c
#include<stdio.h>

int main()
{
    char s1[10];
    char *str="abcdefghijk";
    sscanf(str, "%6s", s1);
    printf("%s", s1);
    return 0;
}
```
- 截取字符串到空格
```c
#include<stdio.h>

int main()
{
    char str[10];
    char *s1="hello world";
    sscanf(s1, "%[^ ]", str);
    printf("%s", str);

    return 0;
}
```
- 包含指定字符集
```c
#include<stdio.h>

int main()
{

    char str[10];
    char *s="123456aAbBcCdDeEfF";
    char *s1="123456abcdefABCDEF";
    sscanf(s, "%[0-9a-z]", str);
    printf("%s\n", str);
    sscanf(s1, "%[0-9a-z]", str);
    printf("%s\n", str);
    return 0;
}
```
- 获取指定字符之间的内容
```c
int main()
{

    char str[20];
    char *s="lios/hello world@122";
    sscanf(s, "%*[^/]/%[^@]",str);
    printf("%s", str);
    return 0;
}
```


## 参考
- [sscanf笔记](https://www.cnblogs.com/yangguang-it/p/7414242.html)
