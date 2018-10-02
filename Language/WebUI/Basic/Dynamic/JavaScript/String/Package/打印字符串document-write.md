---
title: 打印字符串document.write
date: 2016-05-02
tags: [字符串,函数,封装]
categories: Dynamic
---

把字符串打印到屏幕上

```javascript
var b = a.replace(/[<>"&]/g, function(item) {
    switch (item) {
        case "<":
            return "&lt;";
            break;
        case ">":
            return "&gt;";
            break;
        case "&":
            return "&amp;";
            break;
        case "\"":
            return "&quot;";
            break;
    }
});
document.write(b);
```

