---
title: carousel轮播的路由接口数据
date: 2016-07-17
tags: [Model,Package]
categories: Frame
---

关于轮播的路由mock数据配置

```javascript
router.get('/mockjs/demo3', function(req, res){
    var Mock = require('mockjs'),
            callback = null,
            data = null,
            tag = 0,
            count = 0,
            ret = null;

    data = Mock.mock({
        "img|20": [{    // 会mock 20个数组出来，包含在img对象内部
            "img": "@image('500x300', '@color', '@color', '@csentence')",
            "name": "@csentence(10)",
            "tag|+1": 1
        }]
    });
    callback = req.query.callback;
    tag = Math.abs(req.query.tag) - 1;
    count = Math.abs(req.query.count);
    ret = data["img"].slice(tag, tag + count);
    res.send(callback + "(" + JSON.stringify(ret, null, 4) + ")");
});
```


关于轮播的模块接口说明

```javascript
    new carousel({
        url: "http://localhost:3001/mockjs/demo3?callback=?",   // jsonp地址
        index: 1,   // 设置默认的显示页
        count: 5,   // 轮播图片数量
        tag: 10,    // 轮播起始图片标签
        width: 500, // 轮播窗口宽度
        height: 300,    // 轮播窗口高度
        arrowSize: 40,  // 箭头尺寸
        btnHeight: 8,   // 按钮的高度
        btnWidth: 40,       // 按钮的宽度
        btnMargin: 5,       // 按钮的间距
        btnBottom: 20,  // 按钮离底部的距离
        ct: $(".ct1")   // 轮播容器
    });
```

