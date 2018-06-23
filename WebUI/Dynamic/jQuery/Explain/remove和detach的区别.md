---
title: remove和detach的区别
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

俩者都是把元素从`dom`中删除，但区别是，前者删除元素得同时会删除元素绑定的所有事件.

`remove`删除元素是删除前面选中的元素，`$("p").remove()` && `$("p").parent().find("span").remove()`;

```html
<ul>
    <li><span>hello world</span></li>
    <li><span>hello world</span></li>
    <li><span>hello world</span></li>
</ul>

<script>
$(function() {
    var $child = $("ul li:last");
    $child.age = 10;
    $("ul li").click(function() {
        console.log("hello");
    });
    $("ul li").remove("li:last");
    $("ul").append($child);
    console.log($child);
})
</script>

<script>
$(function() {
    var $child = $("ul li:last");
    $child.age = 10;
    $("ul li").click(function() {
        console.log("hello");
    });
    $("ul li").detach("li:last");
    $("ul").append($child);
    console.log($child);
})
</script>
```

因为通过`remove`和`detach`删除的元素都不会返回，返回的都是最开始的选择集合，所以在通过这俩个方法删除元素时候最好先使用变量创建索引，选择要删除的元素，以便之后在把删除的元素插入`DOM`。

如果是确认元素不会用了，那么就使用`remove`,这样会节省内存空间。