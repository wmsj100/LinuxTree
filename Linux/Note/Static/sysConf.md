---
title: 系统配置
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux,sys,conf]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- bash在启动时候会去读取系统配置文件，以规划好操作环境。
- 配置文件分为全局配置（影响所有用户）和用户个人配置文件

### login && non-login
- login shell 取得bash时需要完整的登陆流传
- non-shell 取得bash接口的方法不需要重复登陆的举动，以X Window登陆后在图形界面再次启动终端机，此时不需要输入帐号秘密；或者登陆shell后再次启动一个子进程shell，此时也不需要输入帐号密码；这样的shell就称作'non-login shell'
- 俩种shell读取的配置文件并不一样

### login shell
- login shell 只会读取下面俩个配置文件
    - /etc/profile 系统整体的配置文件，最好不要修改这个文件
        - 利用登陆用户的UID来决定很多重要的变量数据
        - 每个登陆用户取得bash时都会读取的配置文件
        - 会设置一些环境变量； PATH, MAIL, USER, HOSTNAME, HISTSIZE
        - 它还会继续调用其它配置文件，主要是shell的自定义配置，比如颜色，声音，命令别名，语系等
    - ~/.bash_profile 或 ~/.bash_login 或 ~/.profile 用户个人设置
        - 在读取完/etc/profile后会读取用户个人配置文件，个人配置文件如下：
            - ~/.bash_profile
            - ~/.bash_login
            - ~/.profile
        - bash的login shell只会读取三个配置文件中的一个，读取的优先级就是上面的顺序，之所以由三个是为了照顾从其它shell转换过来的用户的使用习惯；
        - 这个文件的主要作用是判断用户的主目录下是否由`~/.bashrc`，如果存在就读入这个配置文件，读入的过程通过`source`
        - ~/.bashrc 会继续调用系统配置文件`/etc/bashrc`文件；并且同时导出自定义变量
        - 因为最后还是会调用`~/.bashrc`文件，所以用户的自定义配置可以写入该文件即可

- 不管是系统配置文件还是用户自定义配置文件，因为都是'login shell'登陆时候才会读取的，所以对这些文件修改后通常需要注销再登陆才会生效
- 也可以利用'source'或'.'来让修改的配置文件立即生效

### non-login shell
- 这种shell仅仅会去读取`~/.bashrc`配置文件，
- 这个配置文件又会去读取`/etc/bashrc`配置文件 
- 如果没有`~/.bashrc`配置文件，登陆后命令提示符会很奇怪，此时可以复制`/etc/skel/.bashrc`到主目录下即可。

- ~/.bash_history 每次登陆后bash会去先读取这个文件，每次注销的时候，会把当前shell的历史操作命令写入到这个文件
- ~/.bash_logout 记录了注销bash后系统帮助我们做完声明操作才会离开。默认情况下，只是帮助我们清掉屏幕信息而已。也可以将备份会其它工作写入到这个文件中，例如清空暂存盘 sync
