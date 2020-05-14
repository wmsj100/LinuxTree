---
title: 比较
date: 2019-04-12 14:47:39	
modify: 2020-05-14 23:08:02 
tag: [basic]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 比较运算
- shell中有三种条件类型：字符串比较、算术比较、文件条件比较
- shell 中进行条件判断建议显示返回数值，这样通过`echo $?`可以获取函数的返回值来确定当前执行是否成功
- exit 0/1 0表示成功 1表示异常
- 函数的返回值可以直接在if条件中进行判断 `if yes_or_not $1`

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
- -h file exist and is a symbolic link
- -b block file
- -p pipe file

## 使用
- 通常在if条件句中使用
```sh
if [ $a -eq $b ]
then
	echo "a is equal b"
fi
```

## 范例
- 函数返回值当作if条件
```sh
yes_or_not(){
    echo "is your name $*"
    read answer
    while true
    do
        case $answer in
            [yY] | [Yy][Ee][Ss])
                echo "good name"
                return 0
                ;;
            [nN] | [nN]*)
                echo "bad name"
                return 1
                ;;
            *)
                echo "error name"
                echo "please reinput yes or not"
                read answer
                ;;
            esac
        done
}

if yes_or_not "$1" # 对函数返回值直接进行if判断
then
    echo "Hi $1,nice name"
else
    echo "Hi $1, bad name"
fi
exit 0
```

## 参考
- [比较运算](http://c.biancheng.net/cpp/view/2736.html)
