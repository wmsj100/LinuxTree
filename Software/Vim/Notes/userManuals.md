---
title: 用户手册 
date: Sat 09 Dec 2017 10:14:55 AM CST
tag: [vim]
categories: Tools
author: wmsj100
mail: wmsj100@hotmail.com
---

## 常规命令
- set rtp? 查看vim的'runtimepath'路径字符串
- ctrl ] 跳转到目标链接
- ctrl o 回到上一次目标，回退
- ctrl i 跳到较新的地方，前进, i在o的前面 
- ctrl t 撤销回退标签
- set showmode 显示vim当前模式
- Esc 回到普通模式
- set compatible? 查看当前兼容设置值
- set ignorecase 忽略大小写
- set hlsearch 高亮显示搜索的值
- set incsearch 在输入搜索值的过程中就开始跳转页面到搜索值的位置
- set autowrite 设置自动保存

## vim 操作命令
- J 删除换行符
- ctrl r 回退
- u 撤销
- a/i 插入
- A 在行尾插入
- I 在行首插入
- o 在下一行插入
- O 在上一行插入
- 9k 向上移动9行
- 5dd 向下删除5行
- :e! 放弃修改重新装载原来的文件。
- 5w 向前跳过5个单词
- b 向后移动一个单词
- 5b 向后移动5个单词
- w 跳到下一个ie单词的词首
- e 跳到下一个单词的词末
- ge 跳到上一个单词的词末
- ^ 移动到一行的第一个非空字符
- 0 移动到当前行的第一个字符
- fx 在当前行向前查找第一个字符'x' f 是'find'查找的意思
- 3fx 在当前行查找第三个'x'字符
- Fx 向左查找第一个字符'x'
- tx 类似fx，只是移动到目标字符的前一个字符， t 是'to'到达的意思
- % 匹配配对的括号
- 33G 跳到33行
- %50 跳到中间位置
- %90 跳到文档90%

## 获取信息
- ctrl g 显示当前文档信息以及光标所处位置
- H 'home' 跳到可视窗口的头部
- M 'middle' 跳到中间
- L 'last' 跳到可视末尾
- ctrl d 向下滚半屏
- ctrl u 向上滚半屏
- ctrl e 上滚一行
- ctrl y 下滚一行
- ctrl f 向前滚动一屏幕
- ctrl b 向后滚动一屏幕
- zz 把光标所在行移动到屏幕的中间
- zt 把光标所在行移动到屏幕顶部
- zb 把光标所在行移动到屏幕底部
- * 把光标移动到要查找的单词上面使用'*'命令，会查找当前单词,
- 3* 向下查找第3个当前光标所在单词
- \> 匹配结尾 'the\>' 匹配the结尾的单词
- \< 匹配开头 '\<the' 匹配’the‘开头的单词
- \<the\> 完整匹配单词’the‘
- ^the 匹配以'the'开头的行
- the$ 匹配以'the'结尾的行
- ^the$ 匹配内容为'the'的行
- c.m 匹配'c'任意字符'm'这样的单词
- ter\. 匹配'ter.' 特殊字符需要转义
- :jumps 输出一个可以跳转位置的列表
- ma 标记，这个功能在页面进行跳转时就很方便了，标记的内容是26个字母（a-z），单字母标记，触发标记是通过单引号"'a",这一就会跳转到a标记的行。
- :marks 可以查看所有的标记列表

## 复合命令
- d4w 删除后面的4个单词
- cc 删除一整行并且进入插入模式， 是'change'的意思。
- x 表示 dl 删除光标下的字符
- X 表示 dh 删除光标左边的字符
- D 表示 d$ 删除至末尾
- C 表示 c$ 修改到行尾
- s 表示 cl 修改一个字符
- S 表示 cc 修改一整行
- r 替换当前字符，替换完成后自动退出编辑模式
- R 一直替换，知道按'Esc'退出替换模式。
- df> 删除从当前光标到当前行的'>'位置为止，在删除'html'模板是否比较有用。'<span>hello</span>' 比如在第一个'<'执行'df>'就可以擅长'<span>'
- . 重复执行前一个命令， 以上面的例子，移动光标到第二个'<'，然后按下'.'就会重复执行前一个命令'df>'删除'</span>'
- 利用'.'重复执行的命令可以进行很多复杂的操作，比如要替换文件内部的多个'four'为'five'，执行的命令如下：
	- /four<Enter> 找到第一个'four'
	- cwfive<Esc>  修改陈'five'
	- n	找到下一个'four'
	- .	重复修改到'five'的操作
	- n	找到下一个'four'
	- .	重复修改,以此类推

