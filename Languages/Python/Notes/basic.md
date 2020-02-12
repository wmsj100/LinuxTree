---
title: python基础知识
date: Tue 19 Dec 2017 11:03:08 PM CST
modify: 2020-02-12 18:30:27
tag: [basic]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# python基础知识

## 实现

- CPython: 是python的参考实现，用C写成。
- PyPy: 是python的子集，具有静态类型，旨在提高性能，是python的5倍性能。
- Jython: python的java实现
- IrconPython: 针对.Net框架的python实现
- PythonNet: 是一个近乎无缝的集成。
- 使用相对导入来导入模块，这样包名称变更后影响很小，可能只需要1秒时间来更改包名称就可以了。

## 范例

- 在终端直接输入'python'就可以进入'python'编辑器模式。
- type(a) 可以查看当前的变量的类型
- input 可以获取键盘输入
```python
number = int(input("Enter an integer: "))
if number <= 100:
    print("less than 100")
else:
    print("lager than 100")
```
- "Year {} Rs. {:.2f}".format(year, value) 字符串格式化
- a,b=12,23 在一行内给多个变量赋值，通过这个技巧可以交换彼此的值；例如`a,b=b,a`这样'a'和'b'的值就交换了。
- 用逗号可以创建元组；在赋值语句的右边创建了一个元组，我们称这为元组的封装，赋值语句的左边我们则做的是元组的拆封。
    - data = ('asdf', 'qwer', zxcv')
    - name, age, time = data
    - name; // 'asdf'
    - age // 'qwer'
    - time // 'zxcv'
