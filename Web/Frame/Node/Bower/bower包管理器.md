---
title: bower包管理器
date: 2016-07-23
tags: [Bower,NPM,Frame]
categories: Frame
---

bower 和 npm 的区别
http://fy98.com/2014/12/10/npm-vs-bower/

bower是一个前端的`js, css`依赖包管理器，比如我现在需要特定版本的jquery，那么我直接可以通过`bower`来加载。
`bower install jquery#1.12.4`

- bower install jquery 加载默认的最新版本jquery
- bower install jquery#1.12.4  会覆盖之前已经下载的jquery版本
- bower help 可以弹出帮助信息
- bower info jquery 可以查看关于jquery的所有信息
- bower home jquery  可以使用默认浏览器打开jquery的github网站
- bower lookup jquery  会弹出jquery的github地址
- bower search jquery  会根据输入的名称在bower库中查找同名或者类似名称的库
- bower update jquery  会根据当前版本1.X/ 2.X进行当前主干的最新版本更新
- bower uninstall jquery 会卸载jquery
- bower init  会初始化一个bower.json的文件，类似`package.json`,里面是bower的包信息，

但是通过`git bush`进行`bower init`会报错，需要使用命令提示符进行这个操作。
之后添加模块时候在后面添加`--save`.
`bower install jquery --save`

开始一个项目之前，最好先使用`angular-seed`来初始化一个项目