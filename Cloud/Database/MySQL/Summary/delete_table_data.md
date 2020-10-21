---
title: delete_table_data
date: 2020-10-21 12:11:55
modify: 
tags: [Summary]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# delete_table_data

## 概要

- 使用`delete from data_table`这样会全部删除表数据，但是存储数据的文件尺寸并不会变化，还是之前大数据量的尺寸
- 之前操作sqlite也发现这种情况了，删除数据后，文件尺寸没有缩小，还是大数据量尺寸
- 这样的好处应该是方便数据找回吧，那个文件就像是一个空间，重新写入数据会覆盖部分数据，但没有被覆盖的数据是可以被恢复或者说有恢复的可能性。

## 参考

