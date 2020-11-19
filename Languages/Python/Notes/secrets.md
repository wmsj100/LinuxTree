---
title: secrets
date: 2020-11-19 15:35:46
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# secrets

## 概要

- 该模块用于生成高加密强度的随机数，
- 很多时候该模块会和`string`模块搭配使用

## 使用

- `secrets.randbelow(12)` 返回一个[0,n)的随机数
- `secrets.randbits(12)` 返回一个具有k个随机比特位的整数
- `secrets.choice('asdf')` 从一个非空序列中随机选取元素
- `secrets.choice(['aa', 'bb', 'cc'])` 也可以是list等序列
- `secrets.token_bytes(12)` 返回n个字节的随机字节串
- `secrets.token_hex(12)`
- `secrets.token_urlsafe()`

## 范例

```python
import string
import secrets

ab = string.ascii_letters + string.digits
pwd = ''.join(secrets.choice(ab) for i in range(10))
```
## 参考

