---
title: webpack的图片路径引用
date: 2016-07-12
tags: [Models, Webpack]
categories: Frame
---

使用`webpack`可以把任何文件都打包，最后页面就只有一个文件，`bundle.js`，图片文件也被打包到`main.js`中。

但是，使用`main.js`中对图片的地址引用时候很容易出现错误

```javascript
var img1 = document.createElement("img");
img1.src = require("small.png");
document.body.appendChild(img1);

var img2 = document.createElement("img");
img2.src = require("big.png");
document.body.appendChild(img2);
```

上面的代码会报错，但是在图片地址前面加上`./`就好了

```javascript
var img1 = document.createElement("img");
img1.src = require("./small.png");
document.body.appendChild(img1);

var img2 = document.createElement("img");
img2.src = require("./big.png");
document.body.appendChild(img2);
```

webpack.config.js

```javascript
module.exports = {
    entry: './main.js',
    output: {
        filename: 'bundle.js'
    },
    module: {
        loaders: [{
        test: /\.(png|jpg)$/,
        loader: 'url-loader?limit=8192'
    }]
    }
}
```

