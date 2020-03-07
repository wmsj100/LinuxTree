---
title: gdebi
date: 2020-03-07 12:15:59
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# gdebi

## 概要

- 这是一种deb的安装方式
- 比直接用dpkg的好处在于它会自动安装依赖,而dpkg如果有依赖未安装会直接报错,需要在执行
- `sudo apt fix-broken install`方式来解决了依赖后再执行dpkg安装
- `sudo apt install gdebi`
- `sudo gdebi  nautilus_nutstore_amd64.deb`
- 这个方法是通过坚果云安装时候看到的

## 参考

- [坚果云安装方式](sudo gdebi  nautilus_nutstore_amd64.deb)
