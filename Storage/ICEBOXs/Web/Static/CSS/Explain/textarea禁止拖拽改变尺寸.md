---
title: textarea禁止拖拽改变尺寸
date: 2016-09-28
tags: [CSS]
categories: Static
---

默认情况下`textarea`是可以动态调整尺寸的，但是可以通过设置`resize: none`来禁用这个功能。

对于这个需求有俩种方式可以达到预期效果：

- `resize: none`，但是这个似乎有兼容性问题，

- 通过限制尺寸，如下：

```CSS
textarea{
    max-width: 200px;
	min-width: 200px;
	width: 200px;
	max-height: 100px;
	min-height: 100px;
	height: 100px;
}
```