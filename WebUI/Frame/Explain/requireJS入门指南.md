---
title: RequireJS 入门指南
date: 2016-07-17
tags: [Models]
categories: Frame
---

http://www.oschina.net/translate/getting-started-with-the-requirejs-library?cmp

简介
如今最常用的JavaScript库之一是RequireJS。最近我参与的每个项目，都用到了RequireJS，或者是我向它们推荐了增加RequireJS。在这篇文章中，我将描述RequireJS是什么，以及它的一些基础场景。

异步模块定义(AMD) 
谈起RequireJS，你无法绕过提及JavaScript模块是什么，以及AMD是什么。

JavaScript模块只是遵循SRP(Single Responsibility Principle单一职责原则)的代码段，它暴露了一个公开的API。在现今JavaScript开发中，你可以在模块中封装许多功能，而且在大多数项目中，每个模块都有其自己的文件。这使得JavaScript开发者日子有点难过，因为它们需要持续不断的关注模块之间的依赖性，按照一个特定的顺序加载这些模块，否则运行时将会放生错误。

When you want to load JavaScript modules, you use script tags. In order to load module dependencies, you need to load the dependency first and then the dependent. When using script tags, you need to arrange their loading in that specific order and the scripts will be loaded synchronously. You can use the asyncanddeferkeywords to make the load asynchronous but you might lose the order of loading in the process. Another option is to bundle all the scripts but still you will need to order them in the right order during the bundling.

AMD is all about defining modules in a way that the module and its dependencies can be asynchronously loaded and in the right order.

Getting Started with RequireJS Library

CommonJS, which is an attempt to standardize common JavaScript patterns, includes an AMD definition that I encourage you to read before you proceed in this post. In ECMAScript 6, the JavaScript vNext specifications, there are specifications for exports, imports and modules which are going to be a part of the JavaScript language but only in the near future. This is where RequireJS is entering our story.


当你要加载JavaScript模块时，就会使用script标签。为了加载依赖的模块，你就要先加载被依赖的，之后再加载依赖的。使用script标签时，你需要按照此特定顺序安排它们的加载，而且脚本的加载是同步的。可以使用async和defer关键字使得加载异步，但可能因此在加载过程中丢失加载的顺序。另一个选择是将所有的脚本捆绑打包在一起，但在捆绑的时候你仍然需要把它们按照正确的顺序排序。

AMD就是这样一种对模块的定义，**使模块和它的依赖可以被异步的加载，但又按照正确的顺序。**

Getting Started with RequireJS Library

CommonJS, 是对通用的JavaScript模式的标准化尝试，它包含有 AMD 定义 ，我建议你在继续本文之前先读一下。在ECMAScript 6这个下一版本JavaScript 规范中，有关于输出，输入以及模块的规范定义，这些将成为JavaScript语言的一部分，而且这不会太久。这也是关于RequireJS我们想说的东西。

RequireJS?
RequireJS is a JavaScript file and module framework that can be downloaded from http://requirejs.org/ or by using Nuget, if you work in Visual Studio environment. It is supported both in the browsers and in server environments like node.js. Using RequireJS, you will load only the relevant module dependencies in their right order.

What RequireJS is doing when you use it is to create script tags for each dependency you defined and load those dependencies on-the-fly using thehead.appendChild()function. Then, after the dependencies are loaded, RequireJS will figure the right order to define the modules and will call each module definition in that right order. That means that you only need one root to load the entire functionality that you need and RequireJS will do the rest. In order to use that functionality appropriate, you will have to define each of your modules using RequireJS API or else nothing will work as expected.

译者信息
RequireJS?
RequireJS是一个Javascript 文件和模块框架，可以从 http://requirejs.org/下载，如果你使用Visual Studio也可以通过Nuget获取。它支持浏览器和像node.js之类的服务器环境。使用RequireJS,你可以顺序读取仅需要相关依赖模块。

RequireJS所做的是，在你使用script标签加载你所定义的依赖时，将这些依赖通过head.appendChild()函数来加载他们。当依赖加载以后，RequireJS计算出模块定义的顺序，并按正确的顺序进行调用。这意味着你需要做的仅仅是使用一个“根”来读取你需要的所有功能，然后剩下的事情只需要交给RequireJS就行了。为了正确的使用这些功能，你定义的所有模块都需要使用RequireJS的API，否者它不会像期望的那样工作。

