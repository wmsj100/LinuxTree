---
title: removeEventListener阻止事件
date: 2016-4-6 14:43:35
tags: [事件,DOM]
categories: Dynamic
---

通过给`addEventListener`添加函数名称，这样就可以通过`removeEventListener`来清除绑定的事件了。

```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>Examples</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
</head>
<body>
    <button>click</button>
    <script type="text/javascript">
    	var btn=document.querySelector("button");
    	function show(){
    		console.log("hello world");
    		btn.removeEventListener("click",show,false);
    	}
    	btn.addEventListener("click",show,false);
    </script>
</body>
</html>
```

