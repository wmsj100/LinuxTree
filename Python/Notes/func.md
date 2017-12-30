---
title: 函数
date: Wed 27 Dec 2017 10:48:30 PM CST
tag: [python,function]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础知识
- 函数可以多次复用代码，
- 有内建函数和自定义函数
- 使用‘def’定义函数
    ```python
    def sum(a,b):
        return a+b
    res = sum(123, 546)
    pritn(res)
    ```
- `__name__` 这是模块的名称，如果直接运行模块，则`__name__` == `__main__`；如果模块是通过`import`的方式导入的，则模块的`__name__`的值是模块的文件名
## 数值函数
- `range` 获取可迭代的对象，返回的并不是数组，需要通过`list()`方法转换为列表
    - `range(5)` [0,1,2,3,4]
    - `range(1,5)` [1,2,3,4]
    - `range(1,15,3)` [1,4,7,10,13]
    - `range(4,15,2)` [4,6,8,10,12,14]
