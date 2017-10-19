---
title: window.name跨域请求
date: 2016-04-26
tags: [浏览器,跨域,ajxa,Web]
categories: Dynamic
---

有三个页面：

- a.com/app.html：应用页面。
- a.com/proxy.html：代理文件，一般是一个没有任何内容的html文件，需要和应用页面在同一域下。
- b.com/data.html：应用页面需要获取数据的页面，可称为数据页面。

实现起来基本步骤如下：

1. 在应用页面（a.com/app.html）中创建一个iframe，把其src指向数据页面（b.com/data.html）。

   ​

   数据页面会把数据附加到这个iframe的window.name上，data.html代码如下：

   ```
   <script type="text/javascript">
       window.name = 'I was there!';    // 这里是要传输的数据，大小一般为2M，IE和firefox下可以大至32M左右
                                        // 数据格式可以自定义，如json、字符串
   </script>
   ```

2. 在应用页面（a.com/app.html）中监听iframe的onload事件，在此事件中设置这个iframe的src指向本地域的代理文件（代理文件和应用页面在同一域下，所以可以相互通信）。app.html部分代码如下：

   ```
   <script type="text/javascript">
       var state = 0, 
       iframe = document.createElement('iframe'),
       loadfn = function() {
           if (state === 1) {
               var data = iframe.contentWindow.name;    // 读取数据
               alert(data);    //弹出'I was there!'
           } else if (state === 0) {
               state = 1;
               iframe.contentWindow.location = "http://a.com/proxy.html";    // 设置的代理文件
           }  
       };
       iframe.src = 'http://b.com/data.html';
       if (iframe.attachEvent) {
           iframe.attachEvent('onload', loadfn);
       } else {
           iframe.onload  = loadfn;
       }
       document.body.appendChild(iframe);
   </script>

   ```

3. 获取数据以后销毁这个iframe，释放内存；这也保证了安全（不被其他域frame js访问）。

   ```
   <script type="text/javascript">
       iframe.contentWindow.document.write('');
       iframe.contentWindow.close();
       document.body.removeChild(iframe);
   </script>

   ```

总结起来即：iframe的src属性由外域转向本地域，跨域数据即由iframe的window.name从外域传递到本地域。这个就巧妙地绕过了浏览器的跨域访问限制，但同时它又是安全操作。

而且`window.name` 的值不会随着页面的跳转而改变，刷新操作也不会改变`window.name` ，除非关闭页面或者重新赋值，否则`window.name` 的值就是永恒的。