RequireJS API exists inside thereq lang=jscriptuirejsnamespace which is loaded when you load the RequireJS script. RequireJS includes three main API functions:

define– the function is used to define a module. Each module is defined with a unique module ID which will be used by RequireJS runtime functionality. Thedefinefunction is a global function and you don’t need to use it with therequirejsnamespace.
require– the function is used to load required dependencies. It is a global function and you don’t need to use it with therequirejsnamespace.
config– the function is used to configure the requirejs runtime functionality.
Later on we will examine how to use those functions, but first lets understand how to start the RequireJS loading process.

译者信息
RequireJS API 存在于RequireJS载入时创建的命名空间requirejs下。其主要API主要是下面三个函数:

define– 该函数用户创建模块。每个模块拥有一个唯一的模块ID，它被用于RequireJS的运行时函数，define函数是一个全局函数，不需要使用requirejs命名空间.
require– 该函数用于读取依赖。同样它是一个全局函数，不需要使用requirejs命名空间.
config– 该函数用于配置RequireJS.
在后面，我们将教你如果使用这些函数，但首先让我们先了解下RequireJS的加载流程。

The data-main Attribute
Once you downloaded RequireJS, the first thing to do after you put its script in your solution is to understand how RequireJS starts working. Once RequireJS is loaded, it search for a script withdata-mainattribute (it should be the same script with thesrcattribute set to load RequireJS). Thedata-mainshould be set to the base URL for all the scripts. From the base URL, RequireJS will start loading all the relevant modules. Here is an example of a script tag with thedata-mainattribute:

<script src="scripts/require.js" data-main="scripts/app.js"></script>
Another way to define the base URL is using theconfigfunction which we will see later on. RequireJS assumes that all the dependencies are scripts so when you declare a dependency you don’t need to use the .js suffix.

译者信息
data-main属性
当你下载RequireJS之后，你要做的第一件事情就是理解RequireJS是怎么开始工作的。当RequireJS被加载的时候，它会使用data-main属性去搜寻一个脚本文件（它应该是与使用src加载RequireJS是相同的脚本）。data-main需要给所有的脚本文件设置一个根路径。根据这个根路径，RequireJS将会去加载所有相关的模块。下面的脚本是一个使用data-main例子：

<script src="scripts/require.js" data-main="scripts/app.js"></script>
另外一种方式定义根路劲是使用配置函数，后面我们将会看到。requireJs假设所有的依赖都是脚本，那么当你声明一个脚本依赖的时候你不需要使用.js后缀。

The config Function
If you want to change the default RequireJS configuration values with your own configurations, you can do that using therequirejs.config function. Theconfigfunction receives an options object that can include a lot of configurations options. Here are some of the configurations that you can use:

baseUrl– the root path to start the loading of modules.
paths– path mapping for modules that don’t exists in under the base URL
shims– configuration for dependencies, exports and initialization function to wrap scripts/modules that don’t use the RequireJSdefinefunction. For example, if underscore library doesn’t use the RequireJSdefinefunction and you still want to use it with RequireJS, you will have to define it as a shim in theconfigfunction. 
deps– array of dependencies to load.
Here is an example of using theconfigfunction:

require.config({
    //By default load any module IDs from scripts/app
    baseUrl: 'scripts/app',
    //except, if the module ID starts with "lib"
     paths: {
        lib: '../lib'
    }, 
    // load backbone as a shim
    shim: {
        'backbone': {
            //The underscore script dependency should be loaded before loading backbone.js
            deps: ['underscore'],
            // use the global 'Backbone' as the module name.
            exports: 'Backbone'
        }
    }
});
The base URL in the example is set to scripts/app, every module that starts with lib is configured to be used from the scripts/lib folder and backbone is loaded as a shim with dependencies.

译者信息
配置函数
如果你想改变RequireJS的默认配置来使用自己的配置，你可以使用require.configh函数。config函数需要传入一个可选参数对象，这个可选参数对象包括了许多的配置参数选项。下面是一些你可以使用的配置：

