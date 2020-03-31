---
title: path
date: 2019-04-20 10:53:43	
modify: 2020-03-31 18:50:03 
tag: [path,shell,bash]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# path

## 概述

- linux的路径设置
- 就是一组路径的字符串变量，当输入的命令不带路径时候，Linux会在path记录的路径中查找命令，有的话则执行，没有就报错命令找不到

## 添加路径到path

- PATH=$PATH:/usr/local/apache/bin 把apache的bin目录添加到path，这种方法只对当前会话有效，登出或注销系统就失效了
- vi /etc/profile: 在profile中设置，在最后面添加`export PATH=$PATH:/usr/local/apache/bin`;这样设置后在执行：`source /etc/profile`
- vi ~/.bash_profile 修改PATH行，把路径添加到PATH中 PATH=$PATH:$HOME/bin:/usr/local/apache/bin; source ~/.bash_profile.

## 设置默认路径

- ~/.bashrc
- export lang_c="/home/pi/Code/HelloWorld/Language/C/nodes"
- source ~/.bashrc
- cd $lang_c

## PATH的默认路径

- `/sbin` 只有root可以使用的命令
- `/bin` 一般用户可用，启动时会用到的命令，即文件系统还没有挂载时也能使用的命令。
- `/usr/sbin` 非必要的系统二进制文件，例如大量网络服务的守护进程
- `/usr/bin` 非必要可执行文件，面向所有用户
- `/usr/local/sbin`
- `/usr/local/bin` 自己安装的软件的可执行文件

## 参考

- [PATH](https://www.cnblogs.com/leibg/p/4479921.html)
