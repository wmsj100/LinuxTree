---
title: 通过document.title修改页面的标题
date: 2016-05-06
tags: [函数,封装,DOM]
categories: Dynamic
---

```html
<head>
	<meta charset="UTF-8">
	<title>DOM</title>
</head>
---
<script>
document.body.onload = function() {
	document.title = "wmsj100";	//修改标题；
}
</script>
```

通过onload函数在页面加载时候修改title，除非查看源代码，否则是无法看出破绽的。