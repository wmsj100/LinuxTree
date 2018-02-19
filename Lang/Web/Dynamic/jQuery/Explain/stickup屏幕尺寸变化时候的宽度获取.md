---
title: stickup屏幕尺寸变化时候的宽度获取
date: 2016-07-12
tags: [jQuery]
categories: Dynamic
---

对于`stickup`的效果,当我改变视口尺寸时候,再滚动屏幕时候,会发现浮动的滚动条尺寸不对了,所以这个时候想到了要获取这个新的`width`值,所以自然而然的想到了`resize`.
但是要达到这个效果不一定非要使用`resize`.
因为宽度改变时候只会影响到宽度自适应的块级元素,而视口尺寸改变时候,需要滚动屏幕才会看到这个尺寸的改变,
所以在`scroll`事件上面重新获取并且设置宽度值就可以达到宽度实时的效果.

```javascript
$(document).ready(function() {
        ready();
        check();
    }).scroll(function() {
        scrollTop = $(this).scrollTop();
        // 当宽度改变时候需要获取新的宽度,获取宽度不需要实时,通过resize取触发,
        width = $wrap.width();  
        $wrap.prev().css("width", width);
        check();
    })
```

就像上面的,重新获取了宽度,并且重新设置了宽度.