---
title: webpack封装css模块和jsx模块
date: 2016-07-21
tags: [Models, Webpack]
categories: Frame
---

main.jsx

```jsx
var React = require('react');
var ReactDOM = require('react-dom');
var style = require('./app.css');

ReactDOM.render(
    <div>
        <h1 className={style.h1}>hello world</h1>
        <h2 className="h2">hello webpack</h2>
    </div>,
    document.querySelector("#example")
)
```
可以看
