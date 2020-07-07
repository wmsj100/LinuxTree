---
title: getopts
date: 2020-07-07 14:13:10
modify: 
tags: [Note]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# getopts

## 概要

- getopts: 获取参数
- 当脚本的参数较少的时候，可以通过$1/$2/$3这样的方式获取，但是当参数较多的时候，这样就很不方便，就需要使用shell的内部方法getopts来获取
- `OPTARG` 获取当前参数后面的值
- `OPTIND` 获取当前参数的位置索引，从1开始。

## 范例

```shell
while getopts 'hd:' flag
do
	case "$flag" in
		h)
			fn_h
			;;
		d)
			fn_d
			;;
		?)
			fn_error
			exit 1
			;;
	esac
done
```

## 参考

- [getopts](https://www.cnblogs.com/kevingrace/p/11753294.html)
