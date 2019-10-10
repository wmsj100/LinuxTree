---
title: 函数this的值
date: 2016-06-18
tags: [Function]
categories: Dynamic
---

```javascript
    var color = "red";
    var o = {
        color: "blue"
    }

    function sayColor() {
        console.log(sayColor.caller);
        return this.color;
    }
    o.sayColor = sayColor;
    sayColor(); //"red"
    o.sayColor(); //"blue"
```

谁调用函数,`this`就指代谁.

`caller` -- 返回调用当前函数的函数引用,如果函数被全局调用,则返回`null`.
像上面的来个调用,虽然第二个是通过`o.sayColor()`进行的调用,但是函数的调用其实还是通过`window`执行的,所以`sayColor.caller`返回的还是`null`.

如果把代码改为如下:

```javascript
    var color = "red";
    var o = {
        color: "blue"
    }

    function sayColor() {
        function fn(){
            console.log(fn.caller.name);
        }
        fn();
        console.log(sayColor.caller)
        return this.color;
    }
    o.sayColor = sayColor;
    sayColor(); //"red"
    o.sayColor(); //"blue"
```

函数`fn`的调用是在`window`调用`sayColor`时候由`sayColor`调用的.所以`fn.caller`就会返回函数`sayColor`的函数本身,通过`fn.caller.name`返回的是调用函数的名称`sayColor`;

为了实现更松散的耦合,可以像这样调用`arguments.callee.caller`