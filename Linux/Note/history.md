---
title: history
date: Tue 20 Feb 2018 07:26:01 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- history 查看命令的历史，显示的数量是由'HISTSIZE'来决定的
- echo $HISTSIZE // 1000
- history n 显示最近n条数据
- history -c 将目前shell中的history内容全部消除
- history -r 将histfiles内容读取到目前这个shell的history中
- history -w 将目前shll的历史写入到histfiles中

- 当bash登陆linux主机时，会主动读取主目录`~/.bash_history`
- 当bash注销时候会把这次登陆的history写入到`~/.bash_history`

- !1 执行history的第一条命令
- !! 执行上一个命令

- 对于多重bash登陆问题，打开多个shell窗口时候，history写入问题，最后关闭的shell会被写入，之前shell的历史记录会被后面的覆盖。
- 建议用单一shell操作，这样可以记录所有的命令，不会出现shell覆盖历史记录丢失的问题。
