---
title: 安装
date: 2018-08-12 20:25:16	
modify: 
tag: [basic]
categories: Java 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 安装

## 概述
- 之前实在linux安装java,但大多数情况下,java的开发是在windows下的,

## 过程
- 安装JDK
- 配置环境变量
	- JAVA_HOME 配置jdk安装路径 `C:\Program Files\Java\jdk1.8.0_171\`
	- PATH 配置jdk的命令文件位置`C:\Program Files\Java\jdk1.8.0_171\bin`
	- CLASSPATH 配置类库文件位置 `C:\Program Files\Java\jdk1.8.0_171\lib`
- 验证
	- 在cmd控制台输入`java/ javac`,都有内容输出就证明配置完成

## 参考
- []()

## Linux安装java

- 在控制台执行“java -version” 可以看到正确的版本信息
- 但是执行“javac”时候，却提示找不到命令
- 在网上查找[解决](http://blog.csdn.net/yalecaltech/article/details/70158620)
- 大意就是用yum安装原生的就行了。
- yum install java-devel
