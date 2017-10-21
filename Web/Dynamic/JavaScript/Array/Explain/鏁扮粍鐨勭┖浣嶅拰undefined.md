---
title: 数组的空位和undefined
date: 2016-06-08
tags: [Array]
categories: Dynamic
---

当数组的某个位置是空元素，即俩个逗号之间没有任何值，我们称这个值为空值(hole);
`a = [1,,2,,3]`
数组的空位不影响数组的长度。

通过`delete`可以删除数组的值，`delete a[0]`;删除之后使用`undefined`填充，`delete`不会影响数组的`length`；

不管是输入数组时候引入空位，还是通过`delete`删除数组，查看时候都是被`undefined`占位。

对于`undefined`，使用`for in`和`forEach`遍历的时候会过滤`undefined`；而使用`for length`和`while`遍历的时候则不会过滤，但是考虑到`for-in`和`forEach`的性能低下一般不建议使用。具体如下：

```javascript
var a = [1, , 2, 3];
delete a[3];
a.forEach(function(item, i) {
    console.log(i, item) //[[0,1],[2,2]]
});

var i = a.length;
while (i--) {
    console.log(i,a[i]); //[[3,undefined],[2,2],[1,undefined],[0,1]]
}

for (var i = 0, len = a.length; i < len; i++) {
    // console.log(i,a[i])  //[[0,1],[1,undefined],[2,2],[3,undefined]]
}

for (var i in a) {
    // console.log(i,a[i]); //[[0,1],[2,2]]
}
```
