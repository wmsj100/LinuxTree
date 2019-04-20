---
title: 初步使用layui
date: 2018-05-05 10:30:50 Sat
modify: 2018-05-05 10:30:50 Sat
tag: [layui, frame, basic]
categories: Web
author: wmsj100
mail: wmsj100@hotmail.com
---

## 优势
- 因为定义时候使用的是`layui.define`方式，它会把模块直接加载到layui对象，所以调用时候不需要单独引用js文件，只需要使用`layui.use`方式，还有css文件引用也可以使用`layui.link`方式动态加载样式文件，让页面极为清爽，这一点是今天早上才意识到的

- 引用时候要使用模块化方式使用。
- layui的模块并不是默认就加载的，必须在依赖中显示写明才会加载，另外依赖的模块名必须是一个合法的模块名，不能包含目录，如果需要目录，建议采用extend建立别名

## 使用内部的jQuery
```js
layui.use(['form', 'demo', 'jquery'], function(){
	var form = layui.form;
	var $ = layui.$;
	var demo = layui.demo;
	demo.hello()
})
```

## 范例
- 在`base.html`中引入`main.js`
- 在`main.js`中可以把依赖的其它第三方库都通过这里引入，比如`underscore`, `echarts`...，也可以引入自己封装的方法
    ```main.js
    layui.config({
        base: "/static/helloWorld/js/"
    }).extend({
        'demo': 'test/demo'
    });
    ```
- 定义的`demo`模块
    ```demo.js
    layui.define(function(exports){
        var obj = {
            'hello': function(){
                console.log("hello world");
            }
        }
        exports('demo',obj);
    });
    ```
- 使用`demo`模块
    ```index.js
    layui.link('/static/helloWorld/css/base.css');
    layui.use(['form', 'demo'], function(){
        var form = layui.form;
        var demo = layui.demo;
        demo.hello()
    })
    ```
