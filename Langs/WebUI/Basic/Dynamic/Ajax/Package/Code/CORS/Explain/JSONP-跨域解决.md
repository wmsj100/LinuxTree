---
title: JSONP 跨域解决
date: 2016-04-26
tags: [浏览器,跨域,JSONP]
categories: Dynamic
---

## 原理解析

### 1. 什么是JSONP

jsonp是一个非官方协议，它允许在服务器端集成Script tags返回至客户端，通过javascript callback的形式实现跨域访问（这仅仅是jsonp简单的实现形式）。单向的数据请求。

### 2. JSONP的原理与实现思路

1. Web页面调用js文件，可跨域。扩展：但凡有`src` 属性的标签都具有跨域能力。
2. 跨域服务器动态生成数据，并存入js文件（通常json后缀），供客户端调用。
3. 为了便于客户端使用数据，形成一个非正式传输协议，称为JSONP。该协议的重点是允许用户传递一个callback参数给服务器，然后服务器返回数据时，将此callback参数作为函数名包裹住JSON数据，使得客户端可以随意的定制自己的函数来自动处理返回的数据。

### 3. 使用JSONP

**动态创建script，添加到head中（你可以往body中添加）。**

在发起方页面动态加载一个script，script的URL指向接收方的一个处理地址（后台），该地址返回的javascript方法会被执行，另外URL中可以传入一些参数，该方法只支持GET方式提交参数。

```javascript
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />  
<script type="text/javascript">  
    function jsonpCallback(result) {  
        //alert(result);  
        for(var i in result) {  
            alert(i+":"+result[i]);//循环输出a:1,b:2,etc.  
        }  
    }  
    var JSONP=document.createElement("script");  
    JSONP.type="text/javascript";  
    JSONP.src="http://crossdomain.com/services.php?callback=jsonpCallback";  
    document.getElementsByTagName("head")[0].appendChild(JSONP);  
</script>
```

js文件载入成功后会执行我们在url参数中指定的函数，并且会把我们需要的json数据作为参数传入。所以jsonp是需要服务器端的页面进行相应的配合的。

**接收方服务器端代码**（php）如下：

```php
<?php
$callback = $_GET['callback'];//得到回调函数名
$data = array('a','b','c');//要返回的数据
echo $callback.'('.json_encode($data).')';//输出
?>
```

JSONP易于实现，但是也会存在一些安全隐患，如果第三方的脚本随意地执行，那么它就可以篡改页面内容，截获敏感数据。但是在受信任的双方传递数据，JSONP是非常合适的选择。

