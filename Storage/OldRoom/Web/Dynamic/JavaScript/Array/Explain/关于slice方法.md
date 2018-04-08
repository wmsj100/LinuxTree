---
title: 关于slice方法
date: 2016-06-23
tags: [Array]
categories: Dynamic
---

slice方法即可以用于数组也可以用于字符串，因为字符串是类数组，所以其实它还是操作数组的方法，
对于字符串，`slice`和`substring`类似，接收俩个参数，开始位置和结束位置(不包含).
对于数组，`slice`和`splice`类似，但是`slice`不会改变原数组，而是返回一个修改后的新数组，而`splice`会改变原数组。

对于类数组，`slice`可以把它们转换为数组，进行真正数组的方法操作。
`Array.prototype.slice.call(a.children,0)`

对于类数组转换数组的兼容性更好的方法是进行枚举数组。当然了，可以结合进行功能性检测分别使用不同方法。