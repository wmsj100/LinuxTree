---
title: xz压缩
date: 2018-03-15 23:18:32 Thu
modify: 2018-03-15 23:18:32 Thu
tag: [linux,tool]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# xz压缩格式

## 概念
- xz是绝大多数linux默认就带的一个压缩工具，xz格式要比7z还要小。

## 用法
- 经常搭配tar包来打包或解包
- 今天下载node发现格式是`.tar.xz`，这个就是先经过了tar打包，然后进行xz压缩
- 解包过程
	- xz -d node.tar.xz
	- tar -xvf node.tar

### 压缩
- xz -z 待压缩文件名
- -k 保留源文件
- -0至-9 调节压缩率，如果不设置，默认压缩率是6；

### 解压缩
- xz -d 待解压的文件
- -k 保留源文件


