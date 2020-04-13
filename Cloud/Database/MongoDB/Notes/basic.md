---
title: basic
date: 2020-04-07 16:51:53
modify: 
tags: [Notes]
categories: MongoDB
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- MongoDB是一个基于分布式文件存储的数据库。
- 由C++语言编写，旨在为web应用提供可扩展的高性能数据存储解决方案。
- MongoDB是一个介于关系数据库和非关系数据库(nosql)之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。
- MongoDB将数据存储为一个文档，数据结构由键值(key=>value)对组成。
- MongoDB文档类似于JSON对象。字段值可以包含其他文档，数组及文档数组。

## 主要特点

- MongoDB提供了一个面向文档存储，操作起来比较简单和容易。
- 可以在MongoDB记录中设置任何属性的索引(FirstName="wang",Address="xian")来实现更快的排序
- 可以通过本地或者网络创建数据镜像，使得MongoDB有更强的扩展性
- 如果负载增加(需要更多的存储空间和更强的处理能力),可以分布在计算机网络中的其他节点上，这就是所谓的分片。
- Mongo支持丰富的查询表达式，查询指令使用JSON形式的标记，可以轻易查询文档中内嵌的对象及数组。
- MongoDB使用update命令可以实现替换完成的文档或者一些指定的数据字段
- MongoDB中的Map/reduce主要用来对数据进行批量处理和聚合操作。
- Map/Reduce: Map函数调用emit(key,value)遍历集合中所有的记录，将key与value传给Reduce函数进行处理。
- Map函数和Reduce函数是使用Javascript编写的，并且通过db.runCommand或mapreduce命令来执行MapReduce操作
- GridFS是mongoDB中的一个内置功能，可以用于存放大量小文件
- MongoDB运行在服务端执行脚本，可以用js编写某个函数，直接在服务端执行，也可以把函数的定义存储在服务端，下次直接调用即可。
- MongoDB支持各种编程语言: RUBY,PYTHON,JAVA,C++,PHP,C#等多种语言。
- MongoDB安装简单

## 概念

- database: 数据库
- collection: 数据库表、集合
- document: 数据记录行、文档
- field: 数据字段、域
- index: 索引
- table joins: 表连接，MongoDB不支持
- primary key: 主键，MongoDB自动将_id字段设置为主键

## 参考

- [mongoDB文档](https://www.mongodb.org.cn/tutorial/6.html)
