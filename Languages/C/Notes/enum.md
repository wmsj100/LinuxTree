---
title: 枚举
date: 2019-04-23 22:28:08	
modify: 
tag: [enum]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 枚举

## 概述
- `enum` 定义枚举类型
- enum week{Mon, Tues, Wed, Thurs, Fri, Sat, Sun};
- 枚举默认值从`0`开始
- enum week{ Mon = 1, Tues = 2, Wed = 3, Thurs = 4, Fri = 5, Sat = 6, Sun = 7 };
- enum week{ Mon = 1, Tues, Wed, Thurs, Fri, Sat, Sun };

## 注意
- 枚举列表中的`Mon/Tues`等这些变量是全局的，不能再定义相同名字的变量
- Mon/Tues等都是常量，不能对它们赋值，只能将他们的值赋给其它变量

## 总结
- 枚举和宏很类似，宏在预处理阶段将名字替换为对应的值
- 枚举在编译阶段将名字替换成对应的值
- 正因为在编译阶段会被替换成真正对应的数值，所以枚举的变量在内存中不占用空间，
- 所以不能通过`&`获取地址。
- 这就是枚举的本质
- 所以在switch的case中可以使用枚举的值，
- 在编译阶段`Mon`会被替换成`1`...

## 范例
```c
#include<stdio.h>

int main()
{

    enum week{Mon=1, Tues, Wed, Thurs, Fri, Sat, Sun};
    int num=0;
    scanf("%d", &num);
    switch(num)
    {
        case Mon:
            puts("Monday");
            break;
        case Tues:
            puts("Tuesday");
            break;
        case Thurs:
            puts("Thusday");
            break;
        case Wed:
            puts("Wednesday");
            break;
        case Fri:
            puts("Friday");
            break;
        case Sat:
            puts("Saturday");
            break;
        case Sun:
            puts("Sunday");
            break;
        default:
            puts("the num is error");
            break;
    }
    return 0;
}
```

## 参考
- [枚举](http://c.biancheng.net/cpp/html/99.html)
