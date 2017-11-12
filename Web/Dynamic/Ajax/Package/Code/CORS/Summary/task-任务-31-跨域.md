---
title: task 任务 31
date: 2016-05-15
tags: [饥人谷,任务,跨域]
categories: 饥人谷
---

1. 什么是同源策略

   同源策略指的是只有网页的协议`http/https` 相同、域名`jirengu.com` 相同、端口`http: 80 / https: 443 / ftp: 21` 才可以进行数据的读写操作，是一种最基本的保护措施。

2. 什么是跨域？跨域有几种实现形式？

   跨域是指突破浏览器的限制，即使网页不同源也可以进行数据的读写操作。

   - `document.domain` --在主域名相同的情况下，可以分别设置俩个域名的`document.domain` 为一个相同的主域名，然后通过`iframe` 来获取数据。

     [a_com.html](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task31/CORS_NEW/domain/dynamic_domain/a_com.html)

     [child_a_com.html](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task31/CORS_NEW/domain/dynamic_domain/child_a_com.html)

   - `JSONP` -- 对于域名没有限制，通过动态生成`script` 标签，把回调函数绑定到`src` 地址上面，`通过动态页面`php` 返回一个执行执行函数。`
   不一定需要动态脚本的支持，只是单纯的JS文件也是可以的。

     - [效果-github/../a_com.php](http://wmsj100.github.io/GrowUp/html/jirengu/task31/CORS_NEW/JSONP/a_com.html)
     - [效果-erheizi/../b_con.php](http://www.erheizi.com/jirengu/task-31/CORS_NEW/JSONP/b_com.php/)

     因为`JSONP` 返回的是一个执行函数，而且发起的请求链接很好模拟，在数据安全方面需要后端进行验证，前端没办法阻止恶意请求。

   - `window.name` -- 原理是一个页面如果没有被关闭，那么在这个页面进行链接跳转，它的`window.name` 是不会变化的。这种方法需要准备3个页面

     - 发起请求的页面[效果-github/.../a_com.html](http://wmsj100.github.io/GrowUp/html/jirengu/task31/CORS_NEW/window_name/a_com.html)
     - 和请求页面在同域名下的代理页面[效果-github/.../a_client.html](http://wmsj100.github.io/GrowUp/html/jirengu/task31/CORS_NEW/window_name/a_client.html)
     - 要获取数据的页面[效果-erheizi.com/.../b_com.html](http://www.erheizi.com/jirengu/task-31/CORS_NEW/window_name/b_com.html)

     这种方法不需要动态页面，但是需要借助`iframe` ，需要在访问结束后清除`iframe` 。但是需要多一个空白页面左代理，比较麻烦。

   - `postMessage` -- 这是`HTML5` 的接口，是推荐标准。这个方法也需要借助`iframe` 。

     - 原理就是在页面`a_com.html` 通过`iframe` 插入`b_com.html` ,然后通过`b_com` 对自己发起`postMessage`请求，
     - 在`b_com.html` 中添加`message` 监听事件，监听到请求之后验证发起请求的域名`event.origin` .然后通过`ajax` 获取数据，然后再创建一个`postMessage` 请求，此时设置为可被所有域名访问，因为前面已经验证过，所以不存在安全问题。
     - 在`a_com.hmtl` 中添加`message` 监听事件，获取数据并展示数据。

     [a_com.html](http://wmsj100.github.io/GrowUp/html/jirengu/task31/CORS_NEW/postMessage/a_com.html)

     [效果-erheizi.com/.../b_com.html](http://www.erheizi.com/jirengu/task-31/CORS_NEW/postMessage/b_com.html)

     [效果-erheizi.com/.../b_com.json](http://www.erheizi.com/jirengu/task-31/CORS_NEW/postMessage/b_com.json)

     因为这是推荐标准，而且不需要动态页面，所以比较推荐使用这种方式。

   - `CORS` -- 这是`HTTP` 通信协议，被访问的页面只需要添加一个头部`header("Access-Control-Allow-Origin:http://a.com");` ，然后`a.com` 域名下面的页面就可以访问该页面了。但缺点是需要动态脚本支持，但优点是几乎不需要做什么，只是添加一个头部。

     [效果-github.com/.../a_com.html](http://wmsj100.github.io/GrowUp/html/jirengu/task31/CORS_NEW/cors/a_com.html)

     [效果-erheizi.com/.../b_com.php](http://www.erheizi.com/jirengu/task-31/CORS_NEW/cors/b_com.php)

