---
title: jQuery表单多选框的自动化触发全选按钮
date: 2016-07-06
tags: [jQuery]
categories: Dynamic
---

[效果](http://jsbin.com/zigoruq/2/edit?html,output)
对于自动触发全选按钮的思路有俩个，
1. 判断多选框的数量和已经选中的选项框的数量是否相同，如果相同，则自动勾选全选框，否则取消勾选。
2. 判断多选框中是否有未被选择的框，如果未被选中的框数量为0，则勾选全选框，否则取消勾选。

```html
<form method="post" action="">
   你爱好的运动是？
   <br/>
    <input type="checkbox" name="items" value="足球"/>足球
    <input type="checkbox" name="items" value="篮球"/>篮球
    <input type="checkbox" name="items" value="羽毛球"/>羽毛球
    <input type="checkbox" name="items" value="乒乓球"/>乒乓球
    <input type="checkbox" id="CheckedAll">全选/全不选
   <br/>
    <input type="button" id="send" value="提　交"/>
</form>


<script>
    $("#CheckedAll").click(function() { 
    // 因为其它选项的勾选情况和`CheckAll`是同步的。所以直接让俩者形同就行
        $(":checkbox").prop("checked", this.checked);
    });

    // 判断选中的框数量和总数量是否相同
    function check() {
        var checkLen = $(":checkbox:not(:last):checked").length,
            checkboxLen = $(":checkbox:not(:last)").length;
        console.log(checkboxLen, checkLen);
        if (checkLen === checkboxLen) {
            console.log(1)
            $("#CheckedAll").prop("checked", true);
        } else {
            $("#CheckedAll").prop("checked", false);
        }
    }

    $(":checkbox:not(:last)").click(function() {
        // check();
        checkTag();
    });

    // 判断未被勾选的框数量是否为零，通过标记来获取状态。
    function checkTag() {
        var flag = false;
        var notSelect = $(":checkbox:not(:last)").not(":checked");  
        // 这个链式选择比较强大
        if (!notSelect.length) {
            flag = true;
        }
        console.log(flag)
        $("#CheckedAll").prop("checked", flag);
    }

    $("#send").click(function() {
        var str = "";
        $(":checkbox:checked").each(function() {
            str += $(this).val();
        });
        console.log(str);
    });
</script>
```

