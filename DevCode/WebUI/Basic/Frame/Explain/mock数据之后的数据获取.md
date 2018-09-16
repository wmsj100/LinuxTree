---
title: mock数据之后的数据获取
date: 2016-07-14
tags: [Mock,Models,Frame]
categories: Frame
---

当数据`mock`完成之后，如何获取数据呢，最常见的方法就是通过`jsonp`。当然了，`mock`数据也得修改一下。

```javascript
router.get('/mockapi', function(req, res, next) {
    var Mock = require("mockjs");
    var data = Mock.mock({
        "status": {
            "code": "0"
        },
        "total": "@natural(0,9999)",
        "count": "@natural(0,10)",
        "data|1-10": [{
            "id": "@natural(0,999)",
            "sid": "@natural(0,999)",
            "name": "@csentence(10,20)",
            "short_name": "@csentence(5,12)",
            "url": "@url('http', 'slide.tech.sina.com.cn')",
            "img_url": "@image()",
            "createtime": "@datetime()",
            "img_count": "@natural(1,15)",
            "short_intro": "@cparagraph(3)",
            "uni_intro": "",
            "sub_ch": "@cname",
            "click": "@natural(0,500000)",
            "click_this_week": "@natural(0,500000)",
            "click_last_week": "@natural(0,500000)",
            "click_this_month": "@natural(0,500000)",
            "click_last_month": "@natural(0,500000)",
            "click_this_day": "@natural(0,500000)",
            "click_last_day": "@natural(0,500000)",
            "source": "东方IC",
            "cmnt_url": "@url('http', 'comment5.news.sina.com.cn')",
            "category_2": ""
        }]

    });
    var ret = JSON.stringify(data, null, 4);
    // 从请求链接的查询字符串中获取callback的值
    var callback = req.query.callback;  
    // 拼装成jsonp的返回格式。
    ret = callback + "(" + ret + ")";
    // console.log(ret);
    res.send(ret);
});
```

然后发起`ajax`请求，

```javascript
$.getJSON("http://a.com:3000/mockapi?callback=?", function(data){
        console.log(data);
    })
```

这样就获取来数据