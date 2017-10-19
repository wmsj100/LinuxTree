---
title: a++-和-++a的优先级
date: 2016-03-24 12:18:58
tags: [JavaScript]
categories: Dynamic
---
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-7c1ff81e5d22ec8f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
<!-- more -->
- 从这是[MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#Table)上面说的，从这个表我们知道——a++的优先级是要高于——++a的，可是，实际测试的结果呢，不是，这样的，他俩在运算中是平级的，没有谁比谁优先的说法：
```
var a=1;
undefined
a++-++a
-2
var a=1;
undefined
++a-a++
0
```
