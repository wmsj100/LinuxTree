---
title: height和css方法获取的高度区别
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

通过`css.("height")`和`.height()`都可以获取元素的高度，区别是，前者获取的是带单位的数值，而且有时候会返回`auto`，这样的数值，但是，后者是经过计算页面信息获取的，返回的是数值，方便计算，所以建议使用后者，而不是前者，
俩者都可以同时设置尺寸。

```javascript
$("div").css("width");  //"200px"
$("div").width();   // 200
$("div").css("width", 300);
$("div").width("300");
```

