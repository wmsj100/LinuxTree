---
title: dict
date: 2020-01-11 14:44:42
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# dict

## 概要

- 字典只是python内置的一种映射
- 字典是一种无序的、可变的序列，是python中唯一的映射类型。
![](http://c.biancheng.net/uploads/allimg/190212/2-1Z212152450U3.gif)
- 字典本身的功能强大，而且对于查询的效率要比列表高，数据量越大，这种优势体现越明显。

## 创建方法

- `dict(name='wmsj100', age=21)` 使用此方法，key值不能带引号
- `dict([['one', 1], ['two', 2]])`
- `dict(zip(['one', 'tow'], [1, 2]))`
- `dict.fromkeys(['name', 'age'], defaultValue)` 创建字典，所有key值有相同的默认值`defaultvalue`
- 空字典要远远大于空数组和空元组
```python
a = dict()
a.__sizeof__() # 216
b = list()
b.__sizeof__() # 40
c = tuple()
c.__sizeof__() # 24
```

## 方法

- `dict.clear` 清空列表，这种场景对于多个变量指向同一个字典值时候非常好用，
- `dict.copy`  字典的浅拷贝
- `from copy import deepcopy deepcopy(dict)` 这样执行的结果就是字典的深拷贝
- `dict.fromkeys(['name', 'age'])` 通过给定的key值创建一个字典，默认值是'None'
- `dict.fromkeys(['name', 'age'], 'empty')` 所有创建的key值的默认值都是'empty'
- `dict.get('key')` 相对宽松的访问字典key值的方法，如果没有key，返回`None`
- `dict.get('key', 'empty')` 如果目标key值不存在就返回提供的默认值`empty`
- `dict.items()` 把键值对按照迭代器的形式返回，可以通过list直接转换为列表
- `dict.keys()` 把key当作迭代器返回
- `dict.pop('name')` 类似列表的功能，删除给定key的key-value，并且返回value
- `dict.popitem()` 随机删除一项key-value，并且返回(key,value)的元组形式，这个方法适用于一个接一个的删除字典的值。因为不用获取字典的key值了。
- `dict.setdefault('name', 'wmsj100')` 类似于get，如果目标key值不存在就赋值给之后提供的默认值，如果存在就返回目标key的value。
- `dict.update(dict1)` 用字典dict2来更新字典dict，有相同的值就用后者更新前者
- `dict.values()` 返回字典的values的迭代器对象

## 格式化字符串

- `a='name is {name}, age is {age}, url is {url}'.format(name='wmsj100', age=22, url='http://www.wmsj100.com')`
- `'name is wmsj100, age is 22, url is http://www.wmsj100.com'`

## 参考

- [python字典格式化字符串](http://c.biancheng.net/view/vip_6002.html)
