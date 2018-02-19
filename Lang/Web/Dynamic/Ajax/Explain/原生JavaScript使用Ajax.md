---
title: 原生JavaScript使用Ajax
date: 2016-4-5 09:47:51
tags: [ajax,DOM]
categories: Dynamic
---

# Ajax

- ajax是`Asynchronous JavaScript and XML`的缩写，这一技术可以向服务器请求额外的数据而无需卸载页面。


<!-- more -->

- 传统的`HTTP`请求流程是这样的：

  - 浏览器向服务器发出请求
  - 服务器根据浏览器的请求生成`response`;
  - 服务器把`response`传回给浏览器；
  - 浏览器刷新整个页面显示最新数据；

  这个过程是同步的、按照顺序进行的。

  - `ajax`在浏览器与服务器的传输过程中使用异步数据传输，

    这里的异步指的是脱离当前浏览器页面的请求、加载等单独执行，这意味着在不需要重新加载页面的情况下，通过`JavaScript`发送请求、接受服务器传来的数据，然后操作`DOM`将新数据对网页的某部分进行更新。

    使用`ajax`最直观的感受就是获取数据不需要重新加载页面；


## XMLHttpRequest对象

`ajax`的核心是`JavaScript`对象`XmlHttpRequest`，这个对象为向服务器发送请求和接收数据提供了流畅的接口。`XmlHttpRequest`可以使用`JavaScript`向服务器提出请求并处理响应，而不阻塞用户。
一个浏览器兼容的创建`XHR`对象的函数写法如下：

```javascript
function createXHR(){
    var xhr = null;
    try {
        // Firefox, Opera 8.0+, Safari，IE7+
        xhr = new XMLHttpRequest();
    }
    catch (e) {
        // Internet Explorer
        try {
            xhr = new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch (e) {
            try {
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                xhr = null;
            }
        }
    }
    return xhr;
}
```

## `XHR`对象用法

### `XHR`对象有俩个重要的方法`open` , `send`;

- `open( method , url , async)`——`method`请求的类型`get , post`俩种；`url`文件在服务器上的位置；`async`有俩个参数`true`表示异步，`false`表示同步，这个一般不用；

- 在使用`XHR`对象时要调用的第一个方法是`open`

  ```
  xhr=new XmlHttpRequest();
  xhr.open('get','default.html',true);
  ```

  这段代码会针对`default.html`页面发送`get`请求，关于这段代码有三点需要注意：

  1. `URL`是相对于当前页面的路径，也可以使用绝对路径；
  2. 调用`open`并不会真的发送请求，而是初始化一个请求准备；
  3. 只能向同一个域中使用相同协议和端口的`URL`发送请求，否则会因为安全原因报错，（同源策略）；

- 要想把请求发往服务器需要调用`send`方法，`send`方法接受一个参数，参数是请求主体要发送的数据，如果不需要发送数据则传入`null`,在调用`send`方法之后请求被发往服务器；

  `xhr.send(null);`

- 请求发往服务器，服务器根据请求生成`response`,传回给`xhr`,在收到响应后相应的数据会填充到`xhr`对象的属性，有四个相关属性会被填充；

  1. `response Text`：作为响应主体被返回的文本；
  2. `response XML`：如果响应内容的类型是`text/xml`或`application/xml`，这个属性将保存包含着相应`XML`数据的`XML`文档；
  3. `status`：响应的HTTP状态（200 ,404, 500[服务器内部错误] );
  4. `status Text` ：`HTTP`状态说明；

- 在收到响应后第一步是检测响应状态，确保响应是否成功返回（200），如果成功，`response Text` , `response XML`可以被访问，为了确保响应有效，我们可以这样检查状态码：

  ```javascript
  xhr.open('get','default.html',false);//准备同步请求
  xhr.send();
  if(xhr.status >= 200 && xhr.status < 300 || xhr.status = 304){
    //do something;
  }else{
    //error handler;
  }
  ```

  上面的代码在发送请求的时候没问题，只有得到响应后才会执行检查`status`状态；

  但是在异步请求时，JavaScript会继续执行，不等生成响应就检查状态码，这样我们不能保证检查状态码语句是在得到响应后执行（实际上也几乎不可能，服务器再快一个HTTP请求也不会快过一条JavaScript执行速度）

