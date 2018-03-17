---
title: a连接调到顶部问题
date: 2016-4-11 10:42:04
tags: [技巧]
categories: Dynamic
---

**问题**： 点奢侈品2的时候页面跳到了顶部，可能是什么原因？如何解决可能是将“奢侈品2”设置为`a`链接，同时`href="#"`，导致点击时跳到了顶部。解决方法：设置为`href="javascript:void(0)"`

```javascript
$("a").attr("href","javascript:void(0)");
```

