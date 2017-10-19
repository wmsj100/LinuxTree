---
title: 2016年JavaScript技术栈展望
date: 2016-3-30 20:38:37
tags: [前端]
categories: Article
---

如果你正在筹划新的前端项目或者重构现有项目，那么你需要认识到现在的前端开发环境已经今非昔比，这其中有太多的选择了：React、Flux、Angular、Aurelia、Mocha、Jasmine、Babel、TypeScript、Flow…… 它们的本意是将开发简单化，却无形中提高了学习成本，也给未来项目的维护带来了不确定性。

<!-- more -->

好在这一现象正在退热，优胜劣汰，优秀的项目慢慢沉淀下来，开发方式也越来越清晰。有些开发者正在尝试使用基于上述技术的框架进行开发，也在一定程度上减少了学习成本。

本文中主要介绍了一些我在 Web 应用开发中所涉及和推崇的技术，其中有一些技术上存在争议，所以我对于每一技术都只做简单的介绍和分析。所有的这些观点都是基于我个人的经验和对社区的接触总结而来的，所以各位还请按需各取所用。

## React

React 可谓风头正盛一时无两：

- 组件化使应用程序更易于开发和维护
- 学习曲线平缓，核心 API 简洁清晰，易于学习
- JSX 语法不落俗套，充分发挥了 JavaScript 的能量
- 天生适配 [Flux](https://facebook.github.io/flux/) 和 Redux
- 社区活跃且具有创造力，奉献了诸多优秀的开发工具
- 单向数据流比双向数据绑定的方式更适合复杂应用程序，质量更高
- 支持服务端渲染

虽然比起 Ember、Aurelia 和 Angular 这些功能丰富的框架，React 不是全能手，但 React 的开发环境更加健壮。就目前而言，使用 React 已经不是一个技术选择，而是一个商业行为，它能提供[更高效和更有效的生产力](https://blog.formidable.com/using-react-is-a-business-decision-not-a-technology-choice-63c4641c5f7)。

> 当你想开发移动应用时，因为已经学习了 React 语法，所以可以直接上手 [React Native](https://facebook.github.io/react-native/) 开发跨平台应用。

## Redux

现在，我们已经具有了开发视图层的能力，接下来，我们需要使用其他工具管理应用程序中的状态和生命周期，在这里推荐的工具就是：[Redux](https://github.com/reactjs/redux)。

为了配合 React，Facebook 开发了管理单向数据流的工具 [Flux](https://facebook.github.io/flux/)，虽然 Flux 基本上实现了对单项数据流的支持，但是同时也带了其他问题，比如如何保存状态、何处发起 Ajax 请求等等。

为了解决这些问题，又衍生了一系列效仿 Flux 模式的框架：Fluxible、Reflux、Alt、Flummox、Lux、Nuclear、Fluxxor……

目前来说被开发社区广泛支持的一个实现就是 Redux。

在 Redux 中，大多数的组件都是[纯函数式的组件](https://en.wikipedia.org/wiki/Pure_function)，也只有一个集中的存储和资源中心。Redux 的实例方法负责整个数据的操作和维护。相比 Flux 来说，Redux 的思路更加清晰。

更重要的是，Redux 非常易于学习。Redux 的作者 [Dan Abramov](https://twitter.com/dan_abramov) 是一个优秀的教师，他制作了一系列深入浅出的 Redux 视频教程。通过观看这些视频，即可成为一个 Redux 方面的专家。我曾经见识到一个零基础的 React 团队在短短几周内迅速开发出了测试版产品，且代码非常稳健和老练。

Redux 周边的生态系统和 Redux 本身一样健壮。从神奇的 [devtool](https://github.com/gaearon/redux-devtools) 到强大的记忆化工具 [reselect](https://github.com/reactjs/reselect)，Redux 开发社区为开发者提供了应有尽有的工具。

开发者可能会本能地去尝试抽象出一个 Redux 模板，这么做有诸多好处，但请在认清需求的基础上来封装模板，而不要盲目的去尝试。

## ES6 和 Babel

是时候抛弃 CoffeeScript 了，这是因为它的诸多特性已在 ES6 中出现类似的语法，而 ES6 是实施标准，代表了 JavaScript 未来的发展方向。

目前[最新的浏览器已经支持](https://kangax.github.io/compat-table/es6/)了 ES6 的大部分特性。Babel 是一个强大的转换工具，用于将 ES6 转换为 ES5。此外，根据目标浏览器可以调整代码转换的程度。

那么是否有类型系统呢？[TypeScript](http://www.typescriptlang.org/) 和 [Flow](http://flowtype.org/) 都为 JavaScript 提供了静态类型系统，使用静态类型检查，可以有效捕获错误，减少测试量。目前来说，我建议对此持观望态度。

TypeScript 在尽力让 JavaScript 向 C# 或 Java 的方向发展，但缺少了许多高级的类型系统特性，比如代数数据类型（[algebraic data types](https://en.wikipedia.org/wiki/Algebraic_data_type)）。此外，它不能像 Flow 一样有效地处理 null。

相比而言，Flow 更加强大，捕获的错误类型也更多，但难于配置。此外，它对 JavaScript 新特性的支持弱于 Babel，也不支持 Windows 系统。

就我个人的角度而言，在前端开发中类型系统并不是至关重要的一环（此处可能有争议）。在类型系统更加健壮且对 Babel 更友好之前，还是让我们静观其变吧。

## ESLint

另一个无可争议的工具是 [ESLint](http://eslint.org/)。ESLint 支持 ES6 语法，还提供了 React 插件，已经不单单是一个代码审查工具了。目前来说，[JSLint](http://www.jslint.com/) 已经过时了，ESLint 可以替代 [JSHint](http://jshint.com/) 和 [JSCS](http://jscs.info/) 独树一帜了。

开发者可以根据自己的需求配置 ESLint，不过在这里我建议根据[AirBNB 的开发规范](https://github.com/airbnb/javascript)进行配置，也可以直接使用 [ESLint airbnb config](https://www.npmjs.com/package/eslint-config-airbnb)。当然这份规范中尚有不足之处，但保持团队整体代码的一致性，可以有效提高代码的可读性。

当你熟悉了 ESLint 之后，建议开发者深入地尝试其中的规则。ESLint 捕获的错误越多，产品的稳定性越高。

## NPM，CommonJS 和 ES6 modules

忘记 Bower 吧，用 NPM 接管一切。类似 Browserify 和 Webpack 的构建工具间接提高了 NPM 在 web 开发中的地位。使用 NPM，版本管理将会更加简单，也将更多地与 Node.js 生态系统接触。目前对于 CSS 的处理尚不足够完善。

你可能会考虑如何在部署服务器上执行构建呢？与 Ruby 的 [Bundler](http://bundler.io/)有所不同，NPM 使用了通配符检索文件，且第三方包可以在代码开发中以及项目发布前做任意修改。使用 [shrinkwrap](https://docs.npmjs.com/cli/shrinkwrap) 文件可以冻结项目中的第三方依赖，我建议使用 [User 的 shrinkwrap](https://github.com/uber/npm-shrinkwrap)，提高输出的一致性。此外，开发者也可以考虑使用类似 [Sinopia](https://www.npmjs.com/package/sinopia) 的工具托管自己的私有 NPM 服务器。

Babel 会将 [ES6 module](http://www.2ality.com/2014/09/es6-modules-final.html) 语法转换为 [CommonJS](https://nodejs.org/docs/latest/api/modules.html)。CommonJS 是一种历经实践的语法，这意味着稳定和通用，此外，使用类似 [tree shaking](http://www.2ality.com/2015/12/webpack-tree-shaking.html)（Webpack 2.0 和 [Rollup](http://http/rollupjs.org/) 已经支持该特性）的机制我们还能实现静态代码分析。

## Webpack

除非你乐意在页面添加数百个脚本标签，否则的话你应该尝试用构建工具来打包页面的资源了。此外，你还需要某些工具让浏览器支持 NPM 第三方包。在这里，我推荐你使用 Webpack。

一年之前对于上述工作，开发者还有诸多[工具](https://github.com/rails/sprockets)可以选择，比如基于 JavaScript 的 [RequireJS](http://requirejs.org/)、[Browserify](http://browserify.org/) 和 Webpack 解决方案，此外还有号称能对 ES6 的模块进行最佳优化的 [RollupJS](http://rollupjs.org/).

在尝试了所有的工具之后，我强烈建议开发者选择 Webpack:

- 通过配置可以应对各种情况
- 支持主流的模块加载方式（AMD，CommonJS，globals）
- 内部机制可以修复破损的模块
- 可以处理 CSS
- 全面的缓存系统
- 支持热重载
- 可以加载大[多数的资源](https://webpack.github.io/docs/list-of-loaders.html)
- 提供高效的[性能优化方案](https://github.com/webpack/docs/wiki/optimization)

Webpack 也非常善于处理大型的单页应用，支持代码分割和惰性加载。

但是值得注意的是，Webpack 的学习曲线异常陡峭。不过一旦你学会了它，那么你就掌握了最强大的构建系统。

那么 Gulp 和 Grunt 呢？相比而言，Webpack 更善于处理各类资源。如果你需要执行其他类型的构建任务，那么 Gulp 和 Grunt 还是有用的。对于类似运行 Webpack 的基本任务，我建议直接使用 [NPM 脚本](https://docs.npmjs.com/cli/run-script)。

## Mocha + Chai + Sinon

在 JavaScript 中，有大量可选的单元测试工具，每一个都很稳定和健壮。如果你只是用于单元测试，那么现有工具完全可以胜任你的需求。

常见的测试工具有 [Jasmine](http://jasmine.github.io/)、[Mocha](https://mochajs.org/)、[Tape](https://github.com/substack/tape)、[AVA](https://github.com/sindresorhus/ava)、[Jest](https://facebook.github.io/jest/) 等，它们各有所长。

我对一个测试框架的要求有如下几条：

- 可以在浏览器运行，便于调试
- 执行速度快
- 便于处理异步测试
- 便于在命令行中使用
- 可以兼容任意断言和数据模拟的第三方库

第一条标准就排除了 Ava 和 Jest。

我喜欢 [Chai 断言](https://github.com/domenic/chai-as-promised)是因为其种类丰富、功能齐全的插件，喜欢 Mocha 是因为其对异步的良好支持。强烈建议使用 [Dirty Chai](https://github.com/prodatakey/dirty-chai) 避免某些问题。Webpack 的 [mocha-leader](https://github.com/webpack/mocha-loader) 插件允许开发者自动执行测试。

对于 React 而言，开发者可以参考一下 AirBNB 的 [Enzyme](https://github.com/airbnb/enzyme) 和[Teaspoon](https://github.com/jquense/teaspoon)。

我非常钟爱 Mocha 的特性，如果你想要的只是最基础的功能，可以参考[这篇文章](https://medium.com/javascript-scene/why-i-use-tape-instead-of-mocha-so-should-you-6aa105d8eaf4)了解一下 Tape。

## Lodash

JavaScript 并没有一个类似 Java 或 .NET 的核心工具库，所以开发者大都会从外部引用一个外部工具库。

目前来说，Lodash 是此类工具中的佼佼者。此外，由于它[惰性执行](http://filimanjaro.com/blog/2014/introducing-lazy-evaluation/)的特性，也让它是目前性能最佳的工具之一。使用 Lodash 时无需引用全部资源，开发者可以按需使用其中的函数。在 4.x 版本中，Lodash 为偏爱函数式编程的开发者提供了一个“函数式开发”模式。

如果你熟悉函数式编程，你可以了解一下 [Ramda](http://ramdajs.com/0.19.1/index.html)。如果你决定使用这个库，可能需要引用一些 Lodash 函数。

## fetch

许多基于 React 的应用程序都不再使用 jQuery 了。除非你正在维护一个陈旧的项目或者用到的第三方库依赖了 jQuery，否则已经没有必要使用它了。

我喜欢让项目保持简洁，在代码中只使用 [fetch](http://ramdajs.com/0.19.1/index.html) 。fetch 基于 promise，Firefox 和 Chrome 都封装了该接口。对于其他浏览器，则需要提供一个腻子脚本。我建议使用 [isomorphic-fetch](https://github.com/matthew-andrews/isomorphic-fetch) 在各个浏览器和服务端保持功能的一致性。

当然也可以其他优秀的第三方库异步获取数据，但我觉得 fetch 已经够用了。

## 同构 JavaScript

同构 JavaScript 是指同时运行在客户端和服务端的 JavaScript，常用于在服务端预先渲染页面，提高性能，便于 SEO。使用 React 可以实现同构 JavaScript，但是并不简单，它提高了程序的复杂度，限制了开发者可选的工具和第三方库。

如果你正在构建一个 B2C 的站点，比如电商网站，那么你可能就需要使用同构 JavaScript。不过，对于内部站点或者 B2B 程序，性能就不是最重要的了，则同构 JavaScript 也就不是太重要了。

## API

最近每个人好像都在思考如何处理 API。每个人都在随波逐流的使用[RESTfull API](https://en.wikipedia.org/wiki/Representational_state_transfer)，[SOAP](https://en.wikipedia.org/wiki/SOAP) 已经成为了过去时。目前业界存在各种 API 协议，比如 [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)、[JSON API](http://jsonapi.org/)、[HAL](http://stateless.co/hal_specification.html)、[GraphQL](https://facebook.github.io/react/blog/2015/05/01/graphql-introduction.html) 等。

GraphQL 赋予了客户端进行任意查询的能力。搭配 [Relay](https://facebook.github.io/relay/)，可以更好地处理客户端的状态和缓存。不过，创建 GraphQL 的服务端接口的难度还较大，且大多数的文档都是面向 Node.js 的。

Netflix 的 [Falcor](https://github.com/Netflix/falcor) 看起来提供了和 GraphQL/Relay 相似的能力，同时还降低了服务端的需求，但它目前尚处于开发者预览状态，尚未应用于实际开发。

所有已知的规范都各有缺陷，有些过于复杂，有些只能处理数据读取而不嗯那个更新，有些和 REST 差异显著。许多开发者选择自己开发，但是还会遇到上述的问题。

我不认为上述有一个完美的解决方案，但我对 API 有一个自己的认知：

- 可预测，遵循一致性协议
- 支持在一次查询中获取多个实体
- 支持更新操作
- 易于调试
- 易于使用

到目前为止，我还没有发现满足上述所有条件的解决方案。

如果你正在使用 RESFful，建议参考 [Swagger](http://swagger.io/) 来编写 API。

## Electron

[Electron](https://github.com/atom/electron) 可以使用前端技术构建桌面程序，github 团队出品的 [Atom](https://atom.io/)编辑器就是基于 Electron 创建的。本质上，Electron 内部封装了一个 Node.js，可以打开 Chrome 窗口渲染 UI，还可以访问操作系统本地的 API，并且没有浏览器中的沙盒机制。开发者可以通过 Electron 打包和分发应用程序。

这是创建跨平台软件最简单的方式，而且还可以利用上述的所有工具。此外，Electron 有完整的文档和活跃的开发社区。

你可能听说过 [nw.js](http://nwjs.io/) 的大名，虽然它已经存在了多年，但相比来说，Electron 更加稳定和易用。

这里有一个基于 [Electron、React 和 hot reload 的模板](https://github.com/chentsulin/electron-react-boilerplate)，尝试一下吧。

## 延伸

下面是一些我在 Twitter 上关注的对象：

建议阅读 Pate Hunt 的 [Learning React](https://github.com/petehunt/react-howto)!

Dan Abramov 发布一系列的视频教程 [Getting started with Redux](https://egghead.io/series/getting-started-with-redux)，强烈推荐！此外，Dan 还发布过一个[关注列表](https://medium.com/@dan_abramov/my-react-list-862227952a8c#.740o0wzee)，比上述更加详细。

Mark Erikson 的 [React/Redux links](https://github.com/markerikson/react-redux-links) 集合也是很好的学习材料。

## 按需使用

JavaScript 的生态环境发展迅速，正日益强大起来。React 的最佳实践正在固化，周边工具的职责和能力也日益清晰。

最重要的事情就是要牢记：保持简洁，按需使用。

如果你的应用程序只有两三屏，那么就无需使用路由系统；如果你正在创建一个单页应用，那么甚至不需要 Redux，只需要 React 自己的 state 属性即可；如果你正在创建一个简单的 CRUD 程序，那么你就不需要使用 Relay；如果你正在学习 ES6，并不需要深入地了解 Async/Await 或装饰器；如果你刚刚开始学习 React，并不需要使用热重载和服务端渲染；如果你刚刚接触 Webpack，你就不需要分离代码和合并多个资源；如果你刚刚学习 Redux，你不需要理解使用 Redux-Form 和 Redux-Sagas。

保持简洁，每次只做一件事！

> 本文根据[@Francois Ward](https://medium.com/@fward)的《[State of the Art JavaScript in 2016](https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b#.x7l3e5j4t)》所译，整个译文带有我们自己的理解与思想，如果译得不好或有不对之处还请同行朋友指点。如需转载此译文，需注明英文出处：[https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b#.x7l3e5j4t](https://medium.com/javascript-and-opinions/state-of-the-art-javascript-in-2016-ab67fc68eb0b#.x7l3e5j4t)。

[!\](filesystem:chrome-extension://mjcnijlhddpbdemagnpefmlkjdagkogk/persistent/images/8559233b30ffb2070404736d31dcac06.png)](https://github.com/pinggod)[南北](http://weibo.com/sunchongsheng)前端开发者，关注性能优化和动效设计，活跃于 github [@pinggod](https://github.com/pinggod) 、微博 [@ping4god](http://weibo.com/sunchongsheng) 和博客 [pinggod.com](http://pinggod.com/)，替身众多。如果你沉醉于 Kairosoft、午时三刻工作室的游戏，请来和我做朋友:)。

如需加载，烦请注明出处：[http://www.w3cplus.com/javascript/state-of-the-art-javascript-in-2016.html](http://www.w3cplus.com/javascript/state-of-the-art-javascript-in-2016.html)

