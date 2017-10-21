---
title: 函数封装-形成闭包-把值附到全局属性this
date: 2016-04-25
tags: [函数,封装]
categories: Dynamic 
---

正常情况下一个函数内部的变量很难被传递出去，要么形成闭包，值被引用，要么就直接命名为全局变量，就是那种没有`var`申明的变量，但是后者有一个隐患是污染全局变量，而且有很大的不安全因素，所以就需要下载这种函数封装方式。

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>01</title>
	<script src="../../jquery.min.js"></script>
</head>
<body>
<script>
var showExp = {
	init: function(str) {
		this.str = str;
      //首先把参数str引入到this的属性上面
      //成为来内部的全局变量
		this.show();
     //通过this来调用show函数
	},
	bind: function(handerStr) {
		var visite = "welcome to here " + handerStr;
		return {
			visite: visite
		};
	},
	show: function() {
		var obj = this.bind(this.str);
      //把参数str传递给bind函数
      //因为bind函数有一个返回值，
      //把返回值赋值给变量obj，
      //返回值就成为来obj的属性
		console.log(obj.visite);
		return obj.visite;
	}
}
showExp.init("wmsj100");
</script>
</body>
</html>
```

函数`bind`内部定义定义的变量`visite`通过return的方式被引入到另一个函数start内部的obj对象上面。