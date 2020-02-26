---
title: 字符串扩展 
date: 2018-06-24 23:34:32	
modify: 2020-02-16 12:19:21  
tag: [string]
categories: ES6
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符串扩展

## 概述
- 字符串的遍历
	```ts
	for(let code of 'hello'){
	   console.log(code);
	}
	```

- includes/startWidth/endsWidth
	- includes(): 返回布尔值，表示是否找到了参数字符串
	- startWidth(): 返回布尔值，表示参数字符串是否在原字符串的头部
	- endsWidth(): 返回布尔值，表示参数字符串是否在原字符串的尾部；
	```ts
	let s = 'Hello world';
	let a = s.startsWith('Hello');
	let b = s.endsWith('ld');
	let c = s.includes('o');
	let d = s.indexOf('e');
	```

- `repeat`: 返回一个新字符串，表示将原字符串重复n次
	- `'x'.repeat(3); // 'xxx'`

- `padStart/padEnd`
	- ES2017引入了字符串补全长度的功能，如果某个字符串不够指定长度，会在头部或尾部补全
	- `padStart`: 补全头部
	- `padEnd`: 补全尾部
	- 这个`TS`暂时不支持

- 模板字符串
	- 传统JS语言，输出模板通常是这样写
	```ts
	$('#result').append(
	  'There are <b>' + basket.count + '</b> ' +
	  'items in your basket, ' +
	  '<em>' + basket.onSale +
	  '</em> are on sale!'
	);
	```
	- 上面这样的写法很不方便且繁琐，ES6引入了模板字符串解决这个问题
	```ts
	$('#result').append(`
	  There are <b>${basket.count}</b> items
	   in your basket, <em>${basket.onSale}</em>
	  are on sale!
	`);
	```
	- 模板字符串是增强版字符串，用反引号(`)标识
	- 如果模板字符串表示多行字符串，所有的空格和缩进都会被保留在输出中。
	- 如果不需要换行，可以使用`trim`方法消除它。
	- 模板字符串中嵌入变量，需要将变量写在`${}`中，内部可以放入任意`JS`表达式，可以进行运算以及对象属性引用。
	- `${}`之间还可以调用函数，如果函数返回值不是字符串，会按照转换规则转换为字符串
	- 模板字符串的出现让后台模板转换称为多余，这个操作直接在浏览器中完成转换，

## 标签模板
- 函数后面紧跟字符串构成标签模板,
- 标签模板不是模板,是函数调用的一种特殊形式,
	```ts
	let a = 5;
	let b = 6;
	function tag(s, v1, v2){
		console.log(s); // ["Hello ", " world ", ""]
		console.log(v1, v2); // 11, 30
	}
	tag`Hello ${a + b} world ${a * b}`;
	```
- tag函数的第一个参数是一个数组,该数组的成员是模板字符串中没有变量替换的部分,
- tag函数的其他参数,都是模板字符串各个变量被替换后的值,

## 参考
- [字符串扩展](http://es6.ruanyifeng.com/?search=%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0&x=10&y=9#docs/string#padStart%EF%BC%8CpadEnd)
