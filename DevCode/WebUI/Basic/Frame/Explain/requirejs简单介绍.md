---
title: requirejs简单介绍
date: 2016-07-17
tags: [Models, jQuery]
categories: Frame
---

http://www.ibm.com/developerworks/cn/web/1209_shiwei_requirejs/index.html

使用 RequireJS 优化 Web 应用前端
基于 AMD（Asynchronous Module Definition）的 JavaScript 设计已经在目前较为流行的前端框架中大行其道，jQuery、Dojo、MooTools、EmbedJS 等纷纷在其最新版本中加入了对 AMD 的支持。本文介绍的是另一款较为精简的 RequireJS 框架，既想使用 AMD 的特性又不想引入一个庞大的库的开发人员，不妨试试 RequireJS。RequireJS 可以帮助用户异步按需的加载 JavaScript 代码，并解决 JavaScript 模块间的依赖关系，提升了前端代码的整体质量和性能。

AMD 简介
前端开发在近一两年发展的非常快，JavaScript 作为主流的开发语言得到了前所未有的热捧。大量的前端框架出现了，这些框架都在尝试着解决一些前端开发中的共性问题，但是实现又不尽相同。在这个背景下，CommonJS 社区诞生了，为了让前端框架发展的更加成熟，CommonJS 鼓励开发人员一起在社区里为一些完成特定功能的框架制定规范。AMD（Asynchronous Module Definition）就是其中的一个规范。
传统 JavaScript 代码的问题
让我们来看看一般情况下 JavaScript 代码是如何开发的：通过 <script> 标签来载入 JavaScript 文件，用全局变量来区分不同的功能代码，全局变量之间的依赖关系需要显式的通过指定其加载顺序来解决，发布应用时要通过工具来压缩所有的 JavaScript 代码到一个文件。当 Web 项目变得非常庞大，前端模块非常多的时候，手动管理这些全局变量间的依赖关系就变得很困难，这种做法显得非常的低效。

AMD 提出了一种基于模块的异步加载 JavaScript 代码的机制，它推荐开发人员将 JavaScript 代码封装进一个个模块，对全局对象的依赖变成了对其他模块的依赖，无须再声明一大堆的全局变量。通过延迟和按需加载来解决各个模块的依赖关系。模块化的 JavaScript 代码好处很明显，各个功能组件的松耦合性可以极大的提升代码的复用性、可维护性。这种非阻塞式的并发式快速加载 JavaScript 代码，使 Web 页面上其他不依赖 JavaScript 代码的 UI 元素，如图片、CSS 以及其他 DOM 节点得以先加载完毕，Web 页面加载速度更快，用户也得到更好的体验。
CommonJS 的 AMD 规范中只定义了一个全局的方法，如清单 1 所示。
清单 1. AMD 规范
 define(id?, dependencies?, factory);
该方法用来定义一个 JavaScript 模块，开发人员可以用这个方法来将部分功能模块封装在这个 define 方法体内。
id 表示该模块的标识，为可选参数。
dependencies 是一个字符串 Array，表示该模块依赖的其他所有模块标识，模块依赖必须在真正执行具体的 factory 方法前解决，这些依赖对象加载执行以后的返回值，可以以默认的顺序作为 factory 方法的参数。dependencies 也是可选参数，当用户不提供该参数时，实现 AMD 的框架应提供默认值为 [“require”，”exports”，“module”]。
factory 是一个用于执行该模块的方法，它可以使用前面 dependencies 里声明的其他依赖模块的返回值作为参数，若该方法有返回值，当该模块被其他模块依赖时，返回值就是该模块的输出。

CommonJS 在规范中并没有详细规定其他的方法，一些主要的 AMD 框架如 RequireJS、curl、bdload 等都实现了 define 方法，同时各个框架都有自己的补充使得其 API 更实用。

RequireJS 是一个非常小巧的 JavaScript 模块载入框架，是 AMD 规范最好的实现者之一。最新版本的 RequireJS 压缩后只有 14K，堪称非常轻量。它还同时可以和其他的框架协同工作，使用 RequireJS 必将使您的前端代码质量得以提升。
目前最新版本的 RequireJS 1.0.8 在 IE 6+、Firefox 2+、Safari 3.2+、Chrome 3+、Opera 10+ 上都工作的很好。

实战 RequireJS
在 Web 应用中使用 RequireJS
在 RequireJS 官方主页上下载最新的版本的 require.js，放到 Web 页面中。示例的 Web 项目结构图 1 所示。

