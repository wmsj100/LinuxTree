---
title: 设置width的尺寸依据box-sizing
date: 2016-04-24
tags: [CSS]
categories: Dynamic
---

盒模型的尺寸默认指的是width，不包括padding，如果设置`padding`，盒模型的总宽度就会变化，但是如果修改宽度的基准，
`box-sizing: border-box;`
这样设置元素的宽度就是元素的总体宽度，