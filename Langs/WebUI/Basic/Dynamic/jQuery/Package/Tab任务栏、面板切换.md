---
title: Tab任务栏切换、面板切换
date: 2016-4-9 16:45:54
tags: [jquery,函数]
categories: Dynamic
---

基础框架代码：HTML和CSS

```css
<style type="text/css">
	<style>
body,html,div,li,ul{
padding: 0;
margin: 0;
}
ul{
	overflow: hidden;
}
li{
list-style-type: none;
float: left;
width: 199px;
border: solid 1px #999;
text-align: center;
padding: 5px 0 5px 0;
font-weight: bold;
}
.active{
background-color: #333;
color: #fff;
cursor: pointer;
}

.panel{
	width: 560px;
	height: 260px;
	border: solid 1px #999;
	display: none;
	padding: 20px;
}
.hide{
	display: block;
}
</style>
```

```html
<div class="mod-tab">
 <ul class="tab">
<li class="tab1 active">tab1</li>
<li class="tab2">tab2</li>
<li class="tab3">tab3</li>
</ul>
<div class="panel hide">内容1</div>
<div class="panel">内容2</div>
<div class="panel">内容3</div>
</div>
```

jQuery代码：

```javascript
$(".tab li").on("click",function(){
		$ind=$(this).index();
  //获取点击的li的下标
		console.log($ind);
		$(this).siblings().removeClass("active");
  //把邻居的“active”去掉
		$(this).addClass("active");
  //给自己添加"active"
		$(".panel").eq($ind)
					.siblings()
					.removeClass("hide");
  //$(".panel").removeClass("hide");
  //去掉所有的“hide”
		$(".panel").eq($ind).addClass("hide");
  //给自己添加“hide”
	})
```

jQuery升级版，当有多个任务面板的时候，切换，找到当前点击的li的父元素，然后在父元素里面找寻panel子元素

```javascript
$(".tab li").on("click", function() {
	var $cur = $(this);
  //$(this)存储到$cur中，不用每次都转换，提高性能
	$ind = $cur.index();
	console.log($ind);
	$cur.siblings().removeClass("active");
	$cur.addClass("active");
	$cur.parents(".mod-tab").find(".panel").removeClass("hide");
	$cur.parents(".mod-tab").find(".panel").eq($ind).addClass("hide");
})
```



JavaScript代码

```html
<ul class="tab">
<li class="tab1">tab1</li>
<li class="tab2">tab2</li>
<li class="tab3">tab3</li>
</ul>
<div class="content"></div>
```

```css
<style>
body,html,div,li,ul{
padding: 0;
margin: 0;
}
li{
list-style-type: none;
float: left;
width: 199px;
border: solid 1px #999;
text-align: center;
padding: 5px 0 5px 0;
font-weight: bold;
}
li:hover{
background-color: #333;
color: #fff;
cursor: pointer;
}
.content{
width: 560px;
height: 260px;
border: solid 1px #999;
float: left;
padding: 20px;
}
```

```javascript
var tab = document.querySelector(".tab");
var content = document.querySelector(".content");
tab.addEventListener("mouseover", function(e) {
var tabName = e.target.className;
console.log(tabName);
switch (tabName) {
case "tab1":
content.innerText = "内容1";
break;
case "tab2":
content.innerText = "内容2";
break;
case "tab3":
content.innerText = "内容3";
break;
}
})
```

