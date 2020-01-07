---
title: switch
date: 2019-04-21 00:11:15	
modify: 
tag: [switch,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# switch

## 概述
- switch用于多条件判断，通常和if可以互换，
- case后面的值只能为整数，字符串也是整数的一种，或者结果为整数的运算表达式，
- case后面不能有变量
- default表示无法匹配到值时候执行
- case后面的条件执行完成需要添加'break'跳出判断

## case
- case后的值只能为整数类型的，
- 字符串不允许，只能是字符，字符使用单引号包裹
- case 'a' ok
- case "a" fault
- case 8+4 ok

## 范例
```c
#include "stdio.h"
#include "string.h"

int main()
{
    char score,result[30]="the valus is ";
    scanf("%c", &score);
    switch(score){
        case 'a': strcat(result,"aa"); break;
        case 'b': strcat(result,"bb"); break;
        case 'c': strcat(result,"cc"); break;
        case 'd': strcat(result,"dd"); break;
        default: strcat(result,"default"); break;

    }
    printf("%c %s", score, result);
    return 0;
}
```

## 参考
- [switch](http://c.biancheng.net/cpp/html/2911.html)
