---
title: 通过js一次性为元素设置多个样式属性
date: 2016-05-23
tags: [DOM,CSS]
categories: Dynamic
---
通过js一次性为元素设置多个样式属性:
在实际应用中可能需要为页面元素设置样式属性。
通常样式属性是各方面的，比如边框、背景或者字体大小等等。
实现此效果的方式多种多样，下面就介绍一下比较常用的两种方式。

一.使用style.cssText属性:
```html
<!DOCTYPE html>
<html>
<head>
<meta charset=" utf-8">
<meta name="author" content="http://www.softwhy.com/" />
<title>蚂蚁部落</title>
<script type="text/javascript"> 
window.onload=function(){
  var odiv=document.getElementById("antzone");
  odiv.style.cssText="color:blue;"
  +"text-align:center;"
  +"background-color:#ccc;"
  +"width:300px;"
}
</script>
</head>
<body>
<div id="antzone">蚂蚁部落</div>
</body>
</html>
```
这个属性非常的遍历，但是好像很多朋友更习惯于style.width="300px"这样的方式一条一条的设置。

对于字符串的分段写入，然后通过引号和链接符`+` 连接的效果那时候就已经写过了，但是因为不是我自己的东西，当时也只是顺眼看了一遍而已。

二.使用className实现此效果:
```html
<!DOCTYPE html>
<html>
<head>
<meta charset=" utf-8">
<meta name="author" content="http://www.softwhy.com/" />
<title>蚂蚁部落</title>
<style>
.set{
  color:blue;
  text-align:center;
  background-color:#ccc;
  width:300px;
}
</style>
<script type="text/javascript"> 
window.onload=function(){
  var odiv=document.getElementById("antzone");
  odiv.classList.remove("set");
  odiv.classList.add("set");
  // odiv.className="set";  //错误，因为这样是完全重置样式
}
</script>
</head>
<body>
<div id="antzone">蚂蚁部落</div>
</body>
</html>
```
