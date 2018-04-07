---
title: JavaScript跨域
date: 2016-04-26
tags: [浏览器,跨域,JSONP]
categories: Dynamic
---

js跨域是指通过js在不同的域之间进行数据传输或通信，比如用ajax向一个不同的域请求数据，或者通过js获取页面中不同域的框架中(iframe)的数据。只要协议、域名、端口有任何一个不同，都被当作是不同的域。

同源策略阻止从一个域上加载的脚本获取或操作另一个域上的文档属性。也就是说，受到请求的 URL 的域必须与当前 Web 页面的域相同。这意味着浏览器隔离来自不同源的内容，以防止它们之间的操作。

| *URL*                                    | *说明*            | *是否允许通信*               |
| ---------------------------------------- | --------------- | ---------------------- |
| [http://www.a.com/a.js](http://www.a.com/a.js)http://www.a.com/b.js | 同一域名下           | 允许                     |
| `http://www.a.com/lab/a.jshttp://www.a.com/script/b.js` | `同一域名下不同文件夹`    | 允许                     |
| `http://www.a.com:8000/a.jshttp://www.a.com/b.js` | 同一域名，不同端口       | 不允许                    |
| `http://www.a.com/a.jshttps://www.a.com/b.js` | `同一域名，不同协议 不允许` | 不允许                    |
| `http://www.a.com/a.jshttp://70.32.92.74/b.js` | 域名和域名对应ip       | 不允许                    |
| [http://www.a.com/a.js](http://www.a.com/a.js)http://script.a.com/b.js | 主域相同，子域不同       | 不允许                    |
| [http://www.a.com/a.js](http://www.a.com/a.js)http://a.com/b.js | 同一域名，不同二级域名（同上） | 不允许（cookie这种情况下也不允许访问） |
| [http://www.cnblogs.com/a.js](http://www.cnblogs.com/a.js)http://www.a.com/b.js | 不同域名            | 不允许                    |

JavaScript出于安全方面的考虑，同源策略不允许跨域调用其他页面的对象。但在安全限制的同时也给注入iframe或是ajax应用上带来了不少麻烦。

javascript跨域简单分为以下情况：

> 1、基于同一父域的子域之间，如：a.c.com和b.c.com 
>
> 1、基于同一父域的子域之间，如：a.c.com和b.c.com 
> 2、基于不同的父域之间，如：www.a.com和www.b.com 
>
> 1、基于同一父域的子域之间，如：a.c.com和b.c.com 
> 2、基于不同的父域之间，如：www.a.com和www.b.com 
> 3、端口的不同，如：www.a.com:8080和www.a.com:8088 
>
> 1、基于同一父域的子域之间，如：a.c.com和b.c.com 
> 2、基于不同的父域之间，如：www.a.com和www.b.com 
> 3、端口的不同，如：www.a.com:8080和www.a.com:8088 
> 4、协议不同，如：[http://www.a.com和https://www.a.com](http://www.a.xn--comhttps-1c2n//www.a.com)

对于端口和协议的不同，需要通过后台proxy来解决，具体方式如下：

> a、在发起方的域下创建proxy程序 
>
> a、在发起方的域下创建proxy程序 
> b、发起方的js调用本域下的proxy程序 
>
> a、在发起方的域下创建proxy程序 
> b、发起方的js调用本域下的proxy程序 
> c、proxy将请求发送给接收方并获取相应数据 
>
> a、在发起方的域下创建proxy程序 
> b、发起方的js调用本域下的proxy程序 
> c、proxy将请求发送给接收方并获取相应数据 
> d、proxy将获得的数据返回给发起方的js

而情况1和2除了通过后台proxy这种方式外，还可以有几种办法来解决：

### 一.JSONP

JSON is a subset of the object literal notation of JavaScript. Since JSON is a subset of JavaScript, it can be used in the language with no muss or fuss.

#### 1.什么是JSONP

JSONP(JSON with Padding)是一个非官方的协议，它允许在服务器端集成Script tags返回至客户端，通过javascript callback的形式实现跨域访问（这仅仅是JSONP简单的实现形式）。单向的数据请求。

#### 2.JSONP的原理与实现思路

1）Web页面调用js文件，可跨域。扩展：但凡有src属性的标签都具有跨域能力。
2）跨域服务器 动态生成数据 并存入js文件(通常json后缀)，供客户端调用。
3）为了便于客户端使用数据，形成一个非正式传输协议，称为JSONP。该协议重点是允许用户传递一个callback参数给服务器，然后服务器返回数据时 将此callback参数作为函数名包裹住JSON数据，使得客户端可以随意定制自己的函数来自动处理返回数据。

#### 3.使用JSONP

**动态创建script，添加到head中（你可以往body中添加）。**

在发起方页面动态加载一个script，script的URL指向接收方的一个处理地址（后台），该地址返回的javascript方法会被执行，另外URL中可以传入一些参数，该方法只支持GET方式提交参数。

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
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

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

js文件载入成功后会执行我们在url参数中指定的函数，并且会把我们需要的json数据作为参数传入。所以jsonp是需要服务器端的页面进行相应的配合的。

**接收方服务器端代码**（php）如下：

```
<?php
$callback = $_GET['callback'];//得到回调函数名
$data = array('a','b','c');//要返回的数据
echo $callback.'('.json_encode($data).')';//输出
?>
```

JSONP易于实现，但是也会存在一些安全隐患，如果第三方的脚本随意地执行，那么它就可以篡改页面内容，截获敏感数据。但是在受信任的双方传递数据，JSONP是非常合适的选择。

### 二.通过修改document.domain来跨子域

浏览器都有一个同源策略，其限制之一就是第一种方法中我们说的不能通过ajax的方法去请求不同源中的文档。 它的第二个限制是浏览器中不同域的框架之间是不能进行js的交互操作的。主域相同，子域不同。

需要说明的是，不同的框架之间（父子或同辈），是能够获取到彼此的window对象的，但获取到的window对象几乎无用（html5中的postMessage方法是一个例外）。

#### 1.document.domain用于不同子域的框架间的交互

如，有一个页面，它的地址是[http://www.example.com/a.html](http://www.example.com/a.html)  ， 在这个页面里面有一个iframe，它的src是http://example.com/b.html, 很显然，这个页面与它里面的iframe框架是不同域的，所以我们是无法通过在页面中书写js代码来获取iframe中的东西的。

我们只要把http://www.example.com/a.html 和 [http://example.com/b.html这两个页面的document.domain都设成相同的域名就可以了。](http://example.com/b.html%E8%BF%99%E4%B8%A4%E4%B8%AA%E9%A1%B5%E9%9D%A2%E7%9A%84document.domain%E9%83%BD%E8%AE%BE%E6%88%90%E7%9B%B8%E5%90%8C%E7%9A%84%E5%9F%9F%E5%90%8D%E5%B0%B1%E5%8F%AF%E4%BB%A5%E4%BA%86%E3%80%82)

但要注意的是，document.domain的设置是有限制的，我们只能把document.domain设置成自身或更高一级的父域，且主域必须相同。例如：a.b.example.com 中某个文档的document.domain 可以设成a.b.example.com、b.example.com 、example.com中的任意一个，但是不可以设成 c.a.b.example.com,因为这是当前域的子域，也不可以设成baidu.com,因为主域已经不相同了。

在页面 [http://www.example.com/a.html](http://www.example.com/a.html) 中设置document.domain:

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<iframe src="http://example.com/b.html" id="iframe" onload="test()"></iframe>
<script>
    document.domain = 'example.com';//设置成主域
    function test(){
        alert(document.getElementById('iframe').contentWindow);
    }
</script>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

在页面 [http://example.com/b.html](http://example.com/b.html) 中也设置document.domain，而且这也是必须的，虽然这个文档的domain就是example.com,但是还是必须显示的设置

```
<script>
    document.domain = 'example.com';//设置成主域
</script>
```

这样我们就可以通过js访问到iframe中的各种属性和对象了。

不过如果你想在http://www.example.com/a.html 页面中通过ajax直接请求http://example.com/b.html 页面，即使你设置了相同的document.domain也还是不行的，所以修改document.domain的方法只适用于不同子域的框架间的交互。

如果你想通过ajax的方法去与不同子域的页面交互，除了使用jsonp的方法外，还可以用一个隐藏的iframe来做一个代理。原理就是让这个iframe载入一个与你想要通过ajax获取数据的目标页面处在相同的域的页面，所以这个iframe中的页面是可以正常使用ajax去获取你要的数据的，然后就是通过我们刚刚讲得修改document.domain的方法，让我们能通过js完全控制这个iframe，这样我们就可以让iframe去发送ajax请求，然后收到的数据我们也可以获得了。

#### 2.document.domain和iframe实现站内AJAX跨域

如：A：[http://www.css88.com/demo/iframe-domain/](http://www.css88.com/demo/iframe-domain/)要获取B：[http://css88.com/demo/iframe-domain/city.html的数据，在](http://css88.com/demo/iframe-domain/city.html%E7%9A%84%E6%95%B0%E6%8D%AE%EF%BC%8C%E5%9C%A8)[A](http://www.css88.com/demo/iframe-domain/) 页面内动态插入一个与B相同域的iframe C[：http://css88.com/demo/domain/iframe.html](http://css88.com/demo/domain/iframe.html) 。B与C可以通信，A通过控制C来获取B的数据。代码如下：   

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
document.domain = "css88.com";

var createAjaxIframe={
    appIframe: function(iframeId, iframeSrc){
        var iframe = document.createElement("iframe");
        iframe.src = iframeSrc// "http://css88.com/demo/domain/iframe.html";
        iframe.id = iframeId;
        iframe.style.display = "none";
        if (iframe.attachEvent) {
            iframe.attachEvent("onload", function(){
                createAjaxIframe.domainAjax(iframeId);
            });
        }else {
            iframe.onload = function(){
                createAjaxIframe.domainAjax(iframeId);
            };
        }
        document.body.appendChild(iframe);
    },
    domainAjax: function(iframeId){
        var iframeDom = document.getElementById(iframeId).contentWindow.$;
        iframeDom.getJSON("http://css88.com/demo/iframe-domain/city.html", function(date){
            var cityOption = "";
            for (i = 0; i < date.length; i++) {
                cityOption += date[i].c_name + "--" + date[i].c_value + "<br />"
            }
            $("#test").html(cityOption);
        });
    }
    
};
createAjaxIframe.appIframe("iframe",http://css88.com/demo/iframe-domain/iframe.html);
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

[演示地址](http://www.css88.com/demo/iframe-domain/)

### 三.window.name实现的跨域数据传输

window对象有个name属性，该属性有个特征：即在一个窗口(window)的生命周期内,窗口载入的所有的页面都是共享一个window.name的，每个页面对window.name都有读写的权限，window.name是持久存在一个窗口载入过的所有页面中的，并不会因新页面的载入而进行重置。

**原理**

有三个页面：

有三个页面：
a.com/app.html：应用页面。

有三个页面：
a.com/app.html：应用页面。
a.com/proxy.html：代理文件，一般是一个没有任何内容的html文件，需要和应用页面在同一域下。在应用页面动态创建iframe

有三个页面：
a.com/app.html：应用页面。
a.com/proxy.html：代理文件，一般是一个没有任何内容的html文件，需要和应用页面在同一域下。在应用页面动态创建iframe
b.com/data.html：应用页面需要获取数据的页面，可称为数据页面。

总结起来即：iframe的src属性由外域转向本地域，跨域数据即由iframe的window.name从外域传递到本地域。这个就巧妙地绕过了浏览器的跨域访问限制，但同时它又是安全操作。

实现起来基本步骤如下：

#### 1.数据页面b.com/data.html代码如下：

```
<script type="text/javascript">
    window.name = 'I was there!';    // 这里是要传输的数据，大小一般为2M，IE和firefox下可以
                                               大至32M左右
                                           // 数据格式可以自定义，如json、字符串
</script>
```

#### 2.应用页面a.com/app.html代码如下：

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE>
<html>
<head>
    <title>跨域获取数据</title>
    <script type="text/javascript">
    function domainData(url, fn)
    {
        var isFirst = true;
        var iframe = document.createElement('iframe');
        iframe.style.display = 'none';
        var loadfn = function(){
            if(isFirst){
                iframe.contentWindow.location = 'http://a.com/proxy.html';// 设置的代理文件
                isFirst = false;
            } else {
                fn(iframe.contentWindow.name);
                //获取数据以后销毁这个iframe，释放内存；这也保证了安全（不被其他域frame js访问）
                iframe.contentWindow.document.write('');
                iframe.contentWindow.close();
                document.body.removeChild(iframe);
                iframe.src = '';
                iframe = null;
            }
        };
        iframe.src = url;
        if(iframe.attachEvent){
            iframe.attachEvent('onload', loadfn);
        } else {
            iframe.onload = loadfn;
        }
         
        document.body.appendChild(iframe);
    }
    </script>
</head>
<body>
 
</body>
    <script type="text/javascript">
    domainData('b.com/data.html', function(data){
        alert(data);
    });
    </script>
</html>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

### 四.利用location.hash+iframe跨域获取数据

如果看懂了window.name+iframe跨域获取数据 ，那么这个就很好理解。一样都是动态插入一个iframe，然后把iframe的src指向服务端地址，而服务端同样都是输出一段js代码，同样都是利用和子窗口之间的通信完成数据传输，同样要针对同源策略做出处理。

location是javascript里边管理地址栏的内置对象，比如location.href就管理页面的url，用location.href=url就可以直接将页面重定向url。而location.hash则可以用来获取或设置页面的标签值。比如http://domain/#admin的location.hash="#admin"。

其实很简单，如果index页面要获取远端服务器的数据，动态插入一个iframe，将iframe的src属性指向服务端地址。这时top window和包裹这个iframe的子窗口是不能通信的（同源策略），所以改变子窗口的路径就行了，将数据当做改变后的路径的hash值加在路径上，然后就能通信了（和window.name跨域几乎相同），将数据加在index页面地址的hash值上。index页面监听地址的hash值变化（html5有hashchange事件，用setInterval不断轮询判断兼容ie6/7），然后做出判断，处理数据。

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<body>
  <script type="text/javascript">
    function getData(url, fn) {
      var iframe = document.createElement('iframe');
      iframe.style.display = 'none';
      iframe.src = url;

      iframe.onload = function() {
        fn(iframe.contentWindow.location.hash.substring(1));
        window.location.hash = '';
        document.body.removeChild(iframe);
      };

      document.body.appendChild(iframe);
    }

    // get data from server
    var url = 'http://localhost:8080/data.php';
    getData(url, function(data) {
      var jsondata = JSON.parse(data);
      console.log(jsondata.name + ' ' + jsondata.age);
    });
  </script>
</body>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<?php
  // 如果有必要则进行数据处理 $_GET['..']
  // code
  
  // 返回的数据
  $data = '{\"name\":\"hanzichi\",\"age\":10}';

  echo 
  "
  <script>
    window.location = 'http://localhost:81/location-hash/proxy.html' + '#' + \"$data\";
  </script>
  "
?>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

location.hash+iframe法和jsonp以及window.name+iframe一样，都是双向的，但是都只能是GET形式，所以数据只能加在url上。

### 五.使用HTML5中新引进的window.postMessage方法来跨域传送数据

postMessage()方法允许来自不同源的脚本采用异步方式进行有限的通信，可以实现跨文本档、多窗口、跨域消息传递。

window.postMessage(message,targetOrigin)  方法是html5新引进的特性，可以使用它来向其它的window对象发送消息，无论这个window对象是属于同源或不同源，目前IE8+、FireFox、Chrome、Opera等浏览器都已经支持window.postMessage方法。

postMessage(data,origin)方法接受两个参数

1.data:要传递的数据，html5规范中提到该参数可以是JavaScript的任意基本类型或可复制的对象，然而并不是所有浏览器都做到了这点儿，部分浏览器只能处理字符串参数，所以我们在传递参数的时候需要使用JSON.stringify()方法对对象参数序列化，在低版本IE中引用json2.js可以实现类似效果。

2.origin：字符串参数，指明目标窗口的源，协议+主机+端口号[+URL]，URL会被忽略，所以可以不写，这个参数是为了安全考虑，postMessage()方法只会将message传递给指定窗口，当然如果愿意也可以建参数设置为"*"，这样可以传递给任意窗口，如果要指定和当前窗口同源的话设置为"/"。

左边的div会根据右边iframe内div颜色变化而变化

[![imag\](http://images0.cnblogs.com/blog/707050/201507/222339179745543.png)](http://images0.cnblogs.com/blog/707050/201507/222339177095857.png)

#### 1.主页[：http://test.com/index.html](http://test.com/index.html)

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!DOCTYPE html>
 2 <html>
 3 <head>
 4     <title>Post Message</title>
 5 </head>
 6 <body>
 7     <div style="width:200px; float:left; margin-right:200px;border:solid 1px #333;">
 8         <div id="color">Frame Color</div>
 9     </div>
10     <div>
11         <iframe id="child" src="http://lsLib.com/lsLib.html"></iframe>
12     </div>
13 
14     <script type="text/javascript">
15 
16         window.onload=function(){
17             window.frames[0].postMessage('getcolor','http://lslib.com');
18         }
19 
20         window.addEventListener('message',function(e){
21             var color=e.data;
22             document.getElementById('color').style.backgroundColor=color;
23         },false);
24     </script>
25 </body>
26 </html>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

#### 2.主页内iframe： http://lslib.com/lslib.html

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<!doctype html>
 2 <html>
 3     <head>
 4         <style type="text/css">
 5             html,body{
 6                 height:100%;
 7                 margin:0px;
 8             }
 9         </style>
10     </head>
11     <body style="height:100%;">
12         <div id="container" onclick="changeColor();" style="widht:100%; height:100%; background-color:rgb(204, 102, 0);">
13             click to change color
14         </div>
15         <script type="text/javascript">
16             var container=document.getElementById('container');
17 
18             window.addEventListener('message',function(e){
19                 if(e.source!=window.parent) return;
20                 var color=container.style.backgroundColor;
21                 window.parent.postMessage(color,'*');
22             },false);
23 
24             function changeColor () {            
25                 var color=container.style.backgroundColor;
26                 if(color=='rgb(204, 102, 0)'){
27                     color='rgb(204, 204, 0)';
28                 }else{
29                     color='rgb(204,102,0)';
30                 }
31                 container.style.backgroundColor=color;
32                 window.parent.postMessage(color,'*');
33             }
34         </script>
35     </body>
36 </html>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

在例子中页面加载的时候主页面向iframe发送’getColor‘ 请求（参数没实际用处）

```
window.onload=function(){
     window.frames[0].postMessage('getcolor','http://lslib.com');
}
```

iframe接收消息，并把当前颜色发送给主页面

```
window.addEventListener('message',function(e){
                if(e.source!=window.parent) return;
                var color=container.style.backgroundColor;
                window.parent.postMessage(color,'*');
 },false);
```

主页面接收消息，更改自己div颜色

```
window.addEventListener('message',function(e){
            var color=e.data;
            document.getElementById('color').style.backgroundColor=color;
},false);
```

当点击iframe事触发其变色方法，把最新颜色发送给主页面

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
function changeColor () {            
                var color=container.style.backgroundColor;
                if(color=='rgb(204, 102, 0)'){
                    color='rgb(204, 204, 0)';
                }else{
                    color='rgb(204,102,0)';
                }
                container.style.backgroundColor=color;
                window.parent.postMessage(color,'*');
}
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

主页面还是利用刚才监听message事件的程序处理自身变色

```
window.addEventListener('message',function(e){
            var color=e.data;
            document.getElementById('color').style.backgroundColor=color;
},false);
```

使用postMessage来跨域传送数据还是比较直观和方便的，但是缺点是IE6、IE7不支持。

### 六.CORS: 跨域资源共享(Cross-Origin Resource Sharing)

当前几乎所有的浏览器（Internet Explorer 8+， Firefox 3.5+， Safari 4+和 Chrome 3+）都可通过名为跨域资源共享（Cross-Origin Resource Sharing）的协议支持ajax跨域调用。

**启用 CORS 请求**

假设您的应用已经在 example.com 上了，而您想要从 www.example2.com 提取数据。一般情况下，如果您尝试进行这种类型的 AJAX 调用，请求将会失败，而浏览器将会出现“源不匹配”的错误。利用 CORS，www.example2.com 服务端只需添加一个HTTP Response头，就可以允许来自 example.com 的请求：

```
Access-Control-Allow-Origin: http://example.com
Access-Control-Allow-Credentials: true（可选）
```

可将 Access-Control-Allow-Origin 添加到某网站下或整个域中的单个资源。要允许任何域向你提交请求，请设置如下：

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true（可选）
```

启用开发人员工具后，您就会在响应中看到 Access-Control-Allow-Origin 。

**提交跨域请求**

如果服务器端已启用了 CORS，那么提交跨域请求就和普通的 XMLHttpRequest 请求没什么区别。例如，现在 example.com 可以向 www.example2.com 提交请求了：

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
var xhr = new XMLHttpRequest();
// xhr.withCredentials = true; //如果需要Cookie等
xhr.open('GET', 'http://www.example2.com/hello.json');
xhr.onload = function(e) {
  var data = JSON.parse(this.response);
  ...
}
xhr.send();
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

cors在移动终端支持的不错，可以考虑在移动端全面尝试；PC上有不兼容和没有完美支持。

CORS提供了一种跨域请求方案，但没有为安全访问提供足够的保障机制，如果你需要信息的绝对安全，不要依赖CORS当中的权限制度，应当使用更多其它的措施来保障。

### 七.Flash

利用flash的URLLoader，也可以轻松实现跨域数据交互。只要站点B的跨域策略文件(crossdomain.xml,在站点根目录下放置)中包含了站点A，A站就可以获取B站的数据，提交数据给B站。[crossdomain.xml的用法](http://www.jb51.net/article/25485.htm)。

我们可以把JS和flash的交互封装一下，更方便的使用。这里有一个别人封装好的版本，使用起来和原生的XMLHttpRequest几乎一模一样：

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
var req;
function callback() {
   if (req.readyState == 4) {
     try {
       if (req.status != 200) {
           alert('error detected 1');
       } else {
         alert("got data: "+req.responseText);
       }
     } catch(e) {
         alert('error detected 2');
     }
   }
}
function test_get() {
  req = new CrossXHR();
  req.onreadystatechange = callback;
  req.open('GET', 'http://www.pliantdev.com/support/test.xml');
  req.send();
}
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

**附:后台proxy代码**

发起方页面代码如下：

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<form id="form1" runat="server"> 
<div> 
<input type="text" id="txtSrc" value="http://www.gzsums.edu.cn/webclass/html/html_design.html" style="width: 378px" /> 
<input id="btnProxy" type="button" value="通过Proxy获取数据" onclick="GetDataFromProxy();" /><br /> 
<br /> 
<br /> 
</div> 
<div id="divData"></div> 
</form> 
</body> 
<script language="javascript" type="text/javascript"> 
function GetDataFromProxy() { 
var src = document.getElementById('txtSrc').value; 
var request = null; 
if (window.XMLHttpRequest) { 
request = new XMLHttpRequest(); 
} 
else if (window.ActiveXObject) { 
request = new ActiveXObject("Microsoft.XMLHTTP"); 
} 
request.onreadystatechange = function() { 
var ready = request.readyState; 
var data = null; 
{ 
if (ready == 4) { 
data = request.responseText; 
document.getElementById('divData').innerHTML = data; 
} 
else { 
document.getElementById('divData').text = "Loading"; 
} 
} 
} 
var url = "Proxy.ashx?src=" + escape(src); 
request.open("get",url,false); 
request.send(null); 
} 
</script>
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

发起方Proxy代码如下：

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
using System.Data; 
using System.Linq; 
using System.Web; 
using System.Web.Services; 
using System.Web.Services.Protocols; 
using System.Xml.Linq; 
using System.IO; 
using System.Net; 
using System.Text; 
namespace WebApplication1 
{ 
/// <summary> 
/// Summary description for $codebehindclassname$ 
/// </summary> 
[WebService(Namespace = "http://tempuri.org/")] 
[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)] 
public class Proxy : IHttpHandler 
{ 
const int BUFFER_SIZE = 8 * 1024; 
public void ProcessRequest(HttpContext context) 
{ 
context.Response.ContentType = "text/plain"; 
string src = context.Request["src"]; 
WebRequest wr = WebRequest.Create(src); 
WebResponse wres = wr.GetResponse(); 
Encoding resEncoding = System.Text.Encoding.GetEncoding("gb2312"); 
StreamReader sr = new StreamReader(wres.GetResponseStream(), resEncoding); 
string html = sr.ReadToEnd(); 
sr.Close(); 
wres.Close(); 
context.Response.Write("<br/><br/><br/><br/>"); 
context.Response.Write(html); 
} 
public bool IsReusable 
{ 
get 
{ 
return false; 
} 
} 
} 
}
```

[![复制代\](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

\-------------------------------------------------------------------------------------------------------------------------------------

