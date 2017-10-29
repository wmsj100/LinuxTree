# 备份

- 导出的文件只是保存数据库中的数据；
- 备份则把数据库的结构/ 约束/ 索引/ 视图等全部另存为一个sql文件；
- mysqldump 是备份命令。

- mysqldump -u root database > back.sql
- mysqldump -u root database table > back.sql;

 
