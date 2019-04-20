---
title: 迭代器
date: Mon 01 Jan 2018 10:39:23 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 迭代器对象需要支持如下俩中方法：
    - __iter__(): 返回迭代器对象自身，则用在`for`和`in`语句中
    - __next__(): 返回迭代器的下一个值，如果没有下一个值可以返回，那么应该抛出`StopIteration`异常

## 生成器
- `yield` 这个关键字在函数内部创建迭代器
    ```python
    def my():
        yield 'a'
        yield 'b'
        yield 'c'

    a = my()
    list(a) // ['a', 'b', 'c']
    ```

- 通常使用生成器进行惰性求值，这样使用生成器是处理大数据的好方法，如果不想再内存中加载所有的数据，可以这样使用生成器，一次只传递一部分数据
- 生成器是不可重复使用的，使用过一次之后就成了空值。
- 一个创建可重复使用生成器的方式是不保存任何状态的基于对象的生成器。

## 生成器表达式
- 生成器表达式是列表推导式和生成器的一个高性能，内存使用效率高的推广
- `sum((x*x for x in range(1,10))` 使用生成器表达式来节省内存使用
- 生成器表达式的语法要求其总是直接在一对括号类，并且不能在俩边有逗号。

## 闭包
- 闭包是由另外一个函数返回的函数，
    ```python
    def add_number(num):
       def adder(number):
            return num + number
       return adder
    ```

## 装饰器
- 装饰器用来给一些对象动态的添加一些新的行为。
- 使用`@`来触发
