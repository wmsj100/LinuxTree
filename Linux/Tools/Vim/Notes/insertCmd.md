---
title: 插入模式命令
date: 2017-12-13 19:09:09
tags: [vim]
categories: Linux
---

## 插入模式
- ctrl w 删除前一个单词
- ctrl u 删除光标前面的所有内容，但保留行首的缩进
- ctrl p 单词补全，如果输入单词的一部分，然后通过ctrl p vim会自动猜测剩余部分。
- ctrl n 类似于ctrl p 区别在于这个是向下匹配，而ctrl p 是向上匹配
- ctrl x ctrl l 查找整行
- ctrl x ctrl f 查找当前文档的文件名
- ctrl x ctrl o 智能输入，这需要在'vimrc'中开启'filetype plugin on'，这个会根据文件类型进行只能补全。
- ctrl a 编辑器会把上次在插入模式下输入的文本再输入一次。
- ctrl y 会一个一个复制上一行的字符
- ctrl e 会复制光标下面的字符，和'ctrl y'相反
- ctrl @ 类似与'ctrl a'但是区别在于粘帖了上一次的内容之后会退出输入模式。
- ctrl r 寄存器，把光标移动到目标单词开头，键入'"vyiw'这是拷贝一个单词，并且存储到寄存器中，调用的时候，'ctrl r v' 这样就把寄存器的内容粘帖出来了。
- :iabbrev ad advertisement 缩写是取代一个长词的短词。例如用'ad'取代'advertisement' 触发是通过输入'ad'然后再输入一个不可能是单词一部分的字符来触发，比如空格或引号。缩写可以使用简略':iab'来实现相同的效果。
- :abbreviate wolrd world 更正拼写错误，只要这样设置后，只要是下次输入单独的单词'wolrd' 会自动被'world'替换。可以加上一系列这样的缩写。
- :abbreviate 可以查看所有的缩写，
	- 'i' 表示只有在插入模式下生效
	- '!' 表示插入模式和命令行模式都生效
- :unabbreviate ad 删除'ad'的缩写
- :abclear 删除所有的缩写
- ctrl k Co '©' 利用二合字母可以输入键盘上找不到的字符，所有支持的二合字母可以通过命令':digraphs'来查看
- ctrl o D 通过'ctrl o'命令可以在插入模式下执行普通模式的命令
