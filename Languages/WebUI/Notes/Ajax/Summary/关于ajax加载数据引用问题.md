---
title: 关于ajax加载数据引用问题
date: 2016-05-10
tags: [Ajax,函数]
categories: Dynamic
---

使用`ajax` 加载的数据是需要时间的，但是这个时间该如何判断呢，当然了，可以简单的添加一个延时函数，设置延时为1s，但是这毕竟是妥协的方式，而且很不安全，万一网络阻塞，那就完蛋了，后面所有的操作都是`null` ，所以我目前想到的比较好的方式就是一直引用函数，所有的操作都在函数中完成，

即当ajax加载成功后把需要调用的内容通过函数的参数传递给调用函数。而在那个函数内部引用通过`ajax` 加载的数据，这样就不存在判断延时时间的问题了。

```javascript
ajax.success: function(){
  this.stickup(document.querySelector("#header"));
}

stickup: function(obj){
		console.log(obj)	//#header
	}
```

