# 数值函数

- abs(x); 返回x的绝对值
- ceil(x) ceiling(x); 向上取整x
- floor(x) 向下取整x
- format(x,d); 格式化数值，保留d为小数
- mod(n,m); n%m; n mod m; 返回n被m除后的余数，就是求模
	- select mod(5,2), 5%2, 5 mod 2; // 1 1 1
	- select mod(34.5, 3); //1.5
- pi() 返回7位pi值
- pow(2,3); power(2,3); 返回2的3次幂 8
- rand(n); 返回0到1之间的随机浮点数，若n存在，则返回重复序列，即重复执行时候，只是重复之前生成的随机数，并不会重新计算生成新的随机数
	- 若要得到i<=R<=j之间的随机数，则需要 floor(i+rand()*(j-i+1));
	- select floor(1+rand()*10);// 生成1到10之间的随机数
- order by rand() 生成随机排列,还可以搭配limit使用，再查询表格中使用比较多。
	- select * from shop order by rand();
- round(x,d); 进行四舍五入,d表示保留d为小数的四舍五入；
	- round(1.3);// 1
	- round(1.234, 2); // 1.23
- sign(x); 返回x的符号，正数为1， 负数为-1， 0 为0；
- sqrt(x); 返回x的平方根；

