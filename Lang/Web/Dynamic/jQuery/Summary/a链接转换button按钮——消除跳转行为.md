---
title: a链接转换button按钮——消除跳转行为
date: 2016-3-31 21:29:17
tags: [函数,DOM]
categories: Dynamic
---

[demo](http://codepen.io/wmsj100/pen/aNygPW?editors=1111)

<!-- more -->
把a链接设置为按钮的时候，因为a链接默认的属性，页面会进行跳转，即便链接地址为`#`还是会调到页面顶部，所以此时就需要取消a链接的默认事情属性。

```html
<a href="http://www.baidu.com" id="btn">点我</a>
<script>
    var btn = document.querySelector("#btn");
    btn.addEventListener("click", function(e) {
    	console.log("wmsj");
    	console.log(e);
    	e.preventDefault();
    })
</script>
```

通过给事件`e`添加属性`preventDefault()`这样点击a链接页面就不会进行跳转啦。

