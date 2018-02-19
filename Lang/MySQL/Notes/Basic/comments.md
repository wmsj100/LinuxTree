# 注释

- mysql支持3种类型的注释

- 以“#” 字符开头到行尾
- 以“--”序列开始到行尾，第二个破折号后面至少跟一个空格符，
- 以“/*”序列开始“*/”序列结束。结束序列不一定再同一行，允许注释跨越多行。

## 实例
- select 1+1; # this is comments
- select 1+1; -- this is comments;
- select 1+ /* this is comments */ 1;
- select 1+
	/*
	this is a 
	comments
	*/1;

