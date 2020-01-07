---
title: deleteGitBigFile
date: 2019-05-11 00:48:39 Saturday
modify:
tag: [deleteGitBigFile]
categories: Git
author: wmsj100
mail: wmsj100@hotmail.com
---

# deleteGitBigFile

## 概述
- git提交记录总会不小心添加很多庞大的文件或者压缩包，这些都是无用的，但是即便在当前目录已经删除了，因为已经存在于git提交记录中了，所以代码库还是很大，浪费很多空间
- 需要从.git中删除无用的内容

## 用法
- 显示10个最大的文件id列表
	`git verify-pack -v .git/objects/pack/pack-*.idx | sort -k 3 -g | tail -10`
	f830d5449f307e45915c2544dfef902cfbfab5d9 blob   3714990 2811488 60010494
	986d0c3904de8a3b08c17b5feb9f29da442ebfd4 blob   5912773 5542283 31754
	c1fd4cf06c9836d1bbd0344729af99a9e5e5f32c blob   7959920 7872976 234245152
	90d45f4b62ce20fb4ff733e83267152951edad97 blob   28553670 28557775 205684107
	a2f423946a59e4a2c83955f4af4d19dc1f048e5f blob   45041599 43163608 74595714
	4949ea380952b32c412943ed77fb36fd5be35e84 blob   45337600 7431701 62822673
	4564140f9e8ee9fefb65db2ae33a8b8a90dc29d3 blob   54272873 54107977 242200239
	09401d185a5cdafadc33105b1d62b868328c0dba blob   54639114 54423305 5574037
	6562f64e52e205bce49f9611e04e82a0e0f956db blob   129540654 82626130 122357710
	3b08a747589895bdc995cd18ae1fe9e70abcd417 blob   697131332 691555610 296308295
- 根据文件id查询文件路径
	`git rev-list --objects --all | grep 3b08a747589895bdc995cd18ae1fe9e70abcd417`
	git rev-list --objects --all | grep 3b08a747589895bdc995cd18ae1fe9e70abcd4173b08a747589895bdc995cd18ae1fe9e70abcd417 yunos_compile/aarch64-linux-gnueabi-4.9-glibc-2.20.tgz
- 移除文件
	`git log --pretty=oneline --branches -- your_file`
- 删除文件历史记录
	`git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch --ignore-unmatch your_file' --prune-empty --tag-name-filter cat -- --all`
- 提交
	`git push --force --all`
- 清除本地缓存
	```
	rm -Rf .git/refs/original
	rm -Rf .git/logs/
	git gc
	git prune
	```

## 参考
- [git 删除无用大文件](https://www.cnblogs.com/langzou/p/9877165.html)

