---
title: 关于event的传递
date: 2016-07-01
tags: [JavaScript,Function]
categories: Dynamic
---

事件分为鼠标事件、键盘事件、自定义事件。
鼠标事件有9个类型，常见的就是click，
键盘事件有3个类型，常见的就是`keyup, keydown, keypress`;
自定义事件，我现在还不知道。

只要是通过事件调用的函数，就会自动生成一个关于事件的所有值的数组，这个数组被添加到函数执行过程中，也就是说，这个数组，只有函数在执行时候可以被访问。
而访问这个数组的方法就是通过给执行函数添加一个变量，索引这个数组。
这个变量可以显示的在事件绑定过程中添加，也可以不添加，只绑定函数。
event是一个事件的指针，只要是事件发送，关于事件的所有值都会在一个集合中存储，而引用这个值就可以通过事件上面绑定的函数来通过变量获取了。

```javascript
    document.addEventListener("click", function(e) {
        console.log(e.target);
    }, false);

    function add(a) {
        console.log(arguments)
        console.log(a.target)
    }

    document.addEventListener("click", add);
```

上面俩个事件效果是一样的，虽然第一个显示的把`event`传递给了函数，而第二个函数之间调用函数，没有显示的传递，而是在函数调用过程中通过变量`a`来引用关于事件的索引。

得出一个结论，只要是函数通过事件被调用。而且函数有参数，那么通过这个参数就可以访问到函数的事件集合，其中常用的值有`e.target`.

---

我需要重新再看一遍这本书，关于事件的解析。
