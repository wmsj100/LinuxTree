---
title: interface 
date: 2018-06-23 18:28:55	
modify: 2018-06-23 18:29:01 
tag: [interface]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# Interface

## 概述
- 在面向对象的语言中,是一个很重要的概念,是对行为的抽象;

## 范例
```ts
interface Person{
	name: string;
	age: number
}
```
- 'age?' 可选参数
- '[propName: string]: string| number' 定义任意属性,
	- 定义了任意属性后,可选属性和确定属性都必须是任意属性的子集'
- 'readonly id: number' 定义只读属性
	- 因为在接口内部的属性不能定义`const`,所以只能定义只读属性

## 参考
- [接口](https://ts.xcatliu.com/basics/type-of-object-interfaces.html)
