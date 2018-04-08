---
title: 如何在HTML不同的页面中，共用头部与尾部
date: 2016-05-09
tags: [HTML,JavaScript]
categories: Frame
---

如何在HTML不同的页面中，共用头部与尾部？，共用尾部

一、asp语言和PHP语言

首先制作一个头部文件head.asp，或者一个底部文件foot.asp。如主页是index.asp，调用头部代码是在index.asp文件代码的开始位置（第一个标记后面，<head>标记前面）增加如下代码：

<!–  #include file=”head.asp”    –> 

调用共用底部文件代码是在index.asp文件代码的结束位置（最后一个标记前面）增加如下代码：

<!–     #include file=”foot.asp”    –>

 

如果是PHP文件，文件名改为 footer.php即可。

二、html语言
制作一个共用头部文件head.htm或一个共用底部文件foot.htm。如主页文件是index.htm，调用头部和底部文件的方法是：在主页文件代码的开始位置和结束位置分别增加下面的代码：
```html
<iframe MARGINWIDTH=0 MARGINHEIGHT=0 HSPACE=0 VSPACE=0 FRAMEBORDER=0 SCROLLING=no src=”head.htm” height=“auto” width="100%"></iframe>

<iframe MARGINWIDTH=0 MARGINHEIGHT=0 HSPACE=0 VSPACE=0 FRAMEBORDER=0 SCROLLING=no src=”foot.htm” height="auto" width="100%"></iframe>
```
比如下面的代码主页面：index.html
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
<link href='head.css'  rel="stylesheet" type="text/css" />
<script type="text/javascript">
</script>
</head>
<body >
//主页面index.html
<div class='miaov_head'>
   <iframe MARGINWIDTH=0 MARGINHEIGHT=0 HSPACE=0 VSPACE=0 FRAMEBORDER=0 SCROLLING=no src="head.html" width="100%"  height="auto">
  </iframe>--------这里调用head.html页面，需要使用div包起来，否则样式会发生改变
</div>

</body>
</html>
```
单独存放的head.html代码如下：
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
 <link href='head.css'  rel="stylesheet" type="text/css" />
</head>
<body >
 <div class='miaov_head'>
    <ul>
      <li><a href="http://www.cnblogs.com/jtjds/">Mac</a></li>
      <li><a href="http://www.cnblogs.com/jtjds/">iPad</a></li>
      <li><a href="http://www.cnblogs.com/jtjds/">iPhone</a></li>
      <li><a href="http://www.cnblogs.com/jtjds/">Watch</a></li>
      <li><a href="http://www.cnblogs.com/jtjds/">Music</a></li>
      <li><a href="http://www.cnblogs.com/jtjds/">Contact Us</a></li>
    </ul>
</div>

</body>
</html>
```
css样式代码如下：
```css
*{margin:0;padding:0;}
body{background:white;position:relative;height:100%;color: #777;font-size: 13px;}
img{border:none;display:block;}
li{list-style:none;text-decoration: none;}
.miaov_head{height:36px;width:100%;margin:0 auto;background: black;margin-bottom: 0px;}
.miaov_head  img{width: 30px ;height: 30px;margin-top: 0;margin-left: 130px;}
.miaov_head  ul{float: left;width:900px;height: 36px;margin-top: 0px;color: white;position: absolute;top: 0px;margin-left: 200px;}
.miaov_head  ul li{float: left;padding-left: 80px;margin-left: 0px;color: white;list-style: none; }
.miaov_head  ul li a{color: white;font-size: 14px;text-decoration: none;}
.miaov_head input{position: absolute;top: 5px;margin-left: 1000px;width: 200px;height: 22px;}
.miaov_head a{line-height:36px;color:#777;}
.miaov_head a:hover{color:#555;}
```
三、script语言--推荐这种
     制作一个共用头部文件head.js和一个共用底部文件foot.js。如主页文件是index.htm，调用头部和底部文件的方法是：在主页文件代码的开始位置和结束位置分别增加下面的代码:<script src=’head.js’>和<script src=’foot.js’>调用共同的网页头部或者网页底部，减少了每个页面都要编写头部或底部的复杂程度，而且方便修改，只要修改一个头部或者底部文件，所有页面的头部或者底部都随之改变，增加了工作效率。

   比如：head.js文件------根据上面的head.html，利用转换工具：http://tool.chinaz.com/Tools/Html_Js.aspx

   html转换为JS:
```javascript
document.writeln("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">");
document.writeln("<html xmlns=\"http://www.w3.org/1999/xhtml\">");
document.writeln("<head>");
document.writeln("<style>");
document.writeln("</style>");
document.writeln("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />");
document.writeln("<title></title>");
document.writeln(" <link href=\'head.css\'  rel=\"stylesheet\" type=\"text/css\" />");
document.writeln("</head>");
document.writeln("<body >");
document.writeln(" <div class=\'miaov_head\'>");
document.writeln("    <ul>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">Mac</a></li>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">iPad</a></li>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">iPhone</a></li>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">Watch</a></li>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">Music</a></li>");
document.writeln("      <li><a href=\"http://www.cnblogs.com/jtjds/\">Contact Us</a></li>");
document.writeln("    </ul>");
document.writeln("</div>");
document.writeln(" ");
document.writeln("</body>");
document.writeln("</html>");
document.writeln("");
```
 以后无论在哪个页面，想调用该头部文件，直接插入head.js文件即可：下面是随便建的一个页面，//MAC.html
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>
 <script type="text/javascript" src="head.js"></script>-------------------这里调用head.js
</head>
<body >

</body>
</html>
```
四：shtml文件

   1：使用ssi技术页面生成shtml文件，只用在头部文件位置加入<!--#include file="header.htm" -->，然后修改的时候只要修改header.htm文件就可以了。使用shtml的好处是对搜索引擎比较友好，需要处理的文件在服务器端完成的， 不会加重访问者的浏览器负担。

五：本地合并

  即将HTML硬拆成头、尾、内容三个部分的文件，在预览或者发布之前用脚本手工合并。很久以前用过，没有后台的时候使用效果不错。

六：ajax动态拉取填充

七：web服务器（比如IIS）中设定包含

   比如我们说的SSI，文档后缀名是.shtml的就可以使用include包含。

   SSI（Server Side Include)，通常称为"服务器端嵌入"或者叫"服务器端包含"，是一种类似于ASP的基于服务器的网页制作技术。默认扩展名是 .stm、.shtm 和 .shtml。SSI就是在HTML文件中，可以通过注释行调用的命令或指针，SSI具有 强大的功能，只要使用一条简单的SSI命令就可以实现整个网站的内容更新，时间和日期的动态显示，以及执行shell和CGI脚本程序等复杂的功能。

八：后台模板引擎处理（字符串拼接）

九：用图片、flash等外部资源做---不推荐，比较麻烦

十：angular js里的<ng-include>的使用

 差不多在静态的html页面中，引入头部和尾部的文件的方法就这么多，列举了一些，其它的感兴趣的可自行钻研。

