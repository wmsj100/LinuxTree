---
title: canvas绘图基础解析
date: 2016-06-26
tags: [Canvas]
categories: Dynamic
---

创建一个`canvas`绘图区

```html
<canvas id="drawing" width="200" height="200"></canvas>

<script>
    var a = document.querySelector("#drawing");
    var cont = a.getContext("2d");  // 获取绘图上下文
    a.toDataURL("image/png");       // 导出绘图区
</script>
```

`2d`绘图操作可以细分为描边`strokeStyle`和填充`fillStyle`操作，

- `cont.fileRect(x,y,width,height)` -- 设置填充矩形框
- `cont.strokeRect(x,y,width,height)` -- 设置描边矩形框
- `cont.clearRect(x,y,width,height)` -- 设置清除矩形框

- `ct.font = "bold 14px Arial"`
- `ct.textAlign = "center"`
- `ct.textBaseline = "middle"`
- `ct.fillText("12", 150, 70)`;


