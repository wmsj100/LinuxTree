---
title: and
date: 2019-05-02 07:58:28	
modify: 
tag: [and]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# and

## 概述
- 且运算，短路运算
- `&&` 放在if条件句之间

## 范例
- 多个条件同时判断
```sh
touch file1
rm -f file2
if [ -f file1 ] && echo "hello file1" && [ -f file2 ] && echo "hello file2"
then
    echo "file1 and file2 exit"
else
    echo "file1 is and file2 not"
fi
exit 0
```

## 参考
- []()
