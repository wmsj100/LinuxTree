---
title: jQuery中关于clone
date: 2016-07-18
tags: [jQuery]
categories: Dynamic
---

之前我知道使用`clone(true)`时候会复制节点的`事件`，即便没有参数`true`，节点的子节点也会被复制，
但是今天在做`轮播`的控件时候发现，如果`clone()`，没有参数`true`，子节点的属性`data-title`没有被复制，
而设置`clone(true)`时候，就可以读取`data-title`自定义属性了，所以如果使用`clone`，那么就彻底一点，直接把绑定的事件和自定义属性也复制，