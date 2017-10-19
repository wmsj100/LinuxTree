---
title: call 和 apply
date: 2016-3-25 10:21:45
tags: [JavaScript]
categories: Dynamic
---

> JavaScript中call和apply方法，其作用基本相同；

## call

- 调用一个对象的方法，以另一个对象替换当前对象。
- call方法可以用来代替另一个对象调用一个方法，
- call方法可将一个函数的对象上下文从初始的上下文改变为由thisObj指定的新对象。
- 如果没有提供thisObj参数，那么Global对象被用作ThisObj。
<!-- more -->
```javascript
function Obj(){this.value="对象!"}
    	var value="global变量";
    	function Fun1(){console.log(this.value);}

    	window.Fun1();	//global变量	
    	Fun1.call(window);		//global变量
    	Fun1.call(document.getElementById("myText"));	
		//input的作用域   inputText
    	Fun1.call(new Obj());	//Obj作用域， 对象！
```

- call和apply方法的第一个参数都是要传入给当前对象的对象，及函数内部的this。后面的参数都是传递给当前对象的参数。运行代码如下：

```javascript
var func=new function(){this.a="func"}
    	var myfunc=function(x){
    		var a="myfunc";
    		console.log(this.a);	//"func"
    		console.log(x);		//"var"
    	}
    	myfunc.call(func,"var");
```

函数解析： 

1. myfunc.call(func,"var")中func是要被myfunc当作对象作用域的，内部的this指代的就是func的作用域，所以this.a其实就是func中的this.a=“func”。
2. “var”是要被myfunc当作参数传入的，所以此时x=“var”；

---

- 对于apply和call两者在作用上是相同的，但两者在参数上有区别的。
- 对于第一个参数意义都一样，但对第二个参数：


- apply传入的是一个参数数组，也就是将多个参数组合成为一个数组传入，而call则作为call的参数传入（从第二个参数开始）。

如 func.call(func1,var1,var2,var3)对应的apply写法为：func.apply(func1,[var1,var2,var3])

同时使用apply的好处是可以直接将当前函数的arguments对象作为apply的第二个参数传入

代码如下：

```javascript
var c=Math.max(1,2,3);	//3;
    	var a=[1,2,3,4];		//^^^
    	var b=Math.max.apply([],a);	
    	//把数组a当作参数传入Math，作用域为null，
    	//作用域可以为[]/{}
    	//4
    	var d=Math.min.apply(null,a);	//1
```

