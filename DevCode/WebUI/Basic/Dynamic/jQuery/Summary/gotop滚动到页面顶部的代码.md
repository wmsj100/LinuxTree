---
title: gotop滚动到页面顶部的代码
date: 2016-09-14
tags: [jQuery]
categories: Dynamic
---

```js
	$top.click(function(){
		$('html,body').animate({scrollTop: '0px'}, 500);
	});
```