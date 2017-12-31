---
title: 类
date: Sun 31 Dec 2017 11:50:57 AM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- 在python中所有的数据类型都可以视为对象，也可以自定义对象，这种数据类型就是面向对象中的类
- class 定义类需要使用
    ```python
    class myClass(object):
        """ A simple class"""
        i = 12345
        def f(self):
            return 'hello world'
    val1 = myClass()
    val1.i // 12345
    val1.f() // 'hello world'
    ```
- `__init__` 类实例化操作会自动为新创建的类实例调用`__init__`方法
    ```python
    class Complex:
        def __init__(self, a,b):
            self.r = a
            self.i = b
    x = Complex(1,2)
    x.r // 1
    x.i // 2
    ```

## 继承
- 当一个类继承另一个类时，它将继承父类的所有功能（变量和方法）。
```python    
class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} studies {} and is in {} year".format(self.name, self.branch, self.year)

class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teachers {}".format(self.name, ','.join(self.papers))

p1 = Person('Sachin')
s1 = Student('Kushal', 'CSE', 2005)
t1 = Teacher('Prashad', ['C', 'C++'])

print(p1.get_details())
print(s1.get_details())
print(t1.get_details())
```

- 定义类的时候可以选择要继承的类，默认时继承`object`,也可以自定义要继承的类`Person`

- del 删除对象，如果对象的引用计数器变为零时，垃圾回收会删除这个对象

