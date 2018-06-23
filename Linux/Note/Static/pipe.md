---
title: pipe管道命令
date: Wed 21 Feb 2018 11:47:49 AM CST
tag: [linux,basic]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# pipe 管道命令

## 基本概念
- 管道命令只会处理标准输出的值，对于标准错误输出不会处理
- 管道命令后接的命令必须要能接受前一个命令的数据作为标准输入
- 经常用来配合管道的命令由'grep', 'cut'；他俩都是以行为单位进行处理的

## cut
- cut的主要用途在于将同一行的数据进行分解。
- echo $PATH | cut -d ':' -f 4 以':'为分割符，读取第4个字段
- export | cut -c 12- 输出每行的12个字符以后的值
- last | cut -d ' ' -f 1 输出登陆的用户名

## grep 分析数据
- grep主要用于分析行内由没有目标数据，由就把该行获取。
- last | grep 'root' 选择‘root’行
- last | grep -v 'root' 反选root行
- last | grep -c 'root' 计算root次数
- last | grep -i 'ROOt' 忽略大小写，查找root

## sort 排序
- sort -f 忽略大小写
- sort -n 使用纯数字进行排序，默认时字符排序
- sort -r 方向排序
- sort -t ':' -k 3 以‘：’为分割符，按照第3个区间排序
- sort -t ':' -k 3 -n 以第3个区间按照数字进行排序

## uniq 合并
- 重复的数据值显示一个
- uniq -i 忽略大小写，
- uniq -c 进行计数
- last | cut -d ' ' -f 1 | sort | uniq -c | sort -nr 按照登陆频率从达到小进行排序，并且输出登陆次数

## wc 统计
- 对文件或标准输入进行字/行/字符进行统计
- wc -l 仅列出行
- wc -w 列出字
- wc -m 多少字符

### 範例
- 如何一行命令统计出这个月的登陆系统中人次
    - 思路： 排除空行和wtmp行
    - last | grep [a-zA-Z0-9] | grep -v 'wtmp' | wc -l // 230

## tee 双向重定向
- tee会将标准输出同时输出到文件和屏幕
- ll /mnt | tee ok 用前面的文件创建或覆盖文件ok
- ll /mnt | tee -a ok  用前面的输出创建或叠加文件ok
