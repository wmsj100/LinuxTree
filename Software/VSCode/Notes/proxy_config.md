---
title: proxy_config
date: 2020-11-23 17:35:10
modify: 
tags: [Notes]
categories: VSCode
author: wmsj100
email: wmsj100@hotmail.com
---

# proxy_config

## 概要

- vscode会涉及到下载大型插件，比如Chromium库，本身大，默认的网络无法支撑下载，需要配置代理
- vscode配置代理的方法
```vscode
{
    "http.proxyAuthorization": "127.0.0.1:8080"
}
```

## 参考

- [vscode 代理](https://www.cnblogs.com/shanyou/p/5565886.html)
