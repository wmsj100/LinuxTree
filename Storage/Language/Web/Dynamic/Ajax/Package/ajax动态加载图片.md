---
title: ajax动态加载图片
date: 2016-4-15 23:53:22
tags: [Ajax,动画]
categories: Dynamic
---

这是一个通过后台PHP生成img图片的data地址，然后通过js控制生成图片的方法，

```php
<?php
/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2016-04-15 16:59:12
 * @version $Id$
 */
$status = $_REQUEST["status"];
if($status === "1"){
	$content = array(
		"img05" => "img/05.jpg",
		"img06" => "img/06.jpg",
		"img07" => "img/07.jpg",
		"img08" => "img/08.jpg",
	);
	$status = array("status" => "success");
	$wrap = array($status,$content);
	echo json_encode($wrap);
}
```

```javascript
$.ajax({
	url: "task-27-4_get.php",
	type: "get",
	data: {
		"status": "1"
	},
	success: function(data) {
		if (data && JSON.parse(data)[0].status === "success") {
			var json = JSON.parse(data)[1];
			$(".wrap").empty().append(addData(json));
		}
	},
	error: function(data) {
		console.log("error");
	},
	complete: function() {
		listContent();
      //通过绑定ajax完成之后的函数，这样就可以读取页面动态生成的内容。
	}
});

function addData(json) {
	var str = "";
	for (var key in json) {
		str +=
			"<li data-bg-img=" + json[key] + ">" + '<a href="#">' + key + '</a></li>';
	}
	return str;
}
 //全部都是局部变量
function listContent() {
	$wrap = $(".wrap");
	imgWidth = $(window).width();
	imgCount = $wrap.children().length;
	$wrap.append($wrap.children().first().clone());
	$wrap.prepend($wrap.children().eq(imgCount - 1).clone());
	var imgRealCount = $wrap.children().length;
	$wrap.css({
		left: -imgWidth,
		width: imgRealCount * imgWidth
	});
	$(".wrap li").css({
		width: imgWidth
	});
	var dataImg = $wrap.children().eq(1).data("bgImg");
	console.log(dataImg);
	$wrap.children().eq(1).css({
		"background-image": "url(" + dataImg + ")"
	});
	// console.log($wrap.children().eq(2).data("bgImg"));
	// console.log($child);
	// return {
	// 	$wrap: $wrap
	// }

}
```

