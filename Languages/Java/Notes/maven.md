---
title: maven
date: 2020-05-29 09:58:20
modify: 
tags: [Notes]
categories: Java
author: wmsj100
email: wmsj100@hotmail.com
---

# maven

## 概要

- maven是java的jar包的管理器，java项目依赖的jar包通过maven来管理。

## 命令

- mvn常用的命令就是编译和打包

- `mvn clean package`依次执行了clean, resources, compile, testResources, testCompile, test, jar(打包)等7个阶段
- `mvn clean install` 依次执行了clean, resources, compile, testResources, testCompile, test, jar(打包), install 等8个阶段
- `mvn clean deploy` 依次执行了clean, resources, compile, testResources, testCompile, test, jar(打包), install, deploy等9个阶段。

## package

- package命令完成了项目编译、单元测试、打包功能，但没有把打好的可执行jar包(war或其它形式的包)部署到本地maven仓库和远程maven私服仓库

## install

- install命令完成了项目编译、单元测试、打包功能，同时把打好的可执行包部署到本地maven仓库，但没有部署到远程maven私服仓库

## deploy

- deploy命令完成了项目编译、单元测试、打包功能，同时把打好的可执行包部署到本地maven仓库和远程maven私服仓库。

## 参考

- [maven打包解释](https://blog.csdn.net/zhaojianting/article/details/80324533)
