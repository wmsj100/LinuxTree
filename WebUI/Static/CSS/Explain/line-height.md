---
title: line-height.md
date: 2016-16-19
tags: [CSS]
categories: Static
---

`line-height`可以设置到行内元素，也可以设置到行内元素的父元素上面，效果是一样的。

```html
<style>
    p{
        border: solid 1px red;
        line-height: 100px;
        height: 100px;
    }
    span{
        border: solid 1px blue;
        font-size: 20px;
        /*line-height: 100px;*/
    }
</style>
<p><span>hello world</span></p>
```

看下面这段代码

```html
<style>
    p{
        /*line-height: 20px;*/
        border: solid 1px red;
        margin-top: 20px;
    }
    span{
        font-size: 16px;
        line-height: 16px;
        border: solid 1px red;
    }
    strong{
        font-size: 24px;
        line-height: 16px;
        border: solid 1px red;
    }
</style>
<p>
    <span>hello world</span>
    <strong>hello world</strong>
</p>
```

块级元素`p`内部有俩个行内元素`span`和`strong`，其中设置的内容框高度就是字体的高度`font-size: 16px`,而行内框的高度就是`line-height: 16px;`,对于`span`内容框和行内框差值为零，所以没有扩张，
但是对于`strong`元素来说就奇怪了，因为内容框的高度`24px`,而行内框的高度`16px`，也就是说，内容落在了行内框的外面，这一点比较奇怪；
虽然`span`和`strong`的字体高度不同，但是因为行内框的值是相同的。所以应该是对齐的。
但是因为`span`和`strong`的内容基线不同，所以还是会有偏移。

---

重新修改代码如下：

```html
<style>
    p{
        line-height: 12px;
        border: solid 1px red;
        margin-top: 50px;
        font-size: 12px;
    }
    span{
        border: solid 1px red;
    }
    strong{
        font-size: 34px;
        border: solid 1px red;
    }
    em{
        vertical-align: top;
        line-height: 4px;
        border: solid 1px red;
    }
</style>
<p>
    <span>hello world</span>
    <strong>hello world</strong>
    <em>hello world</em>
</p>
```

这个因为设置了`em`的对齐方式为`vertical-align: top`,所以`em`的行内框总是顶部和整个行内框的顶部对齐。
但是`em`的行内框`4px`小于内容框`12px`，所以内容框就会落在行内框的外面。

---

```css
em{
    line-height: 24px;
    vertical-align: top;
}
```

这一次修改`em`的行内框大于其内容框，所以`em`此时的内容框就会在原来的基础上`(24-12)/2` => `6px`,又因为设置的对象方式为`顶部对齐`，所以`em`的行内框就会下移`6px`。

为了防止内容的重叠，需要设置行内框和内容框的高度相同。而为了使这种相同持久保存，所以就需要使用相对单位`em`；

```css
em{
    line-height: 1em;
    font-size: 24px;
    vertical-align: top;
}
```

这里设置了`line-height = 1em`,表示和`font-size`值相同，即行内框和内容框高度相同。

---

对于`line-height`的值最好是设置为原始数值，而不是具体的值，因为这样就可以实现继承，缩放因子会在每层间传递，在各层上，这个因子都会和各层的`font-size`相乘，

大多时候会设置行内框和内容框相同，因为这样可以用最小的大小来容纳内容。

行内元素的边框由内容框决定，而不是行内框，

对行内元素设置垂直方向的`padding, margin`不会影响到父元素的尺寸方向尺寸。但是会导致行内元素的偏移和重叠。