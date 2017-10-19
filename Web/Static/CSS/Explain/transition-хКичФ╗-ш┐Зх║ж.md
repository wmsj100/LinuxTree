---
title: transition 动画 过度
date: 2016-4-6 21:24:01
tags: [CSS,效果]
categories: Dynamic
---

`transition`——是css3的标签，有浏览器兼容问题，IE10，常用于过度效果的表示，如`hover`
<!-- more -->

```css
<style type="text/css">
	body{
		font-family: "Microsoft Yahei";
	}
	a{
		border: solid 1px #ccc;
		display: block;
		font-size: 18px;
		padding: 8px;
		margin: 10px;
		border-radius: 5px;
		text-decoration: none;
		color: #333;
		transition: background 0.3s;
	}
	a:hover{
		text-decoration: none;
		background-color: #E27272;
		color: #fff;
	}
	.btn{
		display: block;
		width: 100px;
		margin: 0 auto;
		background-color: #fff;
		color: #E27272;
		border: solid 2px #E27272;
		padding: 5px 10px;
		font-size: 18px;
		font-weight: bold;
		border-radius: 8px;
		transition: background 0.3s;
	}
	.btn:hover{
		background-color: #E27272;
		color: #fff;
	}
</style>
</head>
<body>
	<div class="wrap">
	    <a href="#">内容1</a>
	    <a href="#">内容2</a>
    </div>
    <button class="btn">加载更多</button>
```

![](/file/img/tool/April/0406/01.gif)