---
title: 通过DOM操作来创建表格
date: 2016-05-07
tags: [DOM,函数,封装,HTML]
categories: Dynamic
---

要创建的表格的html代码如下

```html
<table border="1" width="100%">
	<tbody>
		<tr>
			<td>Cell 1,1</td>
			<td>Cell 2,1</td>
		</tr>
		<tr>
			<td>Cell 1,2</td>
			<td>Cell 2,2</td>
		</tr>
	</tbody>
</table>
```

最基本的DOM创建表单

```javascript
var wrap = document.createDocumentFragment();
var table = document.createElement("table");
// table.setAttribute("border", "1");
// table.setAttribute("width", "100%");
table.border = 1;
table.width = "100%";
wrap.appendChild(table);
var tbody = document.createElement("tbody");
table.appendChild(tbody);
var tr_1 = document.createElement("tr");
tbody.appendChild(tr_1);
var td1_1 = document.createElement("td");
td1_1.innerText = "Cell 1,1";
var td2_1 = td1_1.cloneNode(true);
td2_1.innerText = "Cell 2,1";
tr_1.appendChild(td1_1);
tr_1.appendChild(td2_1);
var tr_2 = tr_1.cloneNode(true);
tr_2.childNodes[0].innerText = "Cell 1,2";
tr_2.childNodes[1].innerText = "Cell 2,2";
tbody.appendChild(tr_2);

document.body.appendChild(wrap);
```

高级的DOM标准创建表格的方法：

```javascript
var table = document.createElement("table");
table.border = 1;
table.width = "100%";
var tbody = document.createElement("tbody");
table.appendChild(tbody);
//创建第一行
tbody.insertRow(0);
tbody.rows[0].insertCell(0);
tbody.rows[0].cells[0].appendChild(document.createTextNode("Cell 1,1"));
tbody.rows[0].insertCell(1);
tbody.rows[0].cells[1].appendChild(document.createTextNode("Cell 2,1"));
//创建第二行
tbody.insertRow(1);
tbody.rows[1].insertCell(0);
tbody.rows[1].cells[0].appendChild(document.createTextNode("Cell 1,2"));
tbody.rows[1].insertCell(1);
tbody.rows[1].cells[1].appendChild(document.createTextNode("Cell 2,2"));
document.body.appendChild(table);
```

高级DOM方法简化版

```javascript
var table = document.createElement("table");
table.border = 1;
table.width = "100%";
var tbody = document.createElement("tbody");
table.appendChild(tbody);
tbody.insertRow(0);
tbody.rows[0].insertCell(0);
tbody.rows[0].cells[0].innerText = "Cell 1,1";
tbody.rows[0].insertCell(1);
tbody.rows[0].cells[1].innerText = "Cell 2,1";
tbody.insertRow(1);
tbody.rows[1].insertCell(0);
tbody.rows[1].cells[0].innerText = "Cell 1,2";
tbody.rows[1].insertCell(1);
tbody.rows[1].cells[1].innerText = "Cell 2,2";
document.body.appendChild(table);
```



