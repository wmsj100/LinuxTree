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
- global 通过这个值可以修改全局变量值，但是这个感觉使用场景比较少，因为一般不建议在函数内部直接修改全局变量
- 函数的参数可以添加默认值
    ```python
    def test(a, b=-99):
        if a > b:
            return True
        else:
            return False
    ```
    - 有默认值的参数后面不能有普通参数
    - 默认值只能被赋值一次，但是如果是任何可变对象时会有所不同，比如字典/列表，会产生累积前面传给的参数；
    ```python
    def f(a, data=[]):
        data.append(a)
        return data
    ```
    - 上面的例子，每调用一次函数'f()'，它会把前面的参数累积起来，这是要特别注意的
- 关键字参数
    - 函数可以通过关键字参数的形式来调用，
    ```python
    def func(a, b=5, c=10):
        print(a,b,c)
    func(1) // 1,5,10
    func(1,c=12) // 1,5,12
    func(b=12,c=24, a=-1) // -1,12,24
    ```
- 强制关键字参数，表示函数调用时候必须使用输入完整关键字参数才可以
    ```python
    def func(*, name='user'):
        print(name)
    func('shi') // error
    func(name='shi') // 'shi'
    ```

- 文档字符串
    - python里我们使用文档字符串来说明如何使用代码，使用方式如下：
    ```python
    def fn1(a,b):
        """
        function is to test
        :arg a is int
        :arg b is int
        :return a+b
        """
    print(fn1.__doc__)
    ```
    - 通过`fn1.__doc__`这样就可以查看函数的说明，从而知道函数的作用

## map
- `map`是一个在'python'里非常有用的高阶函数，他接受一个函数和一个序列（迭代器）作为输入，然后对序列的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结构
    ```python
    lst = list(range(1,6))
    def squ(num):
        return num*num
    print(list(map(squ, lst))); // [1,4,9,16,25]
    ```

## 数值函数
- `range` 获取可迭代的对象，返回的并不是数组，需要通过`list()`方法转换为列表
    - `range(5)` [0,1,2,3,4]
    - `range(1,5)` [1,2,3,4]
    - `range(1,15,3)` [1,4,7,10,13]
    - `range(4,15,2)` [4,6,8,10,12,14]
