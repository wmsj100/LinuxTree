---
title: 作用域
date: 2020-01-12 12:16:35
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 作用域

## 概要

- pythn的作用域和其他语言类似，
- 也分全局作用域和局部作用域
- python中没有块级作用域，也就是在if/for/while里定义的变量所在的作用域就是块所属的作用域

## 全局作用域

- 在函数内部可以直接引用全局作用域，但是不能对全局变量本身进行递增等操作'a+=1'
```python
a=3 #定义全局作用域

def ha():
    global a #通过global来申明是全局变量，如果没有这个申明下面会报错，提示需要先定义a
    a = a + 1 # 在函数内部所有的变量赋值操作都是基于局部作用域的，相当于定义一个和全局变量同名的局部变量
    print(a)

ha()
print(a)

def hb():
    b = a + 1 #直接引用全局变量参与运算，结果赋值给局部变量，
    print('b is %d' % b)

hb()

if True:
    b=3
    print(a,b) # 直接引用全局变量
print(a,b)
```


## 参考

