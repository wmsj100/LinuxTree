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
- 对于一个表不能有俩个相同触发时间和触发事件的触发器；
- 通过使用begin。。。end结构，能够定义执行多条语句的触发程序。
	- 定义执行多条语句的触发程序时，如果使用mysql程序来输入触发程序，需要重新定义分割符，以便能够再触发程序中使用“；”；
	- 分割符通过“delimeter来定义；

- if...elseif...end if; 这是mysql中的逻辑判断语句；
- **不能将触发程序和视图关联再一起**

## 删除触发器
- drop trigger tableName.tri_t1; 舍弃触发程序

## 实例
- create trigger int_sum before insert for each row set @sum = @sum + new.account;
	- for each row 定义了每次激活触发程序时将执行的程序；对于受触发语句影响的是每一行都要执行一次。
	- 本例执行语句是简单的set，负责将插入的amount列的值加起来。
	- 该语句将列引用为new.amount 意思是将要插入新行的amount值
	- 这个触发器的作用是把每次插入的amount值加起来存储到变量@sum;
	- set @sum=0; 初始化sum为0；
	- select @sum as "asdf"; 查看当前的sum变量的值

file sq3
'''
create database test3;
use test3;

### if逻辑判断
- delimiter |;
- create trigger up_2 before update on t5
	for each row
	begin
	if new.amount<0 then
	set new.amount=0;
	elseif new.amount > 100 then
	set new.amount = 100;
	end if;
	end;
	|
	delimiter ;
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


