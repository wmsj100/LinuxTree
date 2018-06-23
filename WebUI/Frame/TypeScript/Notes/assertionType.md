---
title: 类型断言 
date: 2018-06-23 22:19:14	
modify: 2018-06-23 22:19:16	
tag: [assertion]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 类型断言

## 概述
- 可以用来手动指定一个值的类型;
	- `<类型>值`
	- `值 as 类型`
- 但TS不确定一个联合类型的变量到底是哪个类型的时候,而有时候,我们需要在不确定类型的时候就访问其中一个类型的属性或方法,
	```ts
	function getLength(something: string | number): number{
		if((<string>something).length){
			return (<string>something).length;
		} else {
			return something.toString().length;
		}
	}
	```
- 类型断言不是类型转换,断言成一个联合类型中不存在的类型是不允许的.


## 参考
- []()
