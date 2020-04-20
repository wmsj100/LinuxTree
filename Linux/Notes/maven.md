---
title: maven
date: 2020-04-17 10:20:45
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# maven

## 概要

- maven是用来管理jar包的一个工具
- 首次运行`mvn -version`，会在用户目录下创建一个.m2的目录，这个目录是maven的本地仓库,仓库是maven中一个很重要的概念。
- 试想一下，我们会再工作中同时创建很多项目，每个项目可能都会引用一些公用的jar包，一种做法是每个项目里，都复制一份这些依赖的jar包，这样显然不好，相同的文件再硬盘上保存了多份，太占用空间，而且这些依赖的jar包的版本也不好管理，如果某个公用的jar包进行了版本升级，所有引用的这个jar包的项目都需要更新，必须一个一个项目修改。
- maven的仓库则很好的解决了这些问题，它再每台机器上创建一个本机仓库，把本机上所有的maven项目依赖的jar包统一管理起来，而且这些jar包用坐标来唯一标识(坐标: 唯一识别某个jar包的文件名、版本号),这样所有的maven项目就不需要再像以前那样把jar包复制到lib目录中，整个maven项目看起来十分清爽。

## 创建项目骨架

- `mvn archetype:generate` 创建一个最基本的maven项目,mvn首次运行时，会从远程"中央仓库"下载一些必需的文件到"本地仓库"
- maven项目的目录结构
	- src/main/java 用于存放源代码
	- src/main/test 用于存放测试代码
	- src/target 用于存放编译、打包后的输出文件
- mvn clean compile 对项目进行编译，自动再target目录中生成class文件，
- mvn clean test 单元测试
- mvn 
## 参考

