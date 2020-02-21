---
title: oss对象文件
date: 2020-02-21 18:34:15
modify: 
tags: [Notes]
categories: OSS
author: wmsj100
email: wmsj100@hotmail.com
---

# oss对象文件

## 概要

- oss对象文件直接存储在bucket中，
- object没有目录，通过名称来模拟目录
- 对所有对象的操作性能都相同, 没有文件系统随着层级深度增加会消耗性能明显

## 上传文件

```python
import oss2
auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
bucket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'wmsj100-python-test')'
bucket.put_object_from_file('test/a.file', '/home/ubuntu/.bashrc') # 把.bashrc 文件上传到`oss://wmsj100-python-test/test/a.file`
bucket.get_object_to_file('test/a.file', '/tmp/tmp/bashrc') # 把bucket的test/a.file 下载到本地的/tmp/tmp/bashrc
```

## 列举文件

```python
from itertools import islice
import oss2

auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
bucket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'wmsj100-python-test')'
for item in islice(oss2.ObjectIterator(bucket), 10):
	print(item.key)
# .vimrc
# image
# image/
# image/2020-02-08_19-55-26_.mm.jpg
# notes/__slots__.md
# notes/array.md
# notes/assert.md
# notes/basic.md
# notes/bibao.md
# notes/callable.md
```

## 删除指定文件

- `bucket.delete_object('image')` 删除当前bucket下的image文件

## 参考

