---
title: webpack 使用教程
date: 2016-07-22
tags: [Models, Webpack]
categories: Frame
---

https://www.zfanw.com/blog/webpack-tutorial.html

概要：
webpack 入门

目录

1 起手式 – 安装 webpack
2 初始化项目
3 webpack 配置
4 实时刷新
5 第三方库
6 模块化
7 打包、构建
我最近大量使用 jspm，但因为它搭建的环境里，测试代码不好写，而项目又有写测试的计划，所以决定改用 webpack。

我还记得我刚接触 webpack 时的心情：零零碎碎。

就没个简单、现成、完整的方案？我是说，我真的不太关心 js 文件要配什么加载器。我只想快一点把开发环境搭起来好干活。总之，几经折腾，我嫌麻烦放弃了 webpack 这个方案。

但今天回头去看，其实它并没那么复杂。

那么，webpack 是什么？

MODULE BUNDLER

它是这么自称的，模块打包器。

在 webpack 里，所有类型的文件都可以是模块，包含我们最常见的 JavaScript，以及 css 文件、图片、json 文件等等。通过 webpack 的各种加载器，我们可以更有效地管理这些文件。

起手式 – 安装 webpack
我们通过 npm 全局安装 webpack：

npm install webpack -g
安装完成后，我们可以使用 webpack 命令，执行

webpack --help
能够查看 webpack 提供的所有命令。

不过，通常建议在项目目录中安装一份本地的 webpack：

npm install webpack --save-dev
如果觉得 npm 安装太慢，可以尝试 npm 的替代工具 ied – 我的使用经历，它的速度比 npm 快太多了。

初始化项目
安装好 webpack 后，我们要怎么开始一个项目？

如果你用过 grunt.js、gulpjs 一类工具，它们可以借助 yeoman 来初始化项目。webpack 的情况不太一样，我们可以把它当作 node.js 项目来初始化。当然，借用一些模板会更省事，比如 react transform boilerplate。

但这里还是聊聊如何手动初始化一个 webpack 项目。

创建一个 package.json 文件，用于保存项目版本、依赖关系等

npm init
在当前目录下安装 webpack

npm install webpack --save-dev
之后，我们的项目下有两个内容：

package.json 文件
node_modules 文件夹
我们还需要一个 index.html 文件，示例如下：

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>webpack 教程</title>
</head>
<body>
</body>
</html>
现在，我们可以通过 live-server 等访问到 index.html 页面。

目前页面上还是一片空白，除了一个标题。

webpack 配置
在单页面应用里，项目通常会有一个入口（entry）文件，假设是 main.js，我们通过配置 webpack 来指明它的位置。

首先，在项目根目录新建一个 webpack.config.js，这是 webpack 默认的配置文件名称，添加以下内容：

module.exports = {
  entry: './main.js'
};
这时在项目根目录执行 webpack，会提示我们，

Output filename not configured.

因为我们只是设定了入口（entry），还没有设定一个输出文件的路径与名称。

在 webpack.config.js 中添加一个 output：

module.exports = {
    entry: './main.js',
    output: {
        path: __dirname, // 输出文件的保存路径
        filename: 'bundle.js' // 输出文件的名称
    }
}
现在在项目里执行 webpack 命令，我们的根目录下会多出一个 bundle.js 文件：

webpack build

接下来，在 index.html 中引用 bundle.js 文件：

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>webpack 教程</title>
</head>
<body>
  <script src="./bundle.js"></script> <!-- 在 index.html 文件中添加这一行代码 -->
</body>
</html>
大功告成。

这是 webpack 与 browserify 一类工具的特点，它们在 HTML 文件中直接引用构建后的 js 文件，而不是源文件。

当然，这可能会引发性能问题，毕竟，如果每一点文件修改都会导致整个 bundle.js 文件重新构建的话，碰上大一点的项目，有几千个源文件要编译，编译速度降下来是必然的。webpack 有它的解决办法，具体参见它的文档。

实时刷新
在 html 文件中引用 bundle.js 文件后，我们有几个问题需要解决。

main.js 或它所引用的模块的变化如何通知 webpack，重新生成 bundle.js？

非常简单，在根目录下执行 webpack --watch 就可以监控目录下的文件变化并实时重新构建。

上面只是实时构建，我们该如何把结果通知给浏览器页面，让 HTML 页面上的 bundle.js 内容保持最新？

webpack 提供了 webpack-dev-server 解决实时刷新页面的问题，同时解决实时构建的问题。

​

安装 webpack-dev-server

在全局环境中安装 webpack-dev-server：

npm install webpack-dev-server -g
在项目根目录下执行命令：

$ webpack-dev-server
这样，我们就可以在默认的 http://localhost:8080 网址上打开我们的 index.html。

此时，我们可能认为事情是按以下顺序发生的，

js 文件修改
webpack-dev-server 监控到变化
webpack 在内存中重新构建 bundle.js
webpack-dev-server 保证页面引用的 bundle.js 文件与内存中一致
但不幸的是，我们「自以为是」了。http://localhost:8080/index.html 对 js 文件的变化无动于衷。

