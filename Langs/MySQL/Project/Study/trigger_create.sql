create database test_db;
use test_db;
create table test1(a1 int);
create table test2(a2 int);
create table test3(a3 int not null auto_increment primary key);
create table test4(
	a4 int not null auto_increment primary key,
	b4 int default 0
);
delimiter |

create trigger testref before insert on test1 for each row begin
insert into test2 set a2=NEW.a1;
delete from test3 where a3=NEW.a1;
update test4 set b4=b4+1 where a4=NEW.a1;
end
|

delimiter ;

insert into test3(a3) values
(null), (null), (null), (null), (null),
(null), (null), (null), (null), (null);

insert into test4(a4) values
(0),(0),(0),(0),(0),(0),(0),(0),(0),(0);
