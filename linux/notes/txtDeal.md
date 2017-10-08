# 简单的文本处理

- tr 用来删除一段文本信息中的某些文字，或者将其进行转换。
	- echo 'hello world'| tr -d 'olh' 删除所有的o/l/h // 'e wrd'
	- echo 'hello world'| tr -s 'l' 去除来连续字符‘l’ // ‘helo world'
	- echo 'hello world'| tr '[a-z]' '[A-Z]' 把所有的小写转换为大写

- col 可以将tab转换对等数量的空格键
	- col -x 将tab转换为空格
	- col -h 将空格转换为tab

- join 俩个文件中包含相同内容的那一行合并在一起
	- join f1 f2 默认就是把f1 f2开头相同的内容合并在一起
	- join -t ':' f1 f2 指定分割符连接文件
	- join -t ':' -1 4 passwd -2 3 group 按照”:“分割，第四个字段连接:w

- paste 与join类似，它不对比数据，只是把多个文件合并在一起，以Tab隔开。
	- paste -d ':' f1 f2 指定‘：’分割符连接文件
	- paste -s f1 f2 不合并到一行，每个文件一行。
