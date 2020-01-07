---
title: Session对象
date: 2016-08-22
tags: [ASP, .NET, c#]
categories: Language
---

为了克服`cookie`问题，设计了`Session`对象，是会话，会议的意思。

对于`web`开发者来说，一次会话就是用户通过浏览器和服务器之间进行的一次通话，它包括浏览器和服务器之间的多次请求和响应。当用户向服务器发出第一次请求时，服务器会为该用户创建唯一的会话，会话将一直持续到用户访问结束（浏览器关闭，本次会话结束）；

与`cookie`不同，`session`是存储在服务器端的数据。针对每一次连接，系统会自动分配一个`ID`来标识每一个不同的用户，该`ID`在客户端和服务器之间进行传递，达到唯一标识某一个用户的目的，要得到该`ID`可以使用`Session.SessionID`,

服务器是怎么知道什么时候分配该`ID`呢，有一下几种方法：
- 将该`ID`存储在`cookie`中，但是如果关闭`cookie`就无法使用。
- 使用`URL`重写技术，将`SessionID`附加到`URL`中；
- 使用表单隐藏字段技术，服务器将`SessionID`以隐藏字段的方式添加到表单中。

`Session`对象的特定如下：
- `Session`对象包含某一个用户的状态信息，此信息只面向该连接，不与其他用户共享
- 会话超时或者过期，服务器即刻清除`Session`对象，释放所占资源。
- 会话期通过`SessionID`传递状态信息，不像`cookie`那样将所有的内容传输，客户端紧对`SessionID`可见，而对状态信息的内容不可见。

通过`web.config`进行`Session`配置：

```c#
<system.web>
    <sessionState timeout="20" cookieless="true" mode="SQLServr">
    </sessionState>
</system.web>
```

`Session`中的过期时间是以分钟为单位的，
`timeout="20"` -- 表示20分钟后过期
`cookieless` -- 此属性值是个枚举，用来指定如何将`cookie`应用于`web`应用程序中，`true`表示会话使用`cookie`作为标识`ID`.
`mode` -- 此属性也是个枚举，指定存储会话状态值的位置。

`Session`有很多优点，但是因为`Session`占用服务器资源，如果存储大量信息，当站点访问量大时，将影响服务器的性能，所以对比俩者的优缺点，

一般将登录状态信息等存在安全需求的内容存储在`Session`中，而用户的浏览记录，访问时间等内容还是存储在`cookie`中。

`Session`的典型应用场景是：存放用户的登录信息，如用户名、密码、权限角色等根据这些信息可以进行身份验证和权限验证。