---
title: 正则-找出html标签
date: 2016-3-28 16:28:47
tags: [正则,函数]
categories: Dynamic
---

找出`"hel <helkj> alsdkj <hell>--"`中的html标签
<!-- more -->
```javascript
var str="hel <hel--kj> alsdkj <hell>";
console.log(str.match(/<\S+>/g))
//["<helkj>", "<hell>"]
```

使用或标签

```javascript
var str="hel <hel --kj> alsdkj <hel l>-- <html>";
console.log(str.match(/<\S+\s+\S+>|<\S+>/g))
//["<hel --kj>", "<hel l>", "<html>"]
```

