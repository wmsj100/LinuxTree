---
title: before_request
date: 2020-10-21 14:21:33
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# before_request

## 概要

- flask请求的流程如下
- 请求=> 服务器 => `before_first_request` => `before_request` => 视图函数 => `after_request` => `teardown_request` => 响应
- ![](https://upload-images.jianshu.io/upload_images/11415306-77006c22f28637b1.png?imageMogr2/auto-orient/strip|imageView2/2/w/653/format/webp)

## 参考

- [flask request](https://www.jianshu.com/p/f619af63f6cc)
