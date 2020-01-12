---
title: 查找first/middle/last方法总结
date: 2020-01-12 09:06:27
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 查找first/middle/last方法总结

## 概要

- 这是‘Python基础教程’这本书的一个实例‘page96'
- 本来就是创建一个简易的数据库，功能是按照姓名的'first/middle/last'来添加和查找姓名
- 我的代码思路比较简单，就是在添加姓名前先查询，如果没有就依次再按照标签key值查找定位并且插入，如果存在就放弃
- 但是作者的思路性能要更好，因为他只查询一次，然后因为目标值是存储在列表中，是属于复杂对象的，可以通过直接返回这个列表，然后赋值给一个变量，直接通过这个变量来操作这个列表
- 因为这些变量指向的列表地址是一样的，所以这样的操作和直接操作列表效果是一样的，而且性能更好，因为少了一次查询定位操作。
- 具体代码如下

## 代码

- 我自己的代码实现
```python
result = {}
labels = 'first','middle','last'

def init():
    result.setdefault(labels[0], {})
    result.setdefault(labels[1], {})
    result.setdefault(labels[2], {})

def store(name):
    names = name.strip().split()
    if len(names) == 2:
        names.insert(1, '')
    elif not len(names):
        print("Please input names like 'ha li luya'")
        return False

    for label,key in zip(labels,names):
        currentList = result.get(label, {}).setdefault(key, [])
        if name not in currentList:
            result[label][key].append(name)

def showPeople():
    print(result)

if __name__ == '__main__':
    init()
    store('wang hao')
    showPeople()
    store('wang hao')
    showPeople()
    store('tan mu xun')
    store('wang yu hao')
    showPeople()
```

- 作者的代码实现
```python
result = {}
labels = 'first','middle','last'

def init():
    result.setdefault(labels[0], {})
    result.setdefault(labels[1], {})
    result.setdefault(labels[2], {})

# 查询并定位列表并且直接返回列表在内存中的指针
def lookup(data,label,first_name):
    return data.get(label, {}).setdefault(first_name, [])

def store(name):
    names = name.strip().split()
    if len(names) == 2:
        names.insert(1, '')
    elif not len(names):
        print("Please input names like 'ha li luya'")
        return False

    for label,key in zip(labels,names):
        people = lookup(result,label,key)
        if people:
            if name not in people:
                people.append(name)
        else:
            people.append(name)

def showPeople():
    print(result)

if __name__ == '__main__':
    init()
    store('wang hao')
    showPeople()
    store('wang hao')
    showPeople()
    store('tan mu xun')
    store('wang yu hao')
    showPeople()
```

