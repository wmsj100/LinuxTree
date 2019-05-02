---
title: bootstrap学习笔记
date: 2016-05-08
tags: [BootStrap,框架]
categories: Frame
---

1. 珊格栅格系统的构架

   1. 内容必须被`<div class="container">...</div>` 包裹
   2. 显示的列必须被行`<div class="row">...</div>` 包裹
   3. 行可以通过class进行控制位置`<div class="col-md-2">..</div>` 

   ```html
   <div class="container">
     <div class="row">
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     <div class="col-md-1">.col-md-1</div>
     </div>
   </div>
   ```

   ​