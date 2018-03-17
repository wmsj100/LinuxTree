---
title: ajax和DOM加载顺序
date: 2016-05-13
tags: [DOM,Ajax]
categories: Dynamic
---

ajax是异步加载的，不会阻塞DOM的渲染，比如

```html
<script>
var carouselDom = document.querySelector("#carousel");
console.log(carouselDom);	//null
</script>
<div id="carousel">hello wrold</div>
```

结果是null，因为解析js时候dom节点还没有渲染，如果把script标签放到页面底部就不会出现问题了

```html
<div id="carousel">hello wrold</div>
<script>
var carouselDom = document.querySelector("#carousel");
console.log(carouselDom);	//<div id="carousel">
</script>
```

对于ajax，因为它的名字就是异步的html和xml技术，就是说加载ajax的时候不会阻塞dom的渲染，所以我把那个脚本放到了ajax内部，虽然ajax是错误的地址，会报错，但是会执行脚本

```javascript
var a = {
	init: function() {
		this.ajax();
	},
	ajax: function() {
		$.ajax({
			url: "sss.ll",
			error: function() {
				var carouselDom = document.querySelector("#carousel");
				console.log(carouselDom);
			}
		});

	}
}
a.init();
```

结果就输出了内容。