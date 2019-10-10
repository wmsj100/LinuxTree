---
title: jQuery ajax -2
date: 2016-4-12 21:57:07
tags: [Ajax,jQuery]
categories: Dynamic
---

我自己的测试代码

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>jquery-ajax</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<style>
	div{
		border: solid 2px #F35252;
		border-radius: 5px;
		padding: 10px;
		color: #F35252;
		font-weight: bold;
		cursor: pointer;
	}	
</style>
</head>
<body>
    <div class="content">this is alerady exit</div>
    <div class="addmore">add more</div>
    <script>
    var ready = true;
    	$(".addmore").on("click",function(){
    		var start = $(this).index();
    		var len=3;
    		
    		var me = $(this);
    		if(!ready){
    				return;
    			}
    			ready = false;
    			me.text("loading....");
    		$.ajax({
    			url: "03.php",
    			type: "post",
    			datatype: "json",
    			data: {
    				start: start,
    				len: len
    			},
    			success: function(data){
    				// console.log(JSON.parse(data).status);
    				if(data && JSON.parse(data).status==="success"){
    					// console.log(JSON.parse(data));
    				var json = JSON.parse(data).items;
    				for(var i=0;i<json.length;i++){
    					me.before('<div class="content">'+json[i]+"</div>")
    					}
    				}
    				else{
    					console.log(JSON.parse(data));
    				}
    			},
    			error: function(data){
    				console.log("error")
    			},
    			complete: function(data){
    				me.text("add more");
    				ready=true;
    			}
    		});
    	})
    </script>
</body>
</html>
```

03.php

```php
<?php
/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2016-04-12 21:14:08
 * @version $Id$
 */
$start = $_REQUEST["start"];
$len = $_REQUEST["len"];
// $start=3;
// $len=3;
$items=array();
$status="success";
for($i=0;$i<$len;$i++){
	array_push($items, "nei rong ".($start+$i));
}
$result = array("status"=>$status, "items"=>$items);
sleep(1);
echo json_encode($result);
```



