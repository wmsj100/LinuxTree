---
title: openssl
date: 2020-10-09 19:02:20
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# openssl

## 概要

- openssl是用来加密http的协议，在python中使用需要先安装python-openssl库
- 在环境中导出变量`ENV REQUESTS_CA_BUNDLE=/root/cacert.crt`
- 拷贝证书和密钥到指定位置`COPY ./docker/cacert.crt /root/cacert.crt`

## 参考

