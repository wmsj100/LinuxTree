---
title: 布局
date: 2020-02-24 18:26:05
modify: 
tags: [Notes]
categories: layui
author: wmsj100
email: wmsj100@hotmail.com
---

# 布局

## 概要

- layui有属于自己的布局方案，类似bootstrap的栅格系统

## 使用

- `<div class="layui-contriner"></div>` 所有的标签都需要被这个标签包裹
- `layui-col-space`可以设置列间距，需要在`layui-row`设置。
- `layui-col-md-offset3`设置列偏移
```html
<div class="layui-contriner">
	<div class="layui-row layui-col-space10">
		<div class="col-md-5"></div>
	</div>
</div>

```
## 参考

