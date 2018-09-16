---
title: 关于submit重复提交的问题
date: 2016-06-26
tags: [DOM,Form]
categories: Dynamic
---

https://segmentfault.com/a/1190000000461339
- 对于表单验证，首先可以监听哪个表单，如果是为了效率最好，那么就在`document`上面绑定一个事件，然后判断触发的目标是哪个表单，然后通过表单查询到`submit`按钮，然后禁用这个按钮。但是整个过程监听的是`submit`事件。

- 对于表单需要知道的一点是，当提交`submit`时候会刷新页面，而我设置的按钮`btn.disabled = true`这个状态被刷新之后，就回到了初始状态，而初始状态，`btn.disabled = false`。

- 其实我之前的之所以可以避免重复点击，我感觉是因为页面没有提交，也就是没有触发刷新，那个时候没有碰到，或者是没有对这个问题深入。

- 如果链接没有变化，那么页面是不会刷新的，所以才会把`btn.disabled = true`，这个状态保存下来。这不是因为成功了，而是因为链接没有变化，页面没有刷新而已。

- 如果是这样的话，那么避免重复提交的清空应该是什么，如果是直接这样的提交过程是无法避免的，除非是通过`ajax`触发的提交，因为是局部刷新，所以才可以把按钮的禁止状态保存下来。

下面这个函数是通过`body`监听`form`事件，
这个问题以解决并且已经封装 -- wmsj.modelUtil.dom.preventRepeatSubmit();

```javascript
function listenForm(){
        wmsj.eventUtil.addHandler(document,"submit", function(event){
            event = wmsj.eventUtil.getEvent(event);
            var target = wmsj.eventUtil.getTarget(event);
            var btn = target.elements["submit"];    
            // 所有的submit按钮都添加name="submit"
            btn.disabled = true;
            console.log(btn)
        })
    }
```

至于使用`ajax`的方法，我暂时也不想这样测试了。等我看完表单的章节最后在试着用ajax解决一下。

解决重复提交的问题大致可以分为俩种,一种是简单的通过内嵌一个`iframe`的方式解决,hack意味十足，https://segmentfault.com/a/1190000000461339,我封装的函数就是这个思路.

第二种方法就是通过`jQuery`封装的关于表单的方法.那个以后碰到了再说吧.