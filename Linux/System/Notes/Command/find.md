# find

- find命令的主要作用是沿着文件层次的结构向下遍历，匹配符合条件的文件，并执行相应的操作。

- print find将匹配的文件输出到标准输出
- exec find命令对匹配的文件执行该参数所给出的shell命令
- name 按照文件名查找
- type 查找某一类型的文件
- prune 使用这一选项可以是find命令不再当前指定的目录中查找
- user 按照文件属主来查找
- group 按照文件所属组来查找文件
- mtime -n +n 按照文件的更改时间来查找文件
	- -n 表示文件更改时间距离现在小于n天
	- +n 表示文件更改时间距离现在大于n天
- atime ctime

## 练习

- find . -print 打印当前目录下的文件目录列表，递归打印
- find -name "*.txt" -print 打印当前目录下的所有以“.txt”结尾的文件
- find -iname "*.txt" 忽略大小写
- find . \( -name "*.txt" -or -name "*.pdf" \) 打印当前目录下所有以".txt"/ ".pdf"结尾的文件名
- find . ! -name "*.txt" 打印当前目录下所有不以txt结尾的文件

## 逻辑操作符
- and 俩边都为真，简写wei -a
- or 一个为真， 简写为-o
- not 匹配条件是假，简写为 ！
- （） 显示的说明优先级，提高可读性，需要用反斜杠对括号进行转义

---

- find . -type l -name "*.txt" 打印当前目录下所有以txt结尾的符号链接
- find . -type f -name "*.php" -perm 777 查找当前目录下的所有权限为777的php文件
- find . -type f -user root 打印当前目录下所有root拥有的文件
- find . -type f \( ! -perm 777 -and ! -perm 644 \) 打印当前目录下所有权限不是777 和644的文件

## exec 高级命令
- find . -name "*.php" -exec ls -l {} \; 查找php文件并且显示其详情
	- {} 是一个占位符，在find执行过程中会不断替换成当前找到的文件
	- \; 是-exec命令结束的标记，通过反斜杠进行转义。

- find . -type f -user wmsj100 -exec cat {} \; > all.c 获取所有的wmsj100的文件并且输出到all.c
- find . -name "*.c" -exec ./command.sh {} \; 通常情况下-exec后面只能使用当个命令，如果使用多个命令，可以将多个命令写入sh文件，然后在-exec中使用这个脚本。

