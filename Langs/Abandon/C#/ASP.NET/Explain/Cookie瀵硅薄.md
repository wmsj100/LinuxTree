---
title: Cookie对象
date: 2016-08-19
tags: [ASP, .NET, c#]
categories: Language
---

`Cookie`可以存储小量信息，它是由服务器发送出来，存储在网络浏览器中，从而当这个访客下一次又访问该站点时候，可以通过该浏览器获得这些信息。

让浏览器记住访问的特定信息，比如上次访问的位置，花费的时间或用户的首选项（如样式表所控制的页面风格等）。

当浏览该`Cookie`对应的站点时，`Cookie`作为`HTTP`的头部文件的一部分在浏览器和服务器之间互相传递，因此`Cookie`分别属于`Response`和`Request`对象。

每一个`Cookie`都属于`Cookies`集合，所以访问`Cookie`可以使用索引器的方式。

- 写入`Cookie` -- `Response.Cookies[Cookie名称].Value=变量值` -- 写入的操作是服务器写入的。
- 读取`Cookie` -- `Request.Cookies[Cookie名称].Value` -- 是通过客户端发起的请求

由于`Cookie`是存储于客户端，出于安全考虑，一般不使用它进行客户登录状态的判断。

`Cookie`的常用属性：
- `name` -- Cookie变量的名称
- `Value` -- 取得或设置`Cookie`变量的值
- `Expires` -- 设定`Cookie`变量的有效时间

如果不设置`Expires`，则`Cookie`的有效值到浏览器程序关闭为止。
如果设置`Expires = MaxValue`，则`Cookie`永久有效。

`Cookie`是依靠名称进行区别的，所有同名的`Cookie`会进行覆盖，通过这个特点可以更新`Cookie`.

大多数浏览器都对`Cookie`有数量和大小限制，限制大小为`4kb`，而且用户还可以禁用`cookie`，此时`cookie`就无法使用。

`cookie`一般的用途是：
- 在用户未登录的情况下记录用户的信息，比如用户的浏览记录，上次登录时间等，进而分析用户多久访问一次网站，用户的关注内容等，