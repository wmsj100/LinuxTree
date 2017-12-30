---
title: 数据结构
date: Sat 30 Dec 2017 09:21:51 AM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 列表操作
- append 给列表末尾添加值
- insert(index, val) 在列表的索引`index`处插入值`val`;
- count(val) 查看值‘val’在列表中出现了几次
- remove(val) 从列表中删除第一个值‘val’
- reverse() 列表反转
- a.extend(b) 把列表b添加到列表a的末尾
- sort() 列表排序，只能是同一类型的值可以排序，如果有不同类型的值，会报错
- del a[1] 删除列表a的索引为1的值

### 列表的栈和队列
- 栈： LIFO （last in first out）
- pop 把列表的最后一个值弹出
- a.pop(1) 把列表的索引为1的值弹出，
- append(val) 把值添加列表的末尾

### 列表推导式
```python
a=[]
a=list(map(lambda x:x**2, range(10))); // [0,1,4,9,16,25,36...81]
a=[x**2 for x in range(10)]; // [0,1,4,9,16,25,36...81]
```

- 列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个for字句，之后可有有零个或多个for或if字句，结果是一个列表，
    `[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]`
- 列表推导式也可以嵌套
    ```python
    a = [1,2,3]
    z = [x+1 for x in [x**2 for x in a]]
    ```

## 元组
- 元组是由数个逗号分割的值组成
- 元组的值不可以i编辑，一旦生成，就不可以在添加/ 修改/ 删除
- a=(12,) 创建只有一个元素的元组，需要在值后面加一个逗号

## 集合
- 集合是无序不重复元素的集。
- 大括号或`set()`函数可以创建集合，
- 'set()' 只能通过set创建空集合
    a = {'a', 'b', 'c'}
    'a' in a; // true
    b = set('wmsj100'); // {'w','m','s','j','1','0'}
- 集合可以进行联合/ 交集/ 差集/ 对称差集等数学运算
- 集合内部的所有值都是字符串
- a.pop()
- a.add('s')
- a.remove('1')

## 字典
- 字典是无序的健值对集合，同一个字典内的健值对。
- {} 创建一个空的键值对
    a={'name': 'wmsj100', 'age': 12}
    a['name']; // 'wmsj100'
- a['level']='two' 创建新的键值对很简单
- del a['level'] 删除键值对
- 'name' in a; 通过‘in’判断键值是否在字典中
- dict((('name', 'wmsj100'),('age', 12))) 这样可以从包含键值对的元组中创建字典。
- a.items 可以遍历字典
- a.setdefault('name', 'wmsj100'); 通过‘setdefault’可以实现如果要添加的键已经存在，则不处理，否则添加默认值
- a.get(key, default), 如果查看字典内不存在的值会报错，可以通过这个方法来查看不存在的值，并且方法默认的值。

## 遍历列表
- enumerate 这个方法可以同时获取元素的索引值和值
    ```python
    for i,j in enumerate(['a', 'b', 'c']):
        print(i, j) // i 索引值，j 值
    ```

- zip 同时遍历俩个序列
    ```python
    a=['a','b','d']
    b=['q','w','e']
    for x,y in zip(a,b):
        print("{} uses {}".format(x, y))
    ```

