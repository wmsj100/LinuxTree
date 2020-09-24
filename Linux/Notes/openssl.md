---
title: openssl
date: 2020-09-19 17:08:28
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# openssl

## 概要

- 这个是用于对数据加密的,多用于http加密为https

## 制作ssl证书

- 可以通过申请公共的证书,也可以制作自签名的证书

## ssl配置文件

```ssl.conf
[req]
prompt = no
default_md = sha256
default_bits = 2048
distinguished_name = dn
x509_extensions = v3_req

[dn]
C = CH
ST = China
L = XIAN
O = wmsj100 Inc.
OU = IT Department
emailAddress = wmsj100@hotmail.com
CN = wmsj100.com

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = *.localhost
DNS.2 = localhost
DNS.3 = nginx
IP.1 = 192.168.2.100
IP.2 = 111.229.241.222
```

## 生成证书

- `openssl req -new -x509 -keyout cakey.key -out cacert.crt -config ssl.conf -days 365`
- `openssl req -new -x509 -newkey rsa:4096 -keyout cakey.key -out cacert.crt -config openssl.cnf -days 365`
- `openssl req -x509 -new -nodes -sha256 -utf8 -days 3650 -newkey rsa:2048 -keyout server.key -out server.crt -config ssl.conf`
- 通过上面的命令可以生成一个有效期365天的证书,
- 执行命令期间需要输入证书的秘密

## 参考

- [openssl](https://medium.com/@charming_rust_oyster_221/flask-%E9%85%8D%E7%BD%AE-https-%E7%B6%B2%E7%AB%99-ssl-%E5%AE%89%E5%85%A8%E8%AA%8D%E8%AD%89-36dfeb609fa8)
