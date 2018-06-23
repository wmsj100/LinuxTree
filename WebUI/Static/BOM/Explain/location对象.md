---
title: location对象
date: 2016-06-22
tags: [BOM]
categories: Static
---

`location`是`BOM`最有用的对象之一，它的特殊性在于既是`window`对象，又是`document`对象。

```javascript
window.location === document.location;  //true
```

`location`将`URL`解析为独立的片段，可以通过不同的属性访问这些片段。

```javascript
var URL = "http://localhost/php/Month/June/12.html?name=1#3";
location.search
"?name=1"
location.pathname
"/php/Month/June/12.html"
location.port
""
location.protocol
"http:"
location.hash
"#3"
location.host
"localhost"
location.href;  //获取完整的链接
"http://localhost/php/Month/June/12.html?name=%E7%8E%8B%E6%B5%A9&age=20&male=male#3"
```

`location.assign` -- 接收一个链接参数并把当前网址替换为参数网址。
使用`window.location`或者`location.href`并进行字符串赋值时候其实也是调用的`location.assign`.
`location.href`是最常用的。

使用`location.replace("http://a.com")`也可以替换链接

`location.reload()` -- 重新加载页面，有可能读取缓存；
`location.reload(true)` -- 重新从服务器获取页面；