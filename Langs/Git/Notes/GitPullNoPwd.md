---
title: git无秘密pull
date: Mon 25 Dec 2017 11:53:05 PM CST
tag: [git,config]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# Git action (Push Pull Clone) 避免输入用户名和密码方法

文地址：http://www.cnblogs.com/ballwql/p/3462104.html

前言

    在大家使用github的过程中，一定会碰到这样一种情况，就是每次要push 和pull时总是要输入github的账号和密码，这样不仅浪费了大量的时间且降低了工作效率。在此背景下，本文在网上找了两种方法来避免这种状况，这些成果也是先人提出来的，在此只是做个总结。

进入git bash终端， 输入如下命令：

    git config --global credential.helper store

执行完后查看%HOME%目录下的.gitconfig文件，会多了一项：

    [credential]

        helper = store

重新开启git bash会发现git push时不用再输入用户名和密码
这样第一次pull可能没有生效，但是第二次就不要嗯了，它已经缓存好了
http://blog.csdn.net/chengly0129/article/details/49128565
