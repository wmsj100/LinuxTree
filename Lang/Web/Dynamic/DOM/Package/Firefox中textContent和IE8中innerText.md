---
title: Firefox中textContent和IE8中innerText
date: 2016-05-08
tags: [DOM,函数,封装]
categories: Dynamic
---

IE中最先实现`innerText` 效果，但是没有被纳入标准，标准是`textContent` ，它是 DOM Level 3 规定的一个属性，所以引用的时候，如果想要向标准靠拢，那么就需要像下面这样的兼容了--推荐使用`innerText` 

```html
<div>hello world</div>

<script>
var a = document.querySelector("div");
function getInnerText(node) {
	return typeof node.textContent === "string" ? node.textContent : node.innerText;
}

function setInnerText(node, txt) {
	if (typeof node.textContent === "string") {
		node.textContent = txt;
	} else if (typeof node.innerText === "string") {
		node.innerText = txt;
	}
}
console.log(getInnerText(a));	//"hello world"
console.log(setInnerText(a, "www"));	//"www"
</script>
```

