# 控制流程函数

## case 
- case val when [compare-value] then result else result2 end; val1和when的compare-value值进行比较，如果相等，则方法result，否则方法else的result2
	- select case 1 when 1 then 'one' when 2 then 'two' else 'more' end;// 'one'
	- select case 3 when 1 then 'one' else 'more' end; // 'more'
- case when [condition] then result else result2 end;  判断条件时候为true，
	- select case when 1>0 then 'true' else 'false' end; // 'true'
- 如果没有else，则返回null

## if
- if(val1, val2, val3); 如果val1为true，则返回“val2”，否则返回“val3”，有点像三目运算
	- if(1<2, 'true', 'false'); // 'true'

## ifnull
- ifnull(val1, val2); 假若val1不为null，则返回val1，否则方法val2；
	- select ifnull(1,2); //1
	- select ifnull(null, 10); //10

## nullif
- nullif(val1, val2); 如果vl1=vla2;则方法值为null， 否则返回值为val1;
	- select nullif(1,1); // null	
	- select nullif(1,2); // 1
- 等效于： select case val1=val2 then null else val1 end;
- 或者 select case val1 when val2 then null else val1 end;
