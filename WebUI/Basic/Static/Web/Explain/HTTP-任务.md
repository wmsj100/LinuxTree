---
title: HTTP-任务
date: 2016-05-21
tags: [HTTP]
categories: Dynamic
---

1. OSI 七层模型指什么 (难度***)

   `OSI` -- Open System Interconnection Reference Model -- 开放式系统互联通信参考模型；一种概念模型，由国际标准化组织提出，试图使计算机在世界范围内互联为网络的标准框架。

   它将计算机网络体系结构划分为七层，从顶层到底层依次为：

   7 => 应用层 -- 提供为应用软件而设的界面，以设置与另一应用软件之间的通信。例如HTTP，HTTPS，FTP，SSH，POP3，SMTP，TELNET等；

   6 => 表示层 -- 该层被弃用-- 把数据转换为能与接收者的系统格式兼容并适合传输的格式。

   5 => 会话层 -- 该层被弃用 -- 负责在数据传输中设置和维护电脑网络中俩台电脑的通信连接。

   4 => 传输层 -- 把传输表头加至数据以形成数据包。传输表头包含了所使用的协议等发送信息。如传输控制协议`TCP` 。

   3 => 网络层 -- 决定数据的路径选择和转寄，把网络表头加至数据包，以形成分组。网络表头包含了网络数据。互联网协议`IP` .

   2 => 数据链路层 -- 负责网络寻址、错误侦测和改错。当表头和表尾被加至数据包时，会形成帧。数据链表头是包含了物理地址和错误侦测和改错的方法。数据链表尾是一串指示数据包末端的字符串。例如以太网、无线局域网(Wi-Fi)和通用分组无线服务(GPRS)等。

   1 => 物理层 -- 在局部局域网上传送帧，它负责管理电脑通信设备网络媒体之间的互通。包括了针脚、电压、线缆规范、集线器、中继器、网卡、主机适配器等。

   OSI不是一个标准，只是一个制定标准时所使用的概念性框架。[维基百科](https://zh.wikipedia.org/wiki/OSI%E6%A8%A1%E5%9E%8B#.E5.8E.86.E5.8F.B2)

2. `HTTP`  的工作原理是什么？ (难度***)

   `HTTP` 协议采用了`请求/响应` 模型；

   `client` 向`server` 发送一个请求报文，请求报文包含：请求的方法、URL、协议、端口、请求头部、和请求数据。

   `server` 以一个状态行作为响应。响应的内容包括：协议的版本号、成功或者错误的状态码、server信息、响应头部和响应数据。

   具体过程如下：

   1. 浏览器与web服务器的端口(80)建立一个`TCP` 连接。
   2. 浏览器向web服务器发送一个文本的请求报文，该报文由请求行、请求头部、空行和请求数据4部分组成。
   3. web服务器接受到请求之后开始解析并定位资源请求，然后向浏览器发回一个响应报文，该报文由状态行、响应头部、空行和响应数据4部分组成。
   4. web服务器主动关闭TCP连接，如果在请求报文或者响应报文中有`Connection:keep-alive` ，该连接就会被保持。
   5. 浏览器首先解析状态行，查看请求是否成功，然后解析每个响应头，响应头告知下面为若干字节的HTML文档和文档字符集。然后浏览器读取响应数据HTML，依据HTML语法对其进行格式化，并在浏览器窗口中显示。

3. URI 的格式是什么？常见的协议有哪些 (难度***)

   <scheme>://<user>:<password>@<host>:<port>/<path>;<params>?<query>#<hash>
   scheme -- 协议 -- http / https
   user: 用户名，在http中已不再使用，ssh 协议中通常是必须的。
   password -- 密码，同上；
   host -- 主机名 -- "www.erheizi.com"
   port -- 端口号 -- 用于区分主机上的进程，以精确定位要连接的服务。
   path -- 路径 -- index.html
   params --参数，以键值对的形式提供，以 ; 分隔开。在例如 ftp 协议中可用于规定文件是以二进制形式还是文本形式传输。
   query -- get请求输入的查询内容 
   hash -- 直接跳转到页面的id=hash的位置

4. HTTP 协议有几种和服务器交互的方法 (难度***)

   1. `GET` -- 请求服务器获取资源，常见的链接查找或者ajax数据获取。
   2. `POST` -- 向服务器发送数据，常用于表单或ajax
   3. `HEAD` -- 和`GET` 类似，但不获取内容，只是获取状态码和头部，用于查看资源的头部信息，确认资源是否存在，或者查看资源是否被修改。
   4. `PUT` -- 向服务器写入请求的URL，由于安全问题一般被服务器禁用；
   5. `TRACE` -- 请求服务器回显其收到的请求信息，用于HTTP的测试和诊断；
   6. `DELETE` -- 请求服务器删除请求的URL，通用处于安全起见被禁用；
   7. `OPTIONS` -- 获取服务器支持的功能；

5. 状态码200，301， 304，403,404,500，503分别代表什么意思 (难度****)

   1. `200` -- 代表资源获取成功
   2. `301` -- 代表文件永久重定向，浏览器在下次访问时候直接访问新地址
   3. `304` -- 代表文件没有修改，浏览器使用本地缓存
   4. `403` -- 资源禁止访问，通常由于服务器文件的权限设置导致
   5. `404` -- 资源不存在
   6. `500` -- 服务器错误
   7. `503` -- 服务器应答超时；

6. 报文有哪几部分组成？ (可选 难度****)

   报文是浏览器和服务器之间发送的简单格式化数据块，每个报文都包含一条来自客户端的请求或者服务器的响应。由3部分组成

   1. 对报文进行描述的起始行 通常包括：请求地址、请求方法、状态码、解析后的IP地址和端口、以及可能有的HTTP协议和版本号
   2. 请求头部以和服务器的应答头部
   3. 空白行
   4. 报文主体。

7. 请求头的格式和作用是什么？给个范例截图说明 (可选 难度****)

   1. 请求报文
      `GET / HTTP/1.1`；
      指明请求的方法和使用的`HTTP`的版本号；
   2. 响应报文
      `HTTP/1.1 304 Not Modified`；
      指明`HTTP`的版本号和返回的请求状态码及相应的说明

8. 首部的格式和作用是什么？给个范例截图说明 (可选 难度****)
   格式: 首部字段由许多HTTP首部字段所构成，首部字段格式:"首部字段名：首部字段值"。一个字段名可以对应多个字段值。
   作用: 包含许多有关客户端和请求正文的信息；
   通用首部
    ![](http://wmsj100.github.io/webFile//2016/May/2016-05-22/000041.png)
   请求首部
   ![](http://wmsj100.github.io/webFile//2016/May/2016-05-22/000042.png)
   响应首部
   ![](http://wmsj100.github.io/webFile//2016/May/2016-05-22/000040.png)
9. 主体的作用是什么？给个范例(可选 截图说明难度****)
   这是一个请求头部，请求主体和请求头部之间有一个空行，用于确定请求头部以及结束
   Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
   Accept-Encoding:gzip, deflate, sdch
   Accept-Language:zh-CN,zh;q=0.8
   Connection:keep-alive
   Host:www.erheizi.com
   Upgrade-Insecure-Requests:1
   User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36

   name:wmsj100&age:10
   作用: 请求头和请求正文之间是一个空行，表示请求头以及结束，接下来是请求正文，内容是客户提交的查询字符串信息；

   这是一个响应头部和响应实体
   Accept-Ranges:bytes
   Connection:Keep-Alive
   Content-Encoding:gzip
   Content-Length:161
   Content-Type:text/html
   Date:Sun, 22 May 2016 09:06:33 GMT
   ETag:"2e41118-ea-5300d37d3781d"
   Keep-Alive:timeout=15, max=300
   Last-Modified:Sat, 09 Apr 2016 13:23:32 GMT
   Server:Apache
   Vary:Accept-Encoding,User-Agent

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>wmsj100</title>
       <style>
           h1{
               color: #333;
           }
       </style>
   </head>
   <body>
       <h1>wmsj100</h1>
   </body>
   </html>
   作用: 响应头部和响应实体之间也是一个空行，表示响应头部以及结束，接下来是响应实体，内容就是一个完整的HTML文档。
10. 简述浏览器缓存是如何控制的(可选 难度*****)
       首先控制方式可以分为HTTP协议控制和非HTTP协议
   1. 非HTTP协议：只需要在HTML的HEAD标签下添加`<META HTTP-EQUIV="Pragma" CONTENT="no-cache">`；这段代码告诉浏览器当前页面不缓存，每次访问都请求服务器，但是只有部分浏览器支持，而所有的缓存代理服务器都不支持，因为代理不解析HTML本身。
   2. HTTP协议的缓存机制：关于缓存有俩个类似功能的消息头字段，分别是Expires，Cache-control;

    **Expires机制**
    Expires是HTTP1.0规定的Web服务器响应消息头字段，在响应请求时告诉浏览器在过期时间前，浏览器可以直接从浏览器缓存读取数据，而无需再次请求。
    ​```
    Date:Sun, 22 May 2016 09:44:22 GMT
    Expires:Sun, 22 May 2016 09:44:51 GMT
    ​```
    Web服务器告诉浏览器在`Sun, 22 May 2016 09:44:51 GMT`之前可以使用缓存，及缓存30s。

    **Cache-control**
    Cache-control是HTTP1.1规定的消息头字段，功能和Expires类似，但是比Expires控制的更细致，选择更多。
    Cache-control的值可以为`public, private, no-cache, no-store, no-transform, must-revalidate, proxy-revalidate, max-age`;
    1. `public` -- 响应可被任何缓存区缓存
    2. `private` -- 指示对于单个或部分用户的响应信息，不能被共享缓存处理。这允许服务器仅仅描述当前用户的响应信息，此响应消息对于其它用户无效。
    3. `no-cache` -- 指示请求或响应消息不能被缓存
    4. `no-store` -- 指示请求或者响应消息不能被缓存
    5. `max-age` -- 指示浏览器可以缓存的最大时间，单位为s。
       `Cache-Control:public, max-age=28`；
       这个表示服务器指示针对当前用户作出响应，并且缓存时间为28s。

    **Last-Modified/If-Modified-Since**
    这俩个要配合`Cache-control`使用；
    `Last-Modified` -- 标识这个响应的资源的最后修改时间。
    `If-Modified-Since` -- 当资源过期时，如果发现资源拥有`Last-Modified`，则再次向服务器请求时带上头`If-Modified-Since`,表示请求时间。Web服务器收到请求后发现有头`If-Modified-Since`,就会和被被请求的资源的最后修改时间进行对比，如果最后修改时间较新，表示当前资源修改过，重新发送资源给浏览器，返回状态200，否则表示资源没有更新，返回状态304，告诉浏览器继续使用所保存的`cache`;

    **Etag/If-None-Match**
    这俩个也要配合`Cache-control`使用；
    `Etag` -- web服务器响应请求时，告诉浏览器当前资源在服务器的唯一标识；
    `If-None-Match` -- 当资源过期时(Cache-control的max-age)，发现资源具有`Etag`声明，则再次向Web服务器请求时带上头`If-None-Match`(Etag的值),Web服务器收到请求后发现有头`If-None-Match`就会和被请求的资源的相应的校验串进行对比，相同则返回304，不同则返回200并重新发送数据。
    > `Etag`的优先级高于`Last-Modified`，服务器会优先验证`Etag`，相同才会再次验证`Last-Modified`，然后决定返回200或者304；
    > 缓存还和用户的行为有关，如果用户使用`F5`刷新页面，则本地缓存可以使用；但是如果使用`Ctrl + F5`来刷新页面，则直接向服务器再次请求数据。
13. 下图各个参数是什么意思(可选 难度*****)
![](http://7xpvnv.com2.z0.glb.qiniucdn.com/257149f7-1e11-4262-9b15-159389db83c6)
**General**通用头部
`Request URL` -- 浏览器向服务器请求的地址；
`Request Method` -- 浏览器的请求方法`PUT`，向服务器写入数据；
`Status Code` -- 状态码 200 表示成功
`Remote Address` -- 域名解析后对于的IP地址和端口
**Response Headers**回应头部
`Connection` -- Keep-alive 表示HTTP访问请求结束后TCP并不断开连接
`Content-Length` -- 表示写入的内容长度
`Content-Type` -- 表示内容的类型，决定浏览器将会以什么形式什么编码读取文件 这里是JSON数据
`Date`-- 表示响应的时间
`Server` -- 表示服务器的信息
`X-Powered-By` -- 非标 准回应字段，表示用于支持当前页面的应用程序的技术；
**Request Headers**请求头部
`Accept` -- 服务器可以返回的内容格式， */*为所有格式
`Accept-Encoding` -- 能够接受回应的编码格式 优先级按照先后顺序
`Accept-Langugae` -- 能够接受的回应的自然语言列表的语言 中文
`Connection` -- 浏览器想要优先使用的连接类型 `keep-alive` 表示一段时间内不断开
`Content-Length` -- `请求体长度`
`Content-Type` -- 请求体的多媒体类型
`Cookie` -- 之前由服务器通过`Set-Cookie`发送的一个超文本传输协议，每次发送请求都会携带这个Cookie；
`Host` -- 服务器的域名及服务器监听的传输控制协议的端口号。
`Origin` -- 发起一个跨来源资源共享的请求(要求服务器在回应中加入一个'访问控制允许来源'('Access-Control-Allow-Origin')字段)
`Referer` -- 表示浏览器所访问的前一个页面，正是那个页面将浏览器带到了当前页面
`User-Agent` -- 用户代理，浏览器的身份标识字符串
`X-Requested-Width` -- 主要用于标识Ajax及可扩展标记语言。大部分的爪哇脚本框架会发送这个字段，并将其值设置为`XMLHttpRequest`;
**Form Data**通过PUT写入的内容
`article: 若愚@饥人谷` 
