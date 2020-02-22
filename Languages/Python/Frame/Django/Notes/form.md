---
title: 表单
date: 2018-05-01 16:30:52 Tue
modify: 2018-05-01 16:30:52 Tue
tag: [form]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 表单模块

## 概述

- 对于表单，如果是修改数据库内容，`method="post"`
- 为了防止跨站点请求伪造，使用`{% csrf_token %}`模板标签
- `request.POST`是一个类似于字典的对象，可以通过关键字获取提交的数据，返回一个字符串
- `request.GET`用来访问GET数据

## 一个form范例

```python
<form action="{% url 'polls:vote' question.id %}" method="post">
	{% csrf_token %}
	{% for choice in question.choice_set.all %}
	<input type="radio" name="choice" id="choice{{forloop.counter }}" value="{{choice.id }}">
	<label for="choice{{forloop.counter}}">{{choice.choice_text}}</label>
	<br>
	{% endfor %}
	<input type="submit" value="Vote">
</form>
```
- `{% csrf_token %}` 可以防止跨域攻击
- `forloop.counter` 指示for标签循环了多少次

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
    return HttpResponse("You're voting on question {}.".format(question_id))
```
- reverse: 用于避免了在视图函数中硬编码URL。
- 一个好的页面反馈是在post提交成功之后要执行重定向，所以建议在每个post后都添加一个`HttpResponseRedirect`
