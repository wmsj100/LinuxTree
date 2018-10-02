---
title: null和undefined的区别
date: 2016-06-08
tags: [Object]
categories: Dynamic
---

null和`undefined`在实际使用中基本类似，而且对于`JS`的替代语言中，去掉了`undefined`，只留下了`null`。

设计初衷是这样的。
`null` -- 表示`无`的对象，转换为数值时是`0`；
`undefined` -- 表示`无`的原始值，转换为数值时是`NaN`；

`2 + null` => `2`;
`2 + undefiend` => "NaN";

对于`null`和`undefined`大致可以像下面这样理解
`null` -- 表示空值，即该处的值现在为空，比如调用函数时候不需要传入值，这时候就可以传入`null`。

```javascript
function fn(a,b){
        return a+b;
    }
    fn(null,null);
```

`null`的使用场景还是比较少的。而`undefined`就会多了。

```javascript
// 变量声明了，但没有赋值
var i;
i // undefined

// 调用函数时，应该提供的参数没有提供，该参数等于undefined
function f(x) {
  return x;
}
f() // undefined

// 对象没有赋值的属性
var  o = new Object();
o.p // undefined

// 函数没有返回值时，默认返回undefined
function f() {}
f() // undefined

```

