---
title: 测试setInterval和setTimeout的效率
date: 2016-03-24 12:18:58
tags: [函数,封装]
categories: Dynamic
---

<!-- more -->
```
function timeTo(){
	for(var i=0;i<1000;i++){
	console.log(1);
	}
}
//通过测试timeto的函数执行时间需要200毫秒左右；
var i=0;
var j=0;

//这是timeOut的自执行函数
(function add(){
	setTimeout(function(){
		console.log("timeout--"+i++);
		timeTo();
		add();
	},1000);
	}())
	timeTo();
	
//这是timeInterval的自执行函数
(function timeInter(){
	setInterval(function(){
	console.log("interval--"+j++);
	timeTo();
},1000)
}())
function stop(){
	clearTimeout(1);
	clearInterval(1);
}
//interval--56
// interval--57
// timeout--44
// interval--58
// timeout--45
// interval--59
// timeout--46
// interval--60
// timeout--47
// 可以看到当setInterval执行到60的时候，setTimeout函数才执行到了47；
```
