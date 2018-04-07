---
title: 关于jQuery的原型函数内部参数的传递
date: 2016-07-16
tags: [jQuery]
categories: Dynamic
---

通过`requirejs`封装模块时候，也是要用到函数的原型，

```javascript
define(["jquery"],function($){
    function fn(opts){
        this.init(opts);
        this.bind();
        // this.opts = opts;   // 这样的做法不好，因为会把这个参数暴露出去。
    };

    fn.prototype = {
        constructor: fn,
        init: function(opts){
            $.extend(this, opts);
        },
        bind: function(){
            // 直接使用this...调用opts的属性。
        }
    }
    });
```

函数原型上面绑定的方法，可以通过在函数内部调用`this`来调用。
对于不想通过构造函数传递参数的函数，就不要使用`this.opts = opts`;
如果想在原型函数内部使用函数的参数`opts`，那么只需要在初始化函数`init`内部传入参数`opts`就可以，然后把这个参数合并到`this`内部，这样后面的函数`bind`就可以通过`this`来调用这个参数来。不需要再次引入参数`opts`。

把参数`opts`合并到`this`使用的是`jQuery`的`extend`方法。
