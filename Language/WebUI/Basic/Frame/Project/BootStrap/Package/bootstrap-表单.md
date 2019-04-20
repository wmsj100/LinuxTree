---
title: bootstrap-表单
date: 2016-05-09
tags: [框架,BootStrap]
categories: Frame
---

1. 表单提示文字和输入框--2列布局

   ```html
   <form role="form" class="form-horizontal">
   	<div class="form-group">
   		<label class="col-sm-2 control-label">name</label>
   		<div class="col-sm-10">
   			<p class="form-control-static">example</p>
   		</div>
   	</div>
   	<div class="form-group">
   		<label for="age1" class="col-sm-2 control-label">age</label>
   		<div class="col-sm-10">
   			<input type="text" class="form-control" id="age1">
   		</div>
   	</div>
   </form>
   ```

   ​