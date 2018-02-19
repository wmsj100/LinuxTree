---
title: 使用requirejs加载模块的知识点
date: 2016-07-12
tags: [Models]
categories: Frame
---

因为使用`requirejs`模块加载的模块是使用`difine`定义的，而我需要模块的函数拥有继承，想要使用`prototype`，那么这个时候函数该怎么构造呢，
其实这个老师在很早的时候就写过了，他一直说要先模仿他的写法，他那时候就是把方法绑定到原型上面，而对于原型的函数调用是通过函数本身来进行的，因为通过函数是可以访问到原型上面的函数的。

```javascript
define(function(){
    function gotop(){
        this.init();
    }

    gotop.prototype.init = function(){
        //...
    }
    })
```

