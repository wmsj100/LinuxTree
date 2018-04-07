---
title: JavaScript数值极限
date: 2016-04-28
tags: [JavaScript,数值,算法]
categories: Dynamic
---

JavaScript的数值极限：

```javascript
Number.MIN_VALUE	
5e-324	//能够表示的最小数值
Number.MAX_VALUE
1.7976931348623157e+308	//能够表示的最小数值
Number.MIN_SAFE_INTEGER
-9007199254740991	//能够表示的最小整数
Number.MAX_SAFE_INTEGER
9007199254740991	//能够表示的最大整数
Number.NEGATIVE_INFINITY
-Infinity	//获取负无穷大
Number.POSITIVE_INFINITY
Infinity	//获取正无穷大
```

如果某次计算返回了正或负的 Infinity 值，那么该值将无法继续参与下一次的计算，因为 Infinity 不是能够参与计算的数值。要想确定一个数值是不是有穷的（换句话说，是不是位于最小和最大的数值之间），可以使用 isFinite() 函数。这个函数在参数位于最小与最大数值之间时会返回 true ，如下面的例子所示：

```javascript
var result = Number.MAX_VALUE + Number.MAX_VALUE;
alert(isFinite(result)); //false
```



