---
title: struct结构体
date: 2019-04-23 20:55:28	
modify: 
tag: [struct,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# struct结构体

## 概述
- 存放一组不同类型的数据
- 内部的元素被称为成员
- 结构体也是一种数据类型，也是一种数据模板，编译器不会为它分配内存
- 结构体变量才包含实实在在的数据，才需要内存存储
- `struct stc stu1, stu2;`定义结构体变量`stu1`and`stu2`;
- 结构体变量有三种定义方式:
  - 先定义结构体，然后通过结构体来定义变量
  - 定义结构体的同时定义变量
  - 没有结构体类型名称，后面直接跟变量名
- 一个结构体的成员也可以是另一个结构体，这样调用时候要使用多个点`struct1.birthday.year`
```c
struct stu
{
	char *name;
	int age;
};
```

## 结构体数组
- 数组中的每个元素都是一个结构体，
- 常用来表示一个拥有相同数据结构的群体，比如一个班的同学
- 定义结构体数组，就是在结构体后面跟数组变量
- 也可以先定义结构体，然后再单独定义结构体数组 `struct Student stu[5]`
- 获取结构体数组的长度 `len=sizeof(stu1)/sizofi(struct stu)`
```c
struct stu
{
	char *name;
    int age;
} class[5];
```

## 结构体指针
- 结构体变量名和数组名不同，数组名在表达式中会被转化为数组指针，而结构体变量名不会
- 无论在任何表达式中，结构体都表示的是整体，
- 可以把结构体赋值给指针
- `struct stu *pstu=&stu1`;
- 通过结构体指针可以获取结构体成员
- `(*pstu).age`或者`pstu->age` 通常使用后者
- `.`点运算符的优先级最高，所以指针使用点时前面指定要条件括号

## 结构体数组指针
- 和结构体指针类似
- 对于结构体数组指针在`for`循环过程中，可以直接对指针进行递增`point++`，这样就可以直接在内部用指针指出当前遍历的结构体值了`point->name`
- 如果指针指向的是结构体第一个值，即首地址，直接把结构体数组赋值给结构体即可`point=structarr`，因为数组本身就表示首地址；
- 如果指针指向的是数组得首地址，就必须使用`&`过去地址了`point=&structarr[2]`

## 范例
- struct具体使用
```c
#include<stdio.h>

int main()
{
    struct stu
    {
      char *name;
      int num;
      int age;
      char group;
      float score;
    };
    struct stu stu1, stu2;
    stu1.name="Tom";
    stu1.age=12;
    stu1.num=421243;
    stu1.group='A';
    stu1.score=88.2;
    printf("%s %d %d %c %.2f",stu1.name, stu1.num, stu1.age,stu1.group,stu1.score);
    return 0;
}
```
- 结构体数组
```c
int main()
{
    struct stu
    {
      char *name;
      int num;
      int age;
      char group;
      float score;
    } class[5] =
    {
        {"Li ping", 5, 18, 'C', 145.0},
        {"Zhang ping", 4, 19, 'A', 130.5},
        {"He fang", 1, 18, 'A', 148.5},
        {"Cheng ling", 2, 17, 'F', 139.0},
        {"Wang ming", 3, 17, 'B', 144.5}
    };
    printf("%s %d %d %c %.2f",class[0].name, class[0].num, class[0].age,class[0].group,class[0].score);
    return 0;
}
```

## 参考
- [struct](http://c.biancheng.net/cpp/html/88.html)
