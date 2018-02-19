---
title: this
data: 2016-05-20
tags: [This]
categories: Dynamic
---

`this` -- 指代的是当前调用环境，内部函数的调用对象也是window

```javascript
function fn(argument) {
	function fn1() {
		console.log(this); //window
	}
	fn1()
}
fn()
```

把父函数的执行环境、作用域也压入了堆栈。

通过`console.trace()` 可以查看堆栈队列

```javascript
function fn(argument) {
	function fn1() {
		function fn2() {
			console.trace(); //fn2() , fn1(), fn() , <匿名>
			console.log(this) //window
		}
		fn2();
	}
	fn1()
}
fn()
```

堆栈--先入后出。那个匿名函数就是全局的执行环境

内部函数的调用在纯函数的环境下仍然是需要window调用的。this指代的不是父函数，而是全局变量

函数嵌套的时候，内部函数的执行环境还是外面的global环境	 

- setTimeout / setInterval 的执行环境也是window；

```javascript
document.addEventListener("click",function(){
	console.log(this);	//HTMLDocument
	setTimeout(function(){
		console.log(this)	//window
	},200)
},false);
```

事件驱动的异步IO模型；

setTimeout是队列模式，全局在维护这个队列

可以把this通过赋值给变量存储起来

```javascript
document.addEventListener("click",function(){
	var me = this;
	console.log(this);	//HTMLDocument
	setTimeout(function(){
		console.log(me)	//HTMLDocument
	},200)
},false);
```

函数的生命周期  ，

函数载入计算机内存，函数调用--周期开始，函数解释，--周期结束，从内存中销毁。

this作为调用对象，谁触发它，谁就是this，所以第一个this指代的是触发的document

```javascript
var obj1 = {
	name: "wmsj",
	fn: function(){
		this.age = 123;
      //this指代obj1；这样就给obj1添加了属性
		console.log(this);
	}
}
obj1.fn();	//Object { name: "wmsj", fn: obj1.fn(), age: 123 }
```

```javascript
var obj1 = {
	name: "wmsj",
	fn: function(){
		this.age = 123;
		console.log(this);	//object;
	}
}
obj1.fn();

var fn2 = obj1.fn;	//把fn赋值给fn2;
fn2();	
//window;	因为执行环境是window，fn2是window执行的。
```

samaritan89.github.io/f2e/fs/构造函数.html

- 构造函数

所谓构造函数，就是通过函数生成一个新对象（object），这时，this就指这个新对象。

new运算符接收一个函数F及其参数；new f(arguments...).这个过程分为三步：

1. 创建类的实例。这步是把一个空对象的`__proto__` 属性设置为`F.prototype` .
2. 初始化实例。函数F被传入参数并调用，关键字this被设定为该实例。
3. 返回实例。

```javascript
function p1(name) {
	this.name = name;
}
p1.prototype.print = function() {
	console.log(this.name);
}
var a1 = new p1("wmsj");
var a2 = new p1("wmsj100");
a1.__proto__ === p1.prototype	//true
```

prototype中的this指代的是p1，因为p1.prototype.print,这个过程是p1在调用，所以this就指向调用的对象 p1；

prototype中设置返回值是没有效果的。

```javascript
p1.prototype.print = function(){
	console.log(this.name);
	return 0;	//这个会被忽略；
}
```

- `bind ` 是ES5加入的参数，IE8支持ES5，bind可以把this指向传入的参数。返回一个新函数，并且使函数内部的this为传入的第一个参数

```javascript
var obj1 = {
	name: "wmsj",
	fn: function(){
		this.age = 123;
		console.log(this);
	}
}
obj1.fn();	//obj1

var fn2 = obj1.fn;
fn2();	//window

var fn3 = obj1.fn.bind(obj1);
fn3();	//obj1
```

bind和call的区别 -- bind改变this的值，但是返回一个函数，不会直接调用，需要单独调用，但是call在改变this的值的时候会立即调用函数，如下

```javascript
fn2.call({"class": "lev12"});
Object { class: "lev12", age: 123 }
```

call 和 bind 其实功能类似，但是call不会存储函数，需要每次都使用call，而bind会把函数存储下来，以后如果要使用函数，就可以直接使用这个返回的函数，不需要再次调用bind了。

```javascript
var obj = {
	fn: function(age, name) {
		this.age = age;
		this.name = name;
		console.log(this);
	}
};
obj.fn(232);
var a = obj.fn;
a();
var b = obj.fn.call(obj, 23, "wmsj");
var d = obj.fn.apply({}, [23, "wmsj"]);
var d = obj.fn.apply(obj, [23, "wmsj"]);
var c = obj.fn.bind(obj);
c(23, "wmsj");
```

arguments

```javascript
function join() {
	var str = "";
	for (var i = 0; i < arguments.length; i++) {
		str += "," + arguments[i];
	}
	return str.substr(1);
}
```

caller -- 指向父元素、父函数

```javascript
function fn4(){
	console.log(fn4.caller);
	function fn(){
		console.log(fn.caller);
	}
	fn();
}
fn4();
```

arguments.callee -- 指向函数自身

```javascript
var i = 0;
document.addEventListener("click", function() {
	console.log(i);
	if (i < 5) {
		i++;
		setTimeout(arguments.callee, 400);
	}
}, false);
```

三种变量

实例变量--（this）只有通过实例才可以访问

静态变量 -- 属性	只有自己可以访问

私有变量 -- var	只有自己可以访问

```javascript
function a(){
  this.b = 1;
  console.log(this);
}
a();	//window;
window.b	//1;
```

其实这个已经很说明问题来，通过实例申明的变量其实是绑定到执行环境上面的属性，比如可以通过`window.b` 来调用。

自由变量。。。

通过DOM绑定对象，谁触发，this就指代谁。