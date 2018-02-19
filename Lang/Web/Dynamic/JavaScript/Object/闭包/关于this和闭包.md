---
title: 关于this和闭包
date: 2016-05-19
tags: [JavaScript]
categories: Dynamic
---

1. `caller` -- 返回调用自己的函数，如果没有函数调用，则返回null, caller--指向父函数，推进栈

   ```javascript
   function fn4(argument) {
   	console.log(fn4.caller)	//null

   	function fn() {
         console.log(fn.caller);	//function: fn4
   	}
   	fn();
   }
   fn4();
   ```

2. `callee` -- 返回函数自己，多在匿名函数的场景中使用,递归。如果没有被调用而直接使用的话，就会报错。

   ```javascript
   var i = 0;
   window.onclick = function() {
   	console.log(i);
   	if (i < 5) {
   		i++;
   		setTimeout(arguments.callee, 1000);
   	}
   }
   ```

3. 三种变量

   1. 实例变量  b--（this）类的实例才可以访问

   2. 静态变量  c --（属性） 直接类型对象可以访问

   3. 私有变量  a  （局部变量）当前作用域内有效

      ```
      function classA() {
      	var a = 1;	
      	this.b = 2;
      }
      console.log(a) //error
      console.log(classA.b); //undefined
      classA.c = 3;
      console.log(classA.c); //3
      var q = new classA();
      console.log(q.a); //undefined
      console.log(q.c); //undefined
      console.log(q.b); //undefined
      ```

   4. 闭包，把函数内部的一个函数赋值给全局变量，然后就可以通过全局变量来访问和执行内部的函数，效果就像是内部函数逃脱，或者是暂存。

      ```javascript
      var a;
      (function fn1() {
      	function fn2() {
      		console.log("fn2");
      	}
      	fn2();
      	a = fn2;
      })()	//fn2
      a()	//fn2
      ```

      `fn1` 是一个自执行函数，但是把fn2赋值给了全局变量a，所以`fn2` 的函数就赋值给了a，`虽然fn2被销毁了，但是a引用的指针还是存在的。`
      因为fn2被全局变量使用着，所以fn2不会被销毁。