---
title: 泛型 
date: 2018-06-24 12:14:08	
modify: 
tag: [basic]
categories: TypeScript 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 泛型

## 概述
- 指在定义函数/接口或类的时候，不预先指定具体的类型，而是在使用的时候再指定类型的一种特性。
	```ts
	function createArray(length:number, value: any):Array<any>{
		let result = [];
		for(let i=0; i<length; i++){
			result.push(value);
		}
		return result;
	}

	createArray(3, 'x'); // ['x', 'x', 'x']
	```
	- 上例中的有一个明显的缺陷，它没有准确定义返回值的类型
	- 我们预期的是，数组中的每一个值的类型应该是`value`的类型
- 使用泛型重新定义
	```ts
	function createArray<T>(length:number, value: T):Array<T>{
		let result: T[] = [];
		for(let i=0; i<length; i++){
			result[i] = value;
		}
		return result;
	}

	createArray<string>(3, 'x'); // ['x', 'x', 'x']
	createArray<number>(4, 100);
	```
	- 在函数名后面添加`<T>`，其中`T`用来指定任意输入的类型，在后面的输入`value:T`和输出`Array<T>`中即可使用；
	- 接着在调用的时候，具体指定类型`string`即可。

- 定义多个类型参数，可以一次定义多个类型参数
	```ts
	function swap<T, U>(tuple: [T, U]): [U, T]{
		return [tuple[1], tuple[0]];
	}

	swap([7, 'seven']);
	swap([4,3]);
	```

- 泛型约束：在函数内部使用泛型时候，由于事先不知道它是哪种类型，所以不能随意的操作它的属性或方法，否则就会报编译错误；
- 这时候可以对泛型进行约束，只允许传入那些包含目标属性`length`的变量
	```ts
	interface Length{
		length: number;
	}

	function fn1<T extends Length>(args: T): T{
		console.log(args.length);
		return args;
	}

	fn1('asdf');
	fn1(2); // error
	```

- 泛型接口
	```ts
	interface CreateArray<T> {
		(length: number, value: T): Array[T];
	}

	let create1: CreateArray<any>;
	create1 = function<T>(length: number, value: T): Array<T>{
		let result T:[] = [];
		for(let i =0; i< length; i++){
			result[i] = value;
		}
		return result;
	}

	create1(3, 'x');
	```

- 泛型用于类
	```ts
	class GeneNum<T>{
		zero: T;
		add: (x: T, y: T) => T;
	}

	let myNum = new GeneNum<number>();
	myNum.zero = 0;
	myNum.add(10, 20){
		return x + y;
	}
	```

## 参考
- [泛型](https://ts.xcatliu.com/advanced/generics.html)
