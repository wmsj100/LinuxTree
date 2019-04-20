---
title: 验证标签class是否含有- "b"  hasClass()
date: 2016-4-1 17:14:21
tags: [DOM,函数,事件]
categories: Dynamic

---

验证标签中是否含有class名词为——b，并且在控制台输出，效果如下：
<!-- more -->
![](/file/img/tool/April/0401/04.gif)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>className</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="http://apps.bdimg.com/libs/bootstrap/3.3.4/css/bootstrap-theme.min.css
" rel="stylesheet">
<style>
	ul{
		float: right;
		margin-right: 60px;
		margin-top: 60px;
	}
	li{
		margin: 10px;
	}
</style>
</head>
<body>
	<ul id="wrap">
		<li><span class="d">item1</span></li>
		<li><span class="d a  c">item2</span></li>
		<li><span class="d">item3</span></li>
		<li><span class="c">item4</span></li>
		<a href="http://www.baidu.com" class="link">wmsj</a>
	</ul>
    <script>
    	var wrap=document.querySelector("#wrap");
    	wrap.addEventListener("click",function(e){
    		var className=e.target.className;
    		var arr=className.split(/\s+/g);
    		console.log(arr);
    		if(/d/g.test(arr)){
    			console.log(e.target.innerHTML);
    			return e.target.innerHTML;
    		}
    		else if(/link/g.test(arr)){
    			console.log("this is a link>>>");
    			return "this is a link>>>";
    		}
    		console.log(false);
    		return false;
    	},false)

    	//   取消a链接的跳转
    	var link=document.querySelector(".link");
    	link.addEventListener("click",function(e){
    		e.preventDefault();	
    	},false)

    </script>
</body>
</html>
```