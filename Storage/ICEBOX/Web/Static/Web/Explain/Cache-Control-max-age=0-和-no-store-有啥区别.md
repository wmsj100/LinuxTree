---
title: Cache-Control: max-age=0 和 no-store 有啥区别？
date: 2016-05-22
tags: [HTTP]
categories: Static
---

max-age=0 和no-store 都是不使用缓存文档，有啥区别呢？是不是在实际使用中都是通用的？                    

max-age指示缓存过期时间，也就是说max-age是会缓存的，只不过值为0时立即过期（下次判断的后重新发起请求）

 no-store指示响应不要被缓存（下次同样的请求在缓存中找不到）

