---
title: 重定向
date: 2018-02-07
tag: [linux,shell]
categories: Linux
---

## 输出字符
- 标准输入（stdin）：代码0，使用< / <<
- 标准输出（stdout): 代码1，使用>/>>
- 标准错误输出（stderr）:代码2，使用2> / 2>>

### 範例
- cat /etc/crontab /etc/wmsj100 1>ok.file 2>err.file 标准输出到ok.file;标准错误输出到err.file;
- find /home /root -name .bashrc 2>/dev/null 只显示正确的信息，把错误的信息丢弃

### 把正确信息和错误信息都导入同一个文件
- find /root /home -name .bashrc 1>file 2>file 
- 上面这样的操作时错误的，因为俩条数据同时写入一个文件，又没有特殊处理，此时俩条数据可能会交叉写入该文件内，造成次序的错乱。最终文件会产生，但是数据时乱的，而且可能会丢失数据
- 正确处理如下
- find /root /home -name .bashrc 1>file 2>&1
- find /root /home -name .bashrc &>file 

### 标准输入 
- cat > f1 键盘输入的值会存储到f1文件中，直到按下ctrl+d
- cat > f1 < err 把err文件的内容输入到f1中
- cat > f1 <<"eof" 进入键盘输入模式，直到在新的一行输入"eof"并且按下"enter"即可完成，不需要按下ctrl+d

### 回传码
- 如果命令执行成功，回传码为0； $?=0;
- echo $? // 0
- 如果命令执行失败，回传码为1或者其它值
## 管道 
- 管道可以把一个命令的输出作为另一个命令的输入；

- tee 它把输出的一个副本输送到标准输出，另一个副本拷贝到相应的文件中
- who | tee who.out  同时有标准输出和输出到文件who.out

## 重定向  
- 标准输入的默认关联是键盘
- 标准输出的默认关联是屏幕
- 标准错误输出的默认关联也是屏幕
- 可以通过 > >> 进行重定向
- > h4  创建一个长度为0的空文件，如果文件存在，清空文件
- ll | grep ^d >> file.out 
- cat < file.out 以文件 file.out 作为标准输入
- sort < file.out 对文件的内容进行排序

- find ./ -name "*.txt" | xargs rm -rf {} \; 2 > /dev/null  把命令的错误消息丢弃

- find /etc -name "shadow" -print 1>ok.file 2>error.file  查看/etc目录下的shadow文件，如果标准输出是正确的，重定向到ok.file; 如果标准输出是错误的，输出到error.file

- cat < 1.txt > 2.txt

- find /etc/ -name "shadow" >> ok.1 2>&1  把正确和错误的标准输出都重定向到ok.1文件
- 2>&1 把标准错误重定向到标准输出

- linux的命令是从左到右执行，所以下面的例子就很好理解了
    - ll block || mkdir block && touch block/file
    - 判断block文件夹时候存在，不存在时就创建，然后创建file文件

- && 一个命令执行成功另一个命令才会继续执行，即回传码为0； $?=0 才会执行后面的。
- cp ./pub ./lib && rm -fr ./pub    执行复制操作执行成功，才会执行删除操作
- || 左边的命令执行失败，才会执行右边的命令
- cp /root ./ || echo "not has deal"
- ll /home/vbirding && echo "exit" || echo "not exit"
- ll /root || echo "error" | mail testuser; exit    读取/root 目录，如果失败，就发送一封邮件给testuser，并且退出当前shell。

## 匹配文本或过滤文本时候
- * 匹配零个或多个前面的字符
- ll | grep "er*or"   可以匹配  eor , eror, error, errrrrrrror 

- 可以使用正在表达式的三剑客
- grep , awk , sed
