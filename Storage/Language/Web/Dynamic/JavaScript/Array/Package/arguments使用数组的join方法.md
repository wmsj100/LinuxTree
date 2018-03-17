---
title: arguments使用数组的join方法
date: 2016-05-20
tags: [Array,Object]
categories: Dynamic
---

```javascript
function join() {
	return Array.prototype.join.apply(arguments);
}
join(1,2)	//"1,2"
```

