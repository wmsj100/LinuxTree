---
title: git-分支机制
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
### git merge --no-f -m "change" wmsj100
- git还是建议在自己的分支上面进行代码开发，然后把完成一部分的代码推送到git库的自己的分支上面去，这样就没有代码丢失的风险了，然后等自己的版块代码完成之后就把分支代码合并到master分支上面，master是所有分支中最稳定的。
<!-- more -->
- 分支合并的时候使用`git merge wmsj100`这样的话，wmsj100分支上面的提交就全部被清除了，只剩下master的提交点了。如果想要把wmsj100分支上面的提交记录也保留下来的话，就是用这个命令——`git merte --no-ff -m ""new branch" wmsj100`
这个的意思就是说不要进行git默认的快速合并机制，而是重新提交并且命名为“new branch”，然后合并的分支是wmsj100；
- 合并之后可以通过命令——`git log --graph --pretty=oneline`进行查看
![git合并分支](http://upload-images.jianshu.io/upload_images/1606281-08b81e4a88cfbe82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 因为这样的合并保留了分支的提交记录，所以可以随时会退到分支的提交点。

### git stash  代码存储
- 当工作只进行到一半的时候，还没发提交，预计还得一天时间。但是，必须要在俩个小时内修复bug，怎么办？
- git stash——可以把当前工作现场“存储”起来，等以后恢复现场后继续工作：`git stash`
- 只需要输入`git stash`即可把当前的工作状态存储起来。当完成bug修复并且切换会自己的分支时候`git checkout wmsj100`，然后输入命令`git stash list`可以查看存储的版本，然后使用`git stash apply`来恢复，但是恢复后，stash内容并不删除，而通过命令`git stash drop`来删除存储。
- 另一种方式是通过输入命令`git stash pop`恢复的同时把stash内容也删除了；

- git branch -D wmsj100——强行删除一个分支；
 - 开发一个新feature，最好新建一个分支；
 - 如果要丢弃一个没有合并过得分支，可以通过`git branch -D wmsj100`强行删除。

## git push and git pull false
1. 首先，可以试图用`git push origin wmsj100`推送自己的修改；
2. 如果推送失败，则因为远程分支比你本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者是解决掉冲突后，再用`git push origin wmsj100`推送就能成功！
> 如果`git pull`提示“no tracking information",则说明本地分支和远程分支的链接没有创建，用命令`git branch --set-upstream branch-name origin/branch-name`。

### 小结：
- 查看远程库信息，使用`git remote -v;
- 本地新建的分支如果不推送到远程，对其他人就是不可见的；
- 从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的提交；
- 在本地创建和远程对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最后一致；
- 建立本地和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name;
- 从远处抓取分支，使用`git pull`，如果有冲突，要先处理冲突。
