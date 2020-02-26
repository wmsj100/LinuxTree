---
title: object
date: 2020-02-16 12:23:40
modify: 
tags: [Notes]
categories: ES6
author: wmsj100
email: wmsj100@hotmail.com
---

# object

## 概要

- es6对对象也有增强

## 具体

- es6允许对象的属性直接写变量，这时候属性名就是变量名，属性值就是变量值
```js
name='wmsj100'
age=32
a = {name, age}
{name: "wmsj100", age: 32}
```

- `...`取出对象所有可遍历属性
```js
let a = {name: "wmsj100", age: 32}
let b = {...a}
b # {name: "wmsj100", age: 32}
```
- `b={...a, ...c}`合并俩个对象

## 新增方法

- assign `a=Object.assign({}, a,b)` 类似于之前的`_.extend`
- Object.is 判断俩个对象是否完全相等

## 参考

