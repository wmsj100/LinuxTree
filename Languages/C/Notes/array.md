---
title: 数组
date: 2019-04-21 09:13:15	
modify: 
tag: [array,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数组

## 概述
- 数组是一个集合，通过scanf赋值数组时候不需要添加`&`
- 如果赋值数组的元素，元素前需要添加`&` &arr[2]
- 数组必须是同一类型的值组成
- 数组在内存中存储连续，所以可以通过步进+1就可以获取下一个值
- len=sizeof(arr)/sizeof(int) 这样可以获取数组的长度

## 重点
- C中的数组是静态的，数组一旦定义，占用的空间就是固定的，容量就不可以改变。这种类型是静态数组
- JS/Python等语言是动态数组，数组可以随意操控插入或删除
- 不能插入和删除，因为在内存中都是连续排列的，如果插入或删除一个值，会需要移动后面所有的值的内存，甚至重新开辟一块内存，这是相当耗费资源的。
- 很多时候需要把数组的地址保存到一个变量(指针),如果数组重新开辟了内存，而变量没有跟着变，还是指向原来的数组地址，就会导致错误，称为野指针。

## 数组初始化
- int arr[]={1,2,3,4} 不写数组长度，通过值来判断
- int arr[5]={0} 赋值第一个值为0，其余的字段默认也会赋值0

## 二维数组
- int arr[5][4]={{0}}
- int arr[5][3] = {{80,75,92}, {61,65,71}, {59,63,70}, {85,87,90}, {76,77,85}};
- 如果全部赋值，第一维的长度可以不写
- int arr[][3] = {{80,75,92}, {61,65,71}, {59,63,70}, {85,87,90}, {76,77,85}};
- 二维数组也可以部分赋值，未赋值的默认取0
- int a[3][3]={{1}, {2}, {3}};
- 二维数组是以行排序的，先写入arr[0]，后面再写入arr[1],内存中的，也是连续的，
- len=sizeof(arr)/sizeof(int)=5\*4=20;

## 越界
- 数组越界分为上限越界和下限越界，
- C语言和编译器并不会去检查值是否越界
- 越界后输出也不会报错，只是输出的值不可控，越界值是随机的。
- 如果对越界的内存没有使用权限，或者该内存压根就没有分配，那么程序将会崩溃

## 溢出
- int a[2]={1,2,3} 3就溢出了，溢出的值会被丢弃
- 溢出会有编译告警，但是结果是可执行的
- 如果是字符串溢出，输出结果就不可控了，因为没有`\0`，
- 高版本的编译器会有编译告警

## 变长数组
- 变长数组实际上也是静态的，区别如下：
- 静态数组是在编译期间就确定分配了内存
- 变长数组是在运行期间才分配内存的

## 参考
- [数组](http://c.biancheng.net/cpp/html/3461.html)