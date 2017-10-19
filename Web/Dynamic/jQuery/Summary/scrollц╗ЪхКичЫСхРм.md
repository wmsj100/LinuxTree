---
title: scroll滚动监听
date: 2016-4-18 23:38:41
tags: [jQuery]
categories: Dynamic
---

当用户在元素内执行了滚动操作，就会在这个元素上触发`scroll`事件。它适用于`window`对象，但也可以是可滚动frames与CSS `overflow`属性设置为`scroll`的元素（或`auto`时，元素的显示高度小于其内容高度）。

```javascript
$(window).on("scroll",function(){
    		console.log(1);
    	})
```

```javascript
$nav = $(".nav");
$width = $nav.width();	//获取元素宽度
$height = $nav.height();	//获取元素高度
$top = $nav.offset().top;	//获取元素顶部偏移
$left = $nav.offset().left;	//获取元素左边界偏移
```

