---
title: 模板语法
date: 2018-07-04 16:28:00
modify: 2018-07-05 15:09:00
tag: [template]
categories: Angular2
auth: wmsj100
email: wmsj100@hotmail.com
---

# 模板语法
> 写过`jQuery`才可以理解`Angular2`的伟大，因为避免了麻烦的`DOM`操作

## 概述
- `Angular2`是`单向数据流`策略，这个`AngularJS`的`双向数据绑定`不一样，而且去除了`脏检查`的机制，更清晰明了。
---
- `HTML` 几乎所有的`HTML`语法都是有效的模板语法，但是`<script>`元素是被禁用的，以阻止脚本注入攻击的风险，(实际上是被忽略了)；
    - 所以在模板中要引用`jTopo`时候只是在页面引入`script`标签是没有效果的，因为被忽略了
    - 只能在`index.hmtl`文件中写入`script`标签引用，它是生效的。

- 插值表达式: 用双花括号的形式把值转换为字符串

## 范例
- `[attr.colspan]="1+1"` 属性绑定
- CSS类绑定
    - `<div class="bad curly" [class]="badCurly"></div>` class生效时候会用新的`class`值覆盖旧值；
    - `[class.special]="!isSpecial"` 这样只会覆盖单个`special`样式
    - `NgClass`可以管理多个类名，通过`key`‘样式名’，`value`‘布尔值’形式，


- 样式绑定
    - `[style.color]="isSpecial ? 'red' : 'green'"`
    - `[style.font-size.em]="isSpecial ? 3 : 1"` 设置有单位的样式
    - `[style.font-size.%]="!isSpecial ? 150 : 50"`
    - `[style.font-size.px]="size"`
    - 样式属性命名方法可以用中线命名法也可以使用驼峰方式如`fontSize`
    - `NgStyle`可以同时控制多个`style`，`key`是样式名，`value`是样式值


- 事件绑定
    - `EventEmitter`自定义事件，创建一个实例，并且把它作为属性暴露出来。指令调用`EventEmitter.emit(payload)`来触发事件，可以传入任何东西作为消息载荷。
    - 场景：点击子组件触点击删除，把删除操作上传到父组件进行实际的删除操作
    ```child.html
    <button (click)="delete()">Delete</button>
    ```
    ```child.ts
    deleteRequest = new EventEmitter<Hero>();
    delete(){
        this.deleteRequest.emit(this.hero);
    }
    ```
    ```father.html
    <hero-detail (deleteRequest)="deleteHero($event)" [hero]="currentHero"></hero-detail>
    ```
    - 当`deleteRequest`事件触发时，`Angular`调用父组件的`deleteHero`方法，在`$event`变量中传入要删除的英雄

## NgIf
- `*NgIf` 为`false`时，`Angular`从`DOM`中物理地移除了这个元素子树。它销毁了子树中的组件及其状态，也潜在释放了可观的资源，最终让用户体验到更好的性能。
- `<div *ngIf="isShow"></div>`

## NgSwitch
- 当需要从一组可能的元素树中根据条件显示一个时，就绑定到`NgSwitch`，渲染时候只会把选中的元素放进`DOM`中。
- `ngSwitch` 绑定返回开关值的表达式
- `ngSwitchCase` 绑定到返回匹配值的表达式
- `ngSwitchDefault` 标记默认值
    ```html
    <span [ngSwitch]="toeChoice">
        <span *ngSwitchCase="'Eenie'">Eenie</span>
        <span *ngSwitchCase="'haha'">haha</span>
        <span *ngSwitchDefault>Other</span>
    </span>
    ```
- 如果没有匹配的值，就把默认的值显示到`DOM`中

## NgFor 重复指令器
- `<div *ngFor="let hero of heroes">{{hero.name}}</div>`
- `ngFor`支持可选的`index`，它在迭代过程中从`0`开始递增。
- `<div *ngFor="let hero of heroes; let i=index">{{i + 1}} - {{hero.name}}</div>`
- 在大型列表中使用`ngFor`会导致性能较差，对一个条目的一丁点改变也会导致级联DOM操作。可以通过添加追踪函数来避免这种折腾。
    - 定义追踪函数
        `trackByHeroes(index:number, hero:Hero){ return hero.id}`
    - 给指令添加追踪函数
        `<div *ngFor="let hero of heroes; trackBy:trackByHeroes">({{hero.id}}) {{hero.name}}</div>`

## 模板变量
- 可以使用`#`和`ref-`表示变量
- `<input #phone>` 
- `<input ref-fax>`

## 声明输入和输出属性
    ```ts
    @input() hero:Hero;
    @output() deleteRequest=new EventEmitter<Hero>(); // --'emitter 发射器'
    ```

## 安全导航操作符
- `?.` 是一种流畅而便利的方式，用来保护出现在属性路径中`null`和`undefined`值。避免页面失败。
- 正常的应对方法是通过`ngIf`或者`&&`进行非空判断，但也仅限于内容少而且会显得突兀，下面的这样就很流畅
- `a?.b?.c?.`
