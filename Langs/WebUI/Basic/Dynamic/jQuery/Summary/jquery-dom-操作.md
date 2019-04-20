---
title: jquery dom 操作
date: 2016-4-9 21:50:15
tags: [jQuery,DOM]
categories: Dynamic
---

可以通过`$(".p").html("wmsj"+html)来给标签添加内容；

```javascript
var html=$(".p").html();
	$(".p").html("wmsj"+html);
```

通过`val()可以获取input输入框的值。也可以设置值；

```javascript
$("input").val()	//asjd
$("input").val("aaaaa")	//aaaaa
```

设置一个输入框，用户输入字母之后立即变为大写，监听的值是`keyup`;

```javascript
$("input").on("keyup",function(){$(this).val($(this).val().toUpperCase())})
```

图片实现懒加载，就是刚开始不加载图片，也就是不设置图片的`src`地址，而是把图片地址设置在自定义属性`data-img`,然后通过jQuery进行设置；

```javascript
<img data-img="http://fanyi.baidu.com/static/translation/img/header/logo_cbfea26.png" alt="" >
$("img").attr("src",$("img").attr("data-img"));
```

