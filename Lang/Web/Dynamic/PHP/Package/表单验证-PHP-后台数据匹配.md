---
title: 表单验证-PHP-后台数据匹配
date: 2016-4-6 00:17:06
tags: [PHP,函数,jax]
categories: Dynamic
---
> `ajax`封装
> <!-- more -->


```php
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>01</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
</head>
<body>
<input type="text" class="user" >
<button class="btn">获取信息</button>
<div class="show"></div>
<script>

var btn = document.querySelector(".btn");
var show = document.querySelector(".show");
btn.addEventListener("click",function(){
	var user = document.querySelector(".user").value;
	console.log(user);
	var url = "02.php"+"?username="+user;
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function(){
	    if(xhr.status === 200 && xhr.readyState === 4){
	    	show.innerHTML = jsonData(xhr.responseText);
	    	}
	    }
	    xhr.open("get",url,true);
	    xhr.send();
},false);
function jsonData(str){
	var jsonStr = JSON.parse(str);
	var info = "";
	for(var i in jsonStr){
		info += "<dt>" + i + "</dt><dd>" + jsonStr[i] + "</dd>";
	}
	info=info.replace(info , "<dl>" + info + "</dl>");
	return info;
}
</script>
</body>
</html>
```

02.php代码：

```php
<?php
	$username=$_GET["username"];
if($username==="wmsj"){
	$ser=array("name"=>"wmsj","sex"=>"男","age"=>20);
}
else if($username==="wanghao"){
	$ser=array('name' =>"wanghao","sex"=>"男","age"=>30);
}
else if($username==="wanmei"){
	$ser=array("name"=>"wanmei","sex"=>"女","age"=>40);
}
else{
	$ser="false";
}
echo json_encode($ser);
```

