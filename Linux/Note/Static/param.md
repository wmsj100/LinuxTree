# 变量名称解析

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


