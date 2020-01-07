---
title: 关于多个setTimeout计时器混合到最后一个
date: 2016-07-19
tags: [Error,jQuery,Debug]
categories: Dynamic
---

http://javascript.ruanyifeng.com/bom/timer.html

http://www.cnblogs.com/souvenir/p/4977407.html

我在创建`轮播`模块时候在结束时候要给页面添加一个`autoPlay`事件，以为是最简单的，结果，也是困扰到现在，设置了俩个计时器，但都作用到最后一个模块。不知道这是什么问题，觉得应该是全局`this`的问题

很多人都会说，定时器(setTimeout, setInterval)中的`this`指代的是全局`window`，我也知道这一点，但是之前没有使用定时器的场景，也没有深刻印象，
在我做轮播模块时候，这一点卡壳来很久，上午11点就结束了，但是因为`autoPlay`的问题，一直拖到现在，

也是看到来阮一峰关于`setTimeout`失效的例子时候才想到要试一试，

```javascript
    function user(login) {
      this.login = login;
      this.sayHi = function() {
        console.log(this.login);
      }
    }

    var a = new user("John");
    setTimeout(a.sayHi, 1000);   // undefined
    setTimeout(a.sayHi.bind(a), 1000);  // John
    setTimeout(function() {
      a.sayHi();    // John
    }, 1000);
```

在`setTimeout`中如果直接调用关联`this`的函数会出现各种问题，阮一峰的解决办法是把函数放到`setTimeout`内部函数里面进行调用，不要直接调用，或者是想要直接调用时候，把函数`bind`绑定到当前环境，而不是`window`。

我最开始其实就是把函数放到来`setTimeout`的内部函数进行调用的，但是不行，多个模块的`autoPlay`都被集中到最后一个模块上去了，

在没办法的时候我尝试着使用来`bind`方法，就是在`setTimeout`中直接调用函数，但是通过`bind`绑定到当前环境中，

```javascript
autoPlay: function(){
    var route = this.autoPlayDirection; // 获取自动播放的方向
            delay = this.autoPlayDelay + this.animateTime,  // 获取自动播放的延时
            routeError = "autoPlay(): The param autoPlayDirection's value must be left or right",
            me = this;

        if(route === "left"){
                this.timer = setTimeout(this.arrowLeftEvent.bind(me), delay);
        } else if (route === "right") {
                this.timer = setTimeout(this.arrowRightEvent.bind(me), delay);
        } else {
            throw new Error(routeError);
        }
}
```

其实这个问题我已经想要放弃了，因为自己实在找不出来，想着要问老师的，可是就这样想出来了，

上午我也没想到自己会想出来。

相信自己。

还可以使用`setTimeout`中使用匿名函数的方式，但是匿名函数内部的`this`也需要传递当前`this`的变量引用。

```javascript
var me = this;
setTimeout(function(){
    me.autoPlay();
    },1000);
```


