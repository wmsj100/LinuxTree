---
title: jQuery绑定函数事件
date: 2016-07-17
tags: [jQuery]
categories: Dynamic
---

对于确定的函数，为了避免对象元素上面事件的累积，可以在绑定事件之前先使用事件命名空间删除事件，然后再重新绑定。

```javascript
$("div.pagination").off("click.listClick");
$("div.pagination").on("click.listClick","li", paginationClick);
```

我在写分页控件时候就出现来函数事件累积情况，所以在绑定事件之前就通过命名空间进行来删除。