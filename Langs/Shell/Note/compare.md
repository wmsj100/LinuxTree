---
title: 比较
date: 2019-04-12 14:47:39	
modify: 2019-05-01 23:11:49	 
tag: [basic]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 比较运算
- shell中有三种条件类型：字符串比较、算术比较、文件条件比较

## 字符串比较
- = 比较字符串相等
- != 比较字符串不等
- z 字符串为空，返回真
- n 字符串不为空

## 算术比较
- `eq` 相等
- `ne` 不相等
- `gt` 大于
- `lt` 小于
- `ge` 大于等于
- `le` 小于等于
- ! 取反

## 文件条件测试
- -d 是目录/文件夹
- -e 文件存在为真，兼容性不好，通常使用`-f`替代
- -f 是文件
- -g 
- -r 可读
- -s 文件大小不为零
- -u 
- -w 文件可写
- -x 文件可执行

## 使用
- 通常在if条件句中使用
```sh
if [ $a -eq $b ]
then
	echo "a is equal b"
fi
```

## 参考
- [比较运算](http://c.biancheng.net/cpp/view/2736.html)
