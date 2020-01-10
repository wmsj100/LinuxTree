---
title: wsgi
date: 2020-01-10 10:38:44
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# wsgi

## 概要

- `Python Web Server Gateway Interface` Web服务器网关接口，是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
- Python应用需要专门的wsgi服务器来管理接口，
- wsgi定义了web服务器如何与python应用程序进行交互，使得用python写的web应用程序可以和web服务器对接起来。

## 为什么需要WSGI规范

- web部署的方案上，有一个方案是目前应用最广泛的
	- 首先部署一个web服务器用来处理HTTP协议层面相关的事情，
	- 然后部署一个用各种语言编写的应用程序，这个应用程序会从web服务器接收客户端的请求，处理完成后，再返回给web服务器，最后由web服务器返回给客户端。
- 如果要采用这种方案，web服务器和应用程序之间就要知道如何进行交互。
- 为了定义web服务器和应用程序的交互过程，就形成了很多不同的规范。

## WSGI如何工作

- WSGI相当于是web服务器和python应用程序直接的桥梁，它存在俩个目的
	- 让web服务器知道如何调用python程序，并且把用户的请求告诉应用程序
	- 让python的应用程序知道用户的具体请求是什么，以及如何返回结果给web服务器

## WSGI中的角色

- 再wsgi中定义了俩个角色，web服务器端称为server/gateway,应用程序端称为application或者framework，(因为WSGI的应用程序端的规范一般都是由具体的框架来实现的)
- server端会先收到用户的请求，然后根据规范的要求调用application端，
- 每个application的入口只有一个，也就是所有的客户端请求都是同一个入口进入到应用程序。
- server端需要知道去哪里找application的入口，这个需要再server端指定一个python的模块，也就是python应用中的一个文件，

## 服务器实现

- 因为WSGI本身比较复杂，一般常用的服务器比如apache/nginx都不会内置wsgi，而是通过扩展来完成的。比如apache通过`mod_wsgi`来支持wsgi。nginx通过proxy的方式把协议封装好，发送给应用服务器(uWSGI),应用服务器会实现wsgi的服务端/进程管理以及对application的调用。

## 参考

- [wsgi讲解](https://www.jianshu.com/p/c66d3adeaaed)
