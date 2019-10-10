---
title: 标签(label)
date: 2016-06-08
tags: [遍历,Array]
categories: Dynamic
---

JavaScript语言允许，语句的前面有标签（label），相当于定位符，用于跳转到程序的任意位置，标签的格式如下。
```javascript
label:
  statement
```
标签通常与break语句和continue语句配合使用，跳出特定的循环。

```javascript
for (var i = 0; i < 5; i++) {
    for (var j = 0; j < 5; j++) {
        console.log(i, j);
        if (i === 1 && j === 1) {
            break;
        }
    }
}
```
对于双层嵌套的循环，如果只是在内部使用`break`只会跳过内部的循环，外部循环会继续执行，如果想在满足一定条件时候停止所有的循环，那么可以使用label标签。

```javascript
top: for (var i = 0; i < 5; i++) {
    for (var j = 0; j < 5; j++) {
        console.log(i, j);
        if (i === 1 && j === 1) {
            break top;
        }
    }
}
```

这样当满足条件时候，会跳出双层循环。
`continue`也可以这样使用，效果第一个代码效果是一样的。