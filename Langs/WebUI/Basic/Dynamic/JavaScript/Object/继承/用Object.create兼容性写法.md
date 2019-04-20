---
title: 用Object.create来创建对象，及其兼容性写法
date: 2016-05-28
tags: [继承]
categories: Dynamic
---

mdn官方的`Object.create`兼容模式写法
```javascript
if (typeof Object.create != 'function') {
  // Production steps of ECMA-262, Edition 5, 15.2.3.5
  // Reference: http://es5.github.io/#x15.2.3.5
  Object.create = (function() {
    //为了节省内存，使用一个共享的构造器
    function Temp() {}

    // 使用 Object.prototype.hasOwnProperty 更安全的引用 
    var hasOwn = Object.prototype.hasOwnProperty;

    return function (O) {
      // 1. 如果 O 不是 Object 或 null，抛出一个 TypeError 异常。
      if (typeof O != 'object') {
        throw TypeError('Object prototype may only be an Object or null');
      }

      // 2. 使创建的一个新的对象为 obj ，就和通过
      //    new Object() 表达式创建一个新对象一样，
      //    Object是标准内置的构造器名
      // 3. 设置 obj 的内部属性 [[Prototype]] 为 O。
      Temp.prototype = O;
      var obj = new Temp();
      Temp.prototype = null; // 不要保持一个 O 的杂散引用（a stray reference）...

      // 4. 如果存在参数 Properties ，而不是 undefined ，
      //    那么就把参数的自身属性添加到 obj 上，就像调用
      //    携带obj ，Properties两个参数的标准内置函数
      //    Object.defineProperties() 一样。
      if (arguments.length > 1) {
        // Object.defineProperties does ToObject on its first argument.
        var Properties = Object(arguments[1]);
        for (var prop in Properties) {
          if (hasOwn.call(Properties, prop)) {
            obj[prop] = Properties[prop];
          }
        }
      }

      // 5. 返回 obj
      return obj;
    };
  })();
}
```


我自己的理解，基本都是照抄
```javascript
Object.create = null;
if (typeof Object.create != "function") {
    Object.create = (function() {
        function temp() {};
        var hasOwn = Object.prototype.hasOwnProperty;
        return function(O) {
            if (typeof O != "object") {
                throw TypeError("必须是对象或者null");
            }
            temp.prototype = O;
            var obj = new temp();
            temp.prototype = null;
            if (arguments.length > 1) {
                var Properties = arguments[1];
                for (var prop in Properties) {
                    if (hasOwn.call(Properties, prop)) { //判断prop是不是Properties的私有属性
                        obj[prop] = Properties[prop];
                    }
                }
            }
            console.log(arguments)
            return obj;
        }
    })()
}

function a(name, sex) {
    this.name = name;
    this.sex = sex;
}

a.prototype.printName = function() {
    console.log(this.name);
}
var b = new a("wmsj", 10)
var c = Object.create(b, {
    like: {
        value: "eat"
    }
});
```

我自己写的`Object.create`的模仿兼容函数`create`；还是自己写的好用

```javascript
Object.create = null;

function create(obj) {
  if (typeof obj != "object") {
    throw TypeError("输入值必须为对象！")
  }
  var proto = new Object();
  if (typeof Object.create === "function") {
    proto = Object.create(obj);
  } else {
    function temp() {};
    temp.prototype = obj;
    proto = new temp();
    temp.prototype = null; //清除不用的引用
  }
  if (arguments.length > 1) {
    var Properties = arguments[1];
    var hasOwn = Object.prototype.hasOwnProperty;
    for (var key in Properties) {
      if (hasOwn.call(Properties, key)) { //这个hasOwn用的特别的巧妙
        proto[key] = Properties[key]["value"];
      }
    }
  }
  return proto;
}
```

//2016-06-14 自己封装的函数
```javascript
function p(name, age) {
    this.name = name;
    this.age = age;
  };
  p.prototype.say = function() {
    return this.name;
  }

  Object.create = null;
  if (typeof Object.create !== "function") {
    Object.create = (function() {
      function temp() {};
      return function(args) {
        if (typeof args !== "object") {
          return;
        } else {
          temp.prototype = args;
          var obj = new temp();
          temp.prototype = null;
          var hasOwn = Object.hasOwnProperty;
          if (arguments.length > 1) {
            var arr = arguments[1];
            for (var i in arr) {
              if (hasOwn.call(arr, i)) {
                obj[i] = arr[i];
              }
            }
          }
          return obj;
        }
      }
    })();
  }

  function Person(name, age, male) {

    p.apply(this, [name, age]);
    this.male = male;
  }
  Person.prototype = Object.create(p.prototype, {
    class: {
      value: "eight"
    }
  });

  var a = new Person("wmsj", 10, "male");
  a; //{name: "wmsj", age: 10, male: "male"}
  a.class; //"eight";
```



网络大神写的，看不懂

http://www.cnblogs.com/lingtong/p/4081931.html
```javascript
    function inherit(p){
  if(p==null){
    throw TypeError();
  }
  if(Object.create){
    return Object.create(p);
  }
  var t=typeof p;
  if(t!=='object'&&t!=='function'){
    throw TypeError();
  }
  function f(){};
  f.prototype=p;
  return new f();
}

function range(from,to){
  var r=inherit(range.methods);
  r.from=from;
  r.to=to;
  return r;
}

range.methods={
  includes:function(x){
    return this.from<=x&&x<=this.to;
  },
  foreach:function(f){
    for(var x=Math.ceil(this.from);x<=this.to;x++) f(x);
  },
  toString:function(){
    return "("+this.from+'...'+this.to+')';
  }
};

var r=range(1,3);

r.includes(2);
r.foreach(console.log);
r.toString();
```
