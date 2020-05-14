---
title: DotNet_to_Linux
date: 2020-05-14 18:38:17
modify: 
tags: [Notes]
categories: Windows
author: wmsj100
email: wmsj100@hotmail.com
---

# DotNet_to_Linux

## 概要

1 .NET简介
.NET 是一个通用开发平台。 它具有几项关键功能，例如支持多种编程语言、异步和并发编程模型以及本机互操作性，可以支持跨多个平台的各种方案。
.NET 支持多种编程语言。 .NET 实现可实现公共语言基础结构 (CLI)，除其他事项外，它指定与语言无关的运行时和语言互操作性。 这意味着可选择任意 .NET 语言在 .NET 上生成应用和服务。
Microsoft 积极开发和支持三种 .NET 语言：C#、F# 和 Visual Basic。
2014年11月12日，微软宣布将完全开放.NET框架的源代码，并提供给Linux和macOS使用。
官方链接：https://docs.microsoft.com/zh-cn/dotnet/

2 .NET 体系结构组件
.NET 应用开发用于并运行于一个或多个 .NET 实现 。 .NET 实现包括 .NET Framework、.NET Core 和 Mono。 .NET 的所有实现都有一个名为 .NET Standard 的通用 API 规范。
2.1 .NET Standard
.NET Standard 是一组由 .NET 实现的基类库实现的 API。 更正式地说，它是构成协定统一集（这些协定是编写代码的依据）的特定 .NET API 组。 这些协定在每个 .NET 实现中实现。 这可实现不同 .NET 实现间的可移植性，有效地使代码可在任何位置运行。
.NET Standard 也是一个目标框架。 如果代码面向 .NET Standard 版本，则它可在支持该 .NET Standard 版本的任何 .NET 实现上运行。
下表列出了支持每个 .NET Standard 版本的最低平台版本。 这意味着所列平台的更高版本也支持相应的 .NET Standard 版本。 例如，.NET Core 2.2 支持 .NET Standard 2.0 及更低版本。

2.2 .NET 实现
Microsoft 积极开发和维护的主要 .NET 实现有 4 个：.NET Core、.NET Framework、Mono 和 UWP。
2.2.1 .NET Core
.NET Core 是 .NET 的跨平台实现，专用于处理大规模的服务器和云工作负荷。 可在 Windows、macOS 和 Linux 上运行。 它实现 .NET Standard，因此面向 .NET Standard 的代码都可在 .NET Core 上运行。 ASP.NET Core、Windows 窗体和 Windows Presentation Foundation (WPF) 都在 .NET Core 上运行。
2.2.2 .NET Framework
.Net Framework 是自 2002 年起就已存在的原始 .NET 实现。 4.5 版以及更高版本实现 .NET Standard，因此面向 .NET Standard 的代码都可在这些版本的 .NET Framework 上运行。 它还包含一些特定于 Windows 的 API，如通过 Windows 窗体和 WPF 进行 Windows 桌面开发的 API。 .NET Framework 非常适合用于生成 Windows 桌面应用程序。
2.2.3 Mono
Mono 是主要在需要小型运行时使用的 .NET 实现。 它是在 Android、macOS、iOS、tvOS 和 watchOS 上驱动 Xamarin 应用程序的运行时，且主要针对小内存占用。 Mono 还支持使用 Unity 引擎生成的游戏。
它支持所有当前已发布的 .NET Standard 版本。
以前，Mono 实现更大的 .NET Framework API 并模拟一些 Unix 上最常用的功能。 有时使用它运行依赖 Unix 上的这些功能的 .NET 应用程序。
Mono 通常与实时编译器一起使用，但它也提供在 iOS 之类的平台使用的完整静态编译器（预先编译）。
2.2.4 通用 Windows 平台 (UWP)
UWP 是用于为物联网 (IoT) 生成新式触控 Windows 应用程序和软件的 .NET 实现。 它旨在统一可能想要以其为目标的不同类型的设备，包括电脑、平板电脑、电话，甚至 Xbox。 UWP 提供许多服务，如集中式应用商店、执行环境 (AppContainer) 和一组 Windows API（用于代替 Win32 (WinRT)）。 应用可采用 C++、C#、Visual Basic 和 JavaScript 编写。 使用 C# 和 Visual Basic 时，.NET API 由 .NET Core 提供。
2.3 .NET 运行时
运行时是用于托管程序的执行环境。 操作系统属于运行时环境，但不属于 .NET 运行时。 下面是 .NET 运行时的一些示例：
.NET Framework 公共语言运行时 (CLR)
.NET Core 核心公共语言运行时 (CoreCLR)
适用于通用 Windows 平台的 .NET Native
用于 Xamarin.iOS、Xamarin.Android、Xamarin.Mac 和 Mono 桌面框架的 Mono 运行时

