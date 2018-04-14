---
title: CSS基础知识-margin-padding
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
### 问答
- line-height有什么作用？
  line-height是用于设置文本的行高的，或者说成行间距更形象些，加入文本很少，此时如果设置文本的line-height的值等于height，那么文本就会垂直居中
  <!-- more -->
```
p{
        height:20px;
        line-height:20px;
        }
```
但这种样式设置只能用于文本少的情况下，如果文本过多，只有第一行的文本是垂直居中的，其他文本会脱离样式行。
- 如何去查CSS熟悉的兼容性？比如inline-block哪些浏览器支持？
  可以借助[CAN I USE](http://caniuse.com/)网站去查看，在输入框中输入  inline-block 下面就会列出主流浏览器的兼容情况；可以看到IE浏览器至少要是IE8，其它浏览器因为可以直接升级软件，所以很少有兼容性的问题。

![inline-block浏览器支持情况](http://upload-images.jianshu.io/upload_images/1606281-016790df49f8c6b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- a标签的href，title，target是什么？title和alt有什么区别？如何在新窗口打开链接？
- a标签中的 href 用来指出链接路径，可以是完整的绝对路径，也可以是相对路径，考虑到网站的迁移和升级问题，链接多用相对路径。
```
<a href="http://www.erheizi.com/test/1.html" >erheizi</a>   
<!--这是绝对路径-->
<a href="1.html">erheizi</a>
<!--这是相对路径-->
```
- title的作用是：当鼠标移到链接上面时候，鼠标下方会浮现出一个文本框，内容就是链接的title描述
```
<a href="1.html" title="erheizi">erheizi</a>
```
![erheizi](http://upload-images.jianshu.io/upload_images/1606281-59ecc3b1d63b2702.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- target的作用是：当鼠标点击链接时候，链接的打开方式，常见的target值是_blank，表示链接在新页面中打开，默认值是_self，表示在当前页面中加载链接
```
<a href="1.html" title="erheizi" target="_blank">erheizi</a>
 - alt常见的用法是用来描述图片由于加载失败后显示的替代文本，titile是鼠标移动到目标上面的时候，在鼠标下方浮现的title提示框，这俩个应该没有什么关联或者相似性吧。
```
<img src="img-1.jpg" title="picture" alt="嫦娥一号卫星">
![嫦娥一号卫星](http://upload-images.jianshu.io/upload_images/1606281-9f3ca9f22d525b84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 在新窗口中打开链接只需要设置` a` 标签中的 `target="_blank"`即可。
- display:none和visibility:hidden有什么作用？有什么区别？
  俩者都可以是元素在页面不可见，但是`display:none`的作用效果是把元素从页面去除，元素后面的标签会自动上移来占据空出来的位置；
  而`visibility:hidden`只是把元素的透明度设置为0，是元素视觉上不显示，但元素实际上还在页面中占据位置，元素后面的元素也不会自动上移。

![原图片](http://upload-images.jianshu.io/upload_images/1606281-591c3203cfd48bae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![visibility的值为hidden](http://upload-images.jianshu.io/upload_images/1606281-72d4eda40ccf27ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![display的值为none时候](http://upload-images.jianshu.io/upload_images/1606281-7df0f4327948d4bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
---
### 代码
1. 写个div，边框为1px，#ccc，宽度为200px，高度为80px，内有一行文字`这里是饥人谷`，文字字体大小是14px，颜色#f0f，文字在div里垂直水平居中
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>task 6-1</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
	.div1{
		border:solid #ccc 1px;
		width:200px;
		height:80px;
		display: table-cell;
		vertical-align: middle;
		text-align: center;
	}
	.div1 p{
		font-size: 14px;
		color:#f0f;

	}
</style>
</head>
<body>
    <div class="div1">
    	<p>这里是饥人谷</p>
    </div>
</body>
</html>
```
![代码1](http://upload-images.jianshu.io/upload_images/1606281-5d86112c47e89c2e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1. 对于如下html代码
2. 给box加个边框 1px，#ccc；
3. 给header设置高度40px，左对齐，左内边距10px，文字16px，颜色#f00，下边框#ccc 1px；
4. 给content设置高度100px，内部a链接去掉下划线，颜色blue，鼠标放置上去后颜色变为red；
5. 给footer设置高度50px，内部btn设置边框1px #ccc，圆角3px，上下内边距4px，左右内边距3px，显示为inline-block，footer居中显示；
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>task 6-2</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
	body,div,h3,a{
		padding:0;
		margin:0;
	}
	.box{
		border:solid 1px #ccc;
		margin:10px;
	}
	.box .header{
		height:40px;
		text-align: left;
		padding-left: 10px;
		font-size:16px;
		color:#f00;
		border-bottom:solid #ccc 1px;
		position:relative;
	}
	.box .header .close{
		float:right;
		position:absolute;
		top:0;
		right:5px;
		text-decoration: none;
		color:red;
		font-weight: bold;
	}
	.box .content{
		height:100px;
	}
	.box .content a{
		text-decoration:none;
		color:blue;
	}
	.box .content a:hover{
		color:red;
	}
	.box .footer{
		height:50px;
		text-align: center;

	}
	.box .footer .btn{
		border:solid 1px #ccc;
		border-radius:3px;
		padding:4px 3px;
		display:inline-block;
		text-decoration: none;
	}
</style>
</head>
<body>
    <div class="box">
    	<div class="header">
    		<h3>我是标题</h3>
    		<a href="#" class="close" title="关闭">X</a>
    	</div>
    	<div class="content">
    		<h3>欢迎来到<a href="http://jirengu.com">饥人谷</a></h3>
    		<p>在这个大家庭你能快乐的学到更多前端技能</p>
    	</div>
    	<div class="footer">
    		<a href="" class="btn btn-cancel">取消</a>
    		<a href="" class="btn btn-confirm">确认</a>
    	</div>
    </div>
</body>
</html>
```
![代码-2](http://upload-images.jianshu.io/upload_images/1606281-3d55b1cbb9a59e6a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1. 写一个如下表格
   ![代码-3](http://upload-images.jianshu.io/upload_images/1606281-c5861efb5ff33cdf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>task 6-3</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
	#table_1{
		border-right:solid 1px #ccc;
		border-bottom:solid 1px #ccc;
		padding:10px;
		border-radius:5px;
		box-shadow: 4px 4px 20px 3px #333;
	}
	.table1{
		border-collapse: collapse;
		width:100%;
		font-family: "Microsoft Yahei";

	}
	.table1 tr{
		text-align: center;
	}
	.table1 tr:hover{
		background-color: #eee;
	}
	.table1 tr th{
		background-color: #11AAAB;
	}
	.table1 tr th,.table1 tr td{
		padding:10px;
		border:solid 1px #ccc;
	}
</style>
</head>
<body>
	<div id="table_1">
    <table class="table1">
    	<tr>
    		<th>姓名</th>
    		<th>性别</th>
    	</tr>
    	<tr>
    		<td>小明</td>
    		<td>男</td>
    	</tr>
    	<tr>
    		<td>小花</td>
    		<td>女</td>
    	</tr>
    </table>
    </div>
</body>
</html>
```
1. 下面的代码有什么作用，举例说明
```
.center{
		width:200px;
		height:200px;
		display:table-cell;
		text-align: center;
		vertical-align: middle;
		background-color: #ccc;
	}
```
这段代码的意思是把`class="center"`的块元素转换为`table-cell`，即表格元素，然后设置元素的水平对齐方式为居中`text-align:center;`；垂直对齐方式为中间对齐`vertical-align:middle`；效果如下图：

![代码-4](http://upload-images.jianshu.io/upload_images/1606281-b4e6ad2afde5f9ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
