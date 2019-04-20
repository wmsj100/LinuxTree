---
title: 关于data值的设置
date: 2016-07-12
tags: [jQuery]
categories: Dynamic
---

如果想要查看或者元素的自定义属性(以`data-`开头),则可以直接调用`data`方法.

```javascript
$("img:eq(3)").data();  // 可以查看目标图片的所以自定义属性
$("img:eq(3)").data("load");    // 可以查看自定义属性`load`的值
$("img:eq(3)").data("load1",2); // 可以添加自定义属性`load1`的值
```

通过`jQuery`设置的`data`属性值不会显示的标识出来,也就是说,即便通过上面的方法设置来值,但是查看`html`时候并没有显示自定义属性,但是通过`data / attr`查看自定义属性时候却是存在的.
这一点需要注意.