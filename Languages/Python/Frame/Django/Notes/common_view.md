---
title: 通用视图
date: 2020-02-22 22:55:50
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# 通用视图

## 概要

- 通用视图将常见的模式抽象化，可以使你在编写应用时甚至不需要编写Python代码

## 场景

- 通常一些视图反映基本的web开发中的一个常见情况：根据URL中的参数从数据库中获取数据、载入模板文件然后返回渲染后的模板。
- 由于这种情况特别常见，Django提供一种快捷方式，叫做"通用视图"系统

- 一般来说，当编写一个Django应用时，首先应该评估一下通用视图是否可以解决，

## 解释

- 每个通用视图都需要指导它将作用于那个模型，这有model属性提供
- `DetailView`期望从URL中捕获pk主键值，所以需要把通用视图中的`question_id`改为`pk`
- 通常情况下，通用视图`DetailView`使用一个`app_name/model_name_detail.html`的模板。
- 在我们的例子中，它将使用`polls/question_detail.html
- `template_name`属性用来告诉Django使用一个指定的模板名字，而不是默认生成的名字。
- `ListView`使用一个`app_name/model_name_list.html`
- 

## 范例

```urls.py
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

```views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'last_questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```
## 参考

- [Django通用视图](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial04/)
