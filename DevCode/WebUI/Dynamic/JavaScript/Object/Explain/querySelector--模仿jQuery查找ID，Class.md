---
title: querySelector--模仿jQuery查找ID，Class
date: 2016-3-29 13:11:27
tags: [选择器,函数]
categories: Dynamic
---
---
<!-- more -->
```javascript
function $(selector){
    	if(selector.[0]==="#"){
    		return document.querySelector(selector);
    	}
    	else{
    		return document.querySelectorAll(selector);
    	}
    }
```

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>task-22-视频</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
</head>
<body>
    <script>
    function $(selector){
    	if(selector.[0]==="#"){
    		return document.querySelector(selector);
    	}
    	else{
    		return document.querySelectorAll(selector);
    	}
    }
    </script>
    <div>
    <p><span>wmsj100</span></p>
    <p id="p2">我是段落2 <a class="link" href="#">hhahaha</a> </p>
    <p class="p3 title">我是段落3</p>
    <p class="p3">我是段落4</p>
	</div>
</body>
</html>
```

