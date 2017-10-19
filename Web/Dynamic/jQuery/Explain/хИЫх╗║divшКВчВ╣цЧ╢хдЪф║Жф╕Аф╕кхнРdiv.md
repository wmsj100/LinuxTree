---
title: 创建div节点时多了一个子div
date: 2016-07-16
tags: [jQuery]
categories: Dynamic
---

```javascript
$("<div>").addClass("pagination").appendTo(this.ct);
this.ct.append("<div class='pagination'><div>");
```

上面俩个的效果是不一样的，下面这个我在项目中会出现错误，多来一个子`div`

```html
<div class="pagination">
    <div></div>
</div>
```

不知道原因，找了半天，最后追查到这里。改为上面第一个就不会有这个问题了，以后遇到类似的问题可以这样想。