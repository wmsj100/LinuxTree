---
title: window解析
date: 2016-06-22
tags: [BOM]
categories: Static
---

`window`既是`JS`访问浏览器窗口的一个接口，又是`ECMAJS`规定的`Global`对象。
在网页中定义的任何一个对象、变量、函数都以`window`作为其`Global`对象。

全局变量不能通过`delete`删除，而定义在`window`对象上的可以。
简单说就是使用`var`申明的变量不能被删除。

```javascript
var age = 10;
window.color = "red";
delete age/ delete window.age;  //false
delete color / delete window.color; //true
age / window.age;   //10
color / window.color;   //error
```

使用`var`语句添加的`window`属性有一个名为`[[configurable]]`的特性，这个特性的值被设置为`false`，因此这样设置的属性不能通过`delete`删除。