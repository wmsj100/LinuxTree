---
title: css动画
date: 2016-09-28
tags: [CSS]
categories: Static
---

简单的动画可以通过`css3`配合`js`的动画基本可以满足，
复杂的动画可以应用`h5`的`canvas`标签来实现效果。

- `transform` -- 变化属性
- `transition` -- 渐变效果
- `@keyframes` -- 制作动画效果

应用`transition`制作动画的过渡效果是更好的选择，比`js`实现更容易，而且可以应用浏览器的硬件加速效果，实现更高的性能。

`transition: height 0.6s, background 1s;` 可以把多个效果放在一个里面，用逗号分割；

`transition: all 0.5s ease-in-out;` 这个表示任意属性的变化都应用过渡动画效果。

使用`@keyframes`制作动画：

```CSS
@keyframes spin{
    0%{
        transform: rotate(0deg);
    }
    50%{
        transform: rotate(90deg);
    }
    100%{
        transform: rotate(180deg);
    }
}
.box{
    animation: spin 4s infinite linear;
}
```
`animation`的参数的意思分别是： 动画名称， 动画执行一次的时间， 动画循环的次数， 动画的速度函数；
`infinite` -- 表示无限循环；

`animation: spin 4s linear infinite alternate;` 这个表示完成一次动画之后就进行反转。

`animation-play-state` -- 表示动画的运行状态，可以有俩个值： `paused, running`;
当然了可以很容易的使用`js`来控制动画的启动和暂停。

```js
box.hover(function(){
	$(this).css({"animation-play-state": "paused"});
}, function(){
    $(this).css({"animation-play-state": "running"});
});
```

