---
title: extend解析
date: 2016-4-11 15:25:58
tags: [jQuery]
categories: Dynamic
---

`$.extend( target, [obj1], [objn] )`---这是浅拷贝，后面的obj替换前面target的内容

#### 合并两个对象，并修改第一个对象。

```html
<div class="log"></div>

    <script>
var target = {
	name: "wmsj",
	age: 28,
	like: {
		name: "reading",
		run: false,
		happy: "almost"
	}
};
var obj1 = {
	sex: "male",
	age: 12,
	like: {
		eat: "meat"
	}
};
$.extend(target, obj1);
$(".log").append(JSON.stringify(target));
//{"name":"wmsj","age":12,"like":{"eat":"meat"},"sex":"male"}
//target的同名内容只是被简单的覆盖了。
      </script>
```

`$.extend( true, target, [obj1], [objn] )`--这是深拷贝

#### 采用递归方式合并两个对象，并修改第一个对象。

```html
<div class="log"></div>

    <script>
var target = {
	name: "wmsj",
	age: 28,
	like: {
		name: "reading",
		run: false,
		happy: "almost"
	}
};
var obj1 = {
	sex: "male",
	age: 12,
	like: {
		eat: "meat"
	}
};
$.extend(true, target, obj1);
$(".log").append(JSON.stringify(target));
//{"name":"wmsj","age":12,"like":{"name":"reading","run":false,"happy":"almost","eat":"meat"},"sex":"male"}
```

#### 合并 defaults 和 options 对象，并且不修改 defaults 对象。这是常用的插件开发模式。

```html
<div class="log"></div>
    <script>
var defaults = {
	name: "wmsj",
	age: 28
};
var options = {
	sex: "male",
	age: 12,
	like: {
		eat: "meat"
	}
};
var settings = $.extend({}, defaults, options);
$(".log").append("<div><b>defaults</b>---" + JSON.stringify(defaults) + "</div>");
$(".log").append("<div><b>options</b>---" + JSON.stringify(options) + "</div>");
$(".log").append("<div><b>settings</b>---" + JSON.stringify(settings) + "</div>");
//defaults---{"name":"wmsj","age":28}
//options---{"sex":"male","age":12,"like":{"eat":"meat"}}
//settings---{"name":"wmsj","age":12,"sex":"male","like":{"eat":"meat"}}
```



