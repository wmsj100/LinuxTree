---
title: Javascript中获取数组最大值和数组最小值的方法
date: 2016-04-24
tags: [数组,JavaScript]
categories: Dynamic
---

方法一：

```javascript
//最小值
Array.prototype.min = function() {
var min = this[0];
var len = this.length;
for (var i = 1; i < len; i++){ 
if (this[i] < min){ 
min = this[i]; 
} 
} 
return min;
}
//最大值
Array.prototype.max = function() { 
var max = this[0];
var len = this.length; 
for (var i = 1; i < len; i++){ 
if (this[i] > max) { 
max = this[i]; 
} 
} 
return max;
}
```

如果你是引入类库进行开发，害怕类库也实现了同名的原型方法，可以在生成函数之前进行重名判断：

```javascript
if (typeof Array.prototype['max'] == 'undefined') { 
Array.prototype.max = function() { 
... ...
}
}
```

方法二：

用Math.max和Math.min方法可以迅速得到结果。apply能让一个方法指定调用对象与传入参数，并且传入参数是以数组形式组织的。恰恰现在有一个方法叫Math.max，调用对象为Math，与多个参数

```javascript
Array.max = function( array ){ 
return Math.max.apply( Math, array );
};

Array.min = function( array ){ 
return Math.min.apply( Math, array );
};
```

但是，John Resig是把它们做成Math对象的静态方法，不能使用大神最爱用的链式调用了。但这方法还能更精简一些，不要忘记，Math对象也是一个对象，我们用对象的字面量来写，又可以省几个比特了。

```javascript
Array.prototype.max = function(){
return Math.max.apply({},this)
}
Array.prototype.min = function(){
return Math.min.apply({},this)
} 
```

[1,2,3].max()// => 3 
[1,2,3].min()// => 1

要找到数组中的最大或最小值，可以像下面这样使用 apply() 方法。

```javascript
var values = [1, 2, 3, 4, 5, 6, 7, 8];
var max = Math.max.apply(Math, values);
Array.max()
```



