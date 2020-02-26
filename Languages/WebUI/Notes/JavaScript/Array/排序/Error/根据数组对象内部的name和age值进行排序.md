---
title: 根据数组对象内部的"name"和"age"值进行排序
date: 2016-04-30
tags: [Array,排序,Function,算法]
categories: Dynamic
---

```javascript
    var arr2 = [{
        name: "Nicholas",
        age: 20
    }, {
        name: "wmsj",
        age: 10
    }];
    function compareFnc(prop){

        return function(obj1,obj2){
            var val1 = obj1[prop];
            var val2 = obj2[prop];

            if(val1 < val2){
                return 1;
            }else if(val1 > val2){
                return -1;
            }else{
                return 0;
            }
        }
    }

    var b = arr2.sort(compareFnc("name"));
    var c = arr2.sort(compareFnc("age"));
```

不管我怎么弄,所有的`b,c,d,e`都不是我的预期,因为不论我怎么弄,`b` = `c`,不管我怎么排序都是这样的.
忽然我想到,因为`arr2`是一个数组,虽然`var b = arr2.sort(..)`;但其实`b`引用的还是内存中`arr2`的指针,然后又进行了`var c = arr2.sort(..)`;这个也是一样的,创建了`c`,然后c复制了`arr2`的指针,因为内存中只有一个`arr2`,而现在变量`b`和`c`都指向数组`arr2`,那么肯定结果就是`b` == `c` == `arr`的最后的排序算法,也就是说,`b` === `c`,因为引用的是一个对象.

```javascript
    var arr2 = [{
        name: "Nicholas",
        age: 20
    }, {
        name: "wmsj",
        age: 10
    }];

    function compareFnc(prop) {

        return function(obj1, obj2) {
            var val1 = obj1[prop];
            var val2 = obj2[prop];

            if (val1 < val2) {
                return -1;
            } else if (val1 > val2) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    var b = arr2.sort(compareFnc("age"));
    arr2.pop();
    var c = arr2.sort(compareFnc("age"));
    b === c;    //true
```

上面这个虽然是先求的`b`,然后删除的数组,然后在计算`c`,但最后还是`b` === `c`,
