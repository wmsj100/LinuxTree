---
title: 函数 
date: 2018-06-23 21:54:02 
modify: 2018-06-23 21:54:06	
tag: [function]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 函数

## 概述
- 函数的参数是固定的,必须完全匹配,确定参数的类型,并且明确函数的返回类型
```ts
function sum(x:number, y:number):number{
	return x + y;
}
```
- `=>` 箭头函数: 用来表示函数的定义,左边是输入类型,需要用括号括起来,右边是输出类型,
	```ts
	let mySum:(x:number, y: number) => number = function(x:number, y:number){
		return x + y;
	}
	```
- 用接口定义函数的形状
	```ts
	interface SearchFunc{
		(source: string, subString: string): boolean;
	}
	let mySearch: SearchFunc;
	mySearch = function(source:string, subString: string){
		return source.search(subString) !== -1;
	}
	```

- 可选参数,可选参数后面不可以有必须参数;
	```ts
	function buildName(firstName: string, lastName?: string){
		return firstName + ' ' + lastName;
	}
	```

- 默认参数,它后面的参数没有限制,可以有可选参数和必填参数;
	```ts
	function buildName(firstName: string, lastName: string = 'Cat'){
		return firstName + ' ' + lastName;
	}
	```
- 剩余参数,用`...rest`方法获取函数中的剩余参数
	```ts
	function push(array:any[], ...items: any[]){
		items.forEach(function(item){
			array,push(item)
		});
	}
	```

- 重载:允许一个函数接受不同数量/类型的参数做出不同的反应
	```ts
	function reverse(x: number):number;
	function reverse(x: string):string;
	function reverse(x: string | number): string | number{
		if(typeof x === 'string'){
			return x.split('').reverse().join('');
		} else if(typeof x === 'number'){
			return Number(x.toString().split('').reverse().join(''));
		}
	}
	```
	- 重复定义了多次函数,前几次都是函数定义,后面是函数的实现,在编辑器中可以精确的看到前面的提示;

## 参考
- []()
