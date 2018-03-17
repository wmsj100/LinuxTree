---
title: 闭包-数组赋值-for循环
date: 2016-3-26 02:06:50
tags: [闭包,数组,遍历]
categories: Dynamic
---

## 问题：通过for循环给数组赋值：

### 一、常规做法：
<!-- more -->
```javascript
var count = [];
for(var i=0;i<10;i++){
  count[i]=function(){
  return i;
}
}
console.log(count[0])
```

这种做法看上去好像是可以的，但是实际运行之后，结果并非想要的。

```javascript
console.log(count)	//查看count数组
//[count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)(), count.(anonymous function)()]
console.log(i)	//查看i的值； 10；
console.log(count[1])	//查看数组的第2个元素
//function(){
  return i;
}	//是一个匿名函数，
console.log(count[1]())	//查看函数的运行结果		
// 10 正好是i的值。
```

1. 这是因为在hor循环的过程中，count数组并没有把过程保存下来，所以就只有一个值，10；
2. 而可以把过程值保存下来的就只有闭包中的自执行函数，因为它会产生不同的作用域，以此来保持不同的值。

### 二、函数闭包

```javascript
var count=[];
for(var i=0;i<10;i++){
  count[i]=(function(num){
  	return function(){
  		return num;
		}	//自执行函数，并且返回闭包；
	}(i));
}
console.log(count[3]());	//3
```

上面的代码是通过for循环来表现的，可以简单的挑选俩个值出来看看：

```javascript
var f1,f2;	//f1,f2是数组里面的俩个值；
f1=function(num){
	return function(){
		return num;
	}
}	//通过返回一个闭包函数；
console.log(f1(1)());	//1
f2=function(num){
	return function(){
		return num;
	}
}
console.log(f2(2)())	//2
```

还可以简化，从函数表达式简化为函数声明，如下：

```javascript
function f(num){
	return function(){
		return num;
	}
	return f;	
	//把函数f自己return出来，方便外面调用；
}
console.log(f(1)());	//1
```

