---
title: print
date: 2020-02-04 19:18:22
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# print

## 概要

- 默认打印、输出在标准输出

## 进阶

- print还可以指定输出目标
```python
f = open('t1', 'w')
print('hello world!')
print('wmsj100')
f.close()
f = open('t1')
f.read() # 'hello world\nwmsj100'
f.close()
```

## 格式化字符串

- `%d` 十进制整数
- `%10d` 输出的整数宽度至少为10
- `%f` 浮点数
- `%2.3f` 最小宽度为2，以实际宽度为准，精度为3位小数
- `%s` 字符串
- `%20s` 输出的字符串宽度至少为20
- `'hello %s age is %d' % ('wmsj100', 23)`

## 参考

