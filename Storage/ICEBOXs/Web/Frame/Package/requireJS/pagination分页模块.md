---
title: pagination分页模块
date: 2016-07-17
tags: [Model,Package]
categories: Frame
---

远程访问路由代码

```javascript
router.get('/mockjs/demo2', function(req, res){
    var Mock = require("mockjs"),
            callback = req.query.callback,
            // pageSize = +req.query.pageSize, // 获取到数字而不是字符串
            // pageIdx = +req.query.pageIdx, // 获取到数字而不是字符串
            pageSize = Math.abs(req.query.pageSize), // 获取到数字而不是字符串
            pageIdx = Math.abs(req.query.pageIdx), // 获取到数字而不是字符串
            totalPage = 0,
            ret = "",
            data = null,
            start = 0,
            end = 0,
            arr;
    data = Mock.mock({
        "info|50": [{
            "num|+1": 1,
            "name": "@cname()",
            "img": "@image('50x50', '@color', '#222', '@first')",
            // 在mock图片数据时候要记得，不能带参数，
            "date": "@date('yyyy年MM月dd日')",
            "link": "@url('http')",
            "phone": "@natural(13000000000, 19999999999)",
            "email": "@email('gmail.com')",
            "comment": "@cparagraph(1,7)"
        }]
});
    start = (pageIdx-1)*pageSize;
    end = start + pageSize;
    totalPage = data.info.length;
    arr = data.info.slice(start, end);
    arr.push({"totalPage": totalPage}); // 把信息总数push到数组内部
    ret = JSON.stringify(arr, null, 4); // 把数组转换为json字符串形式发送
    res.send(callback + "(" + ret + ")");
});
```

模块运行接口文件

```javascript
    var a = new page({
        ct: $(".ct1"),  // 模块的包裹容器
        pageSize: 10,   // 页面显示的信息数量
        pageIdx: 3,     // 页面默认的显示页码
        pageBtnCount: 5,    // 页面按钮数量
        url: "http://localhost:3001/mockjs/demo2?callback=?"    // jsonp地址
    });
```

