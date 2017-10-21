---
title: webpack封装css模块
date: 2016-07-21
tags: [Models, Webpack]
categories: Frame
---

对于`css`文件也可以封装到入口文件`main.js`中，通过`require`来调用。

app.css

```css
body{
    background: pink;
}
```

main.js

```javascript
require('./app.css');
```

对于引用文件时候前面的`./`这个是不能丢的，因为会报错，

webpack.config.js

```javascript
module.exports = {
    entry: './main.js',
    output: {
        filename: 'bundle.js'
    },
    module: {
        loaders: [{ // 通过loaders函数进行编译为原生js
            test: /\.css$/,
            loader: 'style-loader!css-loader'
        }, ]
    }
};
```

index.html

```html
<head>
    <body>
        <script src="bundle.js"></script>
    </body>
</head>
```

可以看到调用时候只有一个入口文件。