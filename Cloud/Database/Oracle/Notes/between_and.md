---
title: between_and
date: 2020-11-02 19:21:07
modify: 
tags: [Notes]
categories: Oracle
author: wmsj100
email: wmsj100@hotmail.com
---

# between_and

## 概要

- between and 查詢效率和<=类似，都会进行转换操作，
```
但是between and中间有一步就是转义成 >= <=
所以直接用>= <= 会好一些。
实际上那点转义的消耗，可以忽略。
```

## 参考

- [oracle between and](http://www.itpub.net/thread-1005365-1-1.html)
