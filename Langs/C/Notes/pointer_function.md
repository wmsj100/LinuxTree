---
title: 函数指针
date: 2019-04-21 16:56:41	
modify: 
tag: [pointer,function,func,c,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 函数指针

## 把指针作为函数参数
- 把指针作为参数传递给函数，在函数内部对指针对应的值做出的修改不会随着函数的结束而消失
- 可以在函数内部对外部变量的值做出修改

## 范例
```c
#include<stdio.h>

void change(int *a,int *b);
int main()
{
    int a=10,b=11;
    printf("a=%d, b=%d\n", a,b);
    change(&a,&b);
    printf("a=%d, b=%d\n", a,b);
    return 0;
}

void change(int *a, int *b)
{
    int pem=*a;
    *a=*b;
    *b=pem;
}
```

## 数组做函数参数
- 数组是一系列数据的集合，无法通过参数的形式将他们一次性传递到函数内部，如果希望在函数内部操作数组，必须传递数组指针，
- 并且同时要传入数组长度
- 参数的传递过程本质上是一次赋值，赋值就是对内存进行拷贝，就是把一块内存上的数据赋值到另一块内存上，
- 因为数组元素没有限制，可能很少，也可能很多，如果直接拷贝数组，会严重影响性能。
- C++/Python/Java等也禁止对大块内存进行拷贝，底层都使用类似指针的方式来实现。

## 范例
```c
#include<stdio.h>

int max(int *arr, int len);
void getVal(int *arr, int len);
int main()
{
    int arr[5]={0},len;
    len=sizeof(arr)/sizeof(int);
    getVal(arr,len);
    int res=max(arr, len);
    printf("max value is %d", res);
    return 0;
}

void getVal(int *arr, int len)
{
    for(int i=0;i<len;i++){
        scanf("%d", &(arr[i]));
    }
}

int max(int *arr, int len)
{
    int max=*arr;
    for(int i=1;i<len;i++){
        if(max<*(arr+i)){
            max=*(arr+i);
        }
    }
    return max;
}
```

## 参考
- [数组指针参数](http://c.biancheng.net/cpp/html/74.html)
