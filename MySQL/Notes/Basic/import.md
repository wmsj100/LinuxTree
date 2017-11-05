# 导入数据

- 可以把一个文件里的数据保存进一张表。

## 导入数据
- load data infile 'finename' into table talbename;
- 但是按照上面进行操作时候却报错，错误码13，查询说是权限不够，然后在博客园中找了一篇文章，说是需要添加“local”就可以了。

## [导入数据失败](http://www.cnblogs.com/youxin/p/5257553.html)

## 实例
- load data local infile '/home/wmsj100/Documents/test/SQL6/in.txt' into table employee; 这样就可以插入数据成功。
