---
title: open
date: 2020-02-03 12:32:42
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# open

## 概要

- 打开文件使用`open`方法

## 模式

- `r`: 默认就以只读模式打开文件
- `r+`: 打开一个文件用于读写，文件指针会放在文件开头，读完就追加。
- `w`: 覆盖写，如果文件不存在就创建文件，通过write写入的内容会覆盖之前的内容
- `a`: 追加模式，write写入的内容会放到文件内容的末尾
- `a+`: 打开一个文件用于读写，文件存在则指针放在文件末尾，是追加模式，否则创建文件

## write

- `f.write('hello')` 打开文件后需要通过这个方法来写入文件
- 写入的内容默认是追加在上一行
- `\n` 换行，如果写入的内容要换行，需要在内容末尾添加

## read

- 默认read是一次性全部读取文件，而且只能读取一次，然后就把指针移动到来文件末尾
- 对于大的文件使用read会影响性能

## readline

- 按照行读取文件内容，每次只读取一行，
- 可以通过循环来读取内容

## with模式

- 通常打开的文件是需要close的，否则会一直占用内存
```python
with open('./test.txt') as f:
	f.read()
```

## 参考

- [python open函数](https://www.cnblogs.com/linshuhui/p/8984326.html)
