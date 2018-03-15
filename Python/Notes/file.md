---
title: 文件的加载
date: Sat 30 Dec 2017 07:19:26 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- open() 通过open来加载文件，参数为文件的绝对路径
- read() 加载好文件后需要用这个方法来获取文件的内容
- 加载文件是有几种模式可以选择，如果不写第二个参数，那么默认是以只读模式加载。

## 范例
```python
file = open('/home/wmsj100/Documents/git/Python/Study/String.txt')
str1 = file.read()
num1 = []
for x in range(len(str1)):
    val = str1[x:x+1]
    if(val.isdigit()):
        num1.append(val)
print("".join(num1))
```
