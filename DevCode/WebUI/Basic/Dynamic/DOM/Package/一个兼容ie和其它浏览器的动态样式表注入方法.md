---
title: 一个兼容ie和其它浏览器的动态样式表注入方法
date: 2016-06-23
tags: [DOM,Package,Function]
categories: Dynamic
---

`ie`把`style`当作了特殊对象，不能访问其子对象，所以不能通过`style.innerText`来注入样式表，但是可以通过`style.styleSheet.cssText`来修改。

```javascript
    function loadStyleString(code) {
        var style = document.createElement("style");
        style.type = "text/css";
        try {
            style.appendChild(document.createTextNode(code));
        } catch (ex) {
            style.styleSheet.cssText = code;
        }
        document.querySelector("head").appendChild(style);
    }
    loadStyleString("body{background-color: yellow;}");
```

虽然现在浏览器的脚本默认是`css`，可以省略`type`，但是对于`ie8`，如果不添加`type`就无法识别，会报错。所以还是添加的好。

`querySelector`是一个通用的选择器。