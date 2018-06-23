---
title: text-decoration
date: 2016-06-17
tags: [CSS]
categories: Static
---

`text-decoration: underline` -- 不会继承，如果父元素设置了这个值，子元素不会继承，但是会产生下划线,而下划线的样式就是父元素的，即便在子元素上面明确声明没有下划线，而且重新设置颜色也是没有用效果的。

```html
<style>
        h3{
            text-decoration: underline;
            color: red;
        }
        em{
            color: gray;
            text-decoration: none;
        }
    </style>
    <h3>hello <em>world</em></h3>
```

虽然没有办法去掉下划线，但是可以在子元素上面重新声明一下`下划线`，这样只是颜色是和子元素相同的。

```html
<style>
        h3{
            text-decoration: underline;
            color: red;
        }
        em{
            color: gray;
            text-decoration: underline;
        }
    </style>
    <h3>hello <em>world</em></h3>
```