webpack-dev-server 提供了两种模式用于自动刷新页面：

iframe 模式

我们不访问 http://localhost:8080，而是访问 http://localhost:8080/webpack-dev-server/index.html

inline 模式

在命令行中指定该模式，webpack-dev-server --inline。这样 http://localhost:8080/index.html 页面就会在 js 文件变化后自动刷新了。

以上说的两个页面自动刷新的模式都是指刷新整个页面，相当于点击了浏览器的刷新按钮。

webpack-dev-server 还提供了一种 --hot 模式，属于较高阶的应用。

第三方库
webpack 并不是包管理器，所以如果我们要使用第三方库，需要借助 npm。比如，在项目里安装 jQuery：

npm install jquery --save
这样我们在当前项目目录下安装了 jquery，并将它写入 package.json 里的依赖里。

模块化
模块化 JavaScript

如果我想用 ES6 的方式引入某个 es6 模块，比如：

import $ from 'whatever';
怎么办？浏览器目前还不提供原生支持，webpack 原生也仅支持 CommonJS 的那种写法，但借助 babel-loader ，我们可以加载 es6 模块：

安装 babel-loader

npm install babel-loader babel-core babel-preset-es2015 --save-dev
配置 webpack.config.js

在 module.exports 值中添加 module：

module.exports = {
entry: {
    app: ['./main.js']
},
output: {
    filename: 'bundle.js'
},
module: {
    loaders: [{
        test: /\.js$/,
        loaders: ['babel?presets[]=es2015'],
        exclude: /node_modules/
    }]
}
}
这样我们就可以在我们的 js 文件中使用 ES6 语法，babel-loader 负责翻译。

上面的方法，是在 webpack.config.js 文件中给某一类型文件定义加载器，我们还可以在代码中直接指定：

import $ from 'babel!whatever'
当然，前一种方法会更优雅。

CSS 加载器

我们可以按传统方法使用 CSS，即在 HTML 文件中添加：

<link rel="stylesheet" href="style/app.css">
但 webpack 里，CSS 同样可以模块化，使用 import 导入。

因此我们不再使用 link 标签来引用 CSS，而是通过 webpack 的 style-loader 及 css-loader。前者将 css 文件以 <style></style> 标签插入 <head> 头部，后者负责解读、加载 CSS 文件。

安装 CSS 相关的加载器

npm install style-loader css-loader --save-dev
配置 webpack.config.js 文件

{
// ...
module: {
    loaders: [
        { test: /\.css$/, loaders: ['style', 'css'] }
    ]
}
}
在 main.js 文件中引入 css

import'./style/app.css';
这样，在执行 webpack 后，我们的 CSS 文件就会被打包进 bundle.js 文件中，如果不想它们被打包进去，可以使用 extract text 扩展。

重启 webpack-dev-server
模块化 CSS

上一步里，我们 import 到 JavaScript 文件中的 CSS 文件中的 CSS 在打包后是仍然是全局的，也就是说，我们只是换了种加载 CSS 的方式，在书写 CSS 的时候，还是需要注意使用命名规范，比如使用 BEM，否则全局环境 CSS 类的冲突等问题不会消失。

这里，webpack 做了一个模块化 CSS 的尝试，真正意思上的「模块化」，即 CSS 类不会泄露到全局环境中，而只会定义在 UI 模块内 – 类似 react.js 这类模块，或者 web components。

autoprefixer

我们在写 CSS 时，按 CSS 规范写，构建时利用 autoprefixer 可以输出 -webkit、-moz 这样的浏览器前缀，webpack 同样是通过 loader 提供该功能。

安装 autoprefixer-loader

npm install autoprefixer-loader --save-dev
配置 webpack.config.js

loaders: [{
test: /\.css$/,
loader: 'style!css!autoprefixer?{browsers:["last 2 version", "> 1%"]}',
//...
}]
重启 webpack-dev-server

假如我们在 CSS 中写了 body { display: flex; } 规则，再查看 bundle.js 文件的话，我们能看到类似如下的代码：

body {\n\tdisplay: -webkit-box;\n\tdisplay: -webkit-flex;\n\tdisplay: -ms-flexbox;\n\tdisplay: flex;\n}
图片

图片同样可以是模块，但使用的是 file loader 或者 url loader，后者会根据定义的大小范围来判断是否使用 data url。

import loadingIMG from 'file!../img/loading.gif'

React.render(<img src={loadingIMG} />, document.getElementById('app'));
打包、构建
项目结束后，代码要压缩、混淆、合并等，只需要在命令行执行：

webpack
即可，webpack 根据 webpack.config.js 文件中的配置路径、构建文件名生成相应的文件。通常，我们会额外定义一个专门用于生产环境的配置文件，比如 webpack.production.config.js，其中可以做许多代码优化。

作者：陈 三
时间：2015-08-28
主题：webpack
分类：前端开发