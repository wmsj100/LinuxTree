---
title: 正则扩展 
date: 2018-06-25 23:08:27	
modify: 
tag: [regexp]
categories: ES6
author: wmsj100
mail: wmsj100@hotmail.com
---

# 正则扩展

## 概述
- `var regexp = new RegExp('xyz', 'i')`
- `var rexexp = new RegExp(/xyz/, 'i')` 这种表示方法在`ES5`中报错
- `var regexp = new RegExp(/xyz/ig, 'i')` === `var regexp = /xyz/i` 前者被后者覆盖

## 字符串正则方法
- 字符串对象公有4个方法,`match/replace/search/split`;
	```ts
	let a = 'hello world';
	let b = 'world';
	let c = a.search(b);
	```
- source 返回正则表达式的正文
- flag 返回正则表达式的修饰符
	```ts
	var reg = /abc/ig;
	reg.source; // 'abc'
	reg.flag; // 'gi'

- `js`语言的正则支持先行断言和先行否定断言,不支持后行断言和后行否定断言;
	- 先行断言: 指的是`x`只有在`y`前面才匹配,
	- `/x(?=y)/`
	- `/\d+(?=%)/` 只匹配`%`前面的数字
	- 先行否定断言: 指的是`x`只有不再`y`前面才匹配
	- `x(?!y)/`
	- `/\d+(?!%)/` 只匹配不在百分号之前的数字

## 具名组匹配
- 之前正则的括号匹配值可以通过`exec`获取,但是只能通过数组的形式获取;
- `ES2018`引入了`具名组匹配`,允许为每一个组匹配指定一个名字,
- 在圆括号内部,模式头部添加`问号+尖括号+组名` `?<name>`;
	```ts
	const re = /(\d{4})-(\d{2})-(\d{2})/;
	const matchObj = re.exec('1990-12-22');
	console.log(matchObj); // ['1990-12-22', '1990', '12', '22'];
	const re1 = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
	let obj = re1.exec('1990-12-22');
	console.log(obj); // ["1990-12-22", "1990", "12", "22"]
	console.log(obj.groups); //{year: "1990", month: "12", day: "22"}
	```

## 解构赋值和替换
- 有了具名组匹配后,就可以使用解构赋值直接从匹配结果上为变量赋值;
	```ts
	let {groups: {year, day}} = re1.exec('1992-15-31');
	console.log(year, day); // 1992 31
	```
- 字符串替换时,使用`$<组名>`引用具名组;
	- `let d = '2015-01-03'.replace(re1, '$<day>/$<month>/$<year>'); // "03/01/2015"`
	
## 引用
- 如果正则表达式内部要引用某个`具名组匹配`,可以使用`\k<组名>`的写法;
- 数字引用`(\1)`依然有效
- 俩种引用语法还可以混用;
	```ts
	var r1 = /^(?<word>[a-z]+)!\k<word>$/;
	var state = r1.test('abc!abc');
	console.log(state); // true
	r1 = /^(?<word>[a-z]+)!\1$/;
	state = r1.test('abc!abc');
	console.log(state); // true
	r1 = /^(?<word>[a-z]+)!\k<word>!\1$/;
	state = r1.test('abc!abc!abc');
	console.log(state); // true
	```

## 参考
- []()
