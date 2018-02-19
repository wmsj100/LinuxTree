---
title: 关于position和offset获取元素尺寸信息
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

`offset` -- 获取元素相对于视窗的偏移距离，返回一个对象，有`left, top`属性
`position` -- 返回元素相对于父元素中设置有`position: absolute, relative`的节点的偏移距离，也是返回一个对象，

```html
<style>
    .wrap{
        width: 300px;
        height: 300px;
        background-color: yellow;
        position: absolute;
        top: 300px;
        left: 300px;
    }
    .p1{
        width: 100px;
        height: 100px;
        background-color: green;
        position: relative;
        top: 100px;
        left: 100px;
    }
</style>
<div class="wrap">
    <div class="p1"></div>
</div>

<script>
    $(".p1").offset();  //Object {top: 400, left: 400}
    $(".p1").offset().top   // 400
    $(".p1").position();    // Object {top: 100, left: 100}
    $(".p1").position().left;   //100
</script>
```

