---
title: 脚本嵌套
date: 2019-04-12 21:47:19	
modify: 
tag: [shell]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 脚本嵌套

## 概述
- 脚本可以互相嵌套，可以通过`. ./test.sh`导入脚本，然后可以在主脚本中读取或者调用子脚本中的变量或者方法

## 范例
```shell
#!/bin/bash
. ./test_for.sh
echo $num, $str
```

## 参考
- [脚本嵌套](http://c.biancheng.net/cpp/view/2740.html)
