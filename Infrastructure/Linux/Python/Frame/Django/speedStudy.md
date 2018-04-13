---
title: Django速度
date: 2018-04-13 18:38:02 Fri
modify: 2018-04-13 18:38:02 Fri
tag: [Django]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- request 是一个HttpRequest对象，每一个视图总是以一个HttpRequest对象作为第一个参数
- offset 是从匹配的URL提取出来的，

## 模板系统
- {{ person_name }} 变量
- {% for item in item_list %}  模板标签   这是一个for标签
- 一旦创建了一个Template对象，可以用context来传递数据，
- 调用template对象的render（）方法来传递context来填充模板
- 一个模板渲染一次，可以重复调用

- 当模板系统在变量中遇到点时解析顺序：
  - 字典类型 foo["bar"]
  - 属性查找 foo.bar
  - 方法调用 foo.bar()
  - 列表类型 foo[bar]

- 一个模板的变量值不存在，模板系统会把它展示为空字符串

- 传递一个完全填充的字典给Context初始化，但是初始化之后，还可以使用标准的python字典语法向上下文对象添加或删除条目

- 用{% endif %} 关闭每一个{% if %}标签
- {% for %}允许在一个序列上进行迭代
- {% for item in items reversed %} 对列表进行反向迭代 
- {% endfor %}
- 在for循环过程中会产生一个变量
  - forloop.first 第一次执行，布尔值 True
  - forloop.counter总是一个表示当前循环执行次数的计数器，从1开始
  - forloop.revcounter 剩余循环整数
  - forloop.last 最后一次执行 True

- ifequal / ifnotequal ， 支持else分支
- {% ifequal vairable 1 %} 参数只能是模板变量、字符串、整数、小数

```html
  {% for item in courseList %}
  {% ifequal item "HTML" %}
  <p style="color: cadetblue">{{ item }}</p>
  {% else %}
  <p style="color:lightsalmon">{{ item }}</p>
  {% endifequal %}
  {% endfor %}
```

- 对于字典的遍历方法
- `for key, value in objInfo.items`
- 意思是把每个对象内的key值对当作一个list看待

```html
  <p>{{ objInfo.name }} 's old is {{ objInfo.age }} 's address is {{ objInfo.city }}</p>
  {% for key,value in objInfo.items %}
  <p>{{ key }} : {{ value }}</p>
  {% endfor %}
```

- 对于循环可以进行判断，
```html
  {% for item in numList %}
  {% if forloop.first %}
  <hr/><b>{{ item }},</b>
  {% elif forloop.last %}
  <b>{{ item }}</b><hr/>
  {% else %}
  <span>{{ item }},</span>
  {% endif %}
  {% endfor %}
```
- {# This is a comment #} 这是注释模板代码，这样的注释必须是单行的
- {% comment %} ... {% endcomment %} 中间的内容都不会渲染
- 正常的大小比较都可以使用 `{% elif item <= 5 %}`
- `{% if 1 in cList %}ok{% endif %}`
- `{% if 7 not in cList %}fail{% endif %}`

过滤器
 - 过滤器采用管道字符 {{ name | lower }}
- date 格式化时间
- length 返回变量的长度

 Python 要求单元素元组中必须使用逗号，以此消除与圆括号表达式之间的歧义
- 也就是说，对于对象或者字典，最后一个值后面必须加逗号


## 模板使用
### 模板加载
- TEMPLATE_DIRS 设置模板的目录
- `os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),`
- `render_to_response`

- locals()  返回的字典对所有局部变量的名称与值进行映射
- `return render_to_response('test/current_datetime.html', {'current_datetime': now})`
- 模板在子目录的调用方式

- include 模板标签
- 允许在模板中包含其它模板的内容， {% include "msg01.html" %}，插入的模板变量的值还是在调用的时候就写入

## 模板继承
- {% block %} 该标签告诉模板引擎，子模板可以重载这些部分，

### 模板目录

- Model 代表数据存取层，View 代表的是系统中选择显示什么和怎么显示的部分，Controller 指的是系统中根据用户输入并视需要访问模型，以决定使用哪个视图的那部分。
  - M ，数据存取部分，由 django 数据库层处理
  - V ，选择显示哪些数据要显示以及怎样显示的部分，由视图和模板处理。
  - C ，根据用户输入委派视图的部分，由 Django 框架根据 URLconf 设置，对给定 URL 调用适当的Python 函
  - M 代表模型（Model），即数据存取层。 该层处理与数据相关的所有事务： 如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。
  - T 代表模板(Template)，即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。
  - V 代表视图（View），即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看作模型与模板之间的桥梁。

## 数据库
- python manage.py makemigrations 创建数据库
- python manage.py makemigrations
- python manage.py migrate 
- 上面俩条命令会自动创建model中的表
- python manage.py flush 清空数据库
- python manage.py dumpdata appname > appname.json 导出数据
- python manage.py loaddata appname.json 导入数据
- python manage.py runserver 9900 用127.0.0.1：9900端口启动服务
- python manage.py createsuperuser 创建超级管理员
- python manage.py dbshell 进入数据库操作界面
- python manage.py shell 进入django的shell界面

## 注意
- 新创建的app必须添加到 setting 中的 INSTALL_APPS中，否则该app下的templates, static文件就无法加载
- a = request.GET['a'] 从url获取请求参数a
- url中用括号括起来表示⽤括号括起来的意思是保存为⼀个⼦组
- 创建一个app后，`from learn import views as learn_views`，这样就可以可以导入

## 链接
- url(r'^add/(\d+)/(\d+)/$', add, name='add') 通过name命名一个url的名称，这个名称唯一，且设定好就不要改动，调用的时候用下面的方式
- `<a href="{% url 'add' 4 5 %}">Link</a>` 这样就会按照add的路径格式进行跳转，传入的参数就是 4 5
- 建议在每一个app下面再创建一个和app同名的文件夹，然后把所有的模板放到下面，这样调用的时候就不用担心模板文件同名的问题了
- {% extends "learn/base.html" %} 调用在app learn下面的base.html

## APP
- 关于app，所有的url和模板都应该在app内部，不应该都写在总urls.py中，所以通过下面这个就可以
- url(r'^learn/', include('learn.urls')),
- 然后在learn内创建一个urls.py 
- url(r'^test/test1/$', learn_views.test1, name='learn_test1'), 这样就定义了一个url，通过访问 /learn/test/test1就可以
