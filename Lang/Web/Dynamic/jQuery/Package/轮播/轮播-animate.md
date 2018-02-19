---
title: 轮播-animate
date: 2016-4-14 18:53:52
tags: [jQuery]
categories: Dynamic
---

这是自动轮播，无缝轮播，

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>me</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<style>
	body,html,div,ul,li{
		margin: 0;
		padding: 0;
	}
	li{
		list-style-type: none;
	}
	a{
		text-decoration: none;
	}
	.carousel{
		width: 200px;
		height: 200px;
		position: relative;
		overflow: hidden;
	}
	.rectangle{
		position: absolute;
	}
	.rectangle:after{
		content: "";
		display: block;
		clear: both;
	}
	.rectangle li{
		float: left;
	}
	.rectangle li img{
		width: 200px;
	}

	.arrow{
		display: block;
		width: 30px;
		height: 30px;
		color: #fff;
		background-color: #333;
		top: 50%;
		margin-top: -15px;
		position: absolute;
		text-align: center;
		line-height: 30px;
		border-radius: 30px;
		opacity: 0.5;
	}
	.arrow:hover{
		opacity: 1;
	}
	.pre{
		left: 10px;
	}
	.next{
		right: 10px;
	}
	
	.opt{
		position: absolute;
		bottom: 10px;
		left: 50%;
		transform: translateX(-50%);
		

	}
	.opt li{
		display: inline-block;
		/*float: left;
		margin: 1px;*/
		width: 18px;
		height: 5px;
		background-color: #ccc;
		border-radius: 4px;
		cursor: pointer;
	}
	li.active{
		background-color: #666;
	}
</style>
</head>
<body>
	<div class="carousel">
		<ul class="rectangle">
			<li data-img="1"><a href="#"><img src="img/01.jpg" alt="轮播图片"></a></li>
			<li data-img="2"><a href="#"><img src="img/02.jpg" alt="轮播图片"></a></li>
			<li data-img="3"><a href="#"><img src="img/03.jpg" alt="轮播图片"></a></li>
			<li data-img="4"><a href="#"><img src="img/04.jpg" alt="轮播图片"></a></li>
		</ul>
		<a href="javascript:void(0)" class="pre arrow"><</a>
		<a href="javascript:void(0)" class="next arrow">></a>
		<ul class="opt">
			<li class="active"></li>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</div>
    <script>
    	var $rect = $(".rectangle"),
    		$child = $rect.children(),
    		$pre = $(".pre"),
    		$opt = $(".opt li"),
    		$next = $(".next"),
    		imgCount = $child.length,
    		imgWidth = $child.width();

    	$rect.prepend($child.last().clone());
    	$rect.append($child.first().clone());
    	var imgRealCount = $rect.children().length;
    	$rect.css({
    		width: imgWidth * imgRealCount,
    		left: 0 - imgWidth
    	});

    	$pre.on("click", function() {
    		playPre();
    	});
    	$next.on("click", function() {
    		playNext();
    	});
    	var rectIdx = 0,
    		animateStatus = false;
    	$opt.on("click", function() {
    		var idx = $(this).index();
    		$opt.removeClass("active").eq(idx).addClass("active");
    		opt(idx);
    	});

    	start(); //自动播放
    	function start() {
    		clock = setInterval(function() {
    			playNext();
    		}, 3000);
    	}

    	//停止自动播放
    	function stop() {
    		clearInterval(clock);
    	}

    	function opt(idx) {
    		stop();
    		console.log(idx);
    		if (idx > rectIdx) {
    			playNext(idx - rectIdx);
    		} else if (idx < rectIdx) {
    			playPre(rectIdx - idx);
    		}
    	}

    	function playNext(idx) {
    		stop();
    		if (!animateStatus) {
    			animateStatus = true;
    			var idx = idx || 1;
    			$rect.animate({
    				left: "-=" + imgWidth * idx
    			}, 1000, function() {
    				rectIdx += idx;

    				console.log(rectIdx);
    				if (rectIdx === imgCount) {
    					$rect.css({
    						left: -imgWidth
    					});
    					rectIdx = 0;
    					// $opt.removeClass("active").eq(rectIdx).addClass("active");
    				}
    				animateStatus = false;
    				$opt.removeClass("active").eq(rectIdx).addClass("active");
    				
    			});

    		}
    		start();
    	}

    	function playPre(idx) {
    		stop();
    		if (!animateStatus) {
    			animateStatus = true;
    			var idx = idx || 1;
    			$rect.animate({
    				left: "+=" + imgWidth * idx
    			}, 1000, function() {
    				rectIdx -= idx;
    				console.log(rectIdx);

    				if (rectIdx === -1) {
    					$rect.css({
    						left: -imgWidth * (imgCount)
    					});
    					rectIdx = 3;
    				}
    				$opt.removeClass("active").eq(rectIdx).addClass("active");
    				animateStatus = false;

    			});
    		}
    		start();
    	}
    </script>
</body>
</html>
```