baseUrl——用于加载模块的根路径。
paths——用于映射不存在根路径下面的模块路径。
shims——配置在脚本/模块外面并没有使用RequireJS的函数依赖并且初始化函数。假设underscore并没有使用  RequireJS定义，但是你还是想通过RequireJS来使用它，那么你就需要在配置中把它定义为一个shim。
deps——加载依赖关系数组
下面是使用配置的一个例子：

require.config({
    //By default load any module IDs from scripts/app
    baseUrl: 'scripts/app',
    //except, if the module ID starts with "lib"
     paths: {
        lib: '../lib'
    }, 
    // load backbone as a shim
    shim: {
        'backbone': {
            //The underscore script dependency should be loaded before loading backbone.js
            deps: ['underscore'],
            // use the global 'Backbone' as the module name.
            exports: 'Backbone'
        }
    }
});
在这个例子中把根路径设置为了scripts/app，由lib开始的每个模块都被配置在scripts/lib文件夹下面，backbone 加载的是一个shim依赖。

Defining Modules Using RequireJS
Modules are just well-scoped objects that expose an API and encapsulate their internals. In order to define a module, RequireJS exposes thedefinefunction. There should be only one call fordefinein each JavaScript file by convention. Thedefinefunction receives an array of dependencies and a function which is going to hold all the module definitions. By convention the module definition function receives as parameters all the previous dependencies and in the order they were supplied in the array. For example, here is a simple module definition:

define(["logger"], function(logger) {        
        return {
             firstName: “John",
             lastName: “Black“,
             sayHello: function () {
                logger.log(‘hello’);
             }
        }
    }
);
As you can see, an array is passed to thedefinefunction with a logger dependency which is later used in the module. Also, you can see that in the module definition function there is a parameter calledloggerwhich will be set to the loaded logger module. Every module should return its API which in this case is two properties (firstNameandlastName) and a function (sayHello). Later on, if you will load this module as another module dependency with a module ID, you will be able to use the exposed API.

译者信息
用RequireJS定义模块
模块是进行了内部实现封装、暴露接口和合理限制范围的对象。ReuqireJS提供了define函数用于定义模块。按照惯例每个Javascript文件只应该定义一个模块。define函数接受一个依赖数组和一个包含模块定义的函数。通常模块定义函数会把前面的数组中的依赖模块按顺序做为参数接收。例如，下面是一个简单的模块定义:

define(["logger"], function(logger) {        
        return {
             firstName: “John",
             lastName: “Black“,
             sayHello: function () {
                logger.log(‘hello’);
             }
        }
    }
);
我们看，一个包含了logger的模块依赖数组被传给了define函数,该模块后面会被调用。同样我们看所定义的模块中有一个名为logger的参数，它会被设置为logger模块。每一个模块都应该返回它的API.这个示例中我们有两个属性(firstName和lastName)和一个函数(sayHello)。然后，只要你后面定义的模块通过ID来引用这个模块，你就可以使用其暴露的API。

Using the require Function
Another useful function in RequireJS is therequirefunction. Therequirefunction is used to load dependencies without the creation of a module. For example, here is a usage of therequirefunction which defines a function that requires jQuery to work:

require(['jquery'], function ($) {
    //jQuery was loaded and can be used now
});
Summary
In the article, I introduced RequireJS which is one of the libraries that I’m using in every JavaScript app project. Other than just loading module dependencies and in the relevant order, RequireJS helps to write modular JavaScript code which is much more maintainable and reusable.

译者信息
使用require函数
在RequireJS中另外一个非常有用的函数是require函数。require函数用于加载模块依赖但并不会创建一个模块。例如：下面就是使用require定义了能够使用jQuery的一个函数。

require(['jquery'], function ($) {
    //jQuery was loaded and can be used now
});
小结
在这篇文章中我介绍了RequireJS库,它是我创建每个Javascript项目都会用到的库函数之一。它不仅仅用于加载模块依赖和相关的命令，RequireJS帮助我们写出模块化的JavaScript代码，这非常有利于代码的可扩展性和重用性。