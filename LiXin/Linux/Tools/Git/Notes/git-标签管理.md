---
title: git-标签管理
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
- 发布一个版本时，我们通常先在版本库中打一个标签，这样，就唯一确定了打标签时刻的版本。将来无论什么时候，取某个标签的版本，就是把那个打标签的时刻的历史版本取出来。所以，标签也是版本库的一个快照。
<!-- more -->
- git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针，所以创建和删除标签都是瞬间完成的。
- 命令`git tag <name>`用于创建一个标签，默认为HEAD，也可以指定一个commit id;
- `git tag -a <tagname> -m "blablabla……"`可以指定标签的信息；
- `git show <tagname>`可以查看tag的信息；
- `git tag`可以查看所有的标签。

- `git push origin <tagname>`可以推送一个本地标签；
- `git push origin --tags`可以推送全部未推送过的本地标签；
- `git tag -d <tagname>`可以删除一个本地标签；
- `git push origin  :refs/tags/<tagname>`可以删除一个远程标签。
