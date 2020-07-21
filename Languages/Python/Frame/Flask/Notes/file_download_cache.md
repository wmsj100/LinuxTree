---
title: 文件下载缓存
date: 2020-07-21 09:22:39
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# 文件下载缓存

## 概要

- 文件通过flask的`send_static_file`方法来下载static目录的文件，但是文件修改后通过浏览器的接口下载的文件未更新，是缓存文件。
- 对于文件这类内容，浏览器会自己缓存，需要清理缓存重新下载就是好的，
- 需要一种方式来实现不使用缓存，最好的方式就是通过时间戳`tag`，而且这也是最常用的。
- 通过给下载链接添加时间戳问题已经解决

## 参考

