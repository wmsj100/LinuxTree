# grep 查找文件的匹配文本

- grep  global search regular expression(RE) and print out the line   全面搜索正在表达式并把行打印出来
- 是一种强大的文本搜索工具，它能使用正在表达式搜索文本，并把匹配的行打印出来。
- 能够接收正则表达式和通配符，可以使用多个grep命令选项来生成各种格式的输出。

- 能够在一个多多个文件中搜索字符呈模板，
- 搜索到的文本被送到标准输出，不影响原有文本
- 可用于shell脚本，通过返回一个状态值来说明搜索状态，如果搜索成功，则返回0，不成功，这返回1；如果搜索的文件不存在，则返回2；利用这些返回值，可以进行一些自动化的文本处理工作。

## 参数
- c 计算找到搜索字符呈的次数
- i 忽略大小想
- n 输出行号
- v 反向选择
- r 递归搜索
- --color=auto 将找到的关键词部分加上颜色显示

## 实例
- grep 'root' /etc/passwd --color=auto
- cat /etc/passwd | grep 'root' --color=auto
- cat /etc/passwd | grep -v 'root' 将没有root的打印出来
- grep -r "main()" 在当前目录下递归搜索包含“mian（）”的文件，经常用于查找某些函数位于哪些源文件代码中。

## 正则表达式
- E 正则表达式标志
- 正则表达式要写在双引号内

## 实例
- grep -E "^0[0-9]{2,3}-[0-9]{8,9}(-[0-9]{3,4})?$" 匹配电话号码，区号0开头，3-4位，号码8-9位，哟可能会有分机号，3-4位。
**使用最广泛的命令之一，用来对文件内容按行进行模式匹配查找**

- 在命令行的正在表达式中 '.' 和 '*' 代表的意思如下：
  - '.' 代表任意一个字符
  - '*' 代表重复前面一个字符0到无穷次
  - '.*' 代表匹配任意字符

- grep root /etc/passwd
- cat /etc/passwd | grep root
- grep -n root /etc/passwd   将root所在的行包括行号打印出来
- grep -v root /etc/passwd  反选root所在的行
- grep -v root /etc/passwd | grep -v nologin  反选root nologin

- grep 'wmsj100' * 在当前目录搜索带‘wmsj100' 的文件
- grep -r 'root' * 在当前目录及其子目录搜索带有'root'的文件
- grep -r -l 'root' *  在当前目录及其子目录搜索带有’root ' 的文件，只显示文件位置，不显示匹配的文件内容
- grep -n 'root' * 匹配当前目录文件中有root的文件，并且显示行号

正则表达式
- grep -n 'w[wm]sj' * 在当前目录匹配含有 wmsj 或 wwsj的文件，并且显示行号
- grep -n '[^g]oo' h1  在h1文件内搜索不以g开头的oo所在的行
- grep -n '[^a-z]' h1  搜索不以小写字母开头的行
- grep -n '^google' h1  搜索以google开头的行
- grep -n 'google$' h1  搜索以google结尾的行
- grep -n '^[^a-zA-Z]' h1 匹配不以英文字母开头的文件
- grep -n '\.$' h1  找出h1文件中以。结尾的行
- grep -n '^$' h1  找出空白行
- grep -n '000*$' h1 搜索h1文件中包含0至少俩个或以上结尾的行
- grep -n 'o\{2\}' h1 搜索o出现俩次的行
- grep -n 'o\{2,5\}' h1 所属o出现2-5次的行

##扩展grep  egrep  或  grep -E
- grep -n 'good|gold' h1  在标准的grep中无法搜索出任何结果
- grep -n -E 'good|gold' h1
- egrep -n 'good|gold' h1 上面俩个结果一样
- 在标准的grep中如果在扩展字符前面添加'\'，grep会自动启用扩展选项'-E'
- grep -n 'good\|gold' h1  启用了扩展
- grep -n 'o\+' h1  搜索至少包含一个o的行
- grep -n '\.[0-9]?' h1 搜索小数位数为0或者1的行
- grep -n -E '(oo)+' h1  搜索至少包含一个的oo组合的行

## 不使用正则表达式 fgrep / grep -F
- fgrep查询速度比grep命令快，但是不够灵活；它只能找固定的文本，而不是规则的表达式；
- fgrep -n '.' h1  查找h1中包含小数点的行。


