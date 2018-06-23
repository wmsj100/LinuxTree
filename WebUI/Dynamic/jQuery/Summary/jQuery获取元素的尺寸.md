---
title: jQuery获取元素的尺寸
date: 2016-07-12
tags: [jQuery,Summary]
categories: Others
---

```javascript
$(".foot").height() // 获取元素的内容尺寸
$(".foot").innerHeight()    // 包括内容和padding，不包括边框
$(".foot").outerHeight();   // 包括内容/padding/border,不包括外边距
$(".foot").outerHeight(true);   // 包括内容/padding/ border/ margins
```

