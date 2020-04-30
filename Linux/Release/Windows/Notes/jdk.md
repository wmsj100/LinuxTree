---
title: jdk
date: 2020-04-30 11:27:32
modify: 
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# jdk

## 概要

- jdk是java的开发环境

## 安装

- `wget https://download.java.net/openjdk/jdk8u41/ri/openjdk-8u41-b04-windows-i586-14_jan_2020.zip` 下载
- `JAVA_HOME:  E:\tools\java-se-8u41-ri`
- `classpath： .;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar`
- `PATH:  %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin`
- 在环境变量添加上面三个参数
- `cmd` 确认java和javac命令ok

## 参考

- [jdk安装配置](https://www.cnblogs.com/linjiqin/archive/2013/11/02/3403095.html)
