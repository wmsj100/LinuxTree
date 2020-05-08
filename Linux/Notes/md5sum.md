---
title: md5sum
date: 2020-05-08 11:42:24
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# md5sum

## 概要

- 是用来确保文件完整性的一个工具
- 采用MD5报文摘要算法(128)计算和检查文件的校验和，默认Linux会自动安装
- MD5算法常常被用来验证网络文件传输的完整性，防止文件被篡改。
- MD5 报文摘要算法 Message-Digest Algorithm 5
- 此算法对任意长度的信息逐位进行计算，产生一个二进制长度为128的指纹，不同文件产生相同的报文摘要的可能性非常非常小

## 使用

- `md5sum a`
- `md5sum a > a.md5`
- `md5sum -c a.md5` 校验a文件
- `md5sum a b > a.md5` 把多个文件的校验信息写入同一个文件

## 参考

- [md5sum用法](https://man.linuxde.net/md5sum)
