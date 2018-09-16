---
title: jQuery停止动画和判断是否处于动画状态
date: 2016-04-26
tags: [jQuery,动画]
categories: Dynamic
---

# jQuery停止动画和判断是否处于动画状态

- [www.tuicool.com](http://getpocket.com/redirect?url=http%3A%2F%2Fwww.tuicool.com%2Farticles%2FvQ7nIfI)
- [查看原始文档](http://getpocket.com/redirect?url=http%3A%2F%2Fwww.tuicool.com%2Farticles%2FvQ7nIfI)
- 四月 15日, 2016
- [动画](chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/a/queue/grid/%E5%8A%A8%E7%94%BB)

#### 停止元素的动画

停止所有在指定元素上正在运行的动画。

很多时候需要停止匹配元素正在进行的动画，如果需要在某处停止动画，需要使用stop()方法。stop()方法的语法缩构为：

```
stop([clearQueue], [gotoEnd])

```

参数clearQHCHC和gotoEnd都是可选的参数，为Boolean值(ture或flase)。

clearQueue如果设置成true，则清空队列，可以立即结束动画。

gotoEnd让当前正在执行的动画立即完成，并且重设show和hide的原始样式，调用回调函数等。

如果接使用stop()方法，经常会遇到这种情况．在为某个元索绑定hover事件之后，用户把光标移入元素时会触发动画效果，而当这个动画还没结束时，用户就将光标移出这个元素了，那么光标移出的动画效果将会被放进队列之中，等待光标移入的动画结束后再执行。因此如果光标移入移出过快就会导致动画效果与光标的动作不一致。

此时只要让光标的移入、移出动作之前加入stop()方法，就能解决这个问题。stop()方法会结束当前在进行的动l画，并立即执行队列中个动画。

#### 判断元素是否处于动画状态

在使用animate()方法的时候，要避免动画积累而导致的动画与用户的行为不一致。当用户快速在某个元素执行animate()动画时，就会出现动画积累。解决方法足判断元素是否正处于动画状态，如果元素不处于动画状态，才为元素添加新的动画，否则不添加。代码如下：

```
if($(element).is(":animated")){    //判断元素是否正处于动画状态
//如果当前没有进行动画，则添加新动画
}

```

这个判断方法在animate()动画中经常被用到，需要特别注意。

