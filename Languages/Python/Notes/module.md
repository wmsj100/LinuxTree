---
title: 模块
date: Sun 31 Dec 2017 03:53:39 PM CST
modify: 2020-02-11 08:07:07 
tag: [python]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# 模块

## 基础概念

- import bar 通过导入同目录文件名来导入模块
- `__name__`: 模块名称，当文件直接被调用时候
	- `__name__ == '__main__'` 当模板被python直接调用
	- `__name__ == 'module_name` 当模块被通过`import`引入调用时候，该模块的`__name__`为该模块名
    
## 为模块编写说明文档

- 在模块的头部用`"""`包裹的内容为说明文档
- 导入模块后，可以通过`module_name.__doc__`来读取说明文档

## 包

- 包是一个文件夹，里面有一个文件`__init__.py`，该文件可以为空。
- 导入包的模块`from bao import test1 test2`，
- `from bao import *` 这样的语法不能导入bao下的任何模块，必须指定导入的具体模块名

## 范例

- 一个好的类封装
```python
class Clang:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __get_info(self):
        return (self.__name, self.__age)

    def __set_info(self, args):
        self.__name, self.__age = args

    def __del_info(self):
        self.__name = 'xxx'
        self.__age = 0

    def get_name(self):
        print('name is ',__name__)

    info = property(__get_info, __set_info, __del_info)

if __name__ == '__main__':
    test = Clang('wmsj100', 32)
    print(test.info)
	test.info = 44,55
    print(test.info)
	del test.info
    print(test.info)
    print('name is ',__name__)
```
