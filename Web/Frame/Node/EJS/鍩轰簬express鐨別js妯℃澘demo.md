---
title: 基于express的ejs模板demo
date: 2016-07-15
tags: [EJS,NPM,Frame]
categories: Frame
---

`ejs`是基于`html`的框架，通过变量动态生成，
因为是使用`express`开启服务器通过路由来调用模板文件的，
所以首先需要创建一个`express`实例，开启服务器。
然后设置路由文件，添加对模板的引用。

index.js
```javascript
router.get('/ejs/demo1', function(req, res) {
    res.render('demo1', {user: "wmsj", title: "homepage"});
} );
```

然后在模板文件夹`views`创建模板

demo1.ejs
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title><%= title %></title>
</head>
<body>
    welcome <%= user %>;
</body>
</html>
```

注意，在模板中定义的变量，在路由中一定要全部涉及，如果模板中出现路由中没有的变量，那么就会报错。

通过`<%- inslude('head.ejs') %>`这种方式可以引入其它的模板。

index.ejs
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <%- include('head.ejs') %>
</head>
<body>
    <%- include('body.ejs') %>
</body>
</html>
```

head.ejs
```html
<meta charset="UTF-8">
<title>hello</title>

<%- include('demo2.ejs') %>
<div>
    Welcome Great User.
</div>
```

body.ejs
```html
<h3><%= user %></h3>
```

因为`body`中有变量`user`，所以在引用`index`的路由设置中需要添加`user`的赋值操作。路由操作如下

index.js
```javascript
router.get('/ejs/demo1', function(req, res) {
    res.render('demo1', {
        user: "wmsj",
        title: "homepage"
    });
});
```

