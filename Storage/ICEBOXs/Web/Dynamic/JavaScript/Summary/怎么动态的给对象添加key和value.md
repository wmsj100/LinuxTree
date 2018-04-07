制造对象的机制有几种：
- var a = {} // 通过对象字面量直接创建对象
- var a = new Object() // 通过构造函数的方式创建对象
- var a = JSON.parse(str) // 通过JSON字符串的方法创建对象
- var a = eval(objstr) // 通过eval的方式创建对象
- var a = {[key]: value} // 这种方法在低版本浏览器会出现报错，比如火狐32或者谷歌43版本的浏览器就会出现报错，不识别这种赋值方式。

通过上面的几种方式可以直接筛选出只有后面的俩种方式可以满足条件

- eval 方法
```js
var a = "asdf"
var b = 1234
var c = {}
eval("c." + a + "=" + b)
c; // {asdf: 1234}
```
- JSON方法
```js
var a = "asdf"
var b = 1234
var c ="{\"" + a + "\":\"" + b + "\"}"
c = JSON.parse(c) // {asdf: 1234}
```

因为在严格模式下是不允许使用`eval`方法的，所以推荐使用"JSON"方法
