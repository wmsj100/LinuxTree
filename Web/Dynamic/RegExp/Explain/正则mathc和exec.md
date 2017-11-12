---
title: 正则mathc和exec
date: 2016-06-18
tags: [RegExp]
categories: Dynamic
---

```javascript
    var a = "mom and dad and baby";
    var pattern = /mom( and dad( and baby)?)?/gi;
    pattern.exec(a)
["mom and dad and baby", " and dad and baby", " and baby"]
a.match(pattern)
["mom and dad and baby"]
```

```javascript
    var a = "0000-000-00";
    var pattern = /\d{4}-\d{3}-\d{2}/g;
    pattern.test(a)
true
a.match(pattern)
["0000-000-00"]
```

