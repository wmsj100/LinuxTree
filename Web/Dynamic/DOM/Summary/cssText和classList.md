---
title: cssText和classList
date: 2016-06-14
tags: [JavaScript,DOM]
categories: Dynamic
---

其实`cssText`和`classList`是完全不相干的事情，因为前者是元素样式修改的一个集合，附属于`style`，而后者是元素上面的`class`集合，具体区别如下；

`cssText` -- 这不是一个读取属性，但是只能读取到元素标签上面的样式设置，

```html
a{
    color: yellow;
}
<a class="link" style="color: green" href="#">hello world</a>
<script>
    var a = document.querySelector("a");
    a.style.cssText;    //"green"
    a.classList;    //"link";
</script>
```

通过`style`标签添加的样式是无法读取的，即便把元素的行内样式删除也是无法读取到那个样式的，此时的`cssText = ""`;

