---
title: 变量的解构赋值 
date: 2018-06-24 18:37:49	
modify: 
tag: [basic]
categories: ES6 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 变量的解构赋值

## 概述
- ES6允许按照一定模式，从数组和对象中提取值，对变量进行赋值，这被称作解构。

## 数组解构
	```ts
	let arr = [1,2,3];
	let [a1, b1, c1] = arr;
	let [x,,y] = arr;
	let [x] = arr;
	let [,,x] = arr;
	let [foo = true] = []; // 指定默认值
	let [x, y='b'] = ['a'];
	let [x=1] = [null]; // x=null;
	```

## 对象解构
- 对象解构与数组的区别是没有按次序排序的，对象的属性没有次序，变量必须与属性名同名，才能取到正确的值。

	```ts
	let a = {foo: 'aaa', bar: 'bbb'};
	let {foo, bar} = a; // foo='aaa', bar='bbb'
	```
- 如果变量名与属性名不一致，必须写成下面这样；
	- `let {foo:haha} = a; // haha='aaa'`
	- 对象解构的内部机制是先找到同名属性，然后再赋给对应的变量，真正被赋值的是后者，而不是前者。
	- foo是匹配的模式，haha才是变量，真正被赋值的是变量haha，而不是模式foo；
- 解构也可以嵌套
	```ts
	const node = {
		loc: {
			start: {
				line: 1,
				column: 5
			}
		}
	};

	let { loc, loc: { start }, loc:{ start:{ line }}} = node;
	```

- 嵌套赋值
	```ts
	let obj = {};
	let arr = [];
	({foo: obj.prop, bar: arr[0]} = {foo: 123, bar: true});
	```

- 指定默认值, 默认值生效的前提是对象的属性值严格等于`undefined`
	```ts
	var { x = 3 } = {}; // x=3
	var { x, y = 5 } = { x: 1 }; // x=1, y=5
	var {x:y = 5} = {}; // x=undefined; y=5
	var {x:y = 3} = {x:5}; // y = 5;
	var {message: msg = 'somethis'} = {}; // msg = 'somethis';
	var {x=3} = {x:null}; // x=null; 
	```
- null !== undefined 所以默认值不会生效；

## 字符串解构
- 字符串也可以解构赋值，因为此时字符串被转换成了一个数组对象
	```ts
	const[a,b,c,d,e] = 'hello';
	a // 'h'
	b // 'e'
	```
- 类似数组对象都有一个`length`属性，因此还可以对这个属性解构赋值
	- `let {length: len} = 'hello'; // len=5`

## 数字和布尔值解构赋值
- 如果等号右边是数值和布尔值，则会先转为对象；
- `let {toString: s} = 123`

## 函数的解构
```ts
function add([x, y]){
	return x + y;
}
add([1,2]); // 3
```
- 上面代码中，函数参数被传入的那一刻，数组参数就被解构成变量x, y;
- 函数解构也可以使用默认值；
	```ts
	function move({x=0, y=0} = {}){
		return [x, y];
	}
	move(); // [0,0]
	move({x:3}) // [3, 0]
	move({y:4}); // [0, 4]
	```
---
## 用途
- 交换变量的值
	```ts
	let x = 1;
	let y = 2;
	[x, y] = [y, x];
	```
	- 上例中的写法简洁而且易读，语义非常清晰
- 从函数返回多个值
	- 函数只能返回一个值，如果要返回多个值，只能将他们放在数组或对象里返回，
	- 通过解构去除这些值就很方便了
	```ts
	function example(){
		return [1,2,3];
	}
	let [a,b,c] = example();

	function example(){
		return {
			foo: 1,
			bar: 2
		}
	}
	let {foo, bar} = example();
	```
- 函数参数的定义
	- 解构赋值可以很方便的将一组参数与变量名对应起来
	```ts
	// 参数是一组有序的值
	function f([x,y,z]){...}
	f([1,2,3]);
	
	// 参数是一组无序的值
	function f({x,y,z}){...}
	f({z:3, y:2, x:1});
	```

- 提取`JSON`数据
	- 解构赋值对提取`JSON`对象中的数据，尤其有用
	```ts
	let jsonData = {
		id: 23,
		status: 'ok',
		data: [12,45]
	};
	let {id, status, data:number} = jsonData; 
	console.log(id, status, number); // 23, 'ok', [12, 45]
	```
- 函数参数的默认值
	```ts
	jQuery.ajax = function (url, {
	  async = true,
	  beforeSend = function () {},
	  cache = true,
	  complete = function () {},
	  crossDomain = false,
	  global = true,
	  // ... more config
	} = {}) {
	  // ... do stuff
	};
	```
- 输入模块的指定方法
	- 加载模块时，往往需要指定输入哪些方法，解构赋值使得输入语句非常清晰。
	- `const { SourceNode } = require("source-map");`

## 参考
- [解构](http://es6.ruanyifeng.com/?search=%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0&x=10&y=9#docs/destructuring)