.NET的跨平台实现只有.NET Core和Mono。

3 .NET移植.NET Core
.NET Core now officially is the future of .NET. It started for most part with a re-write of the ASP.NET MVC framework and console applications, which of course includes server applications.
-- stackoverflow.com
上面内容阐述了.NET Core是.NET的未来，而且随着.NET 5的推出会整合当前的各个.NET的实现，真正实现跨平台.
What used to be the full .NET Framework will linger around in maintenance mode as Full .NET Framework 4.8.x for a few decades, until it will die
-- stackoverflow.com
.NET Framework 将会在维护模式下持续数十年然后直到版本生命周期结束。
现有.NET项目迁移到.NET Core前需要评估如下问题
3.1 不可用于.NET Core的第三方库或NuGet包
确认当前项目是否有使用.NET Core 的第三方库或 NuGet 包，如果有使用需要评估这些库是否支持跨平台，是否开源，是否可以获取源代码，是否有开源类似实现。
3.2 不可用于.NET Core的.NET技术
某些 .NET Framework 技术在 .NET Core 中不可用。 其中一些技术可能在更高版本的 .NET Core 中可用。 但其他技术不会应用于 .NET Core 面向的新应用程序模式，因此可能永远不可用。 以下列表显示无法在 .NET Core 中找到的最常见技术：


1)ASP.NET Web 窗体应用程序：ASP.NET Web 窗体仅在.NET Framework 中可用。 ASP.NET Core 不能用于 ASP.NET Web 窗体。 目前没有将 ASP.NET Web 窗体引入 .NET Core 的计划。
2)ASP.NET网页应用程序：ASP.NET 网页未包含在 ASP.NET Core 中。
3)WCF服务的实现。 虽然 WCF 客户端库可从 .NET Core 使用 WCF 服务，WCF 服务器实现目前只在 .NET Framework 上可用。 这种情况虽然不属于 .NET Core 当前计划，但将来会考虑这点。
4)工作流相关的服务：Windows Workflow Foundation (WF)、工作流服务（WCF + 单个服务中的 WF）和 WCF Data Services（以前称为“ADO.NET Data Services”）仅在 .NET Framework 上可用。 目前没有将这些技术引入 .NET Core 的计划。
5)语言支持：.NET Core 目前支持 Visual Basic 和 F#，但不是所有项目类型都支持。 有关支持的项目模板列表，请参阅 dotnet new 的模板选项。

此外还要确保代码不依赖WinAPI调用，Windows-dll-pinvokes，COM-Components，不区分大小写的文件系统，默认系统编码（代码页）并且没有目录分隔符问题。

排除上面条件之后具体的迁移实施请参考下面文档

4
.NET移植Mono
Mono项目早在2005年就开始，是作为.NET Framework的Linux实现。
Mono包含Web-Forms、Winforms、MVC、Olive，并且支持的IDE实现有MonoDevelop
Mono在Linux的常见搭配策略是ASP.NET-WebForms + WinForms + ASP.NET-MVC 应用。
Mono当前已经把注意力从Linux市场转移到移动市场。
Mono项目移植的前提是要确保代码不依赖WinAPI调用，Windows-dll-pinvokes，COM-Components，不区分大小写的文件系统，默认系统编码（代码页）并且没有目录分隔符问题。
此外在.NET项目的代码还需要做大量适配工作才可以移植，并不能直接拿到Mono运行。
Since Mono is quite unstable and slow (for web applications), I wouldn't recommend it anyway. Try image-processing on .NET core, e.g. WebP or moving GIF or multipage-tiff or writing text on an image, you'll be nastily surprised.
-- stackoverflow.com
当前Mono有不稳定和运行缓慢的表现，尤其是对于web服务，所以不建议web服务迁移到Mono。

5 总结
.NET项目的跨平台实现当前有俩种方案，分别是.NET Core和Mono.
.NET Core是微软主推的实现并且会成为.NET的未来。
Mono现在已经完全专注于移动领域，对于服务器端，现在有不稳定和运行缓慢的问题，尤其是对于web服务，不建议使用。
.NET Core和Mono的迁移有很多前提条件需要满足，而且在具体实施迁移过程中，需要对业务代码做大量更改才可能实现迁移。
迁移完成后需要对业务进行全量的测试，包括功能和性能方面。

6 参考资料
.NET官方文档：
https://docs.microsoft.com/zh-cn/dotnet/standard/components
stackoverflow
https://stackoverflow.com/questions/37738106/net-core-vs-mono
