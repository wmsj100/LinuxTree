---
title: ajax
date: 2020-07-27 11:20:23
modify: 
tags: [Notes]
categories: jQuery
author: wmsj100
email: wmsj100@hotmail.com
---

# ajax

## 概要

- jquery对于ajax是对XMLHttpRequest的封装，让使用ajax非常简单
- ajax支持同步和异步请求，出于性能考虑，默认是按照异步的方式请求的
- jquery的ajax默认是按照异步发出的，如果需要同步请求，需要指明`async: false`

## 使用

```js
$.ajax({
	url: 'xxx',
	type: 'GET',
	dataType: 'json',
	async: true,
	success: function(data){
		console.log(data);
	}
});
```

## 参考

- [ajax 同步、异步](https://blog.csdn.net/ligang2585116/article/details/45484619)
