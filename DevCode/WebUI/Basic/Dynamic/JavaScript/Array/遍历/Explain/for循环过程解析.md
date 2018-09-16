---
title: for循环过程解析
date: 2016-05-02
tags: [遍历]
categories: Dynamic
---

1. 因为for循环的+1操作是在for循环判断时候进行的，如果`i` 符合条件的话就自动加1;
2. `i` 的极限条件也定义了，所以不需要在内部再次申明`i<length` ;
3. `i` 的极限条件只能设置一个，不能同时判断`i` 的最大值和最小值，另一个限制只能放到内部，比如这样的条件是不允许的。`i>-1,i<10` ;

```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";
function findLetter(str, letter) {
	var arr = [];
	for (var i = 0; i < str.length; i++) {
		i = str.indexOf(letter, i);
		if (i === -1) {
			return arr;
		}
		arr.push(i);
	}
}
var b = findLetter(stringValue, "e");
console.log(b);	// Array [ 3, 24, 32, 35, 52 ]
```

- 所有的`for`循环都可以改写为`while`循环
```javascript
for (var i = 0; i < 3; i++) {
    console.log(i);
}

var i = 0,
    len = 3;
while (i < len) {
    console.log(i++);
}
直接在输出过程中使用i++，
```

- `for`语句可以省略全部内容，结果就导致一个无限循环`for(;;;){}`;
