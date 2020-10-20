---
title: Vmmem
date: 2020-10-20 18:17:07
modify: 
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# Vmmem

## 概要

- Vmmem是WSL的子程序，它分配了wsl可以使用的资源，包括CPU、内存
- 如果Vmmem资源占有率很高，可以使用如下方法来解决。

## 解决

- 在powershell 界面执行下面命令
```config
wsl --shutdown # 关闭wsl服务
wsl # 启动wsl服务
```

## 参考