通过在 index.html 中加入一个 <script> 标签直接引入 require.js 即可。
RequireJS 功能初探
RequireJS 使用起来非常的简单，但是这些功能确是在 Web 前端开发中非常重要的，下面我们来逐一看看如何使用 RequireJS 的各项功能。
使用 RequireJS 加载 JavaScript 文件
即使您的 Web 前端由于种种历史原因还没有打算进行模块化的设计，RequireJS 作为 JavaScript 文件的加载器，还是可以帮助您来完成异步非阻塞的文件加载。
如清单 2 所示，有两个 JavaScript 文件 a.js 和 b.js，里面各自定义了 myFunctionA 和 myFunctionB 两个方法，通过下面这个方式可以用 RequireJS 来加载这两个文件，在 function 部分的代码可以引用这两个文件里的方法。
清单 2. 加载 JavaScript 文件
 <script src="./js/require.js"></script> 
     <script> 
    require(["./js/a.js", "./js/b.js"], function() { 
             myFunctionA(); 
             myFunctionB(); 
        }); 
     </script>
require 方法里的这个字符串数组参数可以允许不同的值，当字符串是以”.js”结尾，或者以”/”开头，或者就是一个 URL 时，RequireJS 会认为用户是在直接加载一个 JavaScript 文件，否则，当字符串是类似”my/module”的时候，它会认为这是一个模块，并且会以用户配置的 baseUrl 和 paths 来加载相应的模块所在的 JavaScript 文件。配置的部分会在稍后详细介绍。
这里要指出的是，RequireJS 默认情况下并没有保证 myFunctionA 和 myFunctionB 一定是在页面加载完成以后执行的，在有需要保证页面加载以后执行脚本时，RequireJS 提供了一个独立的 domReady 模块，需要去 RequireJS 官方网站下载这个模块，它并没有包含在 RequireJS 中。有了 domReady 模块，清单 2 的代码稍做修改加上对 domReady 的依赖就可以了。
清单 3. 页面加载后执行 JavaScript
 <script src="./js/require.js"></script> 
     <script> 
    require(["domReady!", "./js/a.js", "./js/b.js"], function() { 
             myFunctionA(); 
             myFunctionB(); 
        }); 
     </script>
执行清单 3 的代码后，通过 Firebug 可以看到 RequireJS 会在当前的页面上插入为 a.js 和 b.js 分别声明了一个 <script> 标签，用于异步方式下载 JavaScript 文件。async 属性目前绝大部分浏览器已经支持，它表明了这个 <script> 标签中的 js 文件不会阻塞其他页面内容的下载。
清单 4. RequireJS 插入的 <script>
 <script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" 
 data-requiremodule="js/a.js" src="js/a.js"></script>
使用 RequireJS 来定义 JavaScript 模块
这里的 JavaScript 模块与传统的 JavaScript 代码不一样的地方在于它无须访问全局的变量。模块化的设计使得 JavaScript 代码在需要访问”全局变量”的时候，都可以通过依赖关系，把这些”全局变量”作为参数传递到模块的实现体里，在实现中就避免了访问或者声明全局的变量或者函数，有效的避免大量而且复杂的命名空间管理。
如同 CommonJS 的 AMD 规范所述，定义 JavaScript 模块是通过 define 方法来实现的。
下面我们先来看一个简单的例子，这个例子通过定义一个 student 模块和一个 class 模块，在主程序中实现创建 student 对象并将 student 对象放到 class 中去。
清单 5. student 模块，student.js
 define(function(){ 
     return { 
        createStudent: function(name, gender){ 
             return { 
                 name: name, 
                 gender: gender 
             }; 
        } 
     }; 
 });
清单 6. class 模块，class.js
 define(function() { 
 var allStudents = []; 
        return { 
            classID: "001", 
            department: "computer", 
            addToClass: function(student) { 
            allStudents.push(student); 
            }, 
            getClassSize: function() { 
            return allStudents.length; 
            } 
        }; 
     } 
 );
清单 7. 主程序
 require(["js/student", "js/class"], function(student, clz) { 
 clz.addToClass(student.createStudent("Jack", "male")); 
 clz.addToClass(student.createStudent("Rose", "female")); 
 console.log(clz.getClassSize());  // 输出 2 
 });
student 模块和 class 模块都是独立的模块，下面我们再定义一个新的模块，这个模块依赖 student 和 class 模块，这样主程序部分的逻辑也可以包装进去了。
清单 8. 依赖 student 和 class 模块的 manager 模块，manager.js
 define(["js/student", "js/class"], function(student, clz){ 
 return { 
    addNewStudent: function(name, gender){ 
    clz.addToClass(student.createStudent(name, gender)); 
        }, 
    getMyClassSize: function(){ 
    return clz.getClassSize(); 
    } 
     }; 
 });
清单 9. 新的主程序
 require(["js/manager"], function(manager) { 
 manager.addNewStudent("Jack", "male"); 
 manager.addNewStudent("Rose", "female"); 
 console.log(manager.getMyClassSize());// 输出 2 
 });
