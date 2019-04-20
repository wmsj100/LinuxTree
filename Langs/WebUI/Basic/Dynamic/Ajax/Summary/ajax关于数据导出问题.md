---
title: ajax关于数据导出问题
date: 2016-05-05
tags: [Ajax,函数,封装]
categories: Dynamic
---

通过`Ajax` 方式获取的数据如何导出，想到几种方式，

1. 把`data` 属性绑定到函数`ajax` 的原型上面，

   ```javascript
   <input class="btn" type="button" value="click" >
   ---
   var state = 0;
   function ajax() {
   	if (state) {
   		return
   	};
   	state = 1;
   	$.ajax({
   		url: "01.php",
   		datatype: "json",
   		type: "get",
   		data: {
   			"state": 1
   		},
   		success: function(data) {
   			ajax.prototype.num = function() {
   				return data;
   			}
   		},
   		error: function() {
   			console.log("error");
   		},
   		complete: function() {
   			state = 0;
   			addData();
   		}
   	});
   }
   $(".btn").on("click", function() {
   	ajax();
   });
   var a;
   function addData() {
   	a = ajax.prototype.num();
   	console.log(a);
   }
   ```

   给`ajax` 添加了锁，防止多次点击，然后通过把函数`addData()` 放置到`ajax` 的`success` 函数里面，确保整个`ajax` 执行完成之后再读取数据，也就是说脚本里面的内容最好不要让它自动执行，而是通过控制函数来按照顺序来执行。

   其实也可以添加延时函数，设置`addData()` 的延时，间隔一段时间，等`ajax` 加载完成在读取数据也行，但是延时间隔不好控制。

2. 把数据存放到`window.name` 里面。但是这样的话，如果后面重新命名了，或者是之前它里面就存放这数据，这样就会更新数据，有很多问题。

   但是可以给window添加一个属性，然后把值存放到属性里面，这样是可以的，但同样还是要考虑`ajax` 加载延时的问题。

3. 如果不是一定要通过点击才获取`ajax` 数据的话，可以在一开始就加载`ajax` ,然后等到使用的时候直接读取就可以了，这样就不存在延时问题了，

   这个感觉是可以的，就是`ajax` 可以在页面读取或刷新的时候就加载；

4. 把数据存储到随笔一个函数的原型上面，然后进行引用也是可以的。当然这个函数必须是函数什么的方式，因为这样才会有函数前置。

```javascript
(function ajax() {
	$.ajax({

		url: "01.php",
		datatype: "json",
		type: "get",
		data: {
			"state": 1
		},
		success: function(data) {
			showData.prototype.num = function() {
				return data;
			}
		},
		error: function() {
			console.log("error");
		},
		complete: function() {}
	});
})();

function showData() {};
var a = showData.prototype;
console.log(a);
```

