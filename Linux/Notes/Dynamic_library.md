---
title: 动态库
date: 2020-04-01 17:08:17
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 动态库

## 概要

- 手动安装gcc时候报错`libzint.so`这个动态库找不到，然后就开始了解动态库的概念

## 动态库与静态库最大的区别

- 静态库是静态链接，也就是在生产可执行文件的时候就把静态库中的实现嵌入到程序中了，一旦编译成功了，静态库也就有存在的价值了，即便静态库不存在了，可执行程序也是可以跑起来的；
- 动态库：遵循动态链接，也就是说编译的时候需要指定路径去找该so文件链接编译，运行的时候也需要指定相应的路径去找。
- 如果在运行的时候，可执行程序会先去默认的系统lib目录下，寻找该so，如果找不到了，就报错了：error while loading shared libraries


## 动态库的搜索路径的先后顺序是：

- 编译目标代码时指定的动态库搜索路径
- 环境变量`LD_LIBRARY_PATH`指定的动态库搜索路径
- 配置文件`/etc/ld.so.conf`中指定的动态库搜索路径
- 默认的动态库搜索路径`/lib, /usr/lib`

## 配置环境变量

- 通过手动配置环境变量可以
- `export LD_LIBRARY_PATH=/usr/local/lib`

## 参考

- [动态链接和静态链接](https://www.cnblogs.com/Recan/p/6012305.html)
