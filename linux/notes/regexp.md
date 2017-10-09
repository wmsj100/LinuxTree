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
