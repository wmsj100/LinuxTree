---
title: if条件判断
date: 2016-06-07
tags: [JavaScript]
categories: Dynamic
---

- `if(expression) statement` ; 如果`expression`的结果可以转换为`true`，则执行后面的语句`statement`；

```javascript
var m = 1;
var n = 2;

if (m !== 1)
if (n === 2) console.log('hello');
else console.log('world');

if (m !== 1) {
    if (n === 2) {
        console.log("hello");
    } else {
        console.log("world")
    }
}
//上面俩个条件是相同的。

if (m !== 1) {
    if (n === 2) {
        console.log("hello");
    }
} else {
    console.log("world")
}
```