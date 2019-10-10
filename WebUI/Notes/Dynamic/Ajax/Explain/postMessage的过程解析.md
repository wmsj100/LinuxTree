---
title: postMessage的过程解析
date: 2016-06-28
tags: [Ajax,JavaScript,Web]
categories: Dynamic
---

`postMessage` -- 是`H5`的协议,是一个比较安全的规则,因为进行了双方验证,具体过程如下

这个协议首先是通过页面内嵌`iframe`,然后通过`iframe.contentWindow`来发送请求,接受俩个参数, 
- data -- 要发送的请求数据
- url -- 内部`iframe`的url地址.
- iframe.contentWindow.postMessage(data, url);

url.html页面对`message`的监听,这里有3个关键性的属性是重要的,
- event.origin -- 获取请求页面的源`http://a.com`,对这个源进行验证,
- event.data -- 获取请求页面发送的数据,
- event.source -- 如果要给请求页面回馈数据,就需要发起`postMessage`,而发起的请求对象就是`event.source`,
- `event.source`在大多数情况下只是`window`对象的代理,并非实际的`window`对象,不能通过这个代理对象访问`window`对象的任何信息,只通过这个代理调用`postMessage`方法.

a.com/../a.html

```javascript
var toUrl = "http://b.com/PHP/Month/June/21.html",
        toData = "status=0";
    toPostMessage(toUrl, toData, function(str) {
        console.log(str);
    })

    function toPostMessage(toUrl, toData, handler) {
        var frame = document.createElement("iframe");
        frame.src = toUrl;
        frame.style.visibility = "hidden";
        document.body.appendChild(frame);
        wmsj.eventUtil.addHandler(frame, "load", function() {
            frame.contentWindow.postMessage(toData, toUrl);
        });
        wmsj.eventUtil.addHandler(window, "message", function(event){
            event = wmsj.eventUtil.getEvent(event);
            console.log(event.data);
        })
    }
```

b.com/../b.html

```javascript
        window.addEventListener("message", function(event) {
            if(event.origin === "http://a.com"){
                event.source.postMessage("aaaaa", "http://a.com");
                console.log(event.data);
            }
            
        }, false);
```


