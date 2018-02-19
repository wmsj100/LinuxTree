---
title: Ajax通讯原理
date: 2016-4-5 13:21:43
tags: [Ajax,DOM,事件]
categories: Dynamic
---

ajax的通讯也是通过`TCP`协议进行的，需要进行3次握手，通过函数来进行讲解：
<!-- more -->
```html
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
    		console.log(xhr.readyState);
    		console.log(xhr.status);
    		xhr.onreadystatechange = function() {
    			console.log(xhr.readyState);
    			console.log(xhr.status);
    			if (xhr.status === 200 && xhr.readyState === 4) {
    				console.log(xhr.responseText);
    				mdiv.innerHTML = xhr.responseText;
    			}
    		}
    		xhr.open('get', 'ajax.php', true);
    		xhr.send();
    	});
    </script>
</body>
```

ajax.php

```php
    <?php 
    $x="this is my name";
    echo $x;
    ?>
```

当点击按钮`btn`的时候触发`ajax`,代码开始依次运行，当运行到

```javascript
var xhr = new XMLHttpRequest();
```

- 开始创建`xhr`的`ajax`接口，此时`xhr`就有了几个比较关键的属性，` onreadystatechange` 是一个监听函数，可以监听` readyState `的值，默认是0，当触发了`xhr.open() `时候，浏览器开始向服务器发送请求，此时`readyState=1`而通过` onreadystatechange `就可以监听到这一次的数值变化，然后给它绑定的函数就会进行操作，大致过程如下图：

![](/file/img/tool/April/0405/01.gif)

## ajax的三次握手

1. 浏览器通过`ajax`的`xhr.open('get',url,true)`来向服务器发送请求，服务器验证了这一次请求，并传回给浏览器，此时`xhr.readyState=1`, 状态`xhr.status=0`，表示服务器连接已经建立；这是第一次握手

2. 浏览器接收到服务器的连接建立消息之后就开始发送数据请求，` xhr.send( )` ，然后服务器查询浏览器的数据请求，如果在自己的目录中找到了数据，就给浏览器传回状态码`200`,如果服务器没有找到，就返回`404`;服务器在传回状态码的同时自己也开始到相应的目录中准备数据，如果是动态数据还有借助与PHP或MySQL，浏览器的`xhr.readyState=2`,表示服务器正在准备数据。这是第二次握手；

3. 服务器找到数据之后就会和浏览器进行第三次握手，告诉浏览器数据已经找到，请接收数据；浏览器接收到请求之后就会开始接收数据，此时`xhr.readyState=3`；等数据接收完成之后，浏览器会向服务器发送请求表示数据已经接收完毕，请断开连接；这是第三次握手；

4. 服务器接收到浏览器的请求之后就会断开连接，并在断开连接之前给浏览器确认信息，浏览器收到确认信息之后连接断开，此时`xhr.readyState=4`,这样请求就结束了，这是第四次握手；

