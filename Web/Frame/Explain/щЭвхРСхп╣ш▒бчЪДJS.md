---
title: 面向对象的JS
date: 2016-06-23
tags: [JavaScript]
categories: Frame
---

多态背后的思想是--“做什么？”，“谁去做以及怎么做？”分离开来。

仅仅增加代码就可以增加功能，这显然会安全和优雅的多。

```javascript
    function makeSound(animal){
        if(animal instanceof Duck){
            console.log("噶嘎嘎");
        }else if(animal instanceof Chick){
            console.log("咯咯咯");
        }
    }
    function Duck() {};
    function Chick() {};
    makeSound(new Duck());
    makeSound(new Chick());
```

进行多态分离，并增加`Dog`；这样的好处是不会出现特别庞大的代码块，而且增加要比修改容易避免错误。

```javascript
    function makeSound(animal) {
        animal.sound();
    }

    function Duck() {};
    Duck.prototype.sound = function() {
        console.log("噶嘎嘎");
    }

    function Chick() {};
    Chick.prototype.sound = function() {
        console.log("咯咯咯");
    }

    function Dog() {};
    Dog.prototype.sound = function() {
        console.log("汪汪汪");
    }
    makeSound(new Duck());
    makeSound(new Chick());
    makeSound(new Dog());
```

