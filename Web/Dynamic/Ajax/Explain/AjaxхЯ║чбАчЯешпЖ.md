---
title: Ajax基础知识
date: 2016-4-6 11:30:55
tags: [Ajax,JavaScript,PHP]
categories: Dynamic
---

## 问答

1. `ajax`是什么？有什么作用？

     `ajax`是异步`JavaScript`和`XML`数据交换技术，它可以避免重新加载全部页面来展现后台数据，通过`JS`来操作`DOM`来实现数据的加载。而且避免了因为后台数据查找和计算造成的页面`卡死`状态，提高了页面的交换性。

2. 前后端开发联调需要注意哪些事情？后端接口完成前如何 mock 数据？

   1. 前后端开发联调时候需要注意一下事情：
      - 在开发之前规定好接口文档并指明由谁来撰写和维护；
      - 接口信息如果改动需要合适的方法向前后端传递改动信息；
      - 规定使用的接口类型，`JSON`或者`JSONP`;
      - 定义数据管理和归属权，是属于前端管理还是后端管理；
      - 规定数据的交流方式，是前端直接把数据请求发送给后端，还是说有前端和后端之间有一个`middle`（中间层），前后端的数据都需要经过它来得到符合自己需求的数据类型；
   2. 后端接口完成前如何`mock`数据：常见的有2种方式，
      1. 自己制作模拟数据，但这种方式工作量比较大，而且需要收集分类要求的数据，如果接口变更，之前的所有数据也需要及时更新。但这样的好处是能够快速的完成前端任务；
      2. 使用模拟数据生成器，[http://mockjs.com/](http://mockjs.com/)；

3. 点击按钮，使用 ajax 获取数据，如何在数据到来之前防止重复点击?

   这个过程可以在浏览器和服务器第一次连接的时候即`xmlhttp.readystate===1`的时候，把`btn`上面绑定的提交函数卸载，然后在`xmlhttp.readystate===4`的时候重新给`btn`绑定提交函数，效果如下：

   ![](http://wmsj100.github.io/webFile/img/2016/April/0408/01.gif)

   我在本地测试是没问题的，但是提交到服务器却弹出警告，因为我使用了PHP的`sleep()`函数，它说不安全，所以没办法演示，只能截图了。代码如下，

   ```html
   <!DOCTYPE html>
   <html>
   <head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
   <title>ajax-2</title>
   <meta name="description" content="">
   <meta name="keywords" content="">
   <link href="http://cdn.bootcss.com/normalize/3.0.3/normalize.min.css" rel="stylesheet">
   <style>
       body{
           font-family: "Microsoft Yahei";
           color: #333;
       }
       .wrap{
           width: 300px;
           margin: 40px auto;
           border: solid 2px #E27272;
           padding: 10px;
           border-radius: 10px;
           text-align: center;
       }
       a{
           display: inline-block;
           text-decoration: none;
           padding: 5px 10px;
           color: #E27272;
           font-weight: bold;
           border: solid 1px #E27272;
           border-radius: 5px;
           margin-right: 30px;
           margin-bottom: 10px;
       }
       a:hover{
           background-color: #E27272;
           color: #fff;
       }
   </style>
   </head>
   <body>
       <div class="wrap">
           <p>2s之后后台会传回数字+1;<br>在2s期间点击按钮无效！</p>
           <a href="#" id="btn">点击</a>
           <span class="show">1</span>
           <div class="content"></div>
       </div>
       <script>
           var btn = document.querySelector("#btn");
           var show = document.querySelector(".show");
           var content = document.querySelector(".content");
           btn.addEventListener("click", ajax, false);

           function ajax(e) {
               console.log(show.innerText);
               var url = "ajax02_01.php" + "?num=" + show.innerText;
               console.log(url);
               content.innerHTML = "content= " + show.innerText + "<br>url=" + url
               e.preventDefault(); //阻止a连接跳转
               var xhr = new XMLHttpRequest();
               xhr.onreadystatechange = function() {
                   if (xhr.readyState === 1) {
                       btn.removeEventListener("click", ajax, false);
                   }
                   if (xhr.readyState === 4) {
                       btn.addEventListener("click", ajax, false);
                   }

                   if (xhr.status === 200 && xhr.readyState === 4) {
                       show.innerText = xhr.responseText;
                       console.log(show.innerText);
                   }
               }
               xhr.open("get", url, true);
               xhr.send();
           }
       </script>
   </body>
   </html>
   ```

   ajax02_01.php

   ```php
   <?php
   $num=$_GET["num"];
   sleep(2);
   echo $num+1;
   ```

## 代码

1. [task 24-1](http://www.erheizi.com/jirengu/task 24/task 24-1/)

2. [task 24-2](http://www.erheizi.com/jirengu/task 24/task 24-2/)

3. [task 24-3](http://www.erheizi.com/jirengu/task 24/task 24-3/)

   ​

     ​