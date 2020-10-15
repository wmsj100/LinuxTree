---
title: hosts
date: 2020-01-08 22:29:35
modify: 2020-10-15 10:01:15  
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# hosts

## 概要

- 域名解析的配置文件

## win10无权限修改文件

- 碰都的情况是在win10上没有权限修改这个文件
- 解决办法是以管理者权限启动powershell,进入到hosts目录，然后执行命令`notepad hosts`，然后修改文件再保存，这样就可以了。
- win10默认hosts文件是读保护的，即该文件只有读取权限，不能执行写入，需要点击该文件"属性"=>"安全"=>"高级",添加写权限，然后属性中修改勾选写入权限，这样就可以修改hosts文件了。

## 总结

- 正常修改hosts文件之后不会立即生效，需要手动触发
```hosts
ipconfig /displaydns 展示所有dns
ipconfig /flushdns 刷新
```
- 这样之后就可以显示自定义的hosts

## 参考

