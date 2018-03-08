---
title: awk 内置变量表
date: 2018-03-05
tag: [linux,tool,awk]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

> awk 是个优秀的文本处理工具，可以说是一门程序处理语言。

## 内置变量表
- $0 当前记录，通常代表逐行
- FS field separator 输入字段分隔符，默认分隔符为空格
- NF number field 按照FS分隔符分割，当前字段划分的列数，
- NR number row 输出读出的记录的行号
- RS row separator 输入的记录分隔符，默认是换行符
- OFS output field separator 输出字段分隔符，默认是空格
- ORS output row separator 输出的行分隔符，默认是换行符
- ARGC 命令行参数个数
- ARGV 命令行参数数组
- FILENAME 当前输入文件的名字
- ENVIRON 获取Unix的环境变量
- OFMT 数字的输出格式，默认是%.6g 显示6个小数
- FIELDWIDTHS field widths 输入字段宽度的空白分隔字符串，FIELDWIDTHS其格式为空格分隔的一串数字，用以对记录进行域的分隔，FIELDWIDTHS="4 2 2 2 2 2"就表示$1宽度是4，$2是2，$3是2  .... 。这个时候会忽略：FS分隔符。
- RSTART 被匹配函数匹配的字符串索引位置(以1开始)
- RLENGTH 被匹配函数匹配的字符串长度

### 总结
- 多个命令可以在一个花括号内，以分号分隔
    - awk 'BEGIN{RS="ha"}{OFS="<==>"}{print $0}'
- 在BEGIN中FILENAME/ $0-$N, NF 都不能使用，BEGIN中不能获取任何和文件记录操作的变量

### 范例
- $0操作
    - awk '/^root/{print $0}' /etc/passwd; // root:x:0:0:root:/root:/bin/bash
- $1/NF/FS/BEGIN/NR 操作
    - awk 'BEGIN{FS=":"}/^root/{print $0,$NF,NR}; // root /bin/bash 输出第一列和$NF(最后一列)
    - awk 'BEGIN{FS=":"}{print NR,$1,$NF}; // 输出行号、第一列、最后一列  1 root /bin/bash
- RS 修改输入记录的分隔符
    - awk 'BEGIN{RS="ha"}{print $0,NF,NR}'; // hello 1 1 wang 1 2 wanmei 1 3 world 1 4 lilei 1 5
- OFS 自定义输出字段分隔符
    - awk 'BEGIN{RS="ha"}{OFS="<==>"}{print $0}'; // hello<==>1<==>1
    - awk 'BEGIN{FS=":";OFS="^^"}/^root/{print NFR,$1,$NF}; // 1^^root^^/bin/bash
- ARGC/ARGV 获取命令行参数个数和读取数组
    - awk 'BEGIN{FS=":";print "ARGC="ARGC;for(k in ARGV) print{k"="ARGV[k]}}; // 获取参数个数，并且分别读取参数
- FILENAME 输出文件名
    - awk 'BEGIN{FS=":"}{print FILENAME}' passwd; // passwd  没一个处理行都会输出一次passwd
- ENVIRON 获取环境变量
    - awk 'BEGIN{print ENVIRON["PATH"]}' passwd; // .....输出环境变量PATH的值
- OFMT 自定义数字输出格式
    - awk 'BEGIN{OFMT="%.3f";print 2/3,123.111111}' passwd; // 0.667 123.111
- FIELDWIDTHS 宽度分隔
    - echo 20180305154356 | awk 'BEGIN{FIELDWIDTHS="4 2 2 2 2 2"}{print $1"-"$2"-"$3,$4":"$5":"$6}'; // 2018-03-05 15:44:56
- RSTART / RLENGTH 匹配字符首位置和字符长度，没有匹配返回-1
    - awk 'BEGIN{star1=match("this is a test",/[a-z]+$/)}{print star1,RSTART,RLENGTH}'; // 11 11 4
