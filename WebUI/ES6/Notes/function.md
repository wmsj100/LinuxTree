---
title: 函数 
date: 2018-06-26 22:25:27	
modify: 
tag: [function]
categories: ES6
author: wmsj100
mail: wmsj100@hotmail.com
---

# 函数

## 概述
- 允许函数的参数写入默认值
	```ts
	function Point(x=0, y=0){
		this.x = x;
		this.y = y;
	}
	```
- 函数的参数是默认声明的,所以不能在函数内部再次声明`let/const`;
- 函数的参数不能重复;
- ```ts
	function foo({x,y=5}={}){
		console.log(x, y);
	}
	foo(); // undefine, 5;
	foo({x:1, y:3}); // 1, 3;
	```
- length 返回参数的个数,如果参数有默认值,这length的值为参数个数减去有默认值的参数个数;
	```ts
	let x = 1;
	function add(y=x){
		console.log(y);
	}

	let a = add(); // 1;
	let b = add(3); // 3;
	```
- 函数的参数的默认值是一个函数;
	```ts
	let foo = 'outer';
	function bar(func = () => foo) {
		console.log(func());
	}

	let a = bar(); // 'outer'
	```
	- 函数bar的参数`func`的默认值是一个匿名函数,返回值是变量`foo`.
	- 函数参数形成的作用域里面并没有定义变量`foo`,所以`foo`指向外层的全局变量`foo`,
- 另一个复杂的例子
	```ts
	var x = 1;
	function foo(x, y = function () { x = 2 }) {
		x = 3;
		y();
		console.log(x);
	}
	foo(x); // 2
	```
	- 函数的参数y的默认值是一个匿名函数,这个函数内部的变量x指向同一个作用域的第一个参数x.
	- 函数内部又声明了一个x,该变量与第一个参数x是同一个作用域,
	- 所以指向y后,x为2;

## rest参数
- rest参数(形式为...变量名),用于获取函数多余的参数,形成一个数组.
	- `const sortN = (...numbers) => numbers.sort();`
- rest参数后面不可以有其他参数,否则会报错
- 函数的`length`属性不包括`rest`参数

## 箭头函数
- `ES6`允许使用`箭头``=>`定义函数
	```ts
	var f = v=>v;
	var f = function(v){
		return v;
	};
	```
	- 上述俩个是等效的
- 如果箭头函数不需要参数或者需要多个参数,就需要使用一个圆括号代表参数部分;
	```ts
	var f = () => 5;
	var f = function(){ return 5 };
	var sum = (num1, num2) => num1 + num2;
	var sum = function(num1, num2){ return num1 + num2};
	```
- 如果箭头函数返回的是一个对象,必须在对象外面加上括号,因为括号被解释成代码块;
	```ts
	let get1 = id => ({id: id, name: 'tom'});
	```


## 参考
- [箭头函数](http://es6.ruanyifeng.com/?search=%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0&x=10&y=9#docs/function)
