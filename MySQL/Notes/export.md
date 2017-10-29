# 导出数据

- 把数据库中某个表的数据保存到一个文件中，
- select col1, col2 into outfile 'finename' from tablename;

## [导出失败](http://www.php230.com/1413458162.html)

- 如果出现“can't create/write to file...” 就是说要导出的文件夹权限不够，需要修改权限，或者是修改导出文件夹为“/tmp”。
- 然后我修改了导出文件夹就ok了。

## 实例
- select * into outfile '/tpm/out.txt' from employee; 导出成功。
- 很奇怪的一点是这样导出的数据在linux下不可见，不管是通过cat/ vim/ ll等各种命令结果都是文件不存在，但是进入mysql中，就可以找到文件，如果重新导出同名文件会提示文件名重名。

