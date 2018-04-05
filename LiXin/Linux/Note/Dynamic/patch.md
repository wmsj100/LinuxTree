# patch 

- 把更改应用到文本文件中。它接受从diff程序的输出，通常用来把教老的文件转换为教新的文件版本。

- 利用diff文件只输出差异
- 利用patch程序将差异应用到源码中

- diff和patch搭配使用的优点
	- 一个diff文件非常小，
	- 一个diff文件简洁的显示的所做的修改，从而允许程序补丁快速的评估

- GUN文档建议这样使用diff命令：
	- diff -Naur old_file new_file > diff_file
	- 在统一模式下递归逐行比较文本差异

## 参数
- p num 忽略几层文件夹
- E 如果发现了空文件，那么就删除它
- R 取消打过的补丁

## 范例
- diff -Naur f1.txt f2.txt > patchdiff.txt 输出补丁文件
- patch < patchdiff.txt  把补丁文件应用到f1.txt
- patch -R < patchdiff.txt 取消上面打过的补丁
