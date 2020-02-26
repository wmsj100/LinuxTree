---
title: link和@import区别
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
页面使用css的方式主要有3种，标签行内引用，页面头部样式引用，外部样式引用，其中外部样式引用有link和import俩种；
link和import都可以对css样式进行外部引用，但它们还是有区别的。
link语法:
<!-- more -->
```
<link rel="stylesheet" type="text/css" href="css文件" media="all">
```
这个代码中有一个media，是用来制作响应式网页的，media=“all” 是用于所有设备， media=“screen” 用于电脑屏幕，平板电脑、智能手机场景，举个例子：
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>Examples</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
<style>
	@media screen and (max-width:800px){
		body{
			background-color: yellow;
		}
	}
</style>
</head>
<body>
   <h1> hello</h1>
</body>
</html>
```
这段代码表示当屏幕的宽度小于等于800像素的时候，页面背景是黄色

![宽度为1366px时候](http://upload-images.jianshu.io/upload_images/1606281-4c624801d405f80b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![宽度为700px时候](http://upload-images.jianshu.io/upload_images/1606281-a983e961db208c7e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
@import语法：
```
<style type="text/css" media="screen">
@import url("css文件");
</style>
```
> ### 俩者的区别有以下几点：

1. link是XHTML标签，除了可以引用css样式外还可以定义RSS等事物，但@import是css标签，只能引用css样式。
2. link在页面加载的同时加载，而@import是在页面内容加载完成之后加载的。
3. link是XHTML标签，没有兼容问题，而@import是在css2.1提出来的，低版本的浏览器不支持。
4. link支持使用javascript控制DOM去改变样式，@import不支持。

> 该文章参考文献:
[http://www.cnblogs.com/zbo/archive/2010/11/17/1879590.html](http://www.cnblogs.com/zbo/archive/2010/11/17/1879590.html)
