---
title: puts
date: 2019-04-13 16:26:55	
modify: 
tag: [puts]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# puts

## 概述
- 给屏幕打印字符串
- 参数可以是单个字符串
- 也可以是通过空格符分隔的多个字符串
- 多个字符串可以写在一行，也可以回车写成多行，
- 读取的时候全部在一行展示

## 范例
```c
#include<stdio.h>
int main()
{
    puts(
            "hello world"
            "wmsj100"
            "what is your name!"
            );
    puts("aaa" "bbb" "ccc");
    return 0;

}
```

## 参考
- [puts](http://c.biancheng.net/cpp/html/2892.html)
