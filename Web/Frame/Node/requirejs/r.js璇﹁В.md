---
title: r.js详解
date: 2016-07-22
tags: [EJS,NPM,Frame,Node]
categories: Frame
---

http://www.cnblogs.com/vajoy/p/3920163.html

```javascript
{
    "appDir": "../js",  // 这个文件下面的所有内容都会被打包
    "dir": "../dist/",  // 这个文件是输出目录
    "baseUrl": "./lib", // 这个是模块的基础路径， 后面的脚本都是以这个目录为依据的
    "modules": [{
        "name": "../main"   
    }],
    "paths": {      // 把main.js中的 require.config的内容移到这里
        app: "../app",  // 这是app的相对目录
        jquery: "jquery-1.12.4"
    }
}
```



```javascript
({ 
    appDir: './',   //项目根目录
    dir: './vajoy',  //输出目录，全部文件打包后要放入的文件夹（如果没有会自动新建的）
    
    baseUrl: './js/pages',   //相对于appDir，代表要查找js文件的起始文件夹，下文所有文件路径的定义都是基于这个baseUrl的
    
    modules: [                      //要优化的模块
      { name:'index'} ,{ name:'reg'}    //说白了就是各页面的入口文件，相对baseUrl的路径，也是省略后缀“.js”
    ],
    
    fileExclusionRegExp: /^(r|build)\.js|.*\.scss$/,    //过滤，匹配到的文件将不会被输出到输出目录去
    
    optimizeCss: 'standard', 
    
    removeCombined: true,   //如果为true，将从输出目录中删除已合并的文件
    
    paths: {    //相对baseUrl的路径
            avalon: '../common/avalon',
            jquery: '../common/jq',
            VJ:'../common/VajoyJS'
    }
    //     ,shim:{ .....}      //其实JQ和avalon都不是严格AMD模式，能shim一下最好了，不过这里咱省略
}) 
```

各参数的意义我是从网上找了一份说明（建议配合我代码上的注释来理解）：

![](http://images.cnitblog.com/i/561179/201408/191935179403796.jpg)