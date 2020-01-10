---
title: README
date: 2018-04-13 22:02:20 Fri
modify: 2018-04-13 22:02:20 Fri
tag: [django,readme]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# README

## 概要
- 该目录主要是关于Django的知识点整理！
- `Django_book_2` 最好的入门书籍，不知道是不是书名，很受用，感谢
- [Django1.11文档](https://yiyibooks.cn/xx/Django_1.11.6/intro/overview.html)
- [Django入门介绍](https://yiyibooks.cn/xx/Django_1.11.6/intro/whatsnext.html)
- [Django官方文档](https://docs.djangoproject.com/zh-hans/2.0/)
- [Django-入门](http://www.cnblogs.com/luxiaojun/p/5791498.html)
- [Django-models教程](https://www.cnblogs.com/luxiaojun/p/5795070.html)

## 详情
- Note 基础知识点的整理目录

## Django架构

- 通过Nginx接收客户端接口请求
- Nginx把接口转发给Uwsgi进行处理并继续下发给django
- django接收请求并返回处理结果给UWsgi
- uwsgi处理结果并且转发给nginx
- nginx返回结果给客户端
- django还需要对mysql进行数据处理
- 整体架构是这样的，而且今天通过文档操作实现了这个流程

## 参考

- [python3 基于Nginx的Django部署](https://blog.csdn.net/yilovexing/article/details/82969103)

## 代办
- sqlite3 安装完成，可以搭建自己的blog了  -- Fri Apr 20 00:12:38 CST 2018
- 学习的最好方法就是开始一个项目 -- Fri May  4 16:23:12 CST 2018
- 我在想为什么不去直接搭建django的环境呢？而且也没有深入学习django。直到现在。
