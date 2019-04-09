# 统计

## 实例
- select year, month, bit_count(bit_or(1<<day)) from t1 group by year,month;
	- 这样的统计会忽略同一天的访问次数，可以知道有那些天是有访问的。
