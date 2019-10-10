---
title: mock数据number数据类型判断错误
date: 2016-07-12
tags: [Models]
categories: Frame
---

通过`mockjs`时候，因为我是要对请求的数据进行判断的，不会得到全部的数据。所以这个判断是在路由中进行判断的。

判断的函数是这样的。

```javascript
router.get('/mockjs/demo2', function(req, res){
    var Mock = require("mockjs"),
            callback = req.query.callback,
            pageSize = +req.query.pageSize, // 这里个地方是错误的根源
            pageIdx = +req.query.pageIdx, // 这里个地方是错误的根源
            ret = "",
            data = null,
            start = 0,
            end = 0,
            arr;
    data = Mock.mock({
        "info|50": [{
            "评论|+1": 1,
            "comment": "@cparagraph(5)"
        }]
});
    // console.log(pageIdx)
    start = (pageIdx-1)*pageSize;
    end = start + pageSize;
    arr = data.info.slice(start, end);
    ret = JSON.stringify(arr, null, 4);
    res.send(callback + "(" + ret + ")");
});
```

首先我通过`req.query`分别获取到请求的`pageIdx`和`pageSize`，但是，我直接对这俩个数据进行了计算。这是错误的根源，因为通过这样获取到的所有数据都是字符串，所以我需要对这些数据进行格式转换。

在前面添加`+`.