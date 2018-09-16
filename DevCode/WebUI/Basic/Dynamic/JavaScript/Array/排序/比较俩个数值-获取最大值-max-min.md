---
title: 比较俩个数值 获取最大值 max min
date: 2016-04-28
tags: [排序,函数,算法]
categories: Dynamic
---

获取俩个数值中的最大值，通过条件操作符进行判断，这应该是最简洁的写法了吧。

```javascript
var num1 = 40,
	num2 = 30;
var sum = (num1 > num2) ? num1 : num2;
console.log(sum);	//40
```

