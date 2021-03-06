---
title: 变量和参数
date: 2017-12-03 08:22:56	
modify: 2020-06-24 17:59:40 
tag: [shell,params]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 概述
- 在shell中每一个变量的值都是字符串，无论给变量赋值时候有没有引号包裹，值都会以字符串形式存储
- 这意味着shell不会区分变量类型，即使给变量赋值整数或小数，都会被视为字符串
- shell和一些工具程序会在需要时候把数值型字符串转换为对应的数值
- shell区分大小写

## 嵌套变量

```shell
sql0='sql com0'
sql1='sql com1'
sql2='sql com2'
mysql='mysql -u root -p 123 -e'

for num in $(seq 0 2)
do
	cmd=$(eval echo '$'sql$num)
	$mysql $cmd
done
```
- 通过上面的例子可以看到要借助eval来实现变量的嵌套使用。
- 而且需要借助中间值cmd来保存变量值

## 定义变量
- var=value
- var='value'
- var="value"
- 注意等号左右不能有空格，shell中尽量不要使用多余的空格，

## 定义和使用变量
- 变量的名字就是保存值的地方，引用变量的值就叫做变量替换
- var1是一个变量的名字，$var1就是引用这个变量的值，
- '$var1'是'${var1}'的简写，某些上下文中'$var1'可能会引起错误，此时就需要使用'${var1}';
- 加花括号帮助解释器识别变量的边界，推荐给所有的变量加花括号
- 已经定义的变量可以被重新定义

## 变量
- 变量名称前添加`$`，花括号是可选的，添加是为了清晰识别边界，推荐给所有变量添加花括号
- 以双引号包围变量的值时，输出时候会想解析里面的变量和命令，
- $() 把shell命令包裹在圆括号内部，
	- log=$(cat text.txt) echo $log  会把txt文件的内容一行输入

## 只读变量
- readonly url 把url变量设置为只读变量，这样变量的值不允许被修改

## 删除变量
- unset url 删除变量，再次打印该变量，会输出空值

## 只读变量
- `readonly`可以将变量定义为只读变量,这个和通过`declare`来声明创建的只读变量类似，
- 只读变量的值不能被改变。
	- readonly a=1
	- a=2; // error
    - declare -r a

## 变量类型
> shell有三种变量
- 局部变量: 在脚本或命令中定义，仅仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量
- 环境变量: 所有的程序，包括shell启动的程序都能访问环境变量，有些程序需要环境变量来保证其正常运行，必要的时候shell脚本也可以定义环境变量
- shell变量: shell程序设置的特殊变量，shell变量中有一部分时环境变量，有一部分时局部变量，
- shell中的变量最好用双引号包裹，这样可以应对变量值为空的时候比较不报错
## 编辑变量

## 变量替换
- -e 对转义字符进行替换
	- echo "value is $a \n" #vlaue is 2 \n
	- echo -e "value is $a \n" # value is 2

### # 从前往后删除
- a=${path#*/ruby-*:}  删除内容至找到ruby开始
    - # 从开始删除，且删除最短
    - ## 符合替换文字的“最长的”哪一个
- a=${path#/*:} 删除最前面的一个目录
- a=${path##/*:} 删除目录只剩下最后一个目录，俩个#表示删除最长的内容

### % 从后往前删除
- a=${path%:/home*} 从后面往前删除，删除内容最小匹配，包括:/home也删除- a=${path%%:*bin} 从后往前删除，按照最大匹配，删除值。

### / 替换
- a=${path/sbin/SBIN}  把匹配到的第一个sbin替换为SBIN
- a=${path//sbin/SBIN} 把匹配到的所有的sbin替换为SBIN

### 变量的测试与替换
- a=${a-root} 如果变量a不存在，则创建变量a，并且赋值root
- a=${a:-root} 如果变量a不存在或赋值为空，则给变量a赋值root  有没有冒号差别很大
- a=${b+root} b没有设置，a为空;b设置为空，则a为root；b有值，a赋值为root；
- a=${b:+root} b没有设置或者赋值为空时候，a为空；b有值，a赋值root
---
- *+/-/:+/:- 这四个都不会影响到参照b的值*
---
- a=${b=root} b不存在，a=b=root; b设置为空，a=b=""; b设置值，a=$b;
- a=${b:=root} b不存在或设置为空，a=b=root; b设置值，a=$b;
---
- =/:= 会影响到参考b的值
---
- a=${b?root} b不存在，则root输出至stderr; b设置为空或有值，a=$b;
- a=${b:?root} 若b不存在或设置为空，root输出至stderr, echo $? // 1; b有值，a=$b;

### 範例
- 删除mail值的其它信息，只留下用户名
    - mail=$MAIL; // /var/spool/mail/wmsj100 
    - b=${mail#*mail/} 删除内容至/mail,包括自身
    - b=${mail##/*/} 删除俩个斜线之间最大的值

## 参考
- [变量](http://c.biancheng.net/cpp/view/2739.html)
