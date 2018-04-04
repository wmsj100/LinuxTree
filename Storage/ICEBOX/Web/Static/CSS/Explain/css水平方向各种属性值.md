---
title: css水平方向各种属性值
date: 2016-06-17
tags: [CSS]
categories: Static
---

元素水平方向有7个值，分别是`margin/ border/ padding/ width`;
- `border/ padding`默认值为0，不可以设置为负值；
- `margin/ width` 只有这三个值可以设置为`auto`；
- 子元素的7个水平值加起来正好是父元素的`width`；
- 当`width`和左右`margin`都设置为`auto`时候，所有值都被显示为0；
- 当`border`和`padding`设置为零，而其它3个值的总和小于父元素的`width`时候，`margin-left`会被强制更改;
- 当`width`和`margin-right`设置为固定值，而`margin-left`不设置，或者设置为`auto`时候，会自动填充使其宽度为父元素的宽度值；