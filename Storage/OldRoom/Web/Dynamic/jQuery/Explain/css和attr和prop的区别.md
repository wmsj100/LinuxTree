---
title: css和attr和prop的区别
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

我刚刚就有点分不清`css, attr, prop`的区别。其实它们区别还是很明显的。
在获取自定义属性时候就使用`attr`或者`prop`，
如果想要获取的是样式表`css`的属性值，那么就果断使用`css`/
对于特殊状态的选中和判断，并且结果是返回布尔值的属性`checked, selected, `这些就需要使用`prop`，
如果只是想要获取一个自定义属性的值，可以使用`attr`/
如果是想要设置并且返回一个布尔值，就使用`prop`。
大多数情况下，可以使用`attr`的场景都可以使用`prop`进行替代。