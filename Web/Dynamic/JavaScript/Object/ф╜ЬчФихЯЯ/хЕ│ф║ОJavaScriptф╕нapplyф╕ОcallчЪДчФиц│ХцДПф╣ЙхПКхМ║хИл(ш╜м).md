---
title: 关于JavaScript中apply与call的用法意义及区别(转)
date: 2016-3-30 21:52:26
tags: [Hexo,工具]
categories: Frame
---

JavaScript中有一个call和apply方法，其作用基本相同，但也有略微的区别。

<!-- more -->
先来看看JS手册中对call的解释：
call 方法
调用一个对象的一个方法，以另一个对象替换当前对象。

`call([thisObj[,arg1[, arg2[,   [,.argN]]]]])`

参数
thisObj
可选项。将被用作当前对象的对象。

arg1, arg2,  , argN
可选项。将被传递方法参数序列。

说明
call 方法可以用来代替另一个对象调用一个方法。call 方法可将一个函数的对象上下文从初始的上下文改变为由 thisObj 指定的新对象。

如果没有提供 thisObj 参数，那么 Global 对象被用作 thisObj。

说明白一点其实就是更改对象的内部指针，即改变对象的this指向的内容。这在面向对象的js编程过程中有时是很有用的。

引用网上一个代码段，运行后自然就明白其道理。
```javascript
<input type="text" id="myText"   value="input text">
<script>
    function Obj(){this.value="对象！";}
    var value="global 变量";
    function Fun1(){alert(this.value);}

    window.Fun1();   //global 变量
    Fun1.call(window);  //global 变量
    Fun1.call(document.getElementById('myText'));  //input text
    Fun1.call(new Obj());   //对象！
</script>
```
call函数和apply方法的第一个参数都是要传入给当前对象的对象，及函数内部的this。后面的参数都是传递给当前对象的参数。
运行如下代码：
```javascript
<script>
   var func=new function(){this.a="func"}
    var myfunc=function(x){
        var a="myfunc";
        alert(this.a);
        alert(x);
    }
    myfunc.call(func,"var");
</script>
```
可见分别弹出了func和var。到这里就对call的每个参数的意义有所了解了。

对于apply和call两者在作用上是相同的，但两者在参数上有区别的。
对于第一个参数意义都一样，但对第二个参数：
apply传入的是一个参数数组，也就是将多个参数组合成为一个数组传入，而call则作为call的参数传入（从第二个参数开始）。
如 `func.call(func1,var1,var2,var3)对应的apply写法为：func.apply(func1,[var1,var2,var3])`

同时使用apply的好处是可以直接将当前函数的arguments对象作为apply的第二个参数传入

