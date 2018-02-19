---
title: data 存储数据
date: 2016-4-13 00:25:15
tags: [jQuery]
categories: Dynamic
---

`.data()` 方法允许我们在DOM元素上绑定任意类型的数据,避免了循环引用的内存泄漏风险。

.data(key, value)

```html
<!DOCTYPE html>
<html>
<head>
  <style>
  div { color:blue; }
  span { color:red; }
  </style>
  <script src="http://code.jquery.com/jquery-latest.js"></script>
</head>
<body>
  <div>
    The values stored were
    <span></span>
    and
    <span></span>
  </div>
<script>
$("div").data("test", { first: 16, last: "pizza!" });
$("span:first").text($("div").data("test").first);
$("span:last").text($("div").data("test").last);
</script>
 
</body>
</html>
```

example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
  div { margin:5px; background:yellow; }
  button { margin:5px; font-size:14px; }
  p { margin:5px; color:blue; }
  span { color:red; }
  </style>
  <script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
</head>
<body>
  <div>A div</div>
  <button>Get "blah" from the div</button>
  <button>Set "blah" to "hello"</button>
 
  <button>Set "blah" to 86</button>
  <button>Remove "blah" from the div</button>
  <p>The "blah" value of this div is <span>?</span></p>
<script>
$("button").click(function(e) {
  var value;
 
  switch ($("button").index(this)) {
    case 0 :
      value = $("div").data("blah");
      break;
    case 1 :
      $("div").data("blah", "hello");
      value = "Stored!";
      break;
    case 2 :
      $("div").data("blah", 86);
      value = "Stored!";
      break;
    case 3 :
      $("div").removeData("blah");
      value = "Removed!";
      break;
  }
 
  $("span").text("" + value);
});
 
</script>
 
</body>
</html>
```

