---
title: this,闭包
date: 2016-05-20
tags: [闭包,This,饥人谷]
categories: Dynamic
---

### 问答

1. apply、call 有什么作用，什么区别

   `apply` 和`call` 都可以设置执行函数的`this` 的值，二者很相似，唯一的区别是`apply` 的参数只有俩个，一个是`this` 的值，而另一个是传入的参数是数组形式，而`call` 的参数个数是不确定的，传入的参数是队列形式排列，实际场合中`apply` 的使用场景会更广泛些，常搭配`arguments` 来使用。

   ```javascript
   obj = {
   	fn: function(age, sex) {
   		this.age = age;
   		this.sex = sex;
   		console.log(this);
   	}
   }
   obj.fn(12, "wmsj100");	//object
   var a = obj.fn;
   a(23);	//window
   a.apply(obj, [12, "wmsj100"]);	//object
   a.call(obj, 12, "wmsj100");	//object
   ```

   `apply` 搭配`arguments` 的一个使用场景，模拟数组的`join` 使参数整合为字符串；

   ```javascript
   function join() {
   	return Array.prototype.join.apply(arguments);
   }
   join(1,2)	//"1,2"
   ```

### 代码

1. ```javascript
   var john = {
   	firstName: "John"
   }

   function func() {
   	alert(this.firstName + ": hi!");
   }
   john.sayHi = func
   john.sayHi()	//"john: hi!"
   ```

   因为`this` 指向调用自己的对象，当直接执行`func` 的时候，因为此时的执行环境是`window` 所以`this` 指向`window` ，而`window` 中并没有定义`firstName` 属性，所以就输出`undefined: hi!` ;

   而把`func` 赋值给对象`john` 的属性`sayHi` 时候，此时调用`func` 的对象是`john` ，而这个对象是拥有`firstName` 属性的，所以就输出了`John：hi！` ；

2. ```javascript
   func()
   function func() {
   	alert(this)
   }	//window
   ```

   这个首先是因为函数声明会前置，因此即便调用函数在函数`func` 定义之前，执行时候也会先创建函数，然后再执行调用。而因为调用函数`func` 的执行环境还是`window` ，所以此时的`this` 仍然指向`window` 。

3. ```javascript
   function fn0() {
   	function fn() {
   		console.log(this); 
   	}
   	fn();
   }

   fn0();	//window

   document.addEventListener('click', function(e) {
   	console.log(this); //document
   	setTimeout(function() {
   		console.log(this); //window
   	}, 200);
   }, false);
   ```

   对于函数来说，它的调用都是被推入堆栈中执行，按照先进后出的原则执行，可以通过`console.trace()` 来查看，它的执行环境都是`window` ，而不是其父函数。 

   对于第二个点击事件，因为是通过`document` 的点击来执行事件的，所以`this` 就指向调用的`document` 对象；

   对于`setTimeout 、setInterval` 来说，执行环境都是window，所以`this` 就指向`window` 。

4. ```javascript
   var john = {
   	firstName: "John"
   }

   function func() {
   	alert(this.firstName)
   }
   func.call(john); //"John"
   ```

   因为`call` 可以定义`this` 的值，在函数`func` 调用的时候，通过`call` 把`this` 的值指定为`john` ，所以此时`this = {firstName : "John"}`,所以通过函数调用`this` 对象的`firstName` 时候就会输出值`John` 。

5. ```javascript
   var john = {
   	firstName: "John",
   	surname: "Smith"
   }

   function func(a, b) {
   	alert(this[a] + ' ' + this[b]);
   }
   func.call(john, 'firstName', 'surname') //"John Smith";
   ```

   函数`func` 在调用的时候，`this` 的值被赋值为对象`john` ，然后通过`call` 传入来俩个参数，所以通过调用`this[a]` 就相当于是通过对象`john` 进行调用`john["firstName"]= "John"` ; `this[b] = john["surname"] = "Smith"` ;所以结果就输出来`"Jonh Smith"` ;

6. ```javascript
      var $btn = $("button");
      var module = {
      	bind: function() {
      		$btn.on('click', function() {
      			console.log(this) //this指代$btn对象；
      			this.showMsg(); 
                //因为在$btn上面没有绑定showMsg函数，所以会报错；
      		})
      	},

      	showMsg: function() {
      		console.log('饥人谷');
      	}
      }
      module.bind();
   ```
   ```

      修改如下：

      ```javascript
      bind: function() {
      	var me = this;
      	$btn.on('click', function() {
      		console.log(this) //this指代$btn对象；
      		me.showMsg(); //饥人谷
      		//把this赋值给变量me，通过me来传递module对象
      	})
      },
   ```

      或者也可以直接通过module来调用它的属性值`showMsg` ；

   ```javascript
      bind: function() {
      	$btn.on('click', function() {
      		console.log(this) //this指代$btn对象；
      		module.showMsg();	//饥人谷
      	})
      },
   ```

      这样也是可以的，但是这样有一个问题，因为把对象直接写死来`module`，当把这个对象赋值给别的变量`a` ，然后在销毁这个对象`module = null` 时候，然后再通过`a.bind()` 调用时候就会报错，因为`module`此时为空。所以这个方法不推荐。

   ```javascript
      var $btn = $("button");
      var module = {
      bind: function() {
      	$btn.on('click', function() {
      		console.log(this) //this指代$btn对象；
      		module.showMsg();
      	})
      },
      	showMsg: function() {
      		console.log('饥人谷');
      	}
      }
      var a = module;
      module = null
      a.bind();	//"error";
   ```

7. ```javascript
   	obj = {
   		go: function() {
   			console.log(this)
   		}
   	}
   	obj.go();	//obj 因为函数go是被obj调用的
   	(obj.go)();	//obj	立即执行函数，但是被调用的还是obj
   	(a = obj.go)();	
   //window 把函数赋值给变量a，而a是全局变量，所以a的执行环境就是window
   	(0 || obj.go)();	
   //window 这个相当于 0||obj.go = obj.go,即把obj.go赋值给 0||obj.go,可以把这一串当作一个未申明的变量，即全局变量，所以执行环境为window
   ```

   ​
