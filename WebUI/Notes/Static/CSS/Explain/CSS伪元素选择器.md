---
title: CSS伪元素选择器
date: 2016-06-16
tags: [CSS]
categories: Static
---

css有4个伪元素：-- 用于块级元素

- `first-letter` -- 用于设置块级元素的第一个字母样式

```html
<style>
    p:first-letter{
        font-size: 24px;
        text-transform: uppercase;
        color: yellow;
    }
</style>
<p>hello world</p>
```

- `:first-line` -- 用于设置块级元素的第一行文字样式

- `:before` -- `p:before:{content: "{.."; color: red;}`;
- `:after` -- `p:after:{content: "{.."; color: red;}`;