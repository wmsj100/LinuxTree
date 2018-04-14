- 今天或者说最开始就一直是想安装了“mysql”后开始学习数据库来着，结果就是无法安装，然后昨天重装了系统，然后重新安装，因为这样我系统内肯定是没有“mysql”的，结果我安装“service”时候还是碰到一大堆文件冲突，安装“client”时候是很顺利的。所以我就果断的使用了“--force”强制安装的命令，结果还是提示“mysql.sokc”无法找到，当然了，服务也是无法启动的，不管是找到"/usr/share/mysql/mysql.service start"这样也不行。

最后百科是要安装”mariadb“这个数据库，我也不知道是什么。

然后在博客园找到了这篇文章： “http://www.cnblogs.com/starof/p/4680083.html”
让我明白了“mariadb”和“mysql”的关系。
内容其实是一样的，只不过因为担心“mysql”被闭源，所以社区开始使用“mariadb”这个版本。但用法是完全一样的。

