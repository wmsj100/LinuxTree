# cut 将文本按列切分的小工具

- 它可以指定分隔每列的定界符。
- 如果一行有多个字段，想要提取其中一个或者多个即使cut大显身手的时候了。

## 参数
- b 以字节为单位进行分割
- c 以字符为单位进行分割
- d 自定义分割符，
- f 自定义字段
- --complement 抽取整个文本行，除了那些由-c -f选项指定的文本

## 实例
- cut -d ' ' -f 1 f1 抽取f1文件的第一列，按照空格分割符
- cut -d ' ' -f 1,3 f1 抽取文件的第一列和第三列
- cut -d ' ' -f 1-3 f1 抽取前三列
- cut -d ' ' -f 1 f1 --complement 抽取除第一列之外的内容
- cut -c 8- f1 抽取第8个字符后的所有内容

- history | cut -c 8- | cut -d ' ' -f 1 | sort | uniq -dc | sort -nr | head -n 20 抽取历史操作的前20高频率命令

- str="hello world"
- echo -n $str | cut -b `echo -n $str | wc -c` 获取到字符的最后一个字母
