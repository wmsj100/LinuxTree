---
title: git中关于忽略指定文件的备份
date: 2016-07-21
tags: [Git]
categories: Frame
---

http://www.cnblogs.com/zhasen/p/3670199.html

开始一个项目时候首先需要创建`git`备份，但是对于`node`项目，里面的`node_module`文件太多了，而且没必要备份，因为可以从`package.json`完整的得到所有内容。
那么如何排除这个文件夹呢，

就是在`git init`之前，在根目录创建一个`.gitignore`文件，里面就是`git`进行备份时候要忽略的内容，我暂时只希望忽略`module`文件，所以就写了一条。
`node_modules/*` -- 忽略整个`node_modules`文件夹

tmp.txt         //忽略tmp.txt
*.log           //忽略所有log文件
tmp/*           //忽略tmp文件夹所有文件
log/**/*.log    //忽略log目录下的包括子目录下的所有log文件

其他的一些过滤条件

？：代表任意的一个字符
＊：代表任意数目的字符
{!ab}：必须不是此类型
{ab,bb,cx}：代表ab,bb,cx中任一类型即可
[abc]：代表a,b,c中任一字符即可
[ ^abc]：代表必须不是a,b,c中任一字符
由于git不会加入空目录，所以下面做法会导致tmp不会存在

tmp/*             //忽略tmp文件夹所有文件
改下方法，在tmp下也加一个.gitignore,内容为

*
!.gitignore
还有一种情况，就是已经commit了，再加入gitignore是无效的，所以需要删除下缓存

git rm --cached ignore_file
这样就OK了。