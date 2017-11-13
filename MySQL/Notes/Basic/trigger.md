# trigger 触发器

- 把sql的bin目录添加到path中，就可以再命令行中执行sql命令；
- 批量执行SQL语句： 如果先批量处理SQL语句，可以考虑将SQL语句放到一个文件中，然后告诉mysql从该文件中读取输入，
	- mysql < sq1 --user=root
	- sq1 内容
		- use test;
		- select * from test;
	- 命令行就会展示查询表格的内容
	- 最常用的参数是 --host --user --password
	- 如果正在执行sql，则可以使用“source”来批量执行外部sql文件

## 创建触发器
- 触发器是与表有关的固定的数据库对象，当表上出现特定事件时，将激活该对象，一般用于给表插入新的值或者进行表内的数值计算之类的更新
- create trigger trigger_name trigger_time trigger_event on ta1_name for each row trigger_stmt;
	- trigger_time 触发器动作时间，可以时before/ after 指明触发器再激活它的语句之前或之后执行
	- trigger_event 指明了激活触发程序的语句类型。
		- insert 将新行插入表时激活触发程序
		- update 更改某一行时激活触发程序
		- delete 从表中删除某一行时激活触发程序
	- trigger_stmt 当触发激活时执行的语句，可以使用begin。。。end执行多个语句；

## 实例
file sq3
'''
create database test3;
use test3;
create table t1 (a1 int);
create table t2(a2 int);
create table t3(
a3 int not null auto_increment primary key,
b3 int default 0
);

delimiter |

create trigger testref before insert on t1
for each row begin
insert into t2 set a2=new.a1;
update t3 set b3=b3+1 where a3=new.a1;
end
|
delimiter ;

insert into t3(a3) values(0),(0),(0),(0),(0),(0),(0),(0),(0);
'''

上面这个脚本创建了三个带有触发器的表格，当给表格t1插入数值时候，t2/t3都会同时进行更新，这个功能就想当厉害了，因为现在的业务中就有创建一个vdc管理员，会自动获取所有project，应该就是利用了trigger事件；
