# 数据类型

## 基础概述
- MySQL支持所有标准的SQL数据类型，主要分为3种
	- 数值类型
	- 字符串类型
	- 时间日期类型

## 类型概览
- 数据类型 大小 用途 格式
- INT 4  整数
- FLOAT 4 单精度浮点数
- DOUBLE 8 双精度浮点数
- ENUM  单选，比如性别  ENUM('a', 'b', 'c')
- SET  多选  SET('1', '2', '3')
- DATE 3 日期 YY:YY-MM-DD
- TIME 3 时间点或持续时间 HH:MM:SS
- YEAR 1 年份值 YYYY
- CHAE 0～255 定长字符
- VARCHAR 0~255 变长字符
- TEXT 0～65535 长文本数据

## char 和 varchar 区别：
- char 的长度是固定的，
- varchar 的长度是可以变化的。
	- “abc”对于 char(10) 表示存储的字符将占有10个字节（包括7个空字符）
	- “abc”对于 varchar(12) 则只占用4个字节的长度，增加一个额外的字节来存储字符呈本身的长度。
	- 12只是最大值，当存储的字节小于12时，按实际长度存储。

## ENUM 和 SET 区别
- ENUM 类型的数据的值，必须时定义时枚举的值的其中之一，即单选
- SET 可以多选。

[数据类型介绍](blog.csdn.net/anxpp/article/details/51284106#comments)
