---
title: http-server 快速创建node.js 静态服务器
date: 2016-07-23
tags: [HTTP,NPM,Frame,Node]
categories: Frame
---

说到node.js 创建服务器,首先想到 express 

之前和大家分享过 关于http-server快速创建node服务

http-server
首先需要 全局安装 http-server

npm install -g http-server
http-server 启动

http-server -a 127.0.0.1 -p 7070
上面的一句命令启动了一个node.js 的静态服务器. 监听本地 7070 端口.
静态目录就是当前运行 命令所在的目录

如果你的当前项目中存在 public 文件夹,那么默认静态目录会指定到 public
如果没有 public 文件夹,那么静态目录就是 根目录 ./

你可以把 http-server -a 127.0.0.1 -p 7070 写入到 package.json 文件中的 scripts 节点


  "scripts": {
   "start": "http-server -a 127.0.0.1 -p 7070"
 }
 
这样就可以通过  npm start 来启动静态服务器