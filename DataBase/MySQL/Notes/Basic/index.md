# 索引

- 索引是一种与表有关的结构，相当于书的目录，可以根据目录的页码快速找到所需的内容。
- 当表中有大量的记录时，若要对表进行查询，没有索引会是全表搜索；将所有记录一一取出，然后和查询条件进行一一对比，然后返回满足条件的记录。
- 这样做会消耗大量的数据库系统时间，并造成大量的磁盘I/O操作。

- 如果有索引值，会先和索引中找到符合条件的索引值，通过索引值就可以快速找到表中的数据，大大加快搜索速度。

## 创建索引
- alter table employee add index idx_id(id);
- create index idx_name on employee(name); 给employee表的name列创建idx_name索引

## 查询索引
- show index from employee;
- 在使用select语句查询的时候，语句中where里面的条件，会自动判断有没有可用的索引。
