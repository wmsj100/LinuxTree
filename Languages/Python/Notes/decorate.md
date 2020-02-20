---
title: 装饰器
date: 2020-02-20 13:32:03
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 装饰器

## 概要

- python的装饰器本质上是一个python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能，
- 装饰器的返回值也是一个函数对象，简单的说装饰器就是一个用来返回函数的函数。

## 使用场景

- 它经常用于有切面需求的场景，比如插入日志、性能测试、事务处理、缓存、权限校验等场景。
- 装饰器是解决这类问题的绝佳设计，
- 有了装饰器，我们可以抽离出大量与函数功能本身无关的雷同代码并继续复用。
- 概括的讲，装饰器的作用就是为已经存在的对象添加额外功能。
- 对于大量函数需要执行雷同操作的都可以抽取成装饰器，方便统一修改。

## 用法

- 装饰器通过使用`@`符号作为语法糖，使我们更方便应用装饰器。
- 要使用语法糖必须return一个函数对象。
- 例如下面函数通过`_deco`内嵌函数包裹

### 不带参数的函数
```python
def use_logging(func):
    def _deco():
        print("{} is running".format(func.__name__))
        print("all function complete")
        return func
    return _deco

@use_logging
def bar():
    print('i am bar')

bar()
```

### 函数带参数的装饰器

- 内嵌函数`_deco`传入参数`*args, **kwargs`来捕获函数传入的所有参数
```python
def use_logging(func):
    def _deco(*args, **kwargs):
        print("{} is running".format(func.__name__))
        print("all function complete")
        return func(*args, **kwargs)
    return _deco

@use_logging
def bar(a,b):
    print('i am bar, result is {}'.format(a*b))

bar(2,5)
```

### 带参数装饰器

- 装饰器装饰的函数会丢失函数的元信息，需要通过`functools.wrap`装饰器来传递函数的元信息
```python
import functools

def logging(level):
    def _deco(func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if level == 'warn':
                print('{} is warning logging running, please lookup'.format(func.__name__))
            return func(*args, **kwargs)
        return _deco
    return _deco

@logging('pass')
def bar(a,b):
    print('i am bar, result is {}'.format(a*b))

bar(2,4)
```

### 实现带参数和不带参数的装饰器

- 装饰器有没有参数通过`callable`来判断传入的是否是函数，如果是函数，则没有带参数，否则带参数
```pthon
import functools

def logged(level):
    if not callable(level):
        def _deco(func):
            @functools.wraps(func)
            def _deco(*args, **kwargs):
                print("decorate has argument")
                print('arguments is {}'.format(level))
                return func(*args, **kwargs)
            return _deco
        return _deco
    else:
        @functools.wraps(level)
        def _deco(*args, **kwargs):
            print("decorate doesn't has argemunt")
            level(*args, **kwargs)
        return _deco

@logged('wmsj param')
#@logged
def bar2(a,b,c,d):
    print('i am bar2, data is {}'.format(a+b+c+d))
    print(bar2.__name__)

bar2(4,3,5,6)
```

### 类装饰器实现带参数的装饰器

- 类装饰器实现的更加简洁，而且可以继承
```python
class Log_class:
    def __init__(self, args='warn'):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if self.args == 'warn':
                self.notify(func)
            return func(*args, **kwargs)
        return _deco

    def notify(self, func):
        print('{} is running'.format(func.__name__))

@Log_class(args='warning')
def bar2(a,b,c,d):
    print('i am bar2, data is {}'.format(a+b+c+d))
    print(bar2.__name__)

bar2(4,3,5,6)
```

### 继承扩展类的装饰器

- 新创建一个类，覆盖类基类的方法
```python
class Log_class:
    def __init__(self, args='warn'):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if self.args == 'warn':
                self.notify(func)
            return func(*args, **kwargs)
        return _deco

    def notify(self, func):
        print('{} is running'.format(func.__name__))

class email_log(Log_class):
    def __init__(self, email='wmsj100@hotmail.com', *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)

    def notify(self, func):
        print('Please send email to {}'.format(self.email))
        print('{} is running'.format(func.__name__))


#@Log_class(args='warning')
@email_log(args='warning')
#@logged('wmsj param')
#@logged
#@logging('warn')
#@use_logging
def bar2(a,b,c,d):
    print('i am bar2, data is {}'.format(a+b+c+d))
    print(bar2.__name__)

bar2(4,3,5,6)
```

## 参考

- [python 装饰器](https://www.cnblogs.com/arvin-feng/p/11108799.html)
