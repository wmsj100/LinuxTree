---
title: 通过for循环添加DOM节点导致的死循环
date: 2016-05-07
tags: [遍历,DOM,函数,封装]
categories: Dynamic
---

```javascript
<div>hello</div>
var a = document.getElementsByTagName("div");
	for(var i=0; i<a.length; i++){
		var div = document.createElement("div");
		div.innerText = "hello world"+i;
		document.body.appendChild(div);
	}
```

大致思路是获取页面中的`div` 数量，然后通过for循环再添加`div` 节点，但是添加数量不超过现在已有的`div` 数量，思路是这样的，但是按照上面的执行时候就出现了死循环，

因为`a.length` 是动态变化的，没添加一个节点，`a.length` 的值就加1，所以循环会一直进行下去，知道页面卡死；

但是如果先获取最开始的`a.length` 的一个快照，然后再循环就不会有问题

```javascript
var a = document.getElementsByTagName("div");
for (var i = 0, len = a.length; i < len; i++) {
	var div = document.createElement("div");
	div.innerText = "hello world" + i;
	document.body.appendChild(div);
}	//循环一次就结束了
```

因为`len` 的值在最开始就写死了，不会随着循环的增加而增加；所以第二种是很保险的做法。

