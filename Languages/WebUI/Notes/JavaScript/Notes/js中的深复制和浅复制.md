---
title: js中的深复制和浅复制
date: 2016-3-30 20:38:37
tags: [复制,JavaScript]
categories: Dynamic
---
在实际情况中经常会遇到对对象复制的问题。比如在处理项目中的一笔多结构的数据存储或者调用，这个时候你就要对对象（json）进行操作，而不 同的操作根据不同的需求来定义。其中最常见最普遍的是对对象的复制，重新定义，扩展等。
<!-- more -->
下面我们正对这些问题来进行探讨。要了解对象，我们首先需要了解 js的内存分配机制:
var o = {a:1};当我们在给一个变量赋值的时候已经在浏览器中开辟了一块内存出来。这块内存在浏览器中占了一定的空间，这个时候，我们可以称变量 o 为栈，称{a:1}为堆，他们之间的关系可以用下面这个图表示:

   我们可以看到，栈上只是存了一个指针，指针就是堆上对象的地址；这个时候我们的程序通过这个指针句柄可以操作堆上的对象；下面我们再声明一个变量b; var b = o;把o复制给b。b通过o获得{a:1}这个对象，但它们并非两个不同的对象，实际上他们的指针都是指向同一个对象。所以当我们通过b重新给{a:1} 赋值的时候，我们可以看到o也对应的改变了:
var o = {a:1}, b = o;
b.a = 2;
console.log(o)
//控制台输出提示:Object {a: 2}

这种简单的对对象赋值引用的方式我们可以称之为浅复制，浅复制故名思义它是对整个对象体复制的，没有开辟新内存，所以就会有牵一发动全身的现象出现。如何避免这样的一种情况呢，我们就必须要考虑对对象进行深度复制了。深度复制是对对象枚举，通过查找最末一层值不为对象的属性，然后将该值赋值给新的对象的同名属性上去，由于字符串或者数字的赋值是开辟新内存的，所以我们可以避免上面的说的改变b而导致o的变化。下面是个简单的例子，说明深度复制的原理:

var o = {a:1};
var b = {};
b.a = o.a;
b.a = 2;
console.log(o)
//Object {a: 1}

从以上的代码我们可以看到，b的a属性已经不关联o的任何属性了，它开辟了新内存，可以做自己的事情不会影响到a;我们可以写一个简单的函数来对对象进行深度复制:

var deepCopy= function(source) {


    var result={};
    
    for (var key in source) {


        result[key] = typeof source[key]===’object’? deepCoyp(source[key]): source[key];
    
     }
   return result;
}

当然，说到对象不要忘记我们的array，它也是属于对象类型的。但是对于数组我们有更简便的方法可以用

1.slice()

var a = [1];
var b = a.slice(1);

2.concat()

var a = [1];
var b = [].content(a);

3.组合兼容函数，我们直接上zepto的源码:

function extend(target, source, deep) {
  for (key in source)
    if (deep && (isPlainObject(source[key]) isArray(source[key]))) {
      if (isPlainObject(source[key]) && !isPlainObject(target[key]))
        target[key] = {}
      if (isArray(source[key]) && !isArray(target[key]))
        target[key] = []
      extend(target[key], source[key], deep)
    }
    else if (source[key] !== undefined) target[key] = source[key]
}

原理和上面写的deepCopy一样，遇到对象就枚举，直到它的值是字符串或者数字，然后给新的对象添加属性并且赋值。

ps：遗憾的事诺大的underscore.js竟然不支持深度复制，这让我着实头痛。无奈只有选zepto来辅助了。

