---
title: 浏览器缓存的思考
date: 2020-02-26 22:51:45
modify: 
tags: [Summary]
categories: WebUI
author: wmsj100
email: wmsj100@hotmail.com
---

# 浏览器缓存的思考

## 概要

- 刚刚在调试css，发现页面缓存无法更新，是django框架。
- 发现css一直无法更新，清除缓存也无法更新文件，后来发现是因为没有调用`python manage.py collectstatic`
- 然后我就在想这个缓存是依据什么来判断的，我觉得请求之前应该是先发一个请求头过去，判断文件是否有更新，如果更新了就下载，否则就使用本地缓存。

## 参考

