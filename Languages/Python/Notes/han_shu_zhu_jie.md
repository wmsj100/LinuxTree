---
title: 函数注解
date: 2020-02-07 22:08:59
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 函数注解

## 概要

- 函数注解是python最独特的功能之一，
- 用于为函数中的行参和返回值提供类似提示信息
- 通过`__annotations__`来查看函数的注解
```python
def hello(name:str, age:int=30)->str:
	return 'name is {}, age is {}'.format(name, age)
hello('wmsj100') # 'name is wmsj100, age is 32'
hello.__annotations__
#{'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
```

## 意义

- 函数注解没有任何语法上的意义，只是为函数参数和返回值做注解，并再运行获取这些注解，仅此而已
- 为函数做注解，Python不做检查，不做强制，不做验证，什么操作都不做
- 函数注解对python解释器没有任何意义。
- 最重要的功能就是类似强类型语言那样，让IDE提示输入和返回，IDE检查

## 参考

- [python 函数注解](http://c.biancheng.net/view/vip_6065.html)
