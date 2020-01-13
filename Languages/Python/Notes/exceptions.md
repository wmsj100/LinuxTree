---
title: 异常
date: 2020-01-13 10:29:36
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# exceptions

## 概要

- 异常就是程序出错，在没有按照期望输入时候就直接抛出异常
- 异常默认是以堆栈跟踪的形式中止的

## 常见异常类型

- Exception 所有异常的基类
- AttributeError 特性引用或赋值失败时引发
- IOError 试图打开不存在的文件时引发
- IndexError 在使用序列中不存在的索引引发异常
- KeyError 使用映射中不存在的键时引发
- NameError 找不到变量名时引发
- SynataxError 代码为错误形式时引发
- TypeError  类型错误
- ValueError 值错误
- ZeroDivisionError 除法或摸的第二个参数为0时的异常

## 异常机制

- 异常本质就是触发了并且被捕获的过程，就像事件冒泡，只要被捕获了就不会再继续传播了。
- 如果捕获了一个异常，还想继续让它传播下去，可以直接使用`raise`
- try/except是调用异常的方式
- 先进行执行，等到出错后才根据错误类型来分别处理，这要比普通的类型或值判断要好得多，那些判断会先进行判断，有多余的动作执行。
```python
try:
    x = input('first number')
    y = input('second number')
    print(int(x)/int(y))
except ZeroDivisionError:
    print('The second number can\'t be zero.')
```
- 下面是带有异常开关的类
```python
class Calculate:
    flag = False
    def cals(self, excp):
        try:
            return eval(excp)
        except ZeroDivisionError:
            if self.flag:
                return 'The Second number can\'t be zero'
            else:
                raise
a=Calculate()
a.flag # False
a.cals('1/0')
#  File "<stdin>", line 1
#    a.flag=!a.flag
#           ^
#SyntaxError: invalid syntax
a.flag = not a.flag #a.flag=True
a.cals('1/0')
#"The Second number can't be zero"
```
- 多个异常可以通过多个except来实现捕获
```python
class Calculate:
    flag = False
    def cals(self, excp):
        try:
            return eval(excp)
        except ZeroDivisionError:
            if self.flag:
                return 'The Second number can\'t be zero'
            else:
                raise
        except TypeError:
            if self.flag:
                return 'Please just input number'
            else:
                raise
        except NameError:
            if self.flag:
                return 'Please make sure param has defined'
            else:
                raise
```
- 可以多个异常在一个块中捕获，需要把多个异常按照元组形式放置
```python
class Cal1:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError):
            return 'Please input correct number'
```
- 捕捉对象:前面说的异常都是阻塞性的异常，程序会中断，可能有时候只是想记录异常并且让程序继续运行，可以按照下面方式实现
```python
class Cal2:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError) as e:
            print(e)
#>>> a=Cal2()
#>>> a.flag=True
#>>> a.cals('1/0')
#division by zero
#>>> a.cals('1/a')
#name 'a' is not defined
#>>> a.cals('1/"a"')
#unsupported operand type(s) for /: 'int' and 'str'
```
- 真正的全捕捉: 就算程序能处理多种类型的异常，但有些异常还会从眼皮底下溜走。这时候就可以使用`Exception`来实现全捕捉
```python
class Cal3:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError) as e:
            print(e)
        except Exception as e:
            print("other error: %s" % e)
#>>> from except1 import Cal3
#>>> a=Cal3()
#>>> a.flag=True
#>>> a.cals('1/')
#other error: unexpected EOF while parsing (<string>, line 1)
#>>> a.cals('1/d')
#name 'd' is not defined
```
- try/except/finally:在`finally`中定义的代码不管是否会触发异常都会被执行
```python
class Cal5:
    def cals(self,exprval):
        try:
            return eval(exprval)
        except Exception as e:
            print("other error: %s" % e)
        else:
            print("start planing ,not error")
        finally:
            print("finally!!!")
```
- 异常和函数:异常和函数能很自然的一起工作，如果异常在函数内引起而不被处理，它就会传播至(浮现)函数调用的地方。如果在那里也没有处理异常，它就会继续传播，一直到达主程序(全局作用域)，如果那里没有异常处理程序，程序会带着栈跟踪中止。
```python
class Cal6:
    def fault(self):
        raise Exception('Something is error')

    def ignore(self):
        self.fault()
    
    def deal(self):
        try:
            self.fault()
        except:
            print("thsi is some error,please deal")

#>>> a.fault()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/home/pi/Documents/python/test/except1.py", line 91, in fault
#    raise Exception('Something is error')
#Exception: Something is error
#>>>
#>>> a.ignore()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/home/pi/Documents/python/test/except1.py", line 94, in ignore
#    self.fault()
#  File "/home/pi/Documents/python/test/except1.py", line 91, in fault
#    raise Exception('Something is error')
#Exception: Something is error
#>>>
#>>> a.deal()
#thsi is some error,please deal
```

## 参考

