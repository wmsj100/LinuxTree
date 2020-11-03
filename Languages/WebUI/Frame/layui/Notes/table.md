---
title: table
date: 2020-07-23 10:20:45
modify: 2020-11-03 11:40:01  
tags: [Notes]
categories: layui
author: wmsj100
email: wmsj100@hotmail.com
---

# table

## 概要

- 如果表格只显示sucess，msg的值，很可能是因为没有配置response

## 复选框

- 对于复选框，如果要格式化数据，需要定义parseData中定义，因为它可以获取到数值，response只是定义返回数据格式。
- `item.LAY_CHECKED = true;` 设置每一条数据的该参数可以让checkbox处于checked状态

## 代码

```html
<table id="oracle_table" class="layui-hide"></table>
<script>
layui.use(['table', 'element', 'layer', 'form'], function(){
	var layer = layui.layer,
		table = layui.table,
		form = layui.form;

	table.render({
		elem: '#oracle_table',
		url: '/oracle/user/',
		cols: [[
//			{ field: 'id', title: 'ID'},
			{ field: 'user', title: '用户名', width: 85},
			{ field: 'host', title: '主机IP', width: 85},
			{ field: 'orcl', title: 'Oracle服务名称'},
			{ field: 'port', title: '端口', width: 80},
			{ field: 'password', title: '密码'},
			{ field: 'is_dba', title: 'SYSDBA', width: 80},
			{ field: 'target_users', title: '查询用户'},
			{ field: 'date', title: '日期'},
		]],
		page: true,
		response: {
			statusName: 'code',
			statusCode: 200
		}
	});
});
</script>
```

## 参考

