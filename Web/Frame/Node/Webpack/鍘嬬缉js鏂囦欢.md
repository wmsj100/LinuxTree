---
title: 压缩js文件
date: 2016-07-21
tags: [Models, Webpack]
categories: Frame
---

webpack.js

```javascript
var webpack = require('webpack');
var uglifyJsPlugin = webpack.optimize.UglifyJsPlugin;
module.exports = {
    entry: './main.js',
    output: {
        filename: 'bundle.js'
    },
     plugins: [
    new uglifyJsPlugin({
      compress: {
        warnings: false
      }
    })
  ]
}
```

main.js

```javascript
var longVariableName = "hello";
longVariableName += " world";
document.write('<h1>' + longVariableName + '</h1>');
```

压缩后的结果

```javascript
!function(r){function e(t){if(o[t])return o[t].exports;var n=o[t]={exports:{},id:t,loaded:!1};return r[t].call(n.exports,n,n.exports,e),n.loaded=!0,n.exports}var o={};return e.m=r,e.c=o,e.p="",e(0)}([function(r,e){var o="hello";o+=" world",document.write("<h1>"+o+"</h1>")}]);
```

