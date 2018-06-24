---
title: post ajax 传输协议
date: 2016-4-6 15:52:58
tags: [Ajax]
categories: Dynamic
---

如果使用`post`协议的话，需要给post添加`header`头部，不然信息无法提交，头部如下，是固定格式：

```javascript
xhr.open("post",url,true);
xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xhr.send("name="+username);
```

后台对于协议是固定的，不可能还通过让用户选择是`post`还是`get`方法，因为一个php文件只支持一种协议，也就是说，不能通过·`if else`进行验证协议，

```php
if($_POST["name"]){
	$name=$_POST["name"];
};
if($_GET["name"]){
 	$name=$_GET["name"];
 }
```

这样是错误的写法。