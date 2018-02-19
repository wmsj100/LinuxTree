---
title: CSS选择器优先级
date: 2016-4-15 16:24:52
tags: [css,选择器]
categories: Dynamic
---

CSS选择器有一个优先级，如果在设置的时候，感觉书写是没问题的，可查看页面的时候，就是没有显示效果，那么这时候很可能是因为自己设置的选择器优先级不够，比如

```css
ul.opt li{
	float: left;
	margin: 0 10px;
	width: 50px;
	height: 8px;
	background-color: #999;
	border-radius: 5px;
	cursor: pointer;
}
.active{
	background-color: #333;
}
<li class="active"></li>
```

我想要让`li`的的第一个元素背景显示`#333`，可是我刷新页面的时候就是没有这个效果，查看CSS时候，发现我设置的元素被覆盖了，我觉得`class`的优先级也足够高了吧，可就是没有，然后我在`.active`前面添加了标签选择器`li`，刷新页面还是没有效果，

```css
li.active{
	background-color: #333;
}
```

然后我继续添加了父元素`.opt`，再刷新页面，有效果了，

```css
ul.opt li.active{
	background-color: #333;
}
```

可是此时我的选择器名称也太长了吧，这不是我想要的效果，所以我把前面的`class`选择器上面的父元素都去掉了，

```css
.opt{
	position: absolute;
	bottom: 100px;
	left: 50%;
	transform: translateX(-50%);
	}
.opt:after{
	content: "";
	display: block;
	clear: both;
	}
.opt li{
	float: left;
	margin: 0 10px;
	width: 50px;
	height: 8px;
	background-color: #999;
	border-radius: 5px;
	cursor: pointer;
}
li.active{
	background-color: #333;
}
```

这样我在`.active`前面只需要添加`li`标签就可以达到我想要的效果了，所以选择器前面不要盲目的添加标签名。