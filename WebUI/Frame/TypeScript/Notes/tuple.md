---
title: 元组类型 
date: 2018-06-23 23:21:48	
modify: 2018-06-23 23:21:51	
tag: [tuple]
categories: TypeScript 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 元组类型

## 概述
- 数组合并了相同类型的对象,而元组合并了不同类型的对象.
- `let xcat: [string, number] = ['hello', 1]` 定义一个值分别为`string`和`number`的元组;
- 当赋值或访问一个已知索引的元素时,会得到正确的类型;
- 也可以定义时有多个类型的值,但只赋值其中一个或几个;
	```ts
	let xcat: [string, number];
	xcat[0] = 'hello';
	```
	- 虽然文档是ok的,而且编译器也没有报错,但是编译后的js在页面会报错;
	- 因为没有赋值的元组,编译后的js赋值为`undefined`;
	- 然后`xcat[0]='hello'`这样直接就报错了,
	- 所以还是建议不要只是声明一个元组,而是在声明的过程中进行赋值操作;

- 但是直接对元组的变量进行初始化或赋值时,需要提供元组定义的所有值,否则会报错.
	```ts
	let xcat: [string, number];
	xcat = ['hello', 1];
	```
- 但赋值为越界的元素时,它的值的类型必须时元组的每个类型的联合类型
	```ts
	xcat[3] = 'cat'; // ok
	xcat[4] = true; // error, must be string | number;

## 参考
- [元组类型](https://ts.xcatliu.com/advanced/tuple.html)
