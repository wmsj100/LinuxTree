---
title: 在元素node子节点中找出元素节点
date: 2016-05-07
tags: [DOM,函数,封装,数组]
categories: Dynamic
---

```html
<div>
	<h3 id="whh" class="class1" title="title">hello world</h3>
	<h3 id="whh" class="class1" title="title">hello world</h3>
	<h3 id="whh" class="class1" title="title">hello world</h3>
</div>
```

正常情况下，如果使用`childNodes` 来获取子节点的话，会包括元素节点和文本节点

```javascript
var a = document.querySelector("div");
a.childNodes	
//NodeList [ #text "
		", <h3#whh.class1>, #text "
		", <h3#whh.class1>, #text "
		", <h3#whh.class1>, #text "
	" ]
a.childNodes.length	//7
```

所以如果想要过滤掉文本节点的话就可以依靠不同类型节点的`nodeType` 值不同来区分；

```javascript
function findElement(node) {
	var array = new Array();
	for (var i = 0, len = node.childNodes.length; i < len; i++) {
		if (node.childNodes[i].nodeType === 1) {
			array.push(node.childNodes[i]);
		}
	}
	return array;
}
findElement(a)
//Array [ <h3#whh.class1>, <h3#whh.class1>, <h3#whh.class1> ]
```

这样就获取了节点的元素节点，而且是数组形式。