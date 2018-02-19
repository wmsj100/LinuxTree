---
title: IE闭包造成的内存泄漏
date: 2016-06-22
tags: [Function]
categories: Dynamic
---

因为`ie9`之前的垃圾回收机制同时存在俩种方法，`清除标记`和`引用次数`。所以闭包在这些版本的`ie`浏览器中会存在一些特殊问题，具体说就是，如果闭包中存在`HTML`元素，那么意外着该元素无法被销毁。

```javascript
    (function fn(){
        var a = document.querySelector("h3");
        console.log(a.id)
        a.onclick = function(){
            console.log(this.id);
        }
    })();
```

上面是一个自执行函数，`a`引用了`HTML`的元素`h3`，给元素`a`绑定了事件，然后内部有对`a`进行了循环引用，所以`a`至少被引用`一次`，因为活动对象就无法被销毁，一直存在与内存中。

虽然可以把`a.id`保存在一个变量中，闭包通过变量来访问，但是因为闭包会保存整个外部函数的作用域链，所以`a`还是被保存了，因此有必要在给`a`绑定完事件之后再清除引用`a = null`.

```javascript
    (function fn(){
        var a = document.querySelector("h3");
        var titleId = a.id;
        a.onclick = function(){
            console.log(titleId);
        }
        a = null;
    })();
```

手动清除不用的对象是一个好习惯。