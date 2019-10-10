---
title: 数组类型 
date: 2018-06-23 18:42:47	
modify: 2018-06-23 18:42:51	
tag: [array]
categories: TypeScript 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数组类型

## 概述
- 数组类型的组内类型全是相同类型;
- 数组的项中不允许出现其他类型的值;
- 枚举: 组内可以定义任意类型的值;

## 内容
- `let name1: number[] = [1,2,3]`
- `let name1: Array<number> = [1,2,3]` 使用数组泛型定义数组
- 可以使用接口表示数组
```ts
interface NumberArray{
	[index: number]: number
}
```
- 表示只要`index`的类型只要是`number`,那么值的类型就必须是`number`;
- `let list: any[] = [1, 'a']` 表示任意类型的数组
- 类数组
```ts
function sum(){
	let args: number[] = arguments;
}
```

## 参考
- [数组](https://ts.xcatliu.com/basics/type-of-array.html)
