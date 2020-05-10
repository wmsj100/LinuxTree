---
title: locale_LC_ALL_LANG
date: 2020-05-09 11:10:26
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# locale_LC_ALL_LANG

## locale

- locale根据计算机用户所使用的语言，所在国家或者地区，以及当地的文化传统所定义的一个软件运行时的语言环境。
- 不同地区对一些计算机词汇、日期显示等方面有各自的习惯。比如大陆使用文件系统，而台湾使用档案系统，这显然不是简单的从简体到繁体的转换而已，
- 所以可以想象，有一套系统在为各个地区的本地化服务。
- locale把按照所涉及到的使用习惯的各个方面分成12个大类，这12个大类分别是：
	- LC_CTYPE: 语言符号及其分类
	- LC_NUMERIC: 数字
	- LC_COLLATE: 比较和习惯
	- LC_TIME: 时间显示格式
	- LC_MONETARY: 货币单位
	- LC_MESSAGES: 信息，提示信息，错误信息，状态信息，标题，标签，按钮和菜单等
	- LC_NAME: 姓名书写方式
	- LC_ADDRESS: 地址书写方式
	- LC_TELEPHONE: 电话号码书写方式
	- LC_MEASUREMENT: 度量测量表达方式
	- LC_PAGER: 默认纸张尺寸大小
	- LC_DENTIFICATION: 对locale自身包含信息的概述

## 参考
0.
