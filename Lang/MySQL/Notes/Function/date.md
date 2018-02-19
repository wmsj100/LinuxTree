# 日期时间函数

- adddate(date, days); 给date添加days天树
	- select adddate('1998-01-02', 31); // ''1998-02-02'
- addtime(datetime, time);
	- select addtime('1989-01-02 23:59:59', '11:1:1'); // 1990-01-01 11:59:59
- convert_tz(); 将时间日期转换时区
	- select convert_tz('2004-01-01 10:00:00', '+00:00', '+10:00'); // '2004-01-01 20:00:00'
- curtime(); 当前时间
- curdate(); 当前日期
- datediff(date1, date2); 计算俩个日期之间的天数
	- select datediff('1997-12-30', '1996-12-30'); // 366

