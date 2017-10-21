# 正则表达式

- () 范围和优先级，gr(a|e)y ==> gray|grey

- -E POSIX扩展正则表达式 ERE
- -G 基本正则表达式 BRE
- -P Perl正则表达式 PCRE

## 正则表达式基础
- -b 将二进制文件作为文本来进行匹配
- -c 统计以模式匹配的数目
- -i 忽略大小写
- -n 显示匹配文本所在行的行号
- -v 反选，输出不匹配的内容
- -r 递归匹配查找
- -A n n为正整数，表示after的意思，除了列出匹配行之外，还列出后面的n行
- -B n n为正整数，表示before的意思，除了列出匹配行之外，还列出前面的n行
- --color=auto 将输出中的匹配项设置为自动颜色显示

- grep '[a-z]' 匹配小写字符
- grep '[0-9]' 匹配数字
- grep '[[:lower::]]' 匹配小写
- grep '[[:upper:]]' 匹配大写
- [:alnum:] 大小写字母及数字
- [:alpha:] 大小写字母
- [:blank:] 空格键及tab
- [:digit:] 数字
- [:graph:] 除了空白字节外的其他所有按键
- [:lower:] 代表小写字符

## 扩展正则
- grep -E 'zo{1}' 匹配“zo”
- grep -E 'zo{1,}' 匹配一个或者以上的zo
- grep -E 'www\.(baidu|google)\.com' 匹配www.baidu.com 或者www.google.com
- grep -Ev 'www\.baidu\.com' 反选字符，“.”需要进行转义
- - grep -n '1,2p' 打印第1行到第5行
- - grep -n '1~2p' 打印以2为步进的所有行
- grep -n 's/hello/HELLO/pg' f1 读取f1文件，把每一行的‘hello’替换为‘HELLO’ ‘g’ 表示全局

## sed 流编辑器
- 在linux里敢称为编辑器的，大都非等闲之辈，比如vim
- -n 安静模式，只打印受影响的行，默认打印输入数据的全部内容
- -s 行内替换
- -c 整行替换
- -a 插入到指定行的后面
- -i 插入到指定行的前面
- -p 打印指定行，通常与-n参数配合使用
- -d 删除指定行
- sed -n '2cwww,baidu.com' f1 把f1文件的第二行替换为‘www.baidu.com'
- sed -i '2cwww.baidu.com' f1 把f1文件的第二行直接写入替换操作。

### sed进阶
- sed 's/a/A/1' 只替换第一个a
- sed 's/a/A/2' 只替换第二个a
- sed '1,2s/a/A/' 只替换前俩行
- sed '1~2s/a/A/' 替换步进为2
- sed 's/s/S/3g' 替换第3个以后的s
- sed '1,3s/my/your/g; 3,$s/This/That/g' f4 多个匹配，
- sed -e '1,3s/my/your/g' -e '3,$s/This/That/g' f4 这个也是多命令处理。
- sed 's/my/[-&-]/' f4 可以用&来当作被匹配的变量，然后可以在左右添加东西。
- sed 's/This is my \([^,$]*\),.*is \(.*\)/\1:\2/' f4 圆括号括起来的正则表达式说匹配字符串可以当作变量来使用，sed中使用\1,\2...
- sed 'N;s/my/your/' f4 把下一行当作缓冲区做匹配，就是说当前修改不涉及下一行内容。
- a 就是append，添加到下一行
- i 就是insert，插入到上一行
	- sed '1 i this is first line' f4 在第一行前面插入“this is first line”
	- sed '$ a this is last line' f4 在最后一行后面添加。。。
	- sed '/my/a ---' f4 在每一行后面都添加---
	- sed '/fish/a ---' f4 在fish这一行的后面添加---
- c 替换匹配行
	- sed '2 c this is second' f4 用“this is second” 体会第二行
- d 删除匹配行
	- sed '/fish/d' f4 删除fish这一行
	- sed '2d' f4 删除第二行
	- sed '1,2d' f4 删除前俩行
- p 打印
	- sed -n '/fish/p' f4 打印fish这一行
	- sed -n '1,/fish/p' 打印包括fish之前的内容，
	- sed -n '/fish/,/dog/p' f4 打印fish， dog内容

##sed 四个高级命令
- sed '/dog/,+3s/^/#/g' f5 匹配dog并且之后3行，在开头添加“#”
- 命令打包，命令可以多个，用分号分开，可以用大括号括起来作为嵌套命令
	- sed '3,6{/This/d}' f5 删除第3，6行的This
	- sed '3,6 {/This/{/fish/d}}' f5 在3，6行先匹配到This，然后匹配fish并且删除该行。
	- sed '1,${/This/d;s/^ *//}' f5 从头到尾，匹配This并且删除，匹配空格开头的删除空格。
- HoldSpace
	- g 将hold space中的内容拷贝到pattern space中，原来pattern space中的内容被清除
	- G 将hold space中的内容append到pattern space后
	- h 将pattern space中的内容拷贝到hold space中，原来hold space的内容被清除；
	- H 将pattern space的内容append到hold space后	
	- x 交换pattern space和hold space的内容
	- 有一个当前处理区和暂存区，暂存区不可诶被删除
	- sed '1G;h;$d' f6 这个命令可以倒序输出内容。	
[sed教程](https://coolshell.cn/articles/9104.html)


## awk文本处理语言
- awk是一种优良的文本处理工具，是一种处理文本的编程语言工具，是linux环境中现有功能最强大的数据处理引擎之一。
- awk的所有操作都是基于pattern(模式)--action(动作)对来实现的。
'''shell
if(NR==1){
print $1 "\n" $2 "\n" $3  
} else {
print 
}
}' f3
'''
- 'NR' 表示当前读入的记录数，当前处理的行数，
- “OFS”输出时的字段的分割符，默认为空格
