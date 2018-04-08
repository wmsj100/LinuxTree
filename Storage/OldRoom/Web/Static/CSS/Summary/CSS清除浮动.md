---
title: CSS清除浮动
date: 2016-4-15 17:57:02
tags: [CSS,浮动]
categories: Static
---

float---记得要给父元素清除浮动。

inline-block---

块级元素收缩----float/ inline-block / absolute

css居中--内容水平居中--transform: translateX(-50%)
如果无法完全显示在一行，总是折行，那么很可能是因为内部单个元素长度过大，可以缩小长度试试。

判断现在有没有动画存在
```
if($($element).is(:animated)){
	
}
```
我估计会钻进去出不来。怎么整理思路，不去想那些乱七八糟的事情。

$wrap = $(".wrap");
$child = $wrap.children();
$child !== $wrap.children();
前者是固定的，是页面本来拥有的内容，如果页面的。wrap内容是通过ajax加载的，
那么此时$child=[],为空值，但是$wrap.children()是动态的，内容是再执行时候页面的内容，
所以此时$wrap.children().length=4;

str.match(/<![^>]*>/g)  

new Date('2014-04-15')

算了，我想先把简单的效果做出来，然后再通过ajax效果进行数据获取。
为了安全需要，我也会购买苹果，这是一个礼物，为了我自己的努力。

本地调试的时候用本地的js库。

心欢喜

之前写的代码也不好，重新写。

task-27-2   页面多个轮播，这个应该简单，明天上午弄完。