---
title: 枚举 
date: 2018-06-23 23:32:37	
modify: 2018-06-23 23:32:40	
tag: [enum]
categories: TypeScript 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 枚举

## 概述
- 枚举类型用于取值限定在一定范围内的场景;
- `enum Days {Sun, Mon, Tue, Wed, Thu, Fri, Sat};`;
- 枚举成员会被赋值为从`0`开始递增的数字,同时也会对枚举值到枚举名进行反向映射;
	```ts
	console.log(Days);
	0:"Sun";
	1 : "Mon";
	2 : "Tue";
	3 : "Wed";
	4 : "Thu";
	5 : "Fri";
	6 : "Sat";
	Fri : 5;
	Mon : 1 ;
	Sat : 6;
	Sun : 0;
	Thu : 4;
	Tue : 2;
	Wed : 3;
	```
- 对于枚举值也可以手动赋值,
	- `enum Days{Sun = 7, Mon = 1, Tue, Wed, Fri, Sat}`;
- 对于未手动赋值的枚举项会在前一个枚举项递增;
- 如果手动赋值的枚举值和未手动赋值的枚举重复了,编译器不会报错,但是编译的时候后者会覆盖前者;
- 手动赋值的枚举也可以不是数字,此时需要使用类型断言来让ts无视类型检查
- `enum Days{Sun=7, Mon, Tue, Wed=<any>'s'}`

- 常数枚举: 使用`const enum`定义
	```ts
	const enum Direct{Up, Down, Left, Right}
	let directions = [Direct.Up, Direct.Right, Direct.Down, Direct.Left];
	console.log(directions); 
	// var directions = [0 /* Up */, 1 /* Right */, 2 /* Down */, 3 /* Left */];
	```

- 外部枚举: 使用`declare enum`定义
	```ts
	declare enum test1{t1, t2, t3};
	let test2 = [test1.t1, test1.t2, test1.t3];
	// 编译后的值
	// var test2 = [test1.t1, test1.t2, test1.t3];
	```

- 使用外部枚举,声明的枚举值必须先定义,否则编译后会报错,找不到枚举值;

## 范例

## 参考
- []()
