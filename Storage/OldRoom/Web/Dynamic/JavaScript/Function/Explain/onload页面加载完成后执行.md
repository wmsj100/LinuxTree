---
title: onload页面加载完成后执行
date: 2016-05-06
tags: [函数,封装]
categories: Dynamic
---

这个函数是在html标签上面执行，意思是在页面加载完成之后执行

```html
<script>
	document.body.onload = function(){
		console.log("hhh");	document.querySelector("ul").addEventListener("click",function(){
			this.removeChild(this.firstChild);
		},false);
	}
	var a = document.querySelector("ul");
</script>
---
<ul>
	<li><span>hello world--1</span></li>
	<li><span>hello world--2</span></li>
	<li><span>hello world--3</span></li>
</ul>
```

原生js的添加事件方法是通过`addEventListener` 来实现的，而不是`jQuery` 中的`on` ，这个要记住。

还有多使用原生js来实现基本效果。理解过程。