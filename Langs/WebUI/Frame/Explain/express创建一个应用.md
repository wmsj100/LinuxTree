---
title: express创建一个应用
date: 2016-07-14
tags: [Models]
categories: Frame
---

1. `npm init` -- 初始化，创建`package.json`；
2. `mkdir app.js` -- 创建入口文件

```javascript
var express = require("express");
var app = express();

app.get('/', function(req, res){
        res.send("hello world!");
});

var server = app.listen(3000, function(){
        var host = server.address().address;
        var port = server.address().port;
        console.log('Example app listening at http://%s:%s', host, port);
});
```

3. `npm install express --save` -- 创建本地`express`模块，并且通过`--save`把信息保存到`package.json`中。 会发现`json`文件中多了一个`dependincies`中关于`express`版本信息。
4. `node app.js` -- 开启服务器
5. `http://localhost:3000/` -- 访问页面。

---

`$ npm install express-generator -g` -- express应用生成器，可以快速创建一个应用骨架

`express wmsj` -- 可以初始化一个应用的基础骨架
`npm install` -- 插入依赖插件，这个加载完成，文档会生成一个`node_modules`包文件夹。进去会发现加载的就是`package.json`中的依赖`dependencies`中罗列出来的模块

`npm start` -- 来启动应用 ，还是在`3000`端口。

---

正常的应用修改需要重启服务器，但是可以通过一个应用`supervisor`来避免这样的操作

`C:\Users\Administrator\AppData\Roaming\npm\node_modules` -- node安装的全局插件在这个地址。

`npm install supervisor -g` -- 在全局中引入插件。
`supervisor ./bin/www` -- 启动页面，然后保持这个命令框开启，重新打开一个命令框，修改引用，这样直接刷新页面就可以刷新页面来。

当创建的脚本文件在node

---

在`express`中集成`mockjs`

这个集成是在路由文件`routes/index.js`中修改文件，添加`mock`的数据内容

```javascript
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', {
        title: 'Express Nodejs'
    });
});

/* GET home page. */
router.get('/mockjs', function(req, res, next) {
    var Mock = require("mockjs");
    var data = Mock.mock({
        "list|1-10": [{
            "id|+1": 1
        }]
    });
    var ret = JSON.stringify(data, null, 4);
    console.log(ret);
    res.render('index', {
        title: ret
    });
});

module.exports = router;
```

通过上面就在创建了一个`/mockjs`路径，当访问这个路径时候就会输出`mock`数据。
如果需要的是`json`格式的数据，那么就需要把`render`改变为`send`。

```javascript
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', {
        title: 'Express Nodejs'
    });
});

/* GET home page. */
router.get('/mockjs', function(req, res, next) {
    var Mock = require("mockjs");
    var data = Mock.mock({
        "list|1-10": [{
            "id|+1": 1
        }]
    });
    var ret = JSON.stringify(data, null, 4);
    console.log(ret);
    res.render('index', {
        title: ret
    });
});

/* GET home page. */
router.get('/mockapi', function(req, res, next) {
    var Mock = require("mockjs");
    var data = Mock.mock({
        "list|1-10": [{
            "id|+1": 1
        }]
    });
    var ret = JSON.stringify(data, null, 4);
    console.log(ret);
    res.send(ret);
});

module.exports = router;
```

这样就创建来俩个接口页面，当访问`mockjs`时候，查看的是`html`格式的数据。
当查看`mockapi`页面时候，查看的是`json`格式的数据。
