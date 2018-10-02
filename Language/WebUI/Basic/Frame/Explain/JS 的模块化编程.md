---
title: JS 的模块化编程
date: 2016-06-06
tags: [模块]
categories: Frame
---

JS 中的模块化编程

模块化编程：按照 “模块” 来开发软件
模块：实现特定功能的一个盒子

    “特定功能”－完整性
    “盒子”－封装性，保护私有，对外接口
    与周围环境，要低耦合－独立性
    与其他模块的关系－依赖性

模块化编程的好处：

    给系统解藕，让代码易于维护
    更专注：不关心内部实现细节，更多精力在业务逻辑
    更灵活：想要什么功能，就加载什么模块

由于 JS 不是模块化编程语言，不支持类，也不支持模块（ES6 之前），所以，JS 通过其它方式在现有的环境中实现“模块”的效果。
模块的基本写法
最简单的模块

其实，一个函数就是一个模块。使用的时候，直接调用即可。 add(2,5);

```javascript
function add(a,b){
    return a+b;
}
```

我们把实现特定功能的一组不同函数简单的放在一起，也是一个模块

```javascript
function add(a,b){
    return a+b;
}
function subtract(a,b){
    return a-b;
}
function multiply(a,b){
    return a*b;
}
function divide(a,b){
    return a/b;
}
```

以上的加减乘数就组成了一个 math 模块。使用的时候，直接调用就可以了

```javascript
add(2,5);
subtract(2,5);
multiply(2,5);
divide(2,5);
```


缺点：污染了全局变量，没法保证不与其他模块发生变量名冲突
封装

封装，避免污染全局变量
我们把那些函数们放到一个对象里，把它们都包起来。对象用 JSON 字面量的形式定义，如下

```javascript
var math = {
    add: function(a,b){
        return a+b;
    },
    subtract: function(a,b){
        return a-b;
    },
    multiply: function(a,b){
        return a*b;
    },
    divide: function(a,b){
        return a/b;
    }
};
```

使用时，直接调用这个对象的属性即可。
math.add(2,5);
math.subtract(2,5);

缺点：暴露模块的所有成员
当模块中有私有的属性和方法时，会被外部函数读写，
进一步封装

假设，math 中有一个私有变量 _count

```javascript
var math = {
    _count: 0,
    add: function(a,b){
        return a+b;
    },
    subtract: function(a,b){
        return a-b;
    }
};
```

对其进行进一步封装：用立即执行函数表达式，Immediately-Invoked Function Expression（IIFE）

```javascript
var math = (function(){
    var _count = 0;
    var add = function(a,b){
        return a+b;
    };
    var subtract = function(a,b){
        return a-b;
    };
    return {
        add: add,
        subtract: subtract
    };
})();
```

小结：

    对内：匿名函数包裹，并立即执行
    对外：返回接口
    这，就是 JS 模块的基本写法。下面再对这种写法进行下加工。

进一步加工

假设，我们想在不动 math 源码的情况下，再给它新添一个方法 max()。
   
```javascript
var myMath = (function(math){
    //添加新方法
    math.max = function(a,b){
        return a>b?a:b;
    };
    return math;  //返回新的接口
})(math || {});  //把math当参数传进去
```

在使用时，我们可以

```javascript
var app = (function($, math){
    var val1 = $('#person1').val(),
        val2 = $('#person2').val();
    $('#sum').val( math.add(val1, val2) );
    $('#max').val( math.max(val1, val2) );
})(jQuery, myMath);  //当依赖两个模块时，类似。传两个参数
```

小结

    模块自己
    （1）对内：良好的封装
    （2）对外：明确的接口
    模块对外-与外界关系清晰明了
    （3）显示地当成参数传进来

模块的构建思想，便是通过这样的方式演化而来的。

### CommonJS

JS 的模块化规范
由于 JS 本身没有内置的模块系统（ES6之前），于是就有了 JS 的模块化规范。模块化规范的目的就是统一模块化的编写方式，比如不同的 java 团队总可以用 import 的方式来加载彼此写的代码，C# 可以用 using 来加载。

目前，比较通行的 JS 模块化规范，有三个：CommonJS/AMD/CMD。下面我们来分别介绍。

CommonJS
简介

CommonJS 是一个旨在构建涵盖web服务器端、桌面应用、命令行app和浏览器JS的JS生态系统。
标准

CommonJS 的标准是符合 module1.1 规范的。CommonJS 的标准如下：

1.require() 全局方法，用来加载模块
假设我们要导入 math 模块（math.js 是一个单独的文件）

```javascript
var math = require('math'); //导入模块
math.add(2,5); //使用模块的方法
```

2.exports 全局变量，用来导入模块的方法
我们来看下在 math.js 中如何定义上面用到的 add() 方法的

```javascript
//math.js
exports.add = function(){
    var sum=0, i=0,
        args=arguments, l=args.length;
    while(i<l){
        sum += args[o];
    }
    return sum;
}
```

3.模块里还有变量 module，它有一个只读的id属性，还有一个uri属性，还有其它的一些命名规范。更多内容可查看 CommonJS 规范的文档页面。
发展

