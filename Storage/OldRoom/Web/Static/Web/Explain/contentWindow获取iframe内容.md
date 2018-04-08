---
title: contentWindow获取iframe内容
date: 2016-04-26
tags: [跨域,浏览器]
categories: Dynamic
---

当页面插入`iframe` 时候，可以通过`contentWindow` 来获取或者设`iframe` 内容样式

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<iframe id="iframe" src="app.html" frameborder="0"></iframe>
</body>
</html>
```

因为`iframe` 引入页面需要时间，所以不能直接操作，否则得到的就是空值，因为页面刚开始`iframe` 还没有插入，所以可以考虑`onload` 或者`setTimeout` 延时函数。

如果使用`onload` 就需要考虑`IE` ，因为它不识别`onload`,所以需要一种兼容写法。

```javascript
var x = document.getElementById("iframe");
if (x.attachEvent) {
	x.attachEvent("onload", function() {
		addColor();
	});
} else {
	x.onload = function() {
		addColor();
	}
}

function addColor() {
	x.contentWindow.document.body.style.backgroundColor = "purple";
}
```

如果使用`setTimeout` 就比较简单来，但是延时间隔不好控制

```javascript
var x = document.getElementById("iframe");
setTimeout(function(){	
 x.contentWindow.document.body.style.backgroundColor="purple";
},2000);
```

