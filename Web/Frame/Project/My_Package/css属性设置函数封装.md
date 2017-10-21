---
title: css属性设置函数封装
date: 2016-06-03
tags: [JavaScript,Package,Function]
categories: Dynamic
---

```javascript
function nodeProp(node, name, value, value2) {  //node属性封装
        if (name == "className") {
            node.className = value;
        } else if (name == "color") {
            node.style.color = value;
        } else if (name == "backgroundColor") {
            node.style.backgroundColor = value;
        } else if (name == "borderColor") {
            node.style.borderColor = value;
        } else if (name == "borderRadius") {
            node.style.borderRadius = value + "px";
        } else if (name == "border") {
            node.style.border = "solid " + value + "px " + value2;
        } else if (name == "padding") {
            node.style.padding = value + "px " + value2 + "px";
        } else if (name == "margin") {
            node.style.margin = value + "px " + value2 + "px";
        } else if (name == "minHeight") {
            node.style.minHeight = value + "px";
        } else if (name == "minWidth") {
            node.style.minWidth = value + "px";
        } else if (name == "width") {
            node.style.width = value + "px";
        } else if (name == "height") {
            node.style.height = value + "px";
        } else if (name == "position") {
            node.style.position = value;
        } else if (name == "title") {
            node.title = value;
        } else if (name == "innerText") {
            node.innerText = value;
        } else if (name == "href") {
            node.href = value;
        } else if (name == "lineHeight") {
            node.style.lineHeight = value + "px";
        } else if (name == "fontSize") {
            node.style.fontSize = value + "px";
        } else if (name == "fontFamily") {
            node.style.fontFamily = value;
        } else if (name == "marginLeft") {
            node.style.marginLeft = value + "px";
        } else if (name == "textAlign") {
            node.style.textAlign = value;
        } else if (name == "right") {
            node.style.right = value + "px";
        } else if (name == "top") {
            node.style.top = value + "px";
        } else if (name == "verticalAlign") {
            node.style.verticalAlign = value;
        } else if (name == "target") {
            node.style.target = value;
        }
    }
```

因为当条件过多的时候`switch`的性能要比`if-else`的好，所以用`switch`改写如下：

```javascript
    function nodeProp(node, name, value, value2) { //node属性封装
        switch (name) {
            case "className":
                node.className = value;
                break;
            case "color":
                node.style.color = value;
                break;
            case "backgroundColor":
                node.style.backgroundColor = value;
                break;
            case "borderColor":
                node.style.borderColor = value;
                break;
            case "borderRadius":
                node.style.borderRadius = value + "px";
                break;
            case "border":
                node.style.border = "solid " + value + "px " + value2;
                break;
            case "padding":
                node.style.padding = value + "px " + value2 + "px";
                break;
            case "margin":
                node.style.margin = value + "px " + value2 + "px";
                break;
            case "minHeight":
                node.style.minHeight = value + "px";
                break;
            case "minWidth":
                node.style.minWidth = value + "px";
                break;
            case "width":
                node.style.width = value + "px";
                break;
            case "height":
                node.style.height = value + "px";
                break;
            case "position":
                node.style.position = value;
                break;
            case "title":
                node.title = value;
                break;
            case "innerText":
                node.innerText = value;
                break;
            case "href":
                node.href = value;
                break;
            case "lineHeight":
                node.style.lineHeight = value + "px";
                break;
            case "fontSize":
                node.style.fontSize = value + "px";
                break;
            case "fontFamily":
                node.style.fontFamily = value;
                break;
            case "marginLeft":
                node.style.marginLeft = value + "px";
                break;
            case "textAlign":
                node.style.textAlign = value;
                break;
            case "right":
                node.style.right = value + "px";
                break;
            case "top":
                node.style.top = value + "px";
                break;
            case "verticalAlign":
                node.style.verticalAlign = value;
                break;
            case "target":
                node.style.target = value;
                break;
        }
    }
```

