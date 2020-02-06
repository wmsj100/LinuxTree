---
title: 疫情统计
date: 2020-02-06 17:56:17
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 疫情统计

## 概要

- 用python统计疫情，所有数据来源于接口

## 接口

- `https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5`

## 规划

- 前端界面先不考虑框架，前端使用vue进行接口请求
	- 界面使用echarts
- 后端使用flask的python框架
- python和uwsgi通信
- nginx和uwsgi通信
- 数据存储到mysql中，	
	- 如何规划mysql的数据库
	- 把请求到的数据进行拆分，分别存储到数据库不同表

## 参考

