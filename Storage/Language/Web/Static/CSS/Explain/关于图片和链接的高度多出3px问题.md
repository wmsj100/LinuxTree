---
title: 关于图片和链接的高度多出3px问题
date: 2016-07-18
tags: [CSS]
categories: Static
---

对于`li`内部包含的图片链接，设置浮动之后，li的高度会多出`3px`，这是为什么呢，
查看`a`的高度会发现有默认的字体高度`16px`，
这是因为行内元素的默认对齐方式是基线对齐，所以需要改变垂直方向的对齐基线。

```css
a{
    font-size: 0;
}
img{
    vertical-align: bottom;
}
```

这样设置之后再查看`li`的高度就会发现已经是正常的了。