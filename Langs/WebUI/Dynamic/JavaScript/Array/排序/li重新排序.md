---
title: li重新排序
date: 2016-3-31 17:08:47
tags: [DOM,数组,排序]
categories: Dynamic
---

页面又一列数组，是乱序，需要重新排序：

<!-- more -->

```html
<ul class="list">
		<li><span>3</span></li>
		<li><span>1</span></li>
		<li><span>4</span></li>
		<li><span>2</span></li>
	</ul>
```

javascript代码如下：

```javascript
var item = document.getElementsByTagName("li");
    	var arr = [];
    	for (var i = 0; i < item.length; i++) {
    		arr.push(item[i])
    	}
    	arr.sort(function(a, b) {
    		return parseInt(a.children[0].innerText) - parseInt(b.children[0].innerText)
    	})
    	 for (var i = 0; i < arr.length; i++) {
    		var newList = document.getElementsByTagName("ul")[0]
    		newList.appendChild(arr[i])
    	}
```

之所以不用删除原来的列表，是因为使用appendChild给元素添加子元素的时候，如果子元素已经存在于父元素中，那么就会先把之前的元素删除，然后再在末尾添加子元素。