---
title: SELinux
date: 2020-03-17 10:03:40
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# SELinux

## 概要

- SELinux使用所谓委任式访问控制,它可以针对特定程序与特定文件资源来进行权限的管理.
- 即使是root,在使用不同软件时候所得的权限也是受限的,不是root权限.
- 这样以来我们针对控制的主体就变成了程序而不是用户了.
- 这个权限模式特别适合网络服务的程序.
- 即使程序使用root身份去启动,如果这个程序被攻击而被取得操作权限,那该程序能做的事情还是很有限的,因为被SELinux限制了能执行的操作.
-
## 参考

- [弄懂selinux](https://www.cnblogs.com/kelelipeng/p/10371593.html)
