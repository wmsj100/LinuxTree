# 字符串函数

- ASCII(str) 返回字符串最左边的值。
- BIN(N) 返回二进制的字符串表示，n为数值
- char_length(str) 获取字符串的长度
- conct(str,str2) 连接字符串，如果有null，则方法null；
- concat_ws(',', str1, str2) 使用分割符连接字符串
- elt(N, str1, str2); 若n为1，则返回str1，若为2，则返回str2；
- field(str, str1, str2,...) 返回值为str1.。。列表中str所在为值，若找不到，则返回0；如果所有参数都是字符串，则按照字符串比较；如果都是数值，则按照数值比较。如果str为null，则返回0；
- find_in_set(str, strlist); 假若字符串str再由N子字符串列表strlist中，则返回1到N之间。一个字符串列表就是由“，”分割的字符串‘a,b,c,s’。如果str不再字符串列表，则返回0；
	- select find_in_set('b', 'a,b,c,d'); // 2
	- seelct find_in_set('e', 'a,b,c,d'); // 0
- format(x,d); 将数值x格式化为“##,###,##”,d表示小数个数
	- select format(1234, 2); // 1,234.00
	- select format(12345,0); // 12,345
- hex(N_or_S)； 参数可以是数值或字符串，都被转换为16进制；
- insert(str,pos,len,newstr); 字符串str再起始为值pos，用字符串newstr替换长度为len,如果pos大于字符串长度，则返回字符串str
	- select insert('abcd', 2,2,'new'); // 'anewd'
- instr(str, substr); 方法字符串str种substr字符串第一次出现的位置。如果没有则返回0；
- left(str, len); 返回字符串左边数len个字符
	- select left('abcd', 2); // 'ab'
- length(str); 返回字符串的长度，和char_length类似
- locate(substr, str, pos); 如果pos不存在，则返回字符串str种第一次出现substr的为值，不存在则返回0；如果pos存在，则从字符串的pos为值开始查找
	- select locate('bar', 'foobarbar');// 4
	- select locate('bar', 'foobarbar', 5); // 7
- lower(str); 返回字符串str的小写
- ltrim(str); 返回删除str左侧空格的字符串；
- ord(N) 返回N八进制的字符串表示；
- repeat(str, count); 返回字符串str重复count次
- replace(str, from_str, to_str); 方法字符串str中字符‘from_str'被替换层’to_str'
- reverse(str); 反转字符串str
- right(str, len); 返回字符串从右侧数len长度的值
- substring(str, pos, len) 从字符串pos位置开始获取长度为len的子字符串；如果pos为负数，则从后面往左数len长度；
	- select substring('abcd', 2); // 'bdc'
	- select substring('abcd', 2,2); // 'bc'
	- select substrign('abcd' from 2); // 'bcd
	- select substring('abcd' from 2 fro 2); // 'bc'
	- select substring('abcd', -2, 2); // 'cd'
- trim(str) ;; 删除字符串左右的空格
	- select trim('  bar  '); // 'bar'
	- select trim(leading 'x' from 'xxxbarxxx'); // 'barxxx'
	- select trim(both 'x' from 'xxxbarxxx'); // 'bar'
	- select trim(trailing 'xyz' from 'barxxya'); // 'barx'

