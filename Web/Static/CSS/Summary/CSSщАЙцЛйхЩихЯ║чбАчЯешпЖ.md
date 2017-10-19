---
title: CSS选择器基础知识
date: 2016-09-19
tags: [CSS,Summary]
categories: Static
---

## `nth-child`

- "li:nth-child(2)" -- 选取父元素内的第2个`<li>`元素，需要同时满足俩个条件：
    - 是不是第2个
    - 是不是`<li>`元素

- "li:nth-child(n)" -- 选取所有的子元素，这时候参数只能是`n`；
- `li:nth-child(2n){ background-color: purple; }` -- 表示所有的偶数项；
- `li:nth-child(2n+1){ background-color: purple; }` -- 表示所有的奇数项；
- `li:nth-child(n+2)` -- 表示从第二个元素开始；之后的所有元素都会应用属性值；
- `li:nth-last-child(2)` -- 和`nth-child()`正好相反，是从后往前数的；

## `nth-of-type`

- `p:nth-of-type(1)` -- 匹配所有`p`元素中的第一个；感觉用的不会太多。

## `target` 目标锚点样式

这个用于通过点击链接，在当前页面内跳转时候给激活元素添加的样式；

```html
<span id="a2">hello world</span>
<a href="#a2">a2</a>

<style>
:target{
    color: red;
    border: solid 1px red;
    padding: 0px 10px;
}
</style>
```

```html
<div id="header">
  <p>hello</p>
  <div>sssss</div>
  <p>word</p>
</div>

<style>
    #header>:first-child{
    color: red;
    padding-top: 0;
    margin-top: 0;
    }
    #header>:last-child{
    color: blue;
    padding-bottom: 0;
    margin-bottom: 0;
    }
</style>
```

---

对于`header`内部的文字包裹可能有`div`，也可能有`p`，如果要统一内容的样式，那么该怎么设置呢？

```html
<div id="header">
  <p>hello</p>
  <div>sssss</div>
  <p>word</p>
</div>

<style>
#header>*{
  color: blue;
  border: solid 1px;
  margin: 1em 1em;
}
</style>
```

