---
title: case
date: 2019-04-12 17:48:34	
modify: 
tag: [case]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# case

## 概述
- case 类似其他语言中的`switch case`
- 必须有关键字`in`
- 判断条件使用圆括号分隔
- 条件结束使用俩个分号`;;`
- `*` 使用这个字符匹配无法匹配的条件

```shell
#!/bin/bash
read num

case $num in
    1)  echo "select 1"
        ;;
    2)  echo "select 2"
        ;;
    3)  echo "select 3"
        ;;
    *)  echo "not gass"
        ;;
esac
```

## 参考
- [shell case](http://c.biancheng.net/cpp/view/7006.html)
