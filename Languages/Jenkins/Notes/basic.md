---
title: basic
date: 2020-03-02 16:03:24
modify: 
tags: [Notes]
categories: Jenkins
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- Jenkins是一个持续集成和部署的工具

## 安装

### 非安装模式

- 直接下载官方war包就可以
- `java -jar jenkins.war --httpPort=8080 jenkins_dir_name` 这样就可以指定一个目录来启动Jenkins。
- 然后进入安装界面，安装时候会卡在一个输入密码的界面
```
*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

6b524890fe504d33993144120696da02

This may also be found at: /home/ubuntu/.jenkins/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
```
- 这个密码就是第一次的登录密码
- `https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json` 这是国内清华的源

### apt安装

- `wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -`
- `echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list`
- `sudo apt update`
- `sudo apt install jenkins`
- 等待安装完成，默认开启8080端口

## 参考

- [jenkins 安装](https://www.jianshu.com/p/845f267aec52)
