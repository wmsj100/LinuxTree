---
title: 文件的加载
date: Sat 30 Dec 2017 07:19:26 PM CST
modify: 2020-02-21 19:32:40 
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 文件

## 概览

- python中操作文件的接口

## 常用方法

- open() 通过open来加载文件，参数为文件的绝对路径
- read() 加载好文件后需要用这个方法来获取文件的内容, read会一次性全部读取所有内容
- readlines() 会一行一行的读取文件
- readline() 只加载第一行文本
- 加载文件是有几种模式可以选择，如果不写第二个参数，那么默认是以只读模式加载。

## 范例

- 读取文件并且获取值
```python
def get_auth():
    auth = dict()

    with open('/home/ubuntu/.ossutilconfig') as file:
        for line in file.readlines():
            print(line)
            if line.find('=') > -1:
                [key, val] = line.split('=')
                auth[key] = val

    return auth

print(get_auth())
```
