---
title: 对于库文件的AMD引用
date: 2016-06-07
tags: [模块]
categories: Frame
---

对于稍微大型的库文件的引用，需要通过`require.config`指明其位置，然后引用的时候只需要库名称就行，不需要待后缀或者`min`这样的字眼

```javascript
require.config({
    // baseUrl: "./",
    paths: {
        "domReady": "domReady",
        "jquery": "jquery.min",
        "underscore": "underscore-min",
        "backbone": "backbone-min"
    }
});
require(["domReady!"],function(doc){
    console.log(doc);
})
require(["jquery","underscore","backbone"],function($,_,Backbone){
    console.log($);
    console.log(_);
    console.log(Backbone);
});
```

像第一个`domReady`不需要指明路径也是可以执行的，但是后面的这些`jQuery。。`就必须要指明路径，而且名称中的`-min`也必须删除。

对于`jquery`的引用地址也可以是`CDN`加速节点

```javascript
paths: {
        "domReady": "domReady",
        "jquery": "http://lib.sinaapp.com/js/jquery/1.7.2/jquery.min",
        "underscore": "underscore-min",
        "backbone": "backbone-min"
    }
```

但是需要注意的是所有的js文件都不能带后缀`.js`，远程引用也是一样的。