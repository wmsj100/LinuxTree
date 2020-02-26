---
title: 延时300ms进行滚动监听scrolltop
date: 2016-04-22
tags: [jQuery,动画]
categories: Dynamic
---

浏览器的`$(window).scrollTop()`函数可以监听滚动条滚动距离，但是因为监听的时间间隔太小了，所以比较耗费性能，可以通过timeout延时函数来变相的实现调整监听时间间隔的效果，因为它只是针对滚动监听函数操作，如果在300ms内，就不会执行`scrollTop`里面的函数，而只是重置监听函数，这个损耗就很小了。

```javascript
$(window).on("scroll", function() {
	if (clock) {
		clearTimeout(clock);
	}
	clock = setTimeout(function() {
		console.log(1);
	}, 1000);
});
```

javascript

```javascript
var clock;
		window.onscroll = function(){
			if(clock){
				clearTimeout(clock);
			}
			clock = setTimeout(function(){
				console.log(1);
			},1000)
		}
```

延时300ms进行监听，首先需要时刻的监听，所以这个延时操作是再scroll函数内部进行的，