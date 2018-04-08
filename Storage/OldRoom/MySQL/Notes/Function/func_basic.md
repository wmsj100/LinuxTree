# mysql 基础函数

## 比较运输
- 比较运算的结果为 1 true； 0 false； null；
- 如果需要，字符串和数字可以互相转换
- 数值比较规则：
	- 若有NUll，则结果为null
	- 如果俩个参数都是字符串类型，则作为字符串比较
	- 若都为整数，则作为整数比较
	- 若有一个为“timestamp”或“datetime”数据类型，其它参数均为常数，再比较之前会先转换为“timestame”类型
	- 其它情况参数作为浮点数进行比较
	- 默认情况下字符串比较不区分大小写; 
		- select "a" < "b" ; 1
		- select "a" < "B"; 1
		- select '0' = 0; 1

### 操作符
- = 等于 如果有一个值为null，则结果为null；
- <=> 空值安全的等号； 再俩个值都是null时候返回1，其它值和null比较时候方法0；
- <> 或 != 不等于
- <= 小于等于
- > 大于
- is boolean 或 is not boolean 根据一个布尔值来检验一个值，布尔值可以时true, false, unknown;
	- select 1 is true, 0 is false; // 1, 1
	- select null is null, null is not true, null is not false, null is unknown; // 1,1 ,1 ,1
- value between min and max  假若value大于等于min或小于等于max，则方法1， 否则返回0；
	- select 1 between 2 and 3; // 0
	- select 'b' between 'a' and 'c' // 1;
- coalesce 返回参数列表的第一个非null值，再没有非null值时候则方法null
	- select coalesce(null, 0, 1); // 0
	- select coalesce(null, null); // null
- greatest(val1, val2) 当有2个或以上的参数时候，返回值最大的的参数
	- select greatest(0,2,1); // 2;
	- select greatest('A', 'b', 'a'); // 'b'
	- select greatest('A', 'B', 'b'); // 'B'
- val in (val1, val2, ..) 若val为in列表的任意一个值，则其返回值为1， 否则为0；字符串比较不区分大小写
	- select 1 in (1,2); // 1
- val not in (val1, val2) 不再范围内
	- select 1 not in (2,3); // 1
- isnull(val) 如果val为null，则方法true
- interval(N,n1,n2,n3); 假若n<n1,则返回0； 假若n<n2,则返回1， n<n3,则返回2，假若n为null，则返回-1；所有的参数均按照整数处理。
	- select interval(1,2,3); // 0
	- select interval(2,1,2,3); // 2
	- select interval(null, 1); // -1;
