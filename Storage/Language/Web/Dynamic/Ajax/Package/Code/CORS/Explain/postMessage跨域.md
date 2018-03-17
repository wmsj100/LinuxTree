---
title: postMessage跨域
date: 2016-04-27
tags: [浏览器,跨域,HTTP]
categories: Dynamic
---

## Cross-document messaging

### Cross-document messaging 简介

由于同源策略的限制，JavaScript 跨域的问题，一直是一个颇为棘手的问题。HTML5 提供了在网页文档之间互相接收与发送信息的功能。使用这个功能，只要获取到网页所在窗口对象的实例，不仅同源（域 + 端口号）的 Web 网页之间可以互相通信，甚至可以实现跨域通信。 要想接收从其他窗口发送来的信息，必须对窗口对象的 onmessage 事件进行监听，其它窗口可以通过 postMessage 方法来传递数据。该方法使用两个参数：第一个参数为所发送的消息文本，但也可以是任何 JavaScript 对象（通过 JSON 转换对象为文本），第二个参数为接收消息的对象窗口的 URL 地址，可以在 URL 地址字符串中使用通配符'*'指定全部地。

### 在 Cross-document messaging 中使用 postMessage 和 onmessage

为了实现不同域之间的通信，需要在操作系统的 hosts 文件添加两个域名，进行模拟。

##### 清单 3. hosts 文件中添加两个不同的域名

```
 127.0.0.1 	 parent.com 
 127.0.0.1 	 child.com
```

在父网页中通过 iframe 嵌入子页面，并在 JavaScript 代码中调用 postMessage 方法发送数据到子窗口。

##### 清单 4. 父页面中嵌入子页面，调用 postMessage 方法发送数据

```
 <html> 
 <head> 
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
 <title>Test Cross-domain communication using HTML5</title> 
 <script type="text/JavaScript"> 
	 function sendIt(){ 
		 // 通过 postMessage 向子窗口发送数据
		 document.getElementById("otherPage").contentWindow 
			 .postMessage( 
				 document.getElementById("message").value, 
				"http://child.com:8080"
			 ); 
	 } 
 </script> 
 </head> 
 <body> 
	 <!-- 通过 iframe 嵌入子页面 --> 
	 <iframe src="http://child.com:8080/TestHTML5/other-domain.html" 
				 id="otherPage"></iframe> 
	 <br/><br/> 
	 <input type="text" id="message"><input type="button" 
			 value="Send to child.com" onclick="sendIt()" /> 
 </body> 
 </html>
```

在子窗口中监听 onmessage 事件，并用 JavaScript 实现显示父窗口发送过来的数据。

##### 清单 5. 子窗口中监听 onmessage 事件，显示父窗口发送来的数据

```
 <html> 
 <head> 
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
 <title>Web page from child.com</title> 
 <script type="text/JavaScript"> 
	 //event 参数中有 data 属性，就是父窗口发送过来的数据
	 window.addEventListener("message", function( event ) { 
		 // 把父窗口发送过来的数据显示在子窗口中
	   document.getElementById("content").innerHTML+=event.data+"<br/>"; 
	 }, false ); 

 </script> 
 </head> 
 <body> 
	 Web page from http://child.com:8080 
	 <div id="content"></div> 
 </body> 
 </html>
```

##### 图 2. 父窗口嵌入子窗口

![父窗口嵌入子窗口](http://www.ibm.com/developerworks/cn/web/1301_jiangjj_html5message/figure2.jpg)

##### 图 3. 父窗口发送数据到子窗口

![父窗口发送数据到子窗口](http://www.ibm.com/developerworks/cn/web/1301_jiangjj_html5message/figure3.jpg)

