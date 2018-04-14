---
title: 获取元素样式的style属性和值
date: 2016-05-08
tags: [DOM,函数,遍历]
categories: Dynamic
---

通过`a.style` 来获取元素身上通过style添加的属性，`a.style[1]` 获取第二个属性名，`a.style.getPropertyValue(a.style[1])` 获取第二个属性名对应的属性值；

```html
<p>hello world</p>

<script>
var a = document.querySelector("p");
a.style.cssText = "color: #fff; background: #DE4444;";
var styleName = [],
	styleValue = [],
	styleObj = {};
for (var i = 0, len = a.style.length; i < len; i++) {
	styleName.push(a.style[i]);
	styleValue.push(a.style.getPropertyValue(a.style[i]));
	styleObj[a.style[i]] = a.style.getPropertyValue(a.style[i]);
}
a.style.removeProperty("color")	//移除color属性；
</script>
```

上面是获取通过style设置的样式属性，但是如何获取元素身上迭代或者继承的样式呢，就需要使用`documen.defaultView.getComputedStyle(a,null)` ;比如获取元素的`width, fontFamily..`

```html
<style>
	p{
		color: #fff;
		background-color: #ACD743;
		font-size: 24px;
		border-radius: 5px;
	}
</style>

<p style="border: solid 1px purple; color: #333">hello world</p>

<script>
var a = document.querySelector("p");
var styleObj = document.defaultView.getComputedStyle(a, null);
styleObj.fontFamily	//"sans-serif"
styleObj.width	//"785px"
styleObj.marginTop	//"24px"
</script>
```

但是有一个问题，那就是IE不识别`document.defaultView` 这个属性，IE有一个类似的功能是`node.currentStyle` ，所以就需要写一个兼容的函数；

```javascript
var a = document.querySelector("p");

function getElementStyle(node, property) {
	var styleObj = null;
	if (typeof document.defaultView === "object") {
		styleObj = document.defaultView.getComputedStyle(node, null);
	} else if (typeof node.currentStyle === "object") {
		styleObj = node.currentStyle;
	}
	return styleObj[property];
}
var b = getElementStyle(a, "color");	//"#333" 
```

