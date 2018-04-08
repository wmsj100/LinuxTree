---
title: 常见列表样式--list-style
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
 - 有序列表：列表前面有数字、字母或其他阿拉伯字符的表示序列的字符，属于块级元素，能够继续嵌套各种形式的标签：
<!-- more -->
 - 无序列表：列表前面是实心圆的、空心圆点、方块、或者自定义图片……总之就是无法区分列表顺序的排序方式，无序列表也可以不限制数量和形式的继续嵌套其他标签：
 - 钩子方式：在IE6时代，人们为了实现自定义图标列表，进行了很多尝试，有的大神就使用了钩子方式，在列表-li-俩测添加空的div，通过设置border各边的样式或宽度也可以实现很多图标，当然这些空的div是没有语义化的，只是为了在不引入图片的情况下实现自定义样式，可以参考：
 - 其实通过样式控制可以很明显的看出，无序列表和有序列表的边界是很模糊的，可以使用有序列表（ol）来实现无序列表的所有样式，反之亦可，只是为了语义化的需要，如果涉及到排序时候，还是建议使用有序列表。不涉及排序时候，使用无序列表。

![列表样式](http://upload-images.jianshu.io/upload_images/1606281-933dcf53b34c2ea0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>task-7-1</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
	*{
		padding:0;
		margin:0;
	}
	body{
		font-family: "Microsoft Yahei",Arial;
		font-size: 16px;
	}
	.list-style{
		border:dashed #555 1px;
		overflow: hidden;
		padding:10px 0;
		border-radius: 5px;
		text-align: center;
		width:1000px;
		margin:20px auto;
	}
	.list-style h3{
		color:#555;
		border-bottom: dashed 1px #555;
		padding-bottom: 10px;
	}
	.list-style>div{
		text-align: center;
		display: inline-block;
		margin:10px;
		padding: 10px;
		border:dotted 1px #999;
		border-right: solid 3px #666;
		border-bottom: solid 3px #666;
		border-radius:10px;
	}
	.list-style div h3{
		color:#333;
		border-bottom: dashed 1px #666;
		margin-bottom: 5px;
	}
	.list-style ol{
		list-style-position: inside;
	}
	.decimal ol{
		list-style-type: decimal;
	}
	.disc ol{
		list-style-type: disc;
	}
	.circle ol{
		list-style-type: circle;
	}
	.square ol{
		list-style-type: square; 
	}
	.decimal-leading-zero ol{
		list-style-type: decimal-leading-zero;
	}
	.lower-roman ol{
		list-style-type: lower-roman;
	}
	.upper-roman ol{
		list-style-type: upper-roman;
	}
	.lower-alpha ol{
		list-style-type: lower-alpha;
	}
	.upper-alpha ol{
		list-style-type: upper-alpha;
	}
	.img ol{
		list-style-image: url("1.png");
	}
	
	.gou-zi ol{
		list-style: none;

	}
	.gou-zi ol div.left{
		width:0;
		height:0;
		border:#555 solid 10px;
		border-top-color:#fff ;
		border-right-color:#fff;
		border-bottom-color: #fff; 
		display: inline-block;
		position: relative;
		top:5px;
		left:0px;
	}
	.gou-zi ol div.right{
		width:0;
		height:0;
		border:#555 solid 10px;
		border-top-color:#fff ;
		border-left-color:#fff;
		border-bottom-color: #fff; 
		display: inline-block;
		position: relative;
		top:5px;
		right:2px;
	}
	.user-style dt{
		font-size: 18px;
		font-weight: bold;
		color:#333;
		border-bottom: dashed 1px #555;
		padding-bottom: 10px;
	}
	.user-style dd:first-of-type{
		margin-top: 10px;
		color:red;
	}
	.user-style dd:last-child{
		color:rgba(123,345,23,0.5);
	}
	.user-style dd:nth-child(3){
		color:purple;
	}

</style>
</head>
<body>
    <div class="list-style">
    	<h3>常见列表样式</h3>
    	<div class="decimal">
    		<h3>decimal</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="disc">
    		<h3>disc</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="circle">
    		<h3>circle</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="square">
    		<h3>square</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="decimal-leading-zero">
    		<h3>decimal-leading-zero</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="lower-roman">
    		<h3>lower-roman</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="upper-roman">
    		<h3>upper-roman</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="lower-alpha">
    		<h3>lower-alpha</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="upper-alpha">
    		<h3>upper-alpha</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="img">
    		<h3>img</h3>
    		<ol>
    			<li>list-lab</li>
    			<li>list-lab</li>
    			<li>list-lab</li>
    		</ol>
    	</div>
    	<div class="gou-zi">
    		<h3>钩子</h3>
    		<ol>
    			<li><div class="left"></div>list-lab <div class="right"></div></li>
    			<li><div class="left"></div>list-lab <div class="right"></div></li>
    			<li><div class="left"></div>list-lab <div class="right"></div></li>
    		</ol>
    	</div>
    	<div class="user-style">
    		<dl>
    			<dt>自定义列表</dt>
    			<dd>list-tab</dd>
    			<dd>list-tab</dd>
    			<dd>list-tab</dd>
    		</dl>
    	</div>
    </div>
    sss

</body>
</html>
```
