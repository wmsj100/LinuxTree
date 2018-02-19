---
title: map给数组中每一项值都进行计算并获取结果
date: 2016-04-30
tags: [数组,遍历]
categories: Dynamic
---

如果有一个数组a，想要给每一项值添加一个字符串，怎么做，可以使用传统的`for` 循环，但是使用`map` 会更加的便捷

```javascript
var a = [1, 2, "red", "blue", 3];
var b = a.map(function(item) {
	return item + "wmsj"
});
console.log(b);
//Array [ "1wmsj", "2wmsj", "redwmsj", "bluewmsj", "3wmsj" ]
```

map不会改变原数组，所以可以把生成的数组复制给变量b，