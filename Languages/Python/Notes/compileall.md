---
title: compileall
date: 2020-09-15 16:44:17
modify: 2020-11-18 17:52:03  
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# compileall

## 概要

- 对于python的代码的加密我之前觉得是无稽之谈，但现在确实是一种需求，然后本来想看看华为的python的代码是什么的时候，发现全部都是pyc文件，然后意识到一点，就是python的文件是可以通过pyc文件来部署的，pyc文件本来就类似与java的编译文件，是跨平台的文件，
- 而且pyc文件要比什么代码混淆要实用的多，文件本身也是压缩模式，
- 之前觉得给动态语言加密是想多了，现在发现是需要的。
- 而这个加密过程也是使用python的自带模块compileall来实现的

## 使用

- 通过下面这个脚本就可以实现python的代码的编译和打包
- 打包的前提需要安装rename
- webapp包内有入口文件`__main__.py`且该文件有`__name__ == '__main__'`入口逻辑
- `python -m compileall webapp` 直接批量递归目录webapp的所有python文件转为pyc文件

```python
python3 -O -m webapp
find webapp -name "*.pyc" -exec rename s'/.cpython-36.opt-1//' {} \;
find webapp -name "*.pyc" -execdir mv {} .. \;
find webapp -name "__pycache__" -exec rmdir {} \;
find webapp -name "*.py" -exec rm {} \;
cd webapp
zip -r ../aa.zip ./*
python aa.zip
```
## 参考

- [python compileall](https://www.cnblogs.com/bonelee/p/8619391.html)
