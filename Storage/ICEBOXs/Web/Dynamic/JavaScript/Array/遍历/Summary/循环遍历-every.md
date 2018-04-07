---
title: 循环遍历-every
date: 2016-4-3 20:04:45
tags: [遍历,函数,技巧]
categories: Dynamic
---

用来测试每个元素的函数。只有全部符合要求才会返回true，否则返回false，可以用于检测数组内容。
<!-- more -->

```javascript
var a = [1, 2, 3, 4, 5, 6];
function hasElement(element,index,array){
	return (element>0)
};
console.log(a.every(hasElement));
//true
```

`some`——用于检测数组内部是否又符合要求的元素，只要有一个符合要求就返回`true`

```javascript
var a = [1, 2, 3, 4, 5, 6];
function hasElement(element,index,array){
	return (element>5)
};
console.log(a.some(hasElement));
//true
```

`some`可以用于检测数组内部是否有要求的元素，这个比较好用。

但是可以看出，`every` , `some` , `forEach` 的效率应该是比较低的，因为感觉这个过程比较漫长，我自己都可以感觉到比`for` 要慢。