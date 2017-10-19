---
title: NaN undefined null和自身比较
date: 2016-04-28
tags: [JavaScript,数值]
categories: Dynamic
---

```javascript
NaN == NaN 	
false
Nan === NaN 
false
undefined == undefined
true
undefined === undefined
true
null == null
true
null === null
true
```
NaN是最特殊的，和自己不相同。
可以通过函数`isNaN( )` 对内容进行判断是否是数值类型
```javascript
isNaN(true)	//false 是数值
isNaN("hllo")	//true	不是数值
```

根据规则，任何操作数与 NaN 进行关系比较，结果都是 false 。于是，就出现了下面这个有意思的现象：

```javascript
var result1 = NaN < 3; //false
var result2 = NaN >= 3; //false
```
按照常理，如果一个值不小于另一个值，则一定是大于或等于那个值。然而，在与 NaN 进行比较时，这两个比较操作的结果都返回了 false 。




