.---
title: mockjs捕获ajax请求返回的参数
date: 2016-07-13
tags: [Models,Frame]
categories: Frame
---

使用`mockjs`捕获数据时候，如果匹配成功，并且不是返回模板数据`template`，而是返回一个函数，那么函数的参数就是mock拦截的请求信息，信息包括3个属性，
分别是：
 - 请求的地址
 - 请求的类型
 - 请求发送的数据，只有post有这个内容。

```javascript
Mock.mock(/\.json/, "post", function(opt){
    return opt;
    }) ;

$.ajax({
    url: "wmsj.json",
    type: "post",
    data: {
        name: "wmsj",
        age: 12
    }
    }).done(function(data){
        $("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
        })

{
    "url": "wmsj.json",
    "type": "POST",
    "body": "name=wmsj&age=12"
}
```

