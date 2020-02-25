---
title: template
date: 2020-02-25 15:30:26
modify: 
tags: [Notes]
categories: layui
author: wmsj100
email: wmsj100@hotmail.com
---

# template

## 概要

- layui里的模板我肯定不会使用了，因为它的变量没有django的变量好用
- 模板是放在script标签内部的，这个在当时也没有用好，我当初是body标签外部，然后设置一个隐藏的父标签包裹着。
- 首先那些最大的不好就是页面渲染时候会选择那些dom，影响性能，其次我的那个操作相当于是复制dom也是高消耗。

## 模板写法

```html
{% extends 'linux/base.html' %}

{% block content %}

{% load static %}
<script src='{% static 'linux/js/test14.js' %}'></script>

<script id="demo" type="text/html">
<div id="test11_include">
	<h1>This is a include</h1>
	<ul>
		<li><a href="">span_11</a></li>
		<li><a href="">span_21</a></li>
		<li><a href="">span_31</a></li>
		<li><a href="">span_41</a></li>
	</ul>
</div>
</script>
{% endblock %}
```

```js
layui.use(['layer', 'jquery'], function(){
	var layer = layui.layer,
		$ = layui.jquery;

	layer.ready(function(){
		layer.open({
			title: 'content',
			content: $('#demo').html()
		});
	});
});
```
- 上面这样的写法是最优雅的写法
- script的内容不会被渲染，只是也字符串的形式展示
- 上面那个写法还可以抽取出来当作类似vue那样的插件使用，提高复用性
```test12_tmp.html
{% load static %}
<link rel="stylesheet" href="{% static 'linux/css/style.css' %}">
<script id="demo" type="text/html">
<div id="test11_include">
	<h1>This is a include</h1>
	<ul>
		<li><a href="">span_11</a></li>
		<li><a href="">span_21</a></li>
		<li><a href="">span_31</a></li>
		<li><a href="">span_41</a></li>
	</ul>
</div>
</script>
```
```test12.html
{% extends 'linux/base.html' %}

{% block content %}

{% load static %}
<script src='{% static 'linux/js/test14.js' %}'></script>
{% include 'linux/test12_tmp.html' %}
{% endblock %}
```
- 像这样`test12_tmp`的组件就成了一个独立的组件，可以共用页面


## 参考

