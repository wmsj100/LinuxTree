---
title: 关于absolute和float
date: 2016-05-12
tags: [CSS]
categories: Static
---

关于`z-index` 只能在定位元素中使用，也就是说只能在`position = absolute, relative, fixed` 中设置。

如果俩个元素一个设置了`position : absolute` ,一个设置了` float : left` ，虽然俩个元素都会脱离文档流，但是绝对定位会覆盖浮动，不管这俩个元素的先后顺序是怎样的。

```html
<style>
.wrap{
	width: 200px;
	height: 200px;
	background-color: #D88D8D;
	position: relative;
}
.a{
	width: 50px;
	height: 50px;
	background-color: yellow;
	position: absolute;
}
.f{
	width: 30px;
	height: 30px;
	background-color: green;
	float: left;
}
</style>
<div class="wrap">
    <div class="f"></div>
    <div class="a"></div>
</div>
```

而且无法给浮动设置`z-index` 来改变这种前后关系，所以只能把浮动也改为绝对定位，。