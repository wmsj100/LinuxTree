---
title: xz压缩
date: 2018-03-15 23:18:32 Thu
modify: 2018-05-07 00:12:32 Thu
tag: [linux,tool]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# xz压缩格式

## 概念
- xz是绝大多数linux默认就带的一个压缩工具，xz格式要比7z还要小。
- xz是压缩率之王，压缩文件比7z还小，但是压缩花费的时间会比较长

## 用法

### 压缩
- xz -z 待压缩文件名
- -k 保留源文件
- -0至-9 调节压缩率，如果不设置，默认压缩率是6；

### 解压缩
- xz -d 待解压的文件
- -k 保留源文件

### 创建或解压tar.xz
- 这个格式是需要先创建tar包，然后通过xz来创建压缩包
- 解压缩的过错也是类似，先解压缩xz为tar包，然后在解压tar包
- 解包过程
	- xz -d node.tar.xz
	- tar -xvf node.tar

