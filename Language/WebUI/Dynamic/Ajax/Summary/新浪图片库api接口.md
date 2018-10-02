---
title: 新浪图片库api接口
date: 2016-05-18
tags: [Ajax,jQuery]
categories: Dynamic
---

http://platform.sina.com.cn/slide/album_tech?app_key=1271687855&num=100&page=1

通过`$.getJSON()`来加载新浪的图片api

```javascript
$.getJSON("http://platform.sina.com.cn/slide/album_tech?app_key=1271687855&num=5&page=1&jsoncallback=?", function(data){
			console.log(data);
		})
```


```javascript
var num = 10,
	page = 1;
$.ajax({
	url: "http://platform.sina.com.cn/slide/album_tech",
	dataType: "jsonp",
	jsonp: "jsoncallback",
	data: {
		"app_key": "1271687855",
		"num": num,
		"page": page
	}
}).done(function(data) {
	console.log(data)
})
//Object {status: Object, total: "7624", count: "10", data: Array[10]}
```

