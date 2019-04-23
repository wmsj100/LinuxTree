---
title: reference.md
date: 2018-03-13 09:31:40 Tue
modify: 2018-03-13 09:31:40 Tue
tag: [shell,basic]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# shell 关于引用
- shell的引用有4中，单引号、双引号、反引号、$();

## 单引号''
- 单引号引用是全引用，所有的特殊字符都只显示字符意思，不会进行变量的替换

### 范例
- a=$(date); //Tue, Mar 13, 2018 9:43:37 AM
- echo '$a' // '$a'

## 双引号""
- 双引号是部分引用，内部的特殊字符会进行编译解释和替换

### 范例
- echo "$a"; // Tue, Mar 13, 2018 9:43:37 AM

## 反引号``
- 反引号后面跟表达式
