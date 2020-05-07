---
title: Hive
date: 2020-05-07 17:06:30
modify: 
tags: [Notes]
categories: Hadoop
author: wmsj100
email: wmsj100@hotmail.com
---

# Hive

## 概要

- Hive由Facebook实现并开源
- 是基于Hadoop的一个数据仓库工具
- 可以将结构化的数据映射为一张数据库表
- 并提供HQL(Hive SQL)查询功能
- 底层数据是存储在HDFS上
- Hive的本质是将SQL语句转化为MapReduce任务运行
- 使不熟悉MapReduce的用户很方便地利用HQL处理和计算HDFS上的结构化的数据，适用于离线的批量数据计算。
- 数据仓库: 数据仓库是一个面向主题的、集成的、相对稳定的、反映历史变化的数据集合，
- Hive依赖于HDFS存储数据，Hive将HQL转换成MapReduce执行，所以说Hive是基于hadoop的一个数据仓库工具，实质就是一款基于HDFS的MapReduce计算框架，对存储在HDFS中的数据进行分析和管理。

## 为什么使用Hive

- 直接使用MapReduce所面临的问题：
	- 人员学习成本太高
	- 项目周期要求太短
	- MapReduce实现复杂查询逻辑开发难度太大
- 为什么要使用Hive
	- 更友好的接口: 操作接口采用类SQL的语法，提供快速开发的能力
	- 更低的学习成本: 避免了写MapReduce，减少开发人员的学习成本
	- 更好的扩展性: 可自由扩展集群规模而无需重启服务，还支持用户自定义函数

## 参考

- [hive](https://www.cnblogs.com/qingyunzong/p/8707885.html)
