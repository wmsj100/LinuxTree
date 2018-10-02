---
title: ajax重复加载 重复点击
date: 2016-4-6 15:16:39
tags: [ajax,技巧,Error]
categories: Dynamic
---

### 点击按钮，使用 ajax 获取数据，如何在数据到来之前防止重复点击?

通过添加状态位，来识别此时ajax是否在加载中。通过给函数`ajax()`添加延时来观察是否加载来按钮保护防止重复点击。

```css
<style>
a{
	text-decoration: none;
}
.wrap .ct{
	/*margin: 20px 0;*/
	border: 1px solid #4BC443;
	padding: 10px;
	font-size: 20px;
	color: #333;
}
.wrap .btn{
	display: block;
	/*width: 80px;*/
	border: solid 1px #DF4141;
	height: 30px;
	line-height: 30px;
	text-align: center;
	font-size: 20px;
	padding: 5px 10px;
	color: #DF4141;
	font-weight: bold;
}
.wrap .btn-bg{
	color: #fff;
	background: #DF4141;
}
</style>
```

```html
<div class="wrap">
	<div class="list"></div>
</div>
```

```php
$status = $_REQUEST["status"];
$start = $_REQUEST["start"];
$len = $_REQUEST["len"];
// $status = "1";
// $start = 0;
// $len = 8;
$content = array();
if($status === "1"){
	for ($i=1; $i <=$len ; $i++) { 
		array_push($content, "内容".($i+$start));
	};
	
}
$transport = array("status"=>"success","items"=>$content);
echo json_encode($transport);
```

```javascript
ajax();
addBtn();
var animate = true;

function ajax() {

	$.ajax({
		url: "task-29-3_get.php",
		type: "get",
		dataType: "json",
		data: {
			"status": "1",
			start: $(".wrap .list").children().length,
			len: "14"
		},
		success: function(data) {
			if (data && data.status === "success") {
				$(".wrap .list").append(dealData(data.items));
			}
		},
		error: function(data) {
			console.log("error");
		},
		complete: function() {
			console.log(animate);
			animate = true;

		}
	});
}

function dealData(arr) {
	var str = "";
	for (var i = 0; i < arr.length; i++) {
		str += "<div class='ct' data-info=" + arr[i] + ">" + arr[i] + "</div>";
	}
	return str;
}

function addBtn() {
	$('<a class="btn" href="javascript:void(0)">加载更多</a>').appendTo($(".wrap"));
}

$(".btn").on("click", function() {

	if (!animate) {
		console.log(animate);
		return;
	}
	animate = false;
	console.log(animate);
	setTimeout(function() {
		ajax();
	}, 1000);
});
```

