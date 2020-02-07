---
title: params
date: 2020-01-12 10:14:53
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# params

## 概要

- python的参数有位置参数和关键字参数
- 通常常见的就是位置参数，必须按照固定顺序写入参数

## 类型

- 位置参数
	- def hello(name, age):
- 关键字参数
	- def hello(name='wmsj100', age=32)
- 查看函数默认参数
	- hello.__default__ ('wmsj100', 32) 返回函数的默认值参数

## 收集参数

- 收集位置参数
	- def hello(*param): 可以输入任意多参数，被param收集在元组中
	- def hello(name, age, *param)
- 收集关键字参数
	- def hello(**param): 收集关键字参数，以字典形式
	- hello(name='wmsj100', age=32)  {'name': 'wmsj100', 'age': 32}
- 混合使用
	- def hello(name, age=32, *param, **dict)
	- hello('wmsj100', 33, 'ha', 'li', people='yellow', blod='red')
	```
	wmsj
	33
	('ha', 'li', 'lu', 'ya')
	{'people': 'yellow', 'blod': 'red'}
	```

## 参数收集逆过程

- 在函数调用过程中加入星号
```python
def hello(**args):
    print(args['name'], args['age'])

data = { 'name': 'wmsj100', 'age': 32}

hello(**data)

def hello2(args):
    print(args['name'], args['age'])

hello2(data)
```
- 在函数定义和调用过程中都使用了星号

## 参考