其实，CommonJS 最早是叫 ServerJS，它是伴随着服务器端的一个 JS 项目而产生的，又伴随着 node.js 的火爆发展而成名的。Module1.0 规范在 node.js 上实践的很好，但由于知道自身在浏览器中的不足，CommonJS 社区便于2009年8月把它的名字改成了 CommonJS，意是想统一服务器端和浏览器端。

通过 CommonJS 的规范和代码可以看出，require() 是同步的，模块系统需要同步读取模块文件的内容，并编译执行以得到模块的接口。在服务端，比如 node.js 中，这一般来说没什么问题，请求的文件（即要加载的模块）都在存放在本地硬盘，可以同步加载，等待的时间就是硬盘读取的时间。

但是，在浏览器端，同步就有问题了，因为浏览器中模块都放在服务器端。要请求文件，就要有网络请求，而一牵扯到网络请求，时间就不可控了。若依然同步加载模块，万一网络请求的时间太长就会导致浏览器假死。

要实现浏览器端的，就要制定新的标准，而在制定新标准的过程中，CommonJS 社区中有了分歧，于是就分出了 AMD 规范


AMD 和 CMD 的区别

    AMD 提前执行依赖 - 尽早执行，requireJS 是它的实现
    CMD 按需执行依赖 - 懒执行，seaJS 是它的实现

言论1

玉伯说： “
AMD 是 RequireJS 在推广过程中对模块定义的规范化产出。
CMD 是 SeaJS 在推广过程中对模块定义的规范化产出。
类似的还有 CommonJS Modules/2.0 规范，是 BravoJS 在推广过程中对模块定义的规范化产出。
还有不少…”
这些规范都是为了JS的模块化开发，特别是在浏览器端。
言论2

屈屈说： “
AMD 运行时核心思想是「Early Executing」，也就是提前执行依赖。这个好理解。
CMD 按需执行依赖可以避免浪费，但是带来更长的等待时间。

SeaJS 对模块的态度是懒执行, 而 RequireJS 对模块的态度是预执行。
我觉得「尽早执行」或「按需执行」两种策略没有明显的优劣之分，但 AMD 这种「模仿别人写法，却提供不一样的特性」这个做法十分愚蠢。这年头，做自己最重要！
因为 CommonJS Wrapper 并不会改变 AMD「尽早执行」依赖的本质！
”
言论3

至此可以对由 commonJS 衍生出来的方案做出总结了。在浏览器端来设计模块加载机制，需要考虑依赖的问题。我们先把依赖分为两种：

    “强依赖” —— 肯定需要
    “弱依赖” —— 可能需要

对于强依赖
如果要性能优先，则考虑参照依赖前置的思想设计你的模块加载器，我个人也更推崇这个方案一些；
如果考虑开发成本优先，则考虑按照依赖就近的思想设计你的模块加载器。

对于弱依赖
只需要将弱依赖的部分改写到回调函数内即可。
如果现在我要实现一个模块加载器，我会将强依赖前置，弱依赖采用异步回调函数的形式，其它的方法我认为都只是语法糖而已，仅此就够了。
其他言论

    建议取消使用 CMD 这个名称，统一使用 CommonJS 规范称谓
    AMD 代码是 requirejs，CMD 则是 seajs
    加载模块时：AMD 提前加载，依赖前置；CMD 延迟加载，依赖就近。
    正如玉伯所说：RequireJS 和 Sea.js 都是模块加载器，倡导模块化开发理念，核心价值是让 JavaScript 的模块化开发变得简单自然。
    根据我大量的阅读文档，在遵循一定的写法，感觉这两个都能实现一样的功能。只是作者在推广其思想要如何如何。

碎碎念

果然 AMD 和 CMD 的讨论很是激烈。之前 75团 的分享上有一次，某人的开场是这样的“今天，我们不讨论 AMD 好还是 CMD 好。今天我们只分享在图搜中的JS模块化应用”。

有时候吧，会觉得，之所以争的如此激烈，是因为有些人只用过了a，且用a的思路去试着用b，结果踩了好多坑（或者这根本就不是坑-而是没用对）又或者是抱着去验证而不是去学习的心态去用，结果可想而知。又或许有一些只用了个皮毛的入门人士，就来网上装作很有经验的样子去大肆批判这个，表扬那个，于是整个空气便浑浊了。看似硝烟弥漫的严肃紧张，实则是背后杂乱无章的瞎嚷嚷。

我个人觉得，对待技术本身：能解决碰到的问题就ok了。至于哪个好哪个不好，没必要争论个你死我活。要讨论就讨论每个的优缺点就可以了，优缺点其实也就是应用场景了。而且，优缺点是可以变的，语言也是在不断根据程序员的需求慢慢变化的….但针锋相对地吵架，就没啥实际意义了，最多是技术圈里的挑话题，炒作 or 刷存在感？

若要真的讨论两者的好坏，那就先做做功课。【自己也在做功课中，于是自己的看法暂且保留】
1.去看源码。。。理解真正的思想是什么？原理是什么？
2.写出符合规范的代码，去浏览器&实际项目中测试性能。。。
3.依据正确的场景去正确的用东西。。
理论和实战相结合后，且有个结论了之后，再来清清楚楚明明白白的争辩。