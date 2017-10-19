---
title: do-while循环结束条件
date: 2016-05-27
tags: [Array]
categories: Dynamic
---

`do while`是个循环，好处是先通过`do`执行代码，然后通过`while`进行判断，因为`while`本身就是一个结束判断条件，所以就不用在`do`中给出循环结束条件

```javascript
var i = 0;
    do{
        i++
        console.log(i);
    }while(i<5);
    console.log(i);
```

- `do while`循环会先执行一次，`while`后面的`;`不能省略。

```javascript
var i = 0;
do {
    i++;
} while (i < 3);
console.log(i);
//i只会输出一次，因为在i<3的时候，会进行循环，
//只有i>=3 的时候才会跳出循环，执行后面的console.log语句。
```

- while循环只要条件为真就会一直循环，这是一个死循环，`while(true){}`