通过上面的代码示例，我们已经清楚的了解了如何写一个模块，这个模块如何被使用，模块间的依赖关系如何定义。还是有一些使用技巧需要提示一下：
尽量不要提供模块的 ID，如 AMD 规范所述，这个 ID 是可选项，如果提供了，在 RequireJS 的实现中会影响模块的可迁移性，文件位置变化会导致需要手动修改该 ID。
每个 JavaScript 文件只定义一个模块，模块名称和文件路径的查找算法决定了这种方式是最优的，多个的模块和文件会被优化器进行优化。
避免模块的循环依赖，如果实在避免不了，可以模块中加上对”require”模块的依赖，在代码中直接用 require(”dependencyModuleName”)。
配置 RequireJS
前面的介绍中，我们似乎忽略了一个基本问题，模块名字是怎么来的？当我在 require 一个模块时，这个模块是如何映射到具体的 JavaScript 文件上去？这就涉及到如何配置 RequireJS。
最简化的加载 RequireJS 的方式如清单 2 所示，在这种情况下，我们没有指定一个 baseUrl 和 paths 给 RequireJS，如果通过如清单 10 所示方式，则 data-main 指定了一个在当前 index.html 目录并行的文件夹下的 /js/main.js 作为程序入口，而 /js 目录也将作为 baseUrl 在其他模块定义时候使用。
清单 10. 载入 require.js
 <script data-main="js/main" src="scripts/require.js"></script>
因此，我们前面示例中的所有模块依赖，都可以去掉”js/”，直接写 ”student”， ”class”，”manager” 等。
一种更为直接的方式显示指定 baseUrl 和 paths 就是利用 require.config 来设置这些参数。如清单 11 所示。
清单 11. 配置 RequireJS
 <script type="text/javascript" src="./js/require.js"></script> 
 <script type="text/javascript"> 
  require.config({ 
    baseUrl: "./js", 
    paths: { 
        "some": "some/v1"
    }, 
 waitSeconds: 10 
 }); 
  require( ["some/module", "my/module", "./js/a.js"], 
    function(someModule,    myModule) {} 
  ); 
 </script>
baseUrl指明的是所有模块的 base URL，比如”my/module”所加载的 script实际上就是 /js/my/module.js。注意，以 .js 结尾的文件加载时不会使用该 baseUrl，它们仍然会使用当前 index.html所在的相对路径来加载，所以仍然要加上”./js/”。如果 baseUrl没有指定，那么就会使用 data-main中指定的路径。
paths 中定义的路径是用于替换模块中的路径，如上例中的 some/module 具体的 JavaScript 文件路径是 /js/some/v1/module.js 。
waitSeconds 是指定最多花多长等待时间来加载一个 JavaScript 文件，用户不指定的情况下默认为 7 秒。
另外一个重要的配置是 packages，它可以指定其他符合 CommonJS AMD 规范的目录结构，由此带来了丰富的扩展性。如 Dojo、jQuery 等的模块也可以通过该配置来让 RequireJS 加载。
其他可配置的选项还包括 locale、context、deps、callback等，有兴趣的读者可以在 RequireJS 的官方网站查阅相关文档。

综合运用 RequireJS
当 RequireJS 与其他框架一起工作的时候，显然它是可以作为统一的加载器来加载其他框架。鉴于 jQuery、Dojo 等已经支持了 AMD ，那么就有可能在定义自己的模块的时候，通过适当配置，直接把其他框架的模块作为依赖对象。
RequireJS 和 Dojo
清单 11是一个基本的 RequireJS 和 Dojo 集成配置方法，这里关键是将 dojo 和 dijit 都在 packages 里面注册一下。
清单 12. 配置 RequireJS 和 Dojo
 <script> 
 require = { 
 packages: [ 
 { 
 name: “dojo”, 
 location: “dojo”, 
 main:”lib/main-browser”, 
 lib: “.”
 }, 
 { 
 name: “dijit”, 
 location: “dijit”, 
 main:”lib/main”, 
 lib: “.”
 } 
 ], 
 paths: { 
 require: “./js”
 }, 
 ready: function () { 
 require([“my/module”], function (module) { 
 }); 
 } 
 }; 
 </script>
在定义 module 这个模块时就可以直接将 dojo 和 dijit 里的模块作为依赖对象了。
RequireJS 和 jQuery
把 jQuery 作为一个依赖模块来使用也非常简单，只需要在 RequireJS 里的 config 里做相应的配置就可以了。
清单 13. 配置 RequireJS 和 jQuery
 require.config({ 
 paths: { 
"jquery": "./js/jquery-1.7"
 } 
 }); 
 require(["jquery"],function(jQ){ 
 console.log(jQ); 
 });
RequireJS 和 Web Workers
Web Workers 是多线程的 JavaScript，每个 worker 里面的脚本都 会启动一个新的线程来执行，通过在 worker 里面用 importsScript 来加载 require.js 可以直接在 worker 里面使用 RequireJS 。
清单 14. RequireJS 和 Web Workers
 importScripts('./js/require.js'); 
 require(["require"], 
    function(require) { 
        postMessage("test"); 
    } 
 );
回页首
小结
本文简单介绍了 AMD 的概念和它带来的好处，深入介绍了如何使用 RequireJS 来定义自己的 JavaScript 模块，管理这些模块的依赖关系，异步按需加载这些模块。并进一步讨论了如何用 RequireJS 和其他框架协同工作，有兴趣的读者可以继续阅读相关文档了解更多详细的用法。