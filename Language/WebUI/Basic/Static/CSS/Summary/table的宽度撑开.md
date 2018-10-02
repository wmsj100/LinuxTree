---
title: table的宽度撑开
date: 2016-08-31
tags: [CSS]
categories: Static
---

对于表格布局的页面，如果宽度需要撑开，可以直接设置`td`的宽度为`955px`。

当然了，表格布局的`table`是不需要设置边框的，

如果要把`td`分割开，就是一行和一行直接有一个空白，那么需要把`tr`设置为`display: block`，然后添加`margin-bottom`就可以了。