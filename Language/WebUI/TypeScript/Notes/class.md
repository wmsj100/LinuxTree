---
title: 类 
date: 2018-06-24 00:13:30	
modify: 2018-06-24 07:51:57  	
tag: [class]
categories: TypeScript 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 类

## 概述
- 传统方法中,js通过构造函数实现类的概念,通过原型链实现继承.在ES6中添加了class;

## 类的概念
- 类: 定义了一件事务的抽象特点,包含它的属性和方法;
- 对象: 类的实例,通过`new`生成;
- 面向对象的三大特征: 封装/继承/多态
- 封装: 将对数据的操作细节隐藏起来,只暴露对外的接口.外界调研端不知道细节就能通过对外提供的接口来访问该对象,同时保证外部无法任意更改内部的数据.
- 继承: 子类继承父类,之类拥有父类的所有特性
- 多态: 由继承而产生了相关的不同的类,对同一个方法可以有不同的响应.
- 存取器: 用以改变属性的读取和赋值
- 修饰符: 是一些关键字,用于限定成员或类型的性质,比如public表示公有属性或方法.
- 抽象类: 抽象类是供其他类继承的基类,抽象类不允许被实例化,抽象类中的抽象方法必须在子类中被实现
- 接口: 不同类之间公有的属性或方法,可以抽象成一个接口.接口可以被类实现.一个类只能继承自另一个类,但是可以实现多个接口

## 属性和方法
- 使用`class`定义类,使用`constructor`定义构造函数
- 通过`new`生成新实例的时候,会自动调用构造函数
	```ts
	class Animal{
	    name:string;
		constructor(name){
			this.name = name;
	    }
		sayHi(){
			return `My name is ${this.name}`;
	    }
	}
	let a = new Animal('Jack');
	```
## 类的继承
- `extends`: 通过该关键字实现继承的操作,
- `super`: 子类中通过该关键字来调用父类的构造函数和方法
	```ts
	class Cat extends Animal{
		constructor(name){
			super(name); // 调用父类的 constructor(name)
		}
		sayHi(){
			return 'Meow, ' + super.sayHi();
		}
	}

	let c = new Cat('Tom'); // "Meow, My name is Tom"
	```

## 存取器
- 使用`geeter`和`setter`可以改变属性的赋值和读取行为
	```ts
	class Animal {
		constructor(name) {
			this.name = name;
		}
		get name() {
			return 'Jack';
		}
		set name(value) {
			console.log('setter: ' + value);
		}
	}

	let a = new Animal('Kitty'); // setter: Kitty
	a.name = 'Tom'; // setter: Tom
	console.log(a.name); // Jack
	```

## 静态方法
- `static` 修饰符修饰的方法称为静态方法,不需要实例化,只能通过类来调用
	```ts
	class Animal{
		name: string;
		constructor(name){
			this.name = name;
		}
		static isAnimal(a){
			return a instanceof Animal;
		}
	}

	let a = new Animal('Jack');
	Animal.isAnimal(a);
	```
	- 上例中对象`a`上没有`isAnimal`方法，直接调用会报错；

## 实例属性
- ES6中实例的属性只能通过构造函数中的`this.xxx`来定义，ES7中可以直接在类里定义
	```ts
	class Animal{
		name = 'Jack';
		constructor(){
			//;
		}
	}
	```

## 静态属性
- 和静态方法类似，只能被类调用

## 类的用法
- TS中可以使用三种访问修饰符，`public`,`private`, `protected`
- `public`: 修饰的属性和方法是公有的，可以在任何地方被访问到，默认所有的属性和方法都是该类；
- `private`: 修饰的属性或方法是私有的，不能在声明它的类的外部访问
- `protected` 修饰的属性或方法是受保护的，和`private`类似，区别是它在子类中也是允许被访问的。
- `abstract`: 抽象类，用于定义抽象类和其中抽象的方法，
	- 抽象类不允许被实例化，
	- 抽象类中的抽象方法必须被子类实现

	```ts
	abstract class Animal{
		protected name;
		public constructor(name){
			this.name = name;
		}
		abstract sayHi();
	}

	class Cat extends Animal{
		constructor(name){
			super(name);
			console.log(this.name);
		}
		public sayHi(){
			//;
		}
	}
	```
	- 类的属性可以添加类型；

---

## 类与接口
- 一般来讲，一个类只能继承自另一个类，有时候不同的类之间有一些共有的特性，可以把特性提取成接口，用`implements`关键字来实现。
	```ts
	interface Alarm{
		alert();
	}

	class Door{

	}

	class SecurityDoor extends Door implements Alarm{
		alert(){
			console.log('SecurityDoor alert');
		}
	}

	class Car implements Alarm{
		alert(){
			console.log('car alert');
		}
	}

	let a = new SecurityDoor();
	let b = new Car();
	```

- 一个类可以实现多个接口
	```ts
	interface Alarm{
		alert();
	}

	interface Light{
		lightOn();
		lightOff();
	}

	class Door{

	}

	class SecurityDoor extends Door implements Alarm{
		alert(){
			console.log('SecurityDoor alert');
		}
	}

	class Car implements Alarm, Light{
		alert(){
			console.log('car alert');
		}
		lightOn(){
			console.log('Car light on');
		}
		lightOff(){
			console.log('car Light off');
		}
	}

	let a = new SecurityDoor();
	let b = new Car();
	```

- 接口和接口之间可以是继承关系
	```ts
	interface Alarm{
		alert();
	}

	interface Light extends Alarm{
		lightOn();
		lightOff();
	}
	class Car implements Light{
		alert(){
			console.log('car alert');
		}
		lightOn(){
			console.log('Car light on');
		}
		lightOff(){
			console.log('car Light off');
		}
	}
	let b = new Car();
	```

- 接口继承类
	```ts
	class Point {
		x: number;
		y: number;
	}

	interface Point3d extends Point {
		z: number;
	}

	let point3d: Point3d = { x: 1, y: 2, z: 3 };
	```

- 混合类型： 使用接口的方式来定义函数的形状
	```ts
	interface Counter{
		(start: number): string;
		interval: number;
		reset():void;
	}

	function getCounter(): Counter{
		let counter = <Counter>function(start: number){}
		counter.interval = 123;
		counter.reset = function(){};
		return counter;
	}

	let c = getCounter();
	c(10);
	c.reset();
	c.interval = 5.0;
	```

## 参考
- [class](https://ts.xcatliu.com/advanced/class.html)
