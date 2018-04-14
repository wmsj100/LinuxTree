---
title: 表格tr无法设置边框
date: 2016-07-07
tags: [CSS]
categories: Static
---

[tr边框问题](https://segmentfault.com/q/1010000002575321);
当给 table 添加样式 border-collapse: collapse;时，下面的设置边框才有效果；如果去掉了这个属性，单独给 tr 设置 border-bottom 时，却没有效果。是怎么回事？

答：边框不折叠的表格 行,列，行组和列组是不具有border的

而且即便是设置了`border-collapse: collapse`,此时设置的`tr`的`border`的边框也是无法设置`padding`和`margin`的。也就是说，实际意义其实不大。

所以通常的做法是设置`th, td`的`margin-bottom`来达到更好地额效果。