---
title: jQuery创建元素DOM
date: 2016-4-19 15:59:09
tags: [jQuery,DOM]
categories: Blog
---

jQuery创建元素很简单，通过下面这种方式就可以。

```javascript
$("<p>hello wmsj100</p>").insertBefore($("body"))
```

即通过操作符`$()`来实现。