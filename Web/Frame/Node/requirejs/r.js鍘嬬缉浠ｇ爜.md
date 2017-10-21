---
title: r.js压缩代码
date: 2016-07-22
tags: [EJS,NPM,Frame,Node]
categories: Frame
---

在压缩代码之前的前提是代码是可以跑得起来的，不要未压缩的代码也跑bu起来，那压缩之后肯定跑不通的。
这是我的`demo1`的错误的问题。

对于通过`requirejs`加载的模块，入口文件`app.js`
`<script data-main="js/app" src="js/lib/requirejs"></script>`

`app.js`入口文件进行配置时候，其`baseUrl`是基于引用自己的`html`的目录的。

```javascript
require.config({
    baseUrl: 'js/lib',  // 是相对于html的相对路径
    paths: {
        jquery: 'http://lib.sinaapp.com/js/jquery/1.10.2/jquery-1.10.2.min',
        app: '../app'
    }
});

require(['app/select']);    // 对于模块的引用是基于`baseUrl`的路径的。
```

当`app.js`规定了`baseUrl`之后，他所引用的模块，以及模块中再引入模块时候，路径都是相对于`baseUrl`。

select.js

```javascript
define(['jquery', 'app/alpha', 'app/beat'], function($){
    // 虽然alpha, beat和select是在一个目录内部，
    // 但是引用时候不能直接调用，省略了前面的 - app/ -
    // 因为模块是通过入口文件被调用的。
    $(function(){
        $("body").alpha().beat();
    })
});
```

当通过模块形式写好文件之后，试着看代码能不能跑通，成功之后查看`网络请求`，会看到每个`js`文件都单独的请求了网络，会带来性能问题。
这个时候再通过`r.js`进行代码的整合和压缩。

通过`r.js`压缩代码时候首先需要准备一个文件夹`tools`，把这个文件夹放到项目的外面，因为这样输出项目的时候不会把`tools`文件包括进去，省去了排除文件

- tools
    + r.js
    + build.js // 配置文件

`build.js`是一个`json`对象，但是可以添加注释，没有真正的`json`严格。
这个文件的格式如下：

```javascript
{
    "appDir": "../www",  // 要整体输出的项目文件
    "baseUrl": "js/lib",   
     // 设置相对路径，这个和入口文件app.js中的设置是相同的。
    "dir": "../build-www",  // 项目输出文件夹
    "mainConfigFile": "../www/js/app.js",   // 定位到入口文件
    "modules": [{
        "name": "app"   // 输出模块的名字
        }]
}
```


