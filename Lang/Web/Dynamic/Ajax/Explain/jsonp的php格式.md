---
title: jsonp的php格式
date: 2016-06-13
tags: [Ajax]
categories: Dynamic
---

很就没弄这个，快要忘记了，对于jsonp，需要动态脚本支持，也就是`php`，而php里面的字符串、对象、数组都是`json`格式，都需要使用引号包括。

首先我之前对于`jsonp`的理解也是有误的，之前认为`jsonp`必须要动态脚本支持，但是现在我知道是错的，因为静态的`js`文件也是可以的，但是脚本需要动态生成。具体实例如下：

```javascript
    var script = document.createElement("script");
    script.src = "http://www.erheizi.com/jirengu/test/0613/jsonp.js";
    document.head.appendChild(script);

    function callback(obj) {
        console.log(obj);
    }
```

服务器上jsonp.js文件：

```javascript
var info = {
    "state": "1",
    "value": {
        "1": {
            "name": "name",
            "value": "wmsj100"
        },
        "2": {
            "name": "age",
            "value": "10"
        },
        "3": {
            "name": "sex",
            "value": "male"
        },
        "4": {
            "name": "work",
            "value": "coder"
        }
    }
};
callback(info);
```


```php
$info = '{
    "state": "1",
    "value": {
        "1": {
            "name": "name",
            "value": "wmsj100"
        },
        "2": {
            "name": "age",
            "value": "10"
        },
        "3": {
            "name": "sex",
            "value": "male"
        },
        "4": {
            "name": "work",
            "value": "coder"
        }
    }
}';
$fn = '[1,2,3]';
```
