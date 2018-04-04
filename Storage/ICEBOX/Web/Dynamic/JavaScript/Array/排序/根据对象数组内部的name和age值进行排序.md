---
title: 根据数组对象内部的"name"和"age"值进行排序
date: 2016-04-30
tags: [数组,排序,函数,算法]
categories: Dynamic
---

客户的存储信息里面一般都会有`name` , `age` 属性，怎么按照这些值重新进行排序呢，说到排序肯定会想到`sort()` 函数，然后就是调用函数写法了。

```javascript
var data = [{
	name: "Zachary",
	age: 28
}, {
	name: "Nicholas",
	age: 29
}, {
	name: "wmsj100",
	age: 25
}, {
	name: "ruoye",
	age: 29
}];
data.sort(check("age"));
function check(prop) {
	return function(obj1, obj2) {
		var value1 = obj1[prop],
			value2 = obj2[prop];
		if (value1 > value2) {
			return 1;
		} else if (value1 == value2) {
			return 0;
		} else {
			return -1;
		}
	}
}
```
