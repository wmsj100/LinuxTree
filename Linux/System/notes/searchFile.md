# 环境变量与文件查找

## 变量名称解析
- declare tmp 声明一个变量名“tmp”，也可以不用声明直接进行赋值操作 tmp=wmsj100
- echo $tmp; // wmsj100 读取变量的值
- 子进程会继承父进程的绝大部分环境变量。
- Shell程序也作为一个进程运行在操作系统之上，而我们在Shell中运行的绝大多数命令都以Shell的子进程的方式运行。

## 变量类型
- 当前Shell进程私有的变量
- Shell本身内建的变量
- 从自定义变量导出的环境变量。
- 通过export可以把当前Shell的私有变量转化为环境变量，这样子进程也可以访问。
- 习惯将环境变量名设为大写。

## 变量生存周期
- 永久的： 需要修改配置文件，变量永久生效
- 临时的： 使用export命令声明即可，变量在关闭shell时失效。
- /etc/bashrc存放Shell变量 /etc/profile 存放环境变量,
- /etc/profile 对所有用户生效，~/.profile 只是对当前用户生效。

## 命令的查找路径与顺序
- 环境变量PATH存放的都是命令的放置目录，这些目录内都是可执行文件。

/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/home/wmsj100/.local/bin:/home/wmsj100/bin

- 系统会按照PATH中设定的路径按照顺序依次到目录中去查找，如果存在同名命令，会执行先找到的那个。

- PATH=$PATH:...path 这样可以把自定义路径添加到PATH，这样就可以直接输入脚本的名称来调用脚本。

- unset tmp 删除变量

- . 或者source ~/.bashrc 让bashrc的修改立即生效。

## 搜索文件
- whereis 搜索数据库中，快速 
- locate 通过/var/lib/mlocate/mlocate.db 数据库查找，这个数据库是使用定时任务每天自动执行updatedb命令来更新一次，所以如果是刚刚添加的文件，需要手动执行一次updatedb. 这个查询可以用通配符。  locate /home/wmsj100/Documents/git/*.jpeg

- which 是Shell内建的一个命令，通常用which来确定时候安装了某个软件，因为它只从PATH指定的路径中去搜索命令；

- find 最强大的搜索命令，它会直接搜索硬盘，通过文件类型/文件名/时间戳/文件权限进行搜索。  find /home/wmsj100 -name hello*  

## 时间相关的命令参数
- -atime 最后访问时间
- ctime 最后修改文件内容的时间
- mtime 最后修改文件属性的时间
- mtime n : n为数字，表示n天之前一天之内修改的文件
- mtime +n: 列出n天之前（不包括n天本身）被修改过的文件
- mtime -n: 列出n天之内（不包括n天本身）被修改过的文件
- newer file: file为一个已存在的文件，列出比file还要新的文件 


- summary:
	介绍了文件的查找命令whereis 查找具体的文件名，查找数据库，快速简单； locate 查找数据库，可以配额通配符 locate /home *.jpg; which 查找PATH路径下的可执行文件； find是查找磁盘，速度最慢但是最强大。
