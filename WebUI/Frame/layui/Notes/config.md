---
title: config
date: 2018-05-04 22:21:17 Fri
modify: 2018-05-04 22:21:17 Fri
tag: [layui]
categories: Web
author: wmsj100
mail: wmsj100@hotmail.com
---

# config

## 概述
- 使用这个框架开始最主要的困惑是如何实现模块加载，经过将近俩小时的测试，现在搞明白了。
- 它定义模块的方法和`requirejs`还是很像的，我没有看出来有什么区别，或者说这样的优势在哪里，应该是还没有理解它的精华所在。
- `requireJs`不会把所有的模块都写在`config`内部，但是`layui`就需要，如果只是在根目录`base`下可以不写，否则就都需要在`extend`内显示的写出来。
- 但是这样的优势是如果调整目录位置时候只需要在`config`文件中修改即可，反之`requireJs`就需要修改每一个引用到的文件。

## 技巧
- layui.link('*.css'); 这样可以在页面动态加载`css`样式文件
## 范例
```js
<script>
	layui.config({
		base: "/static/helloWorld/js/"
	}).extend({
		'demo': 'test/demo'
	});
</script>
```
