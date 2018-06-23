---
title: 关于函数this在调用过程的被改变
date: 2016-06-29
tags: [JavaScript,Function]
categories: Dynamic
---

```javascript
    var fn = {
        message: "fn event",
        bind: function(){
            console.log(this.message);
        }
    }
    wmsj.eventUtil.addHandler(document, "click", fn.bind);
```

上面的函数就是点击页面会弹出`message`信息，预想的是这样，但是实际却弹出`undefined`,因为这样调用函数时候，`fn.bind`函数的执行环境没有被保存，所以this值就是被调用的`document`，而这上面是没有绑定`bind`方法的，所以就是`undefined`。
可以把函数放入闭包，这样函数的执行环境就会被维持。

```javascript
    var fn = {
        message: "fn event",
        bind: function(){
            console.log(this.message);
        }
    }
    wmsj.eventUtil.addHandler(document, "click", function(e){
        fn.bind(e);
    });
```

这样就成功了。

当然了，创建闭包会导致函数难于理解和调试，可以创建一个将函数绑定到特点环境的函数，这样的函数通常叫做bind。

```javascript
    function bind(fn, context) {
        return function() {
            return fn.apply(context, arguments);
        }
    }
    wmsj.eventUtil.addHandler(document, "click", bind(show.bind,show));
```

这样再次调用就会正常的显示我们期望的数值了。
由于ie8不支持,所以封装一个函数如下

```javascript
bind: function(fn, context) {   // 这个函数通过惰性载入的方法封装
            if (Function.prototype.bind) {  // 检测是否支持ES5推出的原生bind方法
                bind = function(fn, context) {  // 覆盖函数
                    return fn.bind(context);
                }
            } else {
                bind = function(fn, context) {  // ie8不支持原生bind，
                    return function() {
                        return fn.apply(context, arguments);    // 通过闭包来保存fn的执行环境
                    }
                }
            }
            return bind(fn, context);
        }
```

因为这样的方式会设计到多个函数嵌套,所以性能会打折扣,建议在需要的时候再使用,
但是到目前为止,我还没有用过,因为我的使用场景太狭小了.

函数柯里化 -- 与函数绑定紧密相联,它用于创建已经设置好了的一个或多个参数的函数.
函数柯里化和函数绑定(bind)思想是一样的,都是通过一个闭包返回一个函数.俩者的区别是:
当函数被调用时候,返回的函数还需要传入参数.

```javascript
function bindFunc(fn,context){
    var args = Array.prototype.slice.call(arguments,2);
    return function(){
        var innerArgs = Array.prototype.slice.call(arguments);
        var finalArgs = args.concat(innerArgs);
        return fn.apply(content,finalArgs);
    }
}
```

其实就是在函数绑定的基础上面添加了参数的设置.
