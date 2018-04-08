---
title: index获取索引
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

通过`index`方法可以获取元素所在位置的索引。

```html
<ul>
    <li  id="tab1">时事</li>
    <li class="selected" id="tab2">新闻</li>
    <li id="tab3">体育</li>
</ul>

<script>
    $("ul li").index($("#tab1")); //0
</script>
```

