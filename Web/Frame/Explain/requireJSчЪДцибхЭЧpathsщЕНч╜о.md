---
title: requireJS的模块paths配置
date: 2016-07-13
tags: [Models]
categories: Frame
---

对于`requirejs`，关键的库的配置都是在入口文件`app.js`中进行配置，然后模块中就可以直接引用这个文件了，不必再一次的引入库文件

app.js
```javascript
require.config({
    baseUrl: "js/lib/",
    paths: {
        app: "../app",
        jquery: "jquery-1.12.4",
        // less: "less-1.7.0.min",
        mock: "mock-min"
    }
});
```

gotop.js
```javascript
// require.config({
//     paths: {
//         jquery: "jquery-1.12.4"
//     }
//     })

define(["jquery"], function($) {
    //....
    });
```

`gotop`中顶部的配置文件就没有必要了，因为在入口文件中`app.js`已经定义了。

如果模块文件中想要单独的配置一个库文件，那么引用的地址也是相对于入口文件`app.js`中设置的`baseUrl`地址。
也就是说，即便想在`gotop`中设置`jquery`，地址也是相对于`js/lib`.因为`jquery`本来就在这个目录，所以就不用在地址中添加位置信息了。