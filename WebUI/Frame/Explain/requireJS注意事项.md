---
title: requireJS注意事项
date: 2016-07-11
tags: [Models]
categories: Frame
---

在`requirejs`中所有的`js`文件都没有后缀`.js`.如果添加了后缀，就会跳过`baseUrl, paths`的路径设置，使用相对位置。这是最常见的错误。

```javascript
require(["app/01.js"],function(a){
    console.log(a);
}); // error

require(["app/01"],function(a){
    console.log(a);
}); // true
```

- 在定义模块的时候使用`define`,而调用的时候需要使用`require`.

- `define`也可以返回一个函数

```javascript
require.config({
    baseUrl: "js/app/"
});

define(["sub", "01"], function(sub, color) {
    return function() {
        return {
            color: color,
            sub: sub(2, 5);
        }
    }
});
```


