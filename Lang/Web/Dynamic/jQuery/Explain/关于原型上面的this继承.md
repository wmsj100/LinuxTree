---
title: 关于原型上面的this继承
date: 2016-07-13
tags: [jQuery]
categories: Dynamic
---

```javascript
var $wrap = $(this.wrap),
    top = $wrap.offset().top;

    <!-- 无效 -->

var wrap = this.wrap,
    $wrap = $(wrap),
    top = $wrap.offset().top;
    <!-- 有效 -->
```

因为是通过原型使用函数定义的wrap参数。所以需要先把参数引入，然后再处理参数。