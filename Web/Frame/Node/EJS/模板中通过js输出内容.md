---
title: 模板中通过js输出内容
date: 2016-07-15
tags: [EJS,NPM,Frame]
categories: Frame
---

模板可以加入js，如下

路由设置 index.js

```javascript
router.get('/ejs/demo4', function(req, res){
    res.render('demo4', {
        names: ['loki', 'tobi', 'jane'],
        title: "wmsj"
    });
});
```

模板内容-demo.ejs

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <% if(names.length){ %>
        <ul>
            <% names.forEach(function(name){ %>
                <li><%= name %></li>
            <% }) %>
        </ul>
    <% } %>
</body>
</html>
```

