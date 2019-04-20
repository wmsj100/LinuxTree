---
title: 全限定域名
date: 2018-04-05 21:40:18 Thu
modify: 2018-04-05 21:40:18 Thu
tag: [net]
categories: NetWork
author: wmsj100
mail: wmsj100@hotmail.com
---

# 全限定域名

## 概述
- Fully Qualified Domain Name
- 同时带有主机名和域名的名称
- windows2012227.test123.com 
	- 主机名：windows201227 
	- 域名：test123.com
- 访问时由DNS解析得到IP地址
- FQDN = Hostname + DomainName
- 当我们申请了一个域名时`test123.com`，就可以使用这个域名来得到IP，
- 域名即创建了一个域，就如命名空间；
- 若这个域名下挂载很多主机，每个主机都可以创建自己的名称，
- web.test123.com
- mail.test123.com
- hostname -f 查看FQDN
- uname -h 查看主机名
