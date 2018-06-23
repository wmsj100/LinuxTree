---
title: 我自己mock的第一个数据范例
date: 2016-07-14
tags: [Mock,Models,Frame]
categories: Frame
---

我自己mock的`sina`的图片`api`。其实何必要找呢，自己`mock`一个就好了。

```javascript
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
$("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
```

