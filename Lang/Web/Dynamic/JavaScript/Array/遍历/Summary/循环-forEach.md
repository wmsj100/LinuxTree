---
title: 循环遍历-forEach
date: 2016-4-3 19:45:34
tags: [遍历,函数,技巧]
categories: Dynamic
---

- js中的循环遍历时候最先想到的就是`for (var i=0; i<arr.length ; i++)`其实也可以使用比较简单的`forEach`

> 参考文献——[forEach解析](http://blog.csdn.net/oscar999/article/details/8671546)
<!-- more -->


```javascript
var a = [1, 2, 3, 4, 5, 6];
var b = [];
a.forEach(function(e) {
	b.push(e);
})
 console.log(b);
 //[1, 2, 3, 4, 5, 6]
```

- `**forEach()**` 方法让数组的每一项都执行一次给定的函数。

`array.forEach(callback[, thisArg])`

`forEach` 方法按升序为数组中含有效值的每一项执行一次`callback` 函数，那些已删除（使用`delete`方法等情况）或者从未赋值的项将被跳过（但不包括哪些值为 `undefined 的项）。`

`callback` 函数会被依次传入三个参数：

- **数组当前项的值**
- **数组当前项的索引**
- **数组对象本身**

`forEach` 遍历的范围在第一次调用 `callback` 前就会确定。调用`forEach` 后添加到数组中的项不会被 `callback` 访问到。

如果已经存在的值被改变，则传递给 `callback` 的值是 `forEach` 遍历到他们那一刻的值。已删除的项不会被遍历到。

没有办法中止或者跳出 forEach 循环，除了抛出一个异常。如果你需要这样，使用forEach()方法是错误的，你可以用一个简单的循环作为替代。如果您正在测试一个数组里的元素是否符合某条件，且需要返回一个布尔值，那么可使用 [`Array.every`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/every) 或[`Array.some`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/some)。

`forEach` 为数组中的元素执行一次 `callback` 函数，不像 `every` 和 `some`，它总是返回 `undefined`。

```javascript
var a = [1, 2, 3, 4, 5, 6];
function logArrayElements(element,index,array){
	console.log("a["+index+"] = "+element);
}
a.forEach(logArrayElements);
//a[0] = 1
//a[1] = 2
//a[2] = 3
//a[3] = 4
//a[4] = 5
//a[5] = 6
```

