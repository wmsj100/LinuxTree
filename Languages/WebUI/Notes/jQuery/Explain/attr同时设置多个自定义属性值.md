---
title: attr同时设置多个自定义属性值
date: 2016-07-18
tags: [jQuery]
categories: Dynamic
---

通过`attr`方法可以通过设置多个自定义属性值。以键值对的方式在对象中设置。

```javascript
$("<span>").attr({"name": "wmsj", "age": 12});
// <span name="wmsj" age="12"></span>
```

