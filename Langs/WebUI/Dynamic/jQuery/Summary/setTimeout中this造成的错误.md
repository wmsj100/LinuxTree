---
title: setTimeout中this造成的错误
date: 2016-07-19
tags: [jQuery,Summary]
categories: Dynamic
---

```javascript
    function user(login) {
      this.login = login;
      this.sayHi = function() {
        console.log(this.login);
      }
    }

    var a = new user("John");
    setTimeout(a.sayHi, 1000);   // undefined
    setTimeout(a.sayHi.bind(a), 1000);  // John
    setTimeout(function() {
      a.sayHi();    // John
    }, 1000);
```

