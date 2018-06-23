---
title: insertDate 
date: 2018-06-23 17:58:45 
modify: 2018-06-23 17:58:49 
tag: [tools]
categories: VIM 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 概述
- 如何插入当前时间,有以下几种方法
	- ':read !date': 在当前焦点下一行插入当前系统日期	2018年06月23日 18:00:39
	- 'iab xtime <c-r>=strftime("%Y-%m-%d %H:%M:%S")<cr>' 在插入模式输入'xtime' 然后按下空格就可以插入日期
# 总结
- 可以自定义插入日期的格式
# 参考
- [vim中方便插入时间的几种方法](https://blog.csdn.net/zimmermanlin/article/details/8922067)

