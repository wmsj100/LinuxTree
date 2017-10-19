---
title: prompt可输入弹出框
date: 2016-04-28
tags: [JavaScript]
categories: Dynamic
---

`alert()` 可以弹出内容框，`prompt("提示输入内容","默认的输入内容")`,当把`prompt` 赋值给变量`usename` 的时候，就可以获取用户输入的值。

```javascript
<body onload="ask()">
	<script>
		function ask() {
			var usename = prompt("输入姓名", "wmsj100");
			document.body.innerHTML += usename;
		}
	</script>
```

