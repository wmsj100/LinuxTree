---
title: trap
date: 2019-05-02 12:04:34	
modify: 
tag: [trap]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# trap

## 概述
- trap命令用于指定在接收到信号后将要采取的行动
- trap命令的一种常见用途是在脚本程序被中断时完成清理工作
- trap命令使用前需要向设置拦截命令
- `trap 'rm -rf trapfile*' INT`
- `trap INT` 取消设置trap

## 范例
- 创建文件，ctrl+C来删除
```sh
trap 'rm -rf trapfile*' INT
a=5
echo "start file"
while [ "$a" -ge 1 ];do
    echo "$a"> "trapfile_${a}"
    echo "$a"
    a=$((a-1))
    echo $(ls -l trapfile*)
    sleep 5
done
trap INT
echo "start delete trapfile*"
```

## 参考
- []()
