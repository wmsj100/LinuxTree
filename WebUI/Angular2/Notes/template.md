---
title: 模板语法
date: 2018-07-04 16:28:00
modify: 
tag: [template]
categories: Angular2
auth: wmsj100
email: wmsj100@hotmail.com
---

# 模板语法
> 写过`jQuery`才可以理解`Angular2`的伟大，因为避免了麻烦的`DOM`操作

## 概述
- `Angular2`是`单向数据流`策略，这个`AngularJS`的`双向数据绑定`不一样，而且去除了`脏检查`的机制，更清晰明了。
---
- `HTML` 几乎所有的`HTML`语法都是有效的模板语法，但是`<script>`元素是被禁用的，以阻止脚本注入攻击的风险，(实际上是被忽略了)；
    - 所以在模板中要引用`jTopo`时候只是在页面引入`script`标签是没有效果的，因为被忽略了
    - 只能在`index.hmtl`文件中写入`script`标签引用，它是生效的。

- 插值表达式: 用双花括号的形式把值转换为字符串
