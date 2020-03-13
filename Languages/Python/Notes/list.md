---
title: 列表基础知识
date: 2019-03-03 10:11:38	
modify: 2020-03-13 22:00:29 
tag: [list]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# 列表基础知识

## 概述

- 列表和js的数组类似,不定长,不定类型,任意类型数值都可以append/insert/extend进入list
- 静态语言是没有数组的操作方法的,因为数组定长

- append 
- count a.count('a') 获取列表a中'a'出现的次数
- extend 再列表末尾一次性追加另一个序列中的多个值。
	- a[len(a):] = b
	- a.extend(b)
	- a=a+b
	- 上面三个结果是一样的，但是中间是效率最高的，而且可读性也最好
- list('asdf') => ['a', 'b', 'c', 'd']
- ''.join(somelist) => string
- somelist.insert(3, 'hello')  在列表的索引3位置插入'hello'字符串
- smlist.index('ha') 查找smlist中'ha’的第一次出现的索引，如果没有就报错
- smlist.pop() 默认移除最后一个值，并且返回该元素，意味着这个函数的结果可以赋值给一个变量
- smlist.pop(0) 移除第一个值
- smlist.remove('four') 移除列表的第一个匹配值
- smlist.reverse() 反转列表
- smlist.sort() 按照顺序直接修改smlist
	- smlist.sort(reverse=True) 按照逆序排序
	- smlist.sort(key=len) 按照长度排序
- sorted('python') # ['h', 'n', 'o', 'p', 't', 'y'] sorted可以用于任何序列却总是返回一个list

## 分片

- a=list('prel') # a=['p', 'r', 'e', 'l']
- a[1:] = list('python') # a=['p', 'p', 'y', 't', 'h', 'o', 'n']
- a[1:] = [] # a=['p']
- 从上面可以看出利用分片也可以实现对list的增删改

## 参考

- []()
