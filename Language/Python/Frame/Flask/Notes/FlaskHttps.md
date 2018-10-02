---
title: 配置HTTPS
date: 2018-10-02 23:35:50	
modify: 
tag: [Flask, basic]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 配置HTTPS

## 概述
- Flask默认开启的是`5000`端口,如果浏览器配置了`https`协议,然后开启的时候,页面会报错
	- `SSL 接收到一个超出最大准许长度的记录【ssl_error_rx_record_too_long】`
- 这是因为模块没有加载`openssl`,而且证书也是错误的,
- 如下配置
	- `pip install pyOpenSSL` pip安装openssl
	- `app.run('0.0.0.0', debug=True, port=5000, ssl_context='adhoc')` 使用`pyOpenSSL`自带证书,
	- 此时刷新页面就可以看到页面正常了,监听到了页面


## 参考
- [Flask 配置https](https://www.cnblogs.com/shengulong/p/6829073.html)
