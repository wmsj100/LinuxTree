---
title: ubuntu_source_list
date: 2020-03-06 10:13:52
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ubuntu_source_list

## 概要

- ubuntu bionic的源。

## 配置

```
deb http://mirrors.tencentyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ bionic-updates main restricted universe multiverse
# deb http://mirrors.tencentyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
# deb http://mirrors.tencentyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ bionic-backports main restricted universe multiverse
```

## 参考

