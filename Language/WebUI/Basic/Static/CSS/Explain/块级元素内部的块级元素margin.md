---
title: 块级元素内部的块级元素margin
date: 2016-06-17
tags: [CSS]
categories: Static
---

块级元素父元素的`border`和`padding`都为零的时候，再设置子元素的`margin`值时候，会使父元素也跟着向下偏移。[jsBin](http://jsbin.com/gevayu/3/edit?html,output)

```html
<style>
    div{
        height: 200px;
        width: 400px;
        background-color: yellow;
    }
    .p1{
        height: 50%;
        width: 100px;
        background-color: green;
        margin-top: 12.5%;
    }
</style>
<div>
    <div class="p1">hello world</div>
</div>
```

但是只要是给父元素添加`padding`或者是`border`，就不会出现这种情况；

```html
<style>
    div{
        height: 200px;
        width: 400px;
        border: solid 1px red;
        /*padding: 10px;*/
        background-color: yellow;
    }
    .p1{
        height: 50%;
        width: 100px;
        background-color: green;
        margin-top: 12.5%;
    }
</style>
<div>
    <div class="p1">hello world</div>
</div>
```

很难相信自己竟然总结出这个规律，我觉得这就是个问题，然后我就钻进去了。

规则： 如果块级元素只有一个块级子元素元素，并且块级元素的高度设置为`auto`，那么块级元素的高度就是块级子元素的上外边距到下外边距的距离，也就是说，如果块级子元素有设置上下`margin`，那么就会超出父元素。不过如果块级元素有设置`border`或者是`padding-top`或者`padding-bottom`,就可以避免这种情况。