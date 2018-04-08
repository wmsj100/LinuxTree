---
title: bootstarp入门知识
date: 2016-07-23
tags: ["Bootstrap"]
categories: Frame
---

- `container` -- 为页面自动计算俩边留白
- `col-xs-12` -- 小屏幕设备时候沾满一行
- `hidden-xs` -- 小屏幕隐藏属性

---

- 所有的列都必须放在row内部
```html
<div class="row">
    <div class="col-sm-3"></div>
</div>
```

- 改变列表的顺序，可以通过使用push, pull;

```html
<div class="container">
    <div class="row">
        <div class="col-sm-9 col col-sm-push-3"></div>
        <div class="col-sm-3 col col-sm-pull-9"></div>
    </div>
</div>
```
- 在标题内部添加small标签可以生成副标题，字号小一，颜色变淡
<h1>hello world<small>hello world</small></h1>

- bootstrap的默认字体高度`14px`, line-height: 1.428;
- 在段落标签上面添加`lead`属性可以是段落凸显出来，字体变大，颜色变深；
- mark标签会给元素内容添加一个背景色。
- del标签是添加删除线
- underline-下划线
- <small>...</small> 等同于 <<p class="small"></p>
- 通过<<strong></strong>可以加深字体颜色，但是通过给<<span class="lead"></span>也会加深字体颜色，但是这个会增加字体尺寸。
- 在HTML5中可以放心使用-`b, i`，b只是加深颜色没有着重意味，strong有着重语义，i斜体，em也是斜体。
- 对于段落内部的文字对齐可以简单的使用`text-left, text-right, text-center`来实现对齐方式
- abbr -- 简写标签，鼠标hover时候会变成？，并且输出全称。
- address -- 地址
- blockquote -- 对于引用样式可以使用 `blockquote`标签包裹，然后内容通过`p`标签包裹，
    - 在`blockquote`内部添加标签`footer`,可以添加引用来源的样式，前面添加中划线，并且颜色变浅
    -  <blockquote class="blockquote-reverse"></blockquote>会使引用右对齐。
- <ul class="list-inline"> -- 可以转换为行内元素，但是有一个padding值



---
