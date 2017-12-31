---
title: Collections模块
date: Sun 31 Dec 2017 09:54:39 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础知识
- Collections是python内建的一个集合模块，提供了许多有用的集合类。
- help(collections.Counter) 查看‘Counter’的帮助信息
    -` c = Counter(a=4,b=2,c=0,d=-2)`
    - `list(c.elements()); // ['a','a','a','a','b','b']`
- most_common() 返回最常见的元素及计数，顺序为最常见到最少
    -` Counter('asdfqwerasdf').most_common()`

- defaultdict 这个方法很有用，比系统默认的setdefault要快
    - `a = defaultdict(list)`
    - `type(a)` 可以查看类型

- namedtuple 命名元组有助于对元组的每个位置赋予意义，并且让代码有更好的可读性和自文档性。
    ```python
    po = namedtuple('Po', ['x', 'y'])
    p = po(10, y=20)
    p // po(x=10,y=20)
    p.x + p.y  // 30
    p[0] + p[1] // 30
    x,y = p
    x // 10
    ```

