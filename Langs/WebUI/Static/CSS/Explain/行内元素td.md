---
title: 行内元素td
date: 2016-07-07
tags: [CSS]
categories: Static
---

一般来讲，行内元素，设置`height, width`是没有效果的，但是如果设置`margin`的水平方向的偏移是有效果的，但是垂直方向没有效果。
而对于`padding`，可以设置垂直方向的值，但是也只是视觉上的扩展，查看`height`时候会发现还是原来的字体高度。而查看`margin，padding`时会发现确实是设置了值的。

```css
span{
  border: solid 1px;
  width: 100px;
  height: 100px;
  background: red;
}
```

上面是通常行内元素的特性。
但是对于表格的`td, th`却又有不同，因为它们虽然也是行内元素，但是却可以设置`width`和`height`尺寸。它们只是表现为行内元素，但是具有块级元素的所有特性。
就像是把块级元素设置了`display: inline-block;`

```css
    table{
        border: o;
        border-collapse: collapse;
    }
    td{
        padding: 5px;
        width: 100px;
    }
    th{
        text-align: left;
        padding: 4px;
        border-bottom: solid 1px #333;
    }
```

