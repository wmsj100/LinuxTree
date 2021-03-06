---
title: JS高级技巧
date: 2016-06-30
tags: [JavaScript,Function]
categories: Dynamic
---

对于对象，JS5新增了几个保护对象的属性

防篡改对象 --  
- `Object.preventExtensions` -- 对象不可被扩展，但是可以删除或修改已有的对象，
- `Object.isExtensible` -- 查看对象是否可扩展，返回布尔值，如果设置了就是`Object.preventExtensions`就返回`false`。

密封对象--
- `Object.seal` -- 对象不可扩展，并且不能删除已有的对象，但是可以修改对象，
- `Object.isSealed` -- 查看对象是否密封

最严格的模式是 -- 冻结模式(Object.freeze)；用于设置库时候使用
-`Object.freeze` -- 对象即不能扩展，也不能删除，同时也不能修改已有的对象。

其实我期望的是成功，而如果失败，我期望的是弹出警告，而不是简单的`console.log`，这样容易被忽略。

---

### 高级定时器

大多数人任务JS的定时器就是一个线程，其实JS是运行于单线程的环境中的，但定时器仅仅是计划在未来的某个时间执行。执行时机是不能保证的，因为在页面的生命周期中，不同时间可能有其它代码在控制JS进程，
在页面下载完成后，代码运行，事件处理程序，ajax回调函数都必须使用同样的线程进行处理。
而浏览器就是对事件进行排序，指派某个事件在某个时间点放入进程执行。

在JS中没有任何代码是立即执行的，但一旦进程空闲，则尽快执行。

定时器对队列的工作方式是，指定一段时间后把事件推入进程，但不表示推入后会立即执行，除非前面没有事件执行和等待。

定时器的关键之处在于设置停止条件，否则就会是死循环。

对于实时操作，`onresize, onscroll`等操作，使用节流操作`throttle`,`throttle`的原理就是先清除计时器，然后创建一个延迟100ms执行`method`方法。每次都会先清除，100ms内的所有操作只会变为一次操作

对于长时间的循环操作，使用模块分割技术`chunk`，`chunk`原理是利用`setTimeout`把要执行的`data`通过`shift`导出`item`，然后执行，并设置一个`100ms`的延时，在这段时间内可以执行其它代码，`100ms`之后会检测`data.length>0`，成立则再次执行一次，。。。。

---

### 自定义事件

事件是JS与浏览器交互的主要操作。
鼠标事件有9个 -- `mouseover, mouseout, mouseenter, mouseleave, mouseup, mousedown, click, dbclick, mousemove`.
键盘事件有3个 -- `keyup, keydown, keypress`.

对象可以发布事件，事件只能依托于对象创建。

事件最常见的是与`DOM`进行交互操作。

事件也可以用于非`DOM`中，---自定义事件

如果直接调用一个不存在的变量，则会弹出警告，但是使用`typeof e`就不会弹出警告，而是会返回`undefined`;

函数的原型`prototype`不要放到函数里面，因为如果是在里面，那么在里面的函数原型上面绑定的值只有函数运行时候才会显示，而且如果是在函数内容重写了`prototype`，那么构造函数创建的值就不会继承函数的原型了。而且这样就会有俩个原型，而且都可以访问到。

自定义事件和通过继承链创建的函数比较的优势是什么。自定义事情其实是模仿JS的事件流程，有一个事件执行列表，可以对一个类型`message`绑定多个函数，然后按照在列表的顺序执行。
自定义事件用于针对复杂情况，什么是复杂情况，就针对刚刚的那个实例，

其实自定义的厉害之处就在于它那个事件列表`handlers`。所以只要获取了那个，就可以很分别的绑定自定义函数。

就像我刚刚封装的函数`isEqualCount` -- 本来是预期传入3个参数，然后自动的判断是什么类型，`args`，`val`，还可以同时判断这俩个值，但是发现分开其实效果是一样的，而且代码会简单很多，如果合并，代码会有大量重复，而这种重复又是很难清除的。

关于`event`,

对于变量有最小路径概念，那么对于函数库的引用也是，把库直接保存到局部变量中，