# 获取物理成绩最高的学生的信息

- select * into outfile '/tmp/physice.txt' from student where sid=(select sid from mark where cid=(select cid from course where cname='physics') order by score desc limit 1);
	- 利用order by score desc 进行降序排序
	- limit 1 只获取一条数据

## 修改Tom的化学成绩添加3分
- update mark set score=(score+3) where sid=(select sid from student where sname='Tom') and cid=(select cid from course where cname='chemistry');
- 最开始我还使用了用户变量进行临时存储
	- set @sid:=(select sid from student where sname='Tom')
	- set @cid:=(select cid from course where cname='chemistry')
	- set @score:=(select score from mark where sid=@sid and cid=@cid)
	- update mark set score=(@score+3) where sid=@sid and cid=@cid
- 其实我这个操作就太啰嗦了，和上面的写法一比较就高下立判了。
