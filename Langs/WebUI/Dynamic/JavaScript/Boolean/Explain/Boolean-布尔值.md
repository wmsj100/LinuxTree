---
title: Boolean值
date: 2016-04-30
tags: [布尔,JavaScript]
categories: Dynamic
---

布尔类型`Boolean`只有俩个状态`真`=>`true`;`假`=>`false`;

下列运算符会返回布尔值
- 俩元逻辑运算 && ||
- 前置逻辑运算符 !
- 相等运算符 === !== == !=
- 比较运算符 > >= < <=

如果JS预期在某个位置应该是布尔值，会将该位置的值自动转换为布尔值，而除了下面6个值转换为`false`时，其它都会转换为`true`；

- false
- undefined
- null
- "",''
- NaN
- 0

需要注意的事`“ ”`空格会被转换为`true`；
空数组和空对象的布尔值都是`true`；
`Boolean(" ")` => `true`;
`Boolean([])` => `true`;
`Boolean({})` => `true`;
