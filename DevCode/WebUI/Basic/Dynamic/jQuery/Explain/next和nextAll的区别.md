---
title: next和nextAll的区别
date: 2016-07-01
tags: [jQuery]
categories: Dynamic
---

next 用于选择紧邻的同辈元素，必须是紧邻的一个元素，如果传入了参数，紧邻的元素和参数不匹配则返回一个空数组，除非紧邻的元素和参数匹配

```javascript
$("#one").next();
//[<div class=​"one" id=​"two" title=​"test">​…​</div>​"]
$("#one").next("span");
//[];
```

nextAll -- 表示选择目标元素后面的所有同辈元素，包括有的没的，甚至会把`script`节点也选中。

---

