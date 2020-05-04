---
title: nutstorage_install
date: 2020-05-04 13:33:16
modify: 
tags: [Notes]
categories: Ubuntu
author: wmsj100
email: wmsj100@hotmail.com
---

# nutstorage_install

## 概要

- 之前是通过`sudo gdebi nautilus_nutstore_amd64.deb`的方式来安装的,这一次无法安装,报错python-kpg版本错误
- 所以通过源码来安装

## 源码安装

- `sudo apt-get install libglib2.0-dev libgtk2.0-dev libnautilus-extension-dev gvfs-bin python-gi gir1.2-appindicator3-0.1`
- `wget https://www.jianguoyun.com/static/exe/installer/nutstore_linux_src_installer.tar.gz`
- `tar zxf nutstore_linux_src_installer.tar.gz`
- `cd nutstore_linux_src_installer && ./configure && make`
- `sudo make install`
- `nautilus -q` 重启
- `./runtime_bootstrap` 自动下载和安装其他二进制组件

## 参考

- [坚果云安装](https://www.jianguoyun.com/s/downloads/linux)
