---
title: ajax同步传输
date: 2016-4-8 12:04:56
tags: [Ajax,DOM]
categories: Dynamic
---

ajax延时5s传来数据，这个过程页面是死的，不能点击

这个过程利用了`PHP`的延时函数`sleep()`

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>ajax-2</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
    .p1{
        width: 300px;
        height: 1200px;
        background-color: yellow;
    }
</style>
</head>
<body>
    <input type="text" id="username" placeholder="username">
    <button id="btn">点击</button>
    <div class="show"></div>
    <div class="p1">wq</div>
    <script>
        var username=document.querySelector("#username").value;
        var btn=document.querySelector("#btn");
        var url="ajax02_01.php"+"?username="+username;

        var show=document.querySelector(".show");
        btn.addEventListener("click",function(){
            console.log(url);
            var xhr=new XMLHttpRequest();
            xhr.onreadystatechange=function(){
                // console.log(xhr.readyState);
                if(xhr.status===200 && xhr.readyState===4){
                    show.innerHTML=xhr.responseText;
                    console.log(username);
                }
            }
            xhr.open("get",url,false);
            xhr.send();
        })
    </script>
</body>
</html>
```

ajax02_01.php

```php
<?php
	$username=$_GET["username"];
if($username==="wmsj"){
	$ser=array("name"=>"wmsj","sex"=>"男","age"=>20);
}
else if($username==="wanghao"){
	$ser=array('name' =>"wanghao","sex"=>"男","age"=>30);
}
else{
	$ser=array("name"=>"wanmei","sex"=>"女","age"=>40);
}
sleep(5);
echo json_encode($ser);

// <?php
// 	$username = $_GET['username'];
// 	if($username === 'kevin'){
// 		$ret = array('sex'=>'男', 'age'=>18);
// 	}else if($username === 'hunger'){
// 		$ret = array('sex'=>'男', 'age'=>20);
// 	}else{
// 		$ret = array('sex'=>'女', 'age'=>30);
// 	}
// 	echo json_encode($ret);

```