- 这时候我们可以检查`XHR`对象的`readyState`属性，该属性表示请求响应时候的当前状态，每当`readyStatus`的值改变一次，都会触发`onreadystatechange`事件，

  1. `onreadystatechange`——存储函数或函数名，每当`readyState`值改变时，就会调用该函数；

  2. `readyState`——存有`XmlHttpRequest`状态，从0-4发生变化；

     0——请求未初始化；

     1——服务器连接已经建立；

     2——请求已接收；

     3——请求处理中；

     4——请求已完成，且响应已就绪；

  3. `status`—-'200'--'OK'; '404'--'未找到页面'；

- 我们可以利用这个事件检查每次`readyState`变化的值，当为4的时候表示所有的数据准备就绪，有一点需要注意，必须在`open`事件之前指定`onreadystatechange`事件出来程序；

  ```javascript
  var xhr = new XmlHttpRequest();
  xhr.onreadystatechange = function(){
    if(xhr.readyState==4 && xhr.status == 200){
    	setContainer('Original Ajax: ' + xhr.responseText);
  	}
  }
  xhr.open('get','ajax.aspx?action=getTime',true);
  xhr.send();
  ```

  我们可以在接受响应之前调用`abort`方法取消异步请求；

  `xhr.abort();`

## `Ajax`-简单的`GET`

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>get</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
</head>
<body>
	<fieldset>
		<legend>简单的GET</legend>
	    <div class="mydiv1">
			<h2>我的名字</h2>
		</div>
		<button class="btn">修改内容</button>
	</fieldset>
    <script>
    	var mdiv = document.querySelector(".mydiv1");
    	var btn = document.querySelector(".btn");
    	btn.addEventListener("click", function() {
    		var xhr = new XMLHttpRequest();
    		xhr.onreadystatechange = function() {
    			if (xhr.status === 200 && xhr.readyState === 4) {
    				mdiv.innerHTML = xhr.responseText;
    			}
    		}
    		xhr.open('get', 'ajax.php', true);
    		xhr.send();
    	})
    </script>
</body>
</html>
```

ajax代码：

```php
    <?php 
    $x="this is my name";
    echo $x;
    $name=
    ?>
```

---

## 带有参数的GET



每个HTTP请求都会带有Header信息，XHR对象也提供了操作这请求Header和响应Header信息的方法，在默认情况下，发送HTTP请求还会发送下列头部信息

1. Accept：浏览器能够处理的内容类型
2. Accept-Charset：浏览器能够处理的字符集
3. Accept-Encoding：浏览器能够处理的压缩编码
4. Accept-Language：浏览器当前设置的语言
5. Connection：浏览器与服务器的连接类型
6. Cookie：当前页面的cookie
7. Referer:发送请求的页面的URI

可以使用`setRequestHeader`方法设置自定义请求Header信息，这个方法接受俩个参数：

1. 头部字段的名称；
2. 头部字段的值；

必须在调用`open`之后`send`之前调用`setRequestHeader`;

## GET和POST请求

GET请求是最常见的请求类型，用于向服务器查询信息，必要时可以将查询字符串参数放在URL尾部发送给服务器，如果参数有特殊字符必须正确编码。我们上面使用的例子都是使用GET请求，非常简单，向服务器询问数据，然后处理数据。

POST请求用于把数据作为主体向服务器提交，POST请求主体可以包含多种格式数据，在open方法第一个参数传入”POST”就可以初始化一个POST请求。发送POST请求第二步就是向send方法传输数据参数，参数可以是xml或者字符串，json等。

## 最后

关于Ajax的总结就到这里，本文介绍的是纯JavaScript使用Ajax很是繁琐复杂，很多优秀JavaScript框架都对JavaScript操作Ajax做了很好封装处理，使用起来非常方便，最出名的是jQuery的ajax了，微软也对Ajax做了很好的封装处理，使其在ASP.NET页面中使用起来相当简单方便，相关知识可以看看[ASP.NET中使用Ajax](http://www.cnblogs.com/dolphinX/p/3242408.html)。









​	







