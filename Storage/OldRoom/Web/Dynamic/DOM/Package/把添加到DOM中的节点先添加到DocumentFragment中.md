---
title: 把添加到DOM中的节点先添加到DocumentFragment中
date: 2016-05-07
tags: [DOM,函数,封装]
categories: Dynamic
---

如果要在DOM中一次性添加多个节点，那么可以通过文档片段`DocumentFragment` 的方式来添加，这样可以避免DOM树的多次渲染

```javascript
<div class="wrap"></div>
---
var wrap = document.querySelector(".wrap");

function addChild(node) {
	var a = document.createDocumentFragment();
	for (var i = 0; i < 3; i++) {
		var item = document.createTextNode("hello item" + (i + 1));
		var para = document.createElement("h3");
		para.appendChild(item);
		a.appendChild(para);
	}
	wrap.appendChild(a);
}
addChild(wrap)
wrap.childNodes	//NodeList [ <h3>, <h3>, <h3> ]
```

通过这个封装函数添加节点就可以避免多渲染俩次页面；