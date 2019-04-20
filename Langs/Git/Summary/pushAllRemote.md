---
title: 同时提交多个分支
date: 2018-03-25 22:03:23 Sun
modify: 2018-03-25 22:03:23 Sun
tag: [tool,git]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# 同时提交多个分支
- git push;git push kyChina master 先提交默认分支，命令执行完成后执行另外一个提交；
- 鸡蛋不要同时放到一个篮子里，这样可以同时把代码提交到github和开源中国
- 开源中国的速度肯定比github的快，所以先提交到开源，然后再提交github
- ~~git config --global alias.ky 'push kyChina master;git push'~~ 这个操作报错，应该是不能这样设置别名
