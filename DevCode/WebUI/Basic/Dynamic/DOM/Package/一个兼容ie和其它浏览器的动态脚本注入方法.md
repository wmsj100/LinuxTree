---
title: 一个兼容ie和其它浏览器的动态脚本注入方法
date: 2016-06-23
tags: [DOM,Package,Function]
categories: Dynamic
---

动态脚本有俩种注入方法，一种是注入脚本链接，这个直接使用`script.src`就可以，所有浏览器都兼容，第二种就是直接在`script`注入脚本内容，这样就出现浏览器兼容问题了，因为`ie`和其它浏览器的方法不同，其它浏览器可以通过操作`script.innerText`可以输入内容，但是`ie`将`<script>`视为一个特殊的元素，不允许`DOM`访问其子节点，所以直接访问`script.innerText`就会报错，但是可以通过`script.text`属性来指定`JS`代码。所以兼容代码如下：

```javascript
    var a = 'console.log("hello world")';
    function loadScriptString(code){
        var script = document.createElement("script");
        try{
            script.appendChild(document.createTextNode(code));
        }catch(ex){
            script.text = code;
        }
        document.body.appendChild(script);
    }
```
