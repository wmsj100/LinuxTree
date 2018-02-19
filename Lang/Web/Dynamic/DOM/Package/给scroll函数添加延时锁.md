---
title: 给scroll函数添加延时锁
date: 2016-05-10
tags: [函数,封装]
categories: Dynamic
---

滚动时候会监听，但是输出时候会判断，如果小于300ms，就清除之前的延时函数，重新监听，

```javascript
var clock;
window.onscroll = function() {
	if (clock) {
		clearTimeout(clock);
	}
	clock = setTimeout(function() {
		console.log(1);
	}, 1000);
};
```



