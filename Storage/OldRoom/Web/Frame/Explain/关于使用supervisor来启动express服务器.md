---
title: 关于使用supervisor来启动express服务器
date: 2016-07-19
tags: [Mock,Models,Frame,Node]
categories: Frame
---

如果是直接通过`npm start`来启动服务器，那么对文件的修改之后需要重启服务器，
但是通过使用`supervisor`就可以避免这样的操作，

通常可以通过`supervisor`来调用入口文件来启动
`supervisor app.js`,

但是有时候会出现问题，报错，所以这时候就需要调用初始化页面
`supervisor ./bin/www`;

因为我所有的文件都是使用`express`自动配置的，

所以创建项目需要以下步骤

- `express wmsj` -- 创建模块的基础架构
- `npm install` -- 加载依赖包
- `npm install mockjs --save` -- 加载自定义包时候需要把这个信息保存到`package.json`的配置文件中。
- 然后就可以进入路由文件进行接口的设计了。