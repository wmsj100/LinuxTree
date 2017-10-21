---
title: extend扩展解析
date: 2016-06-21
tags: [CSS,LESS]
categories: Static
---

- `extend` -- `Less`的一个伪类，扩展的意思，会完全使用它传入的参数的样式,复制参数样式时候执行的是浅复制，即`伪类`样式不会被复制。

```less
h3{
    &:extend(p);
}
p{
    color: red;
    border: solid 1px green;
    &:hover{
        color: #fff;
        background-color: red;
    }
}
```

错误了，它还是可以继续传入第二个参数`all`，表示复制所有的样式，这样即便是`伪类`也会被复制。

```less
h3{
    &:extend(p,all);
    // 扩展".d"的所有实例，比如".x.d"或者".d.x"
}
p{
    color: red;
    border: solid 1px green;
    &:hover{
        color: #fff;
        background-color: red;
    }
}
```

下面这俩个表示方法是一样的。

```less
h3{
    &:extend(p all);
}
h3:extend(p all){};
```

- `extend`可以传入多个对象进行样式复制，每个对象后面也可以继续传入`all`进行深度复制；

```less
h3:extend(.p1 all, .p2 all, .p3 all){

}
.p1{
    color: red;
    &:hover {
        color: #fff;
    }
}
.p2{
    background-color: yellow;
    &:hover {
        background-color: purple;
    }
}
.p3{
    border: solid 1px green;
    &:hover {
        border-color: yellow;
    }
}
```

---

对选择器进行扩展：

- 选择器之后的扩展：

```less
.p1{
    border: solid 1px;
    color: yellow;
    &:hover {
        color: green;
    }
}
h3{
    &:hover:extend(.p1){};
}
```

- 选择器和扩展之间有空格也是允许的

```less
h3{
    &:hover :extend(.p1){};
}
```

`extend`必须位于选择器的最后；`h3 :extend(.p2):hover :extend(.p1 all){}`这是不允许的。

```less
.p1{
    border: solid 1px;
    color: yellow;
    &:hover {
        color: green;
    }
}
.p2{
    color: blue;
    background-color: gray;
}
.p3{
    -webkit-box-shadow: 2px 2px 10px pink;
    box-shadow: 2px 2px 10px pink;
    background-color: pink;
}
<!-- h3 :extend(.p2):hover :extend(.p1 all){} -->
h3{ 
    &:extend(.p2);
    &:hover :extend(.p1, .p3){};
}
```

- `extend`可以识别嵌套选择器

对于命名空间必须使用`class`进行选择

```less
h3 {
    .w1 > .w2;
}
// 如果使用标签名就会出错
h3 {
    p > span;
}
```

- `extend` -- 对象可以进行嵌套，但是嵌套规则是按照`css`编译后的选择器进行的。`h3:extend(p span){}`;

```javascript
p {
    span {
        border: solid 1px;
        color: yellow;

        &:hover {
            color: green;
        }
    }
}
h3:extend(p span all) {
}
```


