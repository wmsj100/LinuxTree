# 逻辑操作符

- 逻辑操作符的计算结果均为“true”， “false”， “null”；

---

- not | ! 取反
	- select not 1; // 0
	- select not 0; // 1;
	- select not null; // null	
	- select !1; // 0
- and | &&; 逻辑且； 所有结果均为非零且不为null时返回1，有0时返回0，否则返回null；
	- select 1 && 0; // 0
	- select true and false; // 0
	- select 1 and null; // null
- or | || 或； 如果俩个操作数均为非null，且任一个为非零，则返回1，否则返回0；
	- select true or false; // 1;
	- select 1 || null; // 1;
	- select null or null; // null
- xor 当任一个值为null，返回null， 当有奇数个非零值，则返回1，否则返回0；
	- select null xor 1; // null
	- select 1 xor 2; // 0 有偶数个非零
	- select 1 xor 0; // 1 有奇数个非零
	- select 1 xor 2 xor 3; // 1 有奇数个非零

