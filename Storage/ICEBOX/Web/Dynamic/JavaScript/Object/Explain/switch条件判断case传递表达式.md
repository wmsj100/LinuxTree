---
title: switch条件判断case传递表达式
date: 2016-04-29
tags: [条件,遍历,函数]
categories: Dynamic
---

`switch` 循环中`case` 不仅可以传递常量，还可以传递变量、表达式，当传递变量时候，`switch` 的值就应该是`true` 

```javascript
var num = 10;
switch (true) {
	case num < 0:
		console.log("Less than 0.");
		break;
	case num >= 0 && num <= 10:
		console.log("Between 0 and 10.");
		break;
	case num > 10 && num <= 20:
		console.log("Between 10 and 20.");
		break;
	default:
		console.log("More than 20.");
}
```

- `switch( 0 || "" || undefined || null || NaN || num )` ----结果输出`More than 20.` 
- `switch(false)` -- 结果输出`Less than 0.` 
- `switch(true)` --只有这次是正确的。

这个例子首先在 switch 语句外面声明了变量 num 。而之所以给 switch 语句传递表达式 true ，是因为每个 case 值都可以返回一个布尔值。这样，每个 case 按照顺序被求值，直到找到匹配的值或者遇到 default 语句为止（这正是这个例子的最终结果）。

switch 语句在比较值时使用的是全等操作符，因此不会发生类型转换（例如，字符串 "10" 不等于数值 10）。