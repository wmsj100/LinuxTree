---
title: 使用css实现的动画效果
date: 2016-09-08
tags: [CSS]
categories: Static
---

其实`jquery`的动画效果就是通过修改`css`属性值来实现的，所以动画其实就是通过`css`来实现的，那么我可以直接通过`css`来设置简单的动画，比如鼠标`hover`文字时候文字的位置变化和颜色变化。

```css
#OrderDetails .list a span{
	color: #555;
	margin-left: 5px;
	transition: color 0.2s;
}
#OrderDetails .list a:hover span{
	color: #ff1256;
	margin-left: 10px;
	font-style: italic;
}
```

上面这就是一个简单的动画。