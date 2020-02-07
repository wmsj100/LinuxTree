---
title: 函数式编程
date: 2020-02-07 19:05:05
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 函数式编程

## 概要

- 函数式编程是指代码中每一块都是不可变的，都是由纯函数的形式组成。
- 这里的纯函数，是指函数本身相互独立、互不影响，总会有相同的输出。
- 函数式编程还具有的一个特定，即允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
- 函数式编程的优点，主要在于纯函数和不可变的特性使程序更加健壮，易于调试和测试；
- 缺点主要在于限制多，难写。
- 纯粹的函数式编程语言`Scala`，其编写的函数中是没有变量的，因此可以保证，只要输入是确定的，输出就是确定的；
- python允许使用变量，所以它并不是一门纯函数式编程语言。
- python仅对函数式编程提供了部分支持，主要包括`map/filter/reduce`这三个函数，他们通常都结合`lambda`匿名函数一起使用。

## 范例

```python
# 非函数式编程，多次调用返回的list的值不同
# 直接修改了传入的list
def double(list):
    for index in range(len(list)):
        list[index] = list[index]*2
    return list

# 函数式编程，多次调用返回结果相同，不直接修改list
def han_shu_double(list):
    result = []
    for val in list:
        result.append(val*2)
    return result

print(double([2,4,3,6]))
print(han_shu_double([2,4,3,6]))
```
## 参考

- [python 函数式编程](http://c.biancheng.net/view/vip_6064.html)
