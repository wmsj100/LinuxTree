---
title: jsonResponse
date: 2020-02-15 12:16:50
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# jsonResponse

## 概要

- django框架现在返回json

## 返回json模板

```python
from django.http import HttpResponse
from .models import Blog
from django.core import serializers

def index(request):
    data = Blog.objects.all()
    json_data = serializers.serialize('json', data)
    return HttpResponse(json_data, content_type='application/json')
```

## 参考

