---
title: bucket存储容器
date: 2020-02-21 18:32:08
modify: 
tags: [Notes]
categories: OSS
author: wmsj100
email: wmsj100@hotmail.com
---

# bucket存储容器

## 概要

- bucket是OSS的存储容器，所有内容必须存储到容器中

## 创建bucket

- 创建一个bucket `wmsj100-new-bucket`
```python
import oss2

auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
bucket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'wmsj100-new-bucket')
bucket.create_bucket()
```

## 枚举buket

- oss2.BucketIterator
- 查看当前所有的存储空间
```python
import oss2

auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
Serve=oss2.Service(auth, 'oss-cn-beijing.aliyuncs.com')
# 这样获取到的是一个对象
[ b.name for b in oss2.BucketIterator(Serve)]
#['wms100-testbuck', 'wmsj100', 'wmsj100-kindle', 'wmsj100-money', 'wmsj100-python-test']
```

- 查看空间是在`Service`中

## 查看bucket的location位置

```python
import oss2

auth = auth=oss2.Auth('accessKeyID', 'accessKeySecret')
bucket=oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'wmsj100-new-bucket')
local_name = buck1.get_bucket_location()
local_name.location # oss-cn-beijing
```

## 判断bucket是否存在

```python
try:
	bucket.get_bucket_info()
except oss2.exceptions.NoBucket:
	return False
except:
	raise
return True
```

## 获取存储空间信息

- info=bucket.get_bucket_info()
- info.name bucket名称
- info.storage_class 存储类型
- info.creation_date 创建日期 2020-02-21T04:04:16.000Z'
- b.intranet_endpoint 'oss-cn-beijing-internal.aliyuncs.com'
- b.extranet_endpoint 'oss-cn-beijing.aliyuncs.com'
- b.owner.id 创建者id
- b.acl.grant bucket的类型，默认私有
- b.data_redundancy_type LRS 加密类型

## 存储空间权限

- 有三种权限，默认是私有
	- oss2.BUCKET_ACL_PRIVATE
	- oss2.BUCKET_ACL_PUBLIC_READ
	- oss2.BUCKET_ACL_PUBLIC_READ_WRITE
- `bucket.put_bucket_acl(oss2.BUCKET_ACL_PUBLIC_READ_WRITE)` 更改为公共读写
- `bucket.get_bucket_info().acl.grant` 变更权限后可以进行查看

## 删除存储空间

- `bucket.delete_bucket()` 只能删除一个空的存储空间
