---
title: JavaScript-DOM-视频解析-4
date: 2016-3-29 10:36:41
tags: [JavaScript,DOM]
categories: Dynamic
---

#### 再控制台输入document可以获得整个页面的信息（源代码）ni
<!-- more -->
```javascript
document
//#document;	获取页面所以信息
document.toString();
//"[object HTMLDocument]"
document.body;
//<body>...</body>	获得了body的内容
document.head;
//<head>...</head>	获得了head的内容
```

#### location——返回一个只读对象，提供了当前文档的URL（统一资源定位符）信息；

```javascript
document.location.href
//"https://www.baidu.com/"	获取整个地址
document.location.protocol
//"https:"	获取地址协议，默认情况是http，
//常见的协议有：http、https、file、ftp、ssh
document.location.host
//"www.baidu.com"	获取当前主机地址（包含端口）默认80
document.location.hostname	获取主机地址（不包含端口）
document.location.pathname
//"/wmsj100"	获取当前文档的路径，跟在主机地址后面
document.location.search	获取链接中的？后面的内容
document.location.hash	获取链接中的#内容，多用于单页
//"#/2"	（http://slides.com/fangfang/summary#/2）
documen.location.assign('http://www.baidu.com')
//页面会跳转到百度；

```

#### 页面跳转的方法——有3个

```
document.location.href="http://www.baidu.com"
window.open("http://www.baidu.com")
//通过这个方式会被浏览器拦截
document.location.assign('http://www.baidu.com')
```

#### location

```javascript
//location是一个全局对象，可以通过document\window\或者直接输入location就可以获得页面的location内容
document.location
window.location
location
//Location {hash: "", search: "", pathname: "/", port: "", hostname: "www.baidu.com"…}
location.href
//"https://www.baidu.com/"
location.reload()	//页面刷新
```

#### document

```javascript
document.title	
//"百度一下，你就知道"	获取页面title
document.charset
//"UTF-8"	获取页面的编码方式
document.readyState
//"complete"	页面处于完成状态
document.cookie	//获取页面的cookie
//"BAIDUID=0FB368C2F46194797EFC4C2FE10A8C2B:FG=1; BIDUPSID=0FB368C2F46194797EFC4C2FE10A8C2B; PSTM=1459215735; BD_HOME=0; H_PS_PSSID=18881_1423_18280_17001_15520_12171; BD_UPN=12314353"
//cookie是服务端写入浏览器页面的一小段数据；多和用户登录数据相关，服务端通过代码写入cookie，发送请求时候，给后天的数据会自动带上cookie
document.cookie=document.cookie+";"+"username=wmsj100"
//"BAIDUID=0FB368C2F46194797EFC4C2FE10A8C2B:FG=1; BIDUPSID=0FB368C2F46194797EFC4C2FE10A8C2B; PSTM=1459215735; BD_HOME=0; H_PS_PSSID=18881_1423_18280_17001_15520_12171; BD_UPN=12314353;username=wmsj100"
//添加cookie就是字符串的相加，再原来的基础上添加';'和想要写入cookie的字符串。
```

#### innerText

获取当前节点的文本内容

```javascript
document.getElementsByTagName("p")
//通过这个方式获取的时p标签的数组，即便只有一个p标签也是获取的数组；
document.getElementsByTagName("p")[0]
//获取第1个p标签内容
//<p>...</p>
p1=document.getElementsByTagName("p")[0]
p1.innerText
//""hello" wmsj100"	获取的是内部所有的文本
p1.innerHTML
//"
    	"hello"
    	<span>wmsj100</span>
    "	获取的时内部结构，包括span标签
p1.innerHTML='<a href="#">lllll</a>'
//lllll链接"
//可以通过p1.innerHTML给页面设置新的标签。
p1.innerText='<a href="#">lllll</a>'
//"<a href="#">lllll</a>"	
//生成的时文本，标签被转义符，
```

使用innerText会更加安全，可以防止用户的恶意输入，XSS注入脚本攻击。

#### document.write

会把页面的内容清空，不建议使用；一般不使用；

#### Element

```javascript
document.getElementsByTagName('p')[0]	
//获取标签名为p的内容，这个方法获得数组
<!-- 这是html内容----->
<p id="p2">我是段落2 <a class="link" href="#">hhahaha</a> </p>
//这是console.log
document.getElementsByClassName("link")
//[<a class="link" href="#">hhahaha</a>]
document.getElementById("p2").getElementsByClassName("link")
//[<a class="link" href="#">hhahaha</a>]
```

#### querySelector

语法类似jQuery，IE8以上都支持；

```javascript
document.querySelector('#p2')
//<p id="p2">...</p>
document.querySelector('.link')
//<a class="link" href="#">hhahaha</a>
document.querySelector('.p3')
//<p class="p3 title">我是段落3</p>
//默认是选择第一个元素，
document.querySelectorAll('.p3')
//[<p class="p3 title">我是段落3</p>, <p class="p3">我是段落4</p>]
//这样就选择了全部的元素。
document.querySelectorAll('.p3')[1]
//<p class="p3">我是段落4</p>
```

封装一个querySelector选择器函数

```javascript
function $(selector){
    	if(selector.[0]==="#"){
    		return document.querySelector(selector);
    	}
    	else{
    		return document.querySelectorAll(selector);
    	}
    }
```

#### Element元素属性

借用上面封装的选择器函数$来选择

```javascript
$("#p2").nodeName	//"p"
$("#p2").id	//"p2";
$("#p2").className	//""
$("#p2").className="classp2"	//"classp2"
//这是通过上面可以位元素添加属性
$("#p2").className=$("#p2").className+" ccc"
//"classp2ddd ccc"
//如果元素有class，那么就要通过字符串+来添加，
//注意添加的class前面一定要添加一个空格，
//不然新添加的class名词和原来的连在了一起
```

#### children/childNodes

```
$("#p2").children
//[<a class=?"link" href=?"#">?hhahaha?</a>?]
//它获取的时子标签的节点
$("#p2").childNodes
//["我是段落2 ", <a class=?"link" href=?"#">?hhahaha?</a>?, #text]
//获取所有的子节点，包括空格，文本
```

