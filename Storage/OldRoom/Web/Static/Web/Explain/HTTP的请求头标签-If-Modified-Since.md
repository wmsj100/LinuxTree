---
title: HTTP的请求头标签 If-Modified-Since
date: 2016-05-22
tags: [HTTP]
categories: Static
---

http://www.cnblogs.com/zh2000g/archive/2010/03/22/1692002.html

一直以来没有留意过HTTP请求头的IMS（If-Modified-Since）标签。

最近在分析Squid的access.log日志文件时，发现了一个现象。
就是即使是对同一个文件进行HTTP请求，第一次和第二次产生的网络流量数据也是不一致的。


在调查的过程中，逐渐了解了HTTP的If-Modified-Since的头标签的作用。

 

大家都知道客户端浏览器是有缓存的，里面存放之前访问过的一些网页文件。
例如IE，会把缓存文件存到“C:\Documents and Settings\zh2000g\Local Settings\Temporary Internet Files”
这样类似的目录里。
其实缓存里存储的不只是网页文件，还有服务器发过来的该文件的最后服务器修改时间。


If-Modified-Since是标准的HTTP请求头标签，在发送HTTP请求时，把浏览器端缓存页面的最后修改时间一起发到服务器去，服务器会把这个时间与服务器上实际文件的最后修改时间进行比较。

如果时间一致，那么返回HTTP状态码304（不返回文件内容），客户端接到之后，就直接把本地缓存文件显示到浏览器中。

如果时间不一致，就返回HTTP状态码200和新的文件内容，客户端接到之后，会丢弃旧文件，把新文件缓存起来，并显示到浏览器中。

 下面用一个简单的小例子说明一下。

由于演示例子需要截取HTTP Request和Response的信息，我在这里使用的工具是Fiddler。
感兴趣的朋友可以到【http://www.fiddler2.com/Fiddler2/version.asp】去下载。

 

1.首先在服务器创建一个简单的HTML文件，用浏览器访问一下，成功表示HTML页面。Fiddler就会产生下面的捕获信息。
  需要留意的是
  （1）因为是第一次访问该页面，客户端发请求时，请求头中没有If-Modified-Since标签。
  （2）服务器返回的HTTP状态码是200，并发送页面的全部内容。
  （3）服务器返回的HTTP头标签中有Last-Modified，告诉客户端页面的最后修改时间。  

2.在浏览器中刷新一下页面，Fiddler就会产生下面的捕获信息。
  需要注意的是
  （1）客户端发HTTP请求时，使用If-Modified-Since标签，把上次服务器告诉它的文件最后修改时间返回到服务器端了。
  （2）因为文件没有改动过，所以服务器返回的HTTP状态码是304，没有发送页面的内容。




3.用文本编辑器稍微改动一下页面文件，保存。再用浏览器访问一下，Fiddler就会产生下面的捕获信息。
需要留意的是
  （1）客户端发HTTP请求时，使用If-Modified-Since标签，把上次服务器告诉它的文件最后修改时间返回到服务器端了。
  （2）因为文件被改动过，两边时间不一致，所以服务器返回的HTTP状态码是200，并发送新页面的全部内容。
  （3）服务器返回的HTTP头标签中有Last-Modified，告诉客户端页面的新的最后修改时间。

 

 

HTTP的If-Modified-Since头标签与客户端缓存相互配合，大大节约了网络流量。

