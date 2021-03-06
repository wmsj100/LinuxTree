---
title: this
date: 2016-08-16
tags: [C#]
categories: Language
---

## this关键字

每个对象都有一个指向自己的`this`引用符，一般情况下，在类的内部，你可以直接使用类的成员，也可以通过`this`引用符使用变量。

尤其是在类的内部函数的参数和类的字段重名时候，只能通过`this`来调用类的字段。

```c#
private int year;
    public Time(int year)
    {
        this.year = year;
    }
```

对于上面的代码，如果不使用`this`，那么编译器就会弹出警告，说不能操作同一个变量。

构造函数的参数和类的成员变量重名，因为方法内部的变量会屏蔽掉外部的同名变量，所以为了在方法内部引用类的成员变量，必须用`this`关键字显示的访问类的成员变量。