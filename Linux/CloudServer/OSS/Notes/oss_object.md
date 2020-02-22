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

- bucket.put_object(cloudpath, localpath)
- 上传不只是可以上传一个文件，还支持上传字符串、unicode、Bytes、网络流
- bucket.put_object_from_file 专门用来上传本地文件
- 下面会把一个接口请求的返回值存储到文件mydata
```python
import requests

input=requests.get('http://myweb.com:8006/app1/mydata')
bucket.put_object('json/mydata', input)
```

```python
import oss2
auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
bucket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'wmsj100-python-test')'
b=bucket.put_object('image/image.jsp', '/tmp/tmp/image') 上传本地文件/tmp/tmp/image到test1/image.jpg
#b.status 200
bucket.put_object_from_file('test/a.file', '/home/ubuntu/.bashrc') # 把.bashrc 文件上传到`oss://wmsj100-python-test/test/a.file`
bucket.get_object_to_file('test/a.file', '/tmp/tmp/bashrc') # 把bucket的test/a.file 下载到本地的/tmp/tmp/bashrc
```

## 下载文件

- bucket.get_object('json/a.json')
- 下载文件用这个方法，get_object获取到的是类文件对象，可以进行迭代，，返回的是一个stream流，需要执行read()才能计算返回数据的CRC，
- 调用该接口后都需要进行crc验证
- b.client_crc == b.server_crc
- **bucket.get_object_to_file** 专门用来下载文件的接口。
- 指定下载范围 **byte_range**
	- `bucket.get_object('json/b.json', byte_range(0,99))` 下载文件的前100字节数据，如果范围错误，则下载整个文件
```python
b=a.bucket.get_object('json/a.json')
b.client_crc == b.server_crc # True
```



## 列举文件

- oss2.ObjectIterator(bucket) 用于列举文件
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

## 文件管理

- `bucket.object_exists('json/a.json')` 返回布尔值，判断文件是否存在
- `bucket.get_object_acl('json/a.json').acl` 获取文件的权限
- `bucket.get_object_meta('json/a.json')`
- `bucket.header_object('json/a.json')` 
- `[b.key for b in oss2.ObjectIterator(b)]` 列举文件
- `[b.key for b in oss2.ObjectIterator(b, prefix='json/')]` 只获取指定前缀json/的文件,会把json/的所有子文件进行遍历
- `[b.key for b in oss2.ObjectIterator(b, prefix='json/', delimiter='/')]` 只获取json目录下的文件和目录名称

## 删除指定文件

- `bucket.delete_object('image')` 删除当前bucket下的image文件
- `b.batch_delete_objects(['json/a.json', 'json/b.json'])` 通过`batch_delete_objects`来批量删除多个文件，
- 删除目录所有文件夹其实是删除指定前缀的文件夹，是通过遍历来间接实现的。
```python
for obj in oss2.ObjectIterator(b, prefix='json/'):
	b.delete_object(obj.key)
```

## bucket间对象拷贝

- `b.copy_object('wmsjtest', 'str/a', 'json/a.json')` 从wmsjtest的bucket拷贝str/a文件到当前bucket的json/a.json
- bucket拷贝的前提是在同一个地域可以实现这样的操作	

## 参考


