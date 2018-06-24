---
title: let和const
date: 2018-06-24 16:00:46	
modify: 
tag: [basic]
categories: ES6 
author: wmsj100
mail: wmsj100@hotmail.com
---

# let和const

## 概述
- ES6目标：是js可以用来编写复杂的大型应用程序，成为企业级开发语言；

## let声明
- let 块作用域变量声明，这个作用在`for`循环中特别有用
	```ts
	for(let i=0;i<3; i++){
		console.log(i);
	}
	console.log(i);// error 找不到i
	```
- let创建的变量在for循环中每一次都是单独的一个全新的变量；
- var创建的变量会出现变量提升，即可以在声明之前使用，值为`undefined`；let不允许这样，否则报错；

### 暂时性死区
- 只要块级作用域内存在`let`命令，它所声明的变量就“绑定”这个区域，不再受外部影响。
	```ts
	var tmp = 123;
	if(true){
		tmp = 32; // error 在声明之前就使用了变量
		let tmp;
	}
	```
	- 虽然`tmp`是一个全局变量，但是因为在块级作用域内使用`let`重新声明，形成了暂时性死区，所以在声明前对`tmp`赋值就会报错；
- ES6明确规定，如果区块中存在`let`和`const`命令，这个区块对这些命令声明的变量，从一开始就形成了封闭作用域，凡是在声明之前就使用这些变量，就会报错。
- 暂时性死区意味着`typeof`不再是一个百分百安全的操作了。
	```ts
	function bar(x=y, y=2){
		return [x, y];
	}
	bar();
	```
	- 上述代码会报错，因为x赋值为y，而此时y还没有声明，属于死区，
	```ts
	function bar(x=2, y=x){
		return [x, y];
	}
	bar();
	```
	- 上面这样的声明是正确的；

- `let x=x` 这样的代码也是不允许的，因为x还没有声明完成前就使用，会报错；

- 不允许重复声明变量，在函数内部也不允许重复声明参数；
	```ts
	function func(arg){
		let arg; // error 不允许重复声明
	}
	function func(arg) {
		{ let arg; } // ok 在块作用域内，重新声明
	}
	```

## 块级作用域
- ES5只有全局作用域和函数作用域，没有块级作用域，
	```ts
	var tmp = new Date();
	function f(){
		console.log(tmp);
		if(false){
			var tmp = "hello world";
		}
	}
	f(); // undefined
	```
	- 上面的代码本意是在函数内部先获取全局的作用域变量`tmp`，但是因为函数内部重新声明了变量`tmp`，所以相当于变量提升，所以`console.log`时候就是`undefined`;

- 外层的作用域无法读取内层作用域的变量；
- 内层作用域可以定义外层的同名变量；
- 块级作用域的出现，使得获得广泛使用的立即执行函数不再必要了。
- 尽可能使用函数表达式而不是声明声明，

## const
- 声明一个只读变量，一旦声明，就不能改变；意味着`const`一旦声明必须立即初始化，不能留到以后赋值；
- const变量和`let`类似，也存在暂时性死区。
- 和`let`一样，也不能重复声明；
- `const`并不是变量的值不得改动，而是变量指向的那个内存地址不得改动。
	- 对于简单类型的值,(数字/字符串/布尔值),值就保存在变量指向的那个内存地址，
	- 对于复合类型的值，(对象和数组),变量指向的内存地址，保存的只是一个指针，`const`只能保证这个指针是固定的，至于它指向的数据结构是不是可变的，就完全不能控制了。
	```ts
	const a = {
		a: 1,
		b: 2
	};
	a.a = 45;
	a['c'] = true;
	const b = [];
	b.push('asdf');
	b.length = 0;
	```
	- 常量`a/b`都可以更改内部的值，只是不能重新给`a/b`赋值修改指向的内存地址；

- ES6有六种声明命令的方法；`var/ function/let/const/class/import`

## 顶层对象
- ES5中顶层对象的属性和全局变量是挂钩的，这被认为是JS语言设计的败笔之一。
- ES6规定，var/function命令声明的全局变量，依旧是顶层对象的属性；
	- `let`,`const`, `class`命令声明的全局变量，不属于顶层对象的属性。


## 参考
- []()

