# 模式匹配

- 有俩种模式：
	- 标准sql模式匹配： _ %，使用like和not like
	- 扩展正则表达式匹配

## 标准sql模式实例
- select * from pet where name like 'b%'; 找出名称以b开头的
- select * form pet where name like '%fy' 找出名称以fy结尾的
- select * from pet where name like '%w%' 找出名称包含w的
- select * from pet where name like '_____' 找出名称长度为5的

## 扩展正则表达式 regext or rlike 
- select * from pet where name regexp '^b';
- select * from pet where name regexp 'fy$';
- select * from pet where name regexp 'w'; 找出包含w的名称
- select * from pet where name regexp '^.{5}$' 找出长度为5的

