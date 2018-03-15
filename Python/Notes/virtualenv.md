---
title: 虚拟环境
date: Wed 03 Jan 2018 10:35:57 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- 永远记住当开发新应用时创建虚拟环境，这会帮助系统模块保持干净

- sudo pip3 install virtualenv
- mkdir virtual
- cd virtual
- virtualenv virt1
- source virt1/vin/active
- 这样就进入了虚拟环境，然后就可以在虚拟环境中安装模块了。
- sudo pip3 install redis==2.8
