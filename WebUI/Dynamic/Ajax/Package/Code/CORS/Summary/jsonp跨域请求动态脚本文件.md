---
title: JSONP跨域请求动态脚本文件
date: 2016-04-26
tags: [JSONP,浏览器,跨域]
categories: Dynamic
---

利用JSONP进行跨域，其实就是利用动态创建`script` 标签，在请求中输入调用的`callback` 函数名，进行`get` 请求，当然来，要请求的页面必须是动态页面，比如`php` 类型，因为要返回数据的，静态页面无法返回数据。

a.com/.../ajsonp.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>jsonp</title>
	<script src="../../../jquery.min.js"></script>
</head>
<body>
	a_jsonp
	
	<script>
	var jsonp = document.createElement("script");
	jsonp.src = "//child.a.com/php/test/0426/b-file/b01.php?callback=jsonpCallback";
	document.getElementsByTagName("head")[0].appendChild(jsonp);

	function jsonpCallback(arr) {
		var str = "";
		for (var i in arr) {
			str += "<div>" + i + ":" + arr[i] + "</div>"
		}
		$("body").append(str);
	}
	</script>
</body>
</html>
```

b.com/../bjsonp.php

```php
<?php 
$jsonp = $_GET['callback'];
$data = array('a','b', 'c', 'd');
echo $jsonp.'('.json_encode($data).')';
```

