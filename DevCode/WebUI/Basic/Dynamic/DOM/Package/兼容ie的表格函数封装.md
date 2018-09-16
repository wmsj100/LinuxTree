---
title: 兼容ie的表格函数封装
date: 2016-06-23
tags: [DOM,Package,Function]
categories: Dynamic
---

`ie9`不支持`table.createTBody`,所以需要使用传统的创建`tbody`的方法。

未封装的写法

```javascript
    var table = document.createElement("table"),
        tbody;
    table.border = 1;
    table.width = "100%";
    try {
        tbody = table.createTBody();
    } catch (ex) {
        tbody = document.createElement("tbody");
        table.appendChild(tbody);
    }
    tbody.insertRow(0);
    tbody.rows[0].insertCell(0);
    tbody.rows[0].insertCell(1);
    tbody.rows[0].cells[0].innerText = "Cell 1,1";
    tbody.rows[0].cells[1].innerText = "Cell 2,1";
    tbody.insertRow(1);
    tbody.rows[1].insertCell(0);
    tbody.rows[1].insertCell(1);
    tbody.rows[1].cells[0].innerText = "Cell 1,2";
    tbody.rows[1].cells[1].innerText = "Cell 2,2";
    document.body.appendChild(table);
```

封装好的函数写法；

```javascript
    var arr = [
        ["Cell 1,1", "Cell 2,1"],
        ["Cell 1,2", "Cell 2,2"]
    ];

    function createTable(arr) {
        var table = document.createElement("table"),
            tbody,
            rowLen,
            colLen,
            i,
            j;
        table.border = 1;
        table.width = "100%";   //记得上引号。
        try {
            tbody = table.createTBody();
        } catch (ex) {
            tbody = document.createElement("tbody");
            table.appendChild(tbody);
        }
        for (i = 0, rowLen = arr.length; i < rowLen; i++) {
            tbody.insertRow(i);
            for (j = 0, colLen = arr[i].length; j < colLen; j++) {
                tbody.rows[i].insertCell(j);
                tbody.rows[i].cells[j].innerText = arr[i][j];
            }
        }
        document.body.appendChild(table);
    }
    createTable(arr);
```

