---
title: JS性能优化
date: 2016-06-11
tags: [JavaScript]
categories: Dynamic
---

JS的性能优化

```javascript
function hasEitherClass(element, className1, className2){
return element.className == className1 || element.className == className2;
}
```

这个很明显`element.className`值是不会变的，但是却在原型链中搜索了俩次，所以可以把这个值存储在局部变量中，减少一次搜索。

```javascript
function hasEitherClass(element, className1, className2){
    var currentClassName = element.className;
return currentClassName == className1 || currentClassName == className2;
}
```

此重写后的版本中成员搜索只进行了一次。既然两次对象搜索都在读属性值，所以有理由只读一次并将值存入局部变量中。局部变量的访问速度要快得多。

一般来说，如果在同一个函数中你要多次读取同一个对象属性，最好将它存入一个局部变量。以局部变量替代属性，避免多余的属性查找带来性能开销。在处理嵌套对象成员时这点特别重要，它们会对运行速度产生难以置信的影响。


```javascript
function toggle(element){
if (YAHOO.util.Dom.hasClass(element, "selected")){
YAHOO.util.Dom.removeClass(element, "selected");
return false;
} else {
YAHOO.util.Dom.addClass(element, "selected");
return true;
}
}
```

此代码重复 YAHOO.util.Dom 三次以获得三种不同的方法。每个方法都产生三次成员搜索过程，总共九
次，导致此代码相当低效。一个更好的方法是将 YAHOO.util.Dom 存储在局部变量中，然后访问局部变量：

```javascript
function toggle(element){
var Dom = YAHOO.util.Dom;
if (Dom.hasClass(element, "selected")){
Dom.removeClass(element, "selected");
return false;
} else {
Dom.addClass(element, "selected");
return true;
}
}
```

总的成员搜索次数从九次减少到五次。在一个函数中，你绝不应该对一个对象成员进行超过一次搜索，除非该值可能改变。

在 JavaScript 中，数据存储位置可以对代码整体性能产生重要影响。有四种数据访问类型：直接量，变
量，数组项，对象成员。它们有不同的性能考虑。

直接量和局部变量访问速度非常快，数组项和对象成员需要更长时间。

局部变量比域外变量快，因为它位于作用域链的第一个对象中。变量在作用域链中的位置越深，访问所需的时间就越长。全局变量总是最慢的，因为它们总是位于作用域链的最后一环。

避免使用 with 表达式，因为它改变了运行期上下文的作用域链。而且应当小心对待 try-catch 表达式的 catch子句，因为它具有同样效果。

嵌套对象成员会造成重大性能影响，尽量少用。

一个属性或方法在原形链中的位置越深，访问它的速度就越慢。

一般来说，你可以通过这种方法提高JavaScript代码的性能：将经常使用的对象成员，数组项，和域外变量存入局部变量中。然后，访问局部变量的速度会快于那些原始变量。