---
title: setTimeout(function(){},0)——函数后置
date: 2016-03-24 12:18:58
tags: [函数,封装]
categories: Dynamic
---
---
<!-- more -->
```javascript
var a=1;
setTimeout(function(){
	console.log("before---",a);
		 a=2;
	console.log("after-----",a);
},0);
a=100;
console.log(a);
```
这个的执行顺序如下：
```
var a=1;
a=100;
console.log(a);	//100
setTimeout(function(){
	console.log("before---",a);	//100
		 a=2;
	console.log("after-----",a);	//2
},0);
```
