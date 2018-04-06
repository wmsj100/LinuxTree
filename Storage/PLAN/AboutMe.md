# 联系方式

- 手机：18700468541
- Email：wmsj100@hotmail.com
- 微信号：wanmeikaixin
---

# 个人信息

 - 王浩/男/1990
 - 本科/黑龙江八一农垦大学工业设计
 - 工作年限：4年
 - 技术博客：[简书](https://www.jianshu.com/u/c179b17d547a)
 - Github：[https://github.com/wmsj100](https://github.com/wmsj100/)
 - 期望职位：Linux运维工程师
 - 期望薪资：税前月薪9k~，特别喜欢的公司可例外
 - 期望城市：西安
---

# 工作履历

## 软通动力技术服务有限公司 （ 2016年11月 ~ 至今 ）

### Manage One SC 6.0-6.1 （ 2016年11月 ~ 2017年8月）
- SC6.0-6.1这是华为的私有云项目，我在此项目负责了VDC（Virtual Data Center）的用户模块和订单审批模块；
- 用户模块涉及到用户的创建、修改、关联解关联资源、删除等流程并且区分用户角色，有管理侧和租户侧俩套环境；
- 订单审批涉及到用户对vdc配额的申请和审批流程，也是区分管理侧和租户侧，我做的是管理侧的审批流程；
- 在做用户的过程中没有像其它模块一样简单按照管理侧和租户侧分别创建页面，而是提取了可用的公共页面和方法，在提取过程中涉及到角色区分所以主动去对接了后台和框架的人，在这个过程中对SC的角色和框架有了更深入的认识，而且总代码量减少了2/3，减少了因方案变更造成的代码修改量，得到了同事和领导的肯定。
- 在做订单审批时候因为管理侧的前端框架无法实现租户侧的后台表格排序，导致一个流程在俩套界面体验不统一，我主动尝试在框架的基础上封装方法实现后台排序的功能，期间虽然有出过问题单，但最终完美实现了效果，得到了领导表扬；

### Manage One SC 6.3微服务 （2017年8月 ~ 至今）
- SC项目到6.3版本采用了微服务开发模式
  - 在开发过程中每个服务独立开发部署，互不干扰；
  - 部署过程采用了管道化的自动部署，极大的提升了开发部署效率，缩减了联调时间，避免了像6.0和6.1版本开发过程中个别模块出错阻塞全体模块联调的问题；
  - 开发环境采用了多节点部署，环境响应速度有了质的提升；
  - 每个服务采用单独数据库，而且数据库在开发过程中不删库，在模块迭代过程中避免了很多重复性工作，比如用户的创建和资源的关联申请等；
  - 代码管理工具从SVN切换到Git，对于本地多版本多分支开发更加灵活；
  - 对于代码检视更加重视，并且引入专门代码管理平台，使代码提交更加规范化；每个人都可以检视别人代码，提高了错误代码的暴光率，加固了代码质量
  - 微服务开发每个模块独立部署，对于前端要引用的框架和第三方依赖通过专门服务（ConsoleHome）统一管理；其它模块使用时候通过ConsoleHome来调用，完全避免了像6.0和6.1版本时候出现的管理侧和租户侧框架版本不一致，版本升级不及时的问题；

- Manage One SC 6.3 VDC用户模块
  - 采用微服务开发模式后我刚接手的还是熟悉的用户模块，在项目开发模式切换的同时前端框架也进行了大版本升级，控件的API调用接口和方法变更，影响到所有模块；而且代码管理工具也变更到Git，这一系列因素增加了新项目的上手难度；我在短时间内掌握了新框架的使用后因为之前有Git使用经验，马上在小组内开展了新框架和Git的使用心得交流会议，大大缩短了组内成员的学习时间，留出更多的时间去了解服务部署和架构方面的知识。这一系列举动赢得了同事和领导的高度认可；
  - 在初期项目交付完后UCD针对当前环境的页面进行了全模块无死角检视，提出了一系列修改建议和新的交互规范；我在高质量完成自己模块页面整改的同时主动申请了全模块添加Enter键需求。这个需求的预期是使所有模块的不同场景交互操作统一，通过Enter键代替鼠标完成提交或确认等操作，提高了交互体验缩短了操作时间；但难点是不同模块的场景不同，页面不同，有弹框，有进度条页面，有单独页面，而且还涉及到页面嵌套问题，还要为封装的方法预留自定义途径；针对这些困难我在咨询了专家建议和同事进行过多次技术交流后在时间节点前圆满完成任务，获得项目SE的技术表扬，并且在全团队输出了文档。

- Manage One SC 6.3 登录模块
  - 在UCD的另一次整改中我接手了登录模块，之前没有接触过，这个模块很特殊，有很多环境设置的逻辑，还有很多历史遗留代码，而可视的页面又很少。
  - 我在仔细阅读了代码并且和后台进行了多次尝试性修改后发现框架升级需要前后台配合修改的代码量太大，而可感知的收益却很小；
  - 我主动拉通相关人员称述了我的观点“框架不升级UI效果升级”，会议通过了我的表述。这个技术难点是旧框架无法实现新框架的交互效果，需要基于旧框架自己封装方法，还要避免兼容性问题和保证交互体验的一致。我在参考了新框架的实现原理后自己封装并且实现了像素级别的模仿，保证了全系统的无差异体验。这个过程提升我阅读源码能力同时也增加了我对自己的技术自信。

- Manage One SC 6.3 Iaas模块
  - 之前做的是私有云项目，现在参与的是混合云项目，在这个项目参与开发的时间不是很多，主要是学习基础业务
  - 学习了私有云和混合云的特点，知道了云服务的三种计算模式SaaS/PaaS/IaaS，在参与混合云的开发过程中对项目有了更全面的认识
  - 当前项目是IaaS模式，以基础资源为服务，而基础资源包括云主机、云硬盘、路由、负载均衡等，我深入参与的是云硬盘服务
  - 在做VPN整改的过程中学习了很多网络知识，知道了路由、VPN、网关、负载均衡等概念

### 转行理由
- 从SC6.0版本UI补丁需要通过shell卸载环境沙箱开始接触到linux然后就被它吸引了，那时开始自学linux，入门教程是鸟哥的私房菜；后来因为手头电脑太旧，跑不动Win7，索性就安装了CentOS7，彻底进入linux世界。
- SC到6.3版本转型微服务开发模式，环境部署只需要在云龙简单勾选一些参数然后点击确认按钮就会自动部署，此时完全被linux的能力折服了，惊叹自动化还可以做到如此程度，因为之前6.0时候搭建一套环境是很痛苦的；
- 我认为微服务模式之所以可行一定是依靠强有力的运维团队打造强大的工具出来，每一次在云龙上部署环境都会感激运维团队的付出。
- 开发微服务过程中经常需要通过shell手动重启微服务，随着对linux的学习的深入，开始能看懂一些脚本，很简单的几行代码却可以做这么多工作，然后就开始意识到linux才是我的方向。
- 决定了linux方向，然后就又系统的过了一遍基础知识点，简单的看过python、sql语法，写过几个简单的shell脚本。
- 我写过一个批量更新微服务包代码的脚本，因为微服务开发模式每个人本地会有很多服务包代码，每次都需要手动更新代码，有时候还因为忘记更新代码而导致代码提交失败，通过分享我自己的脚本可以正在在工作中帮助到同事还是很自豪的。

## 上海婚淘淘科技有限公司 （ 2014年3月 ～ 2016年9月 ）

### 婚淘淘电商平台
- 这是一个创业型公司的项目，以影楼助手软件为突破点做到婚嫁行业最大的O2O平台；我因为看重它的互联网平台概念所以进入公司做平面设计、全景制作工作。
- 做了半年左右的设计后偶然接触到运维，然后就开始转到运维部门，做的工作是帮助客户管理后台数据进行远程技术协助。因为公司前期还是以销售软件为主，客户的所有数据都存储在公司的服务器，影楼通过付费模式委托公司协助管理数据。
- 因为工作中有很多操作是重复性的规律性质的操作，我通过借助软件写了很多批处理脚本，让工作效率实现了数量级的提升，而且出错更少，此时就开始意识到编程的重要性了，决心要学习编程。
- 随着对互联网接触的日渐深入然后就开始自学HTML、CSS；后来专门报名了远程网络培训，系统的学习了前端知识，为后来转型前端做好了铺垫；

### 离职理由
- 首先意识到太原的互联网氛围不好，编码对IDE严重依赖，使用的.NET语言和框架不是我感兴趣的，window服务器环境和主流脱节，技术更新严重滞后；虽然是互联网公司，但是公司内部流程还是很传统，而且在俩年多时间我尝试了公司没有几乎所有技术岗位，最后选中的编程领域公司无法满足我的需求，所以就想到离职，换一个互联网氛围更好的环境。

## 山西瑞飞科技有限公司 （ 2013年7月 ～ 2014年2月 ）

### 豆制品生产线项目
- 这是一个机械制造企业，我所在的技术部门主要做豆制品生产线，我的工作是按照客户的要求绘制CAD图纸，如果方案敲定后作出ProE三维模型。
- 因为在学校就一直迷恋三维模型绘制，所以常见的三维软件像CATIA/ProE/SolidWorks都使用的得心应手，我会经常组织项目技术人员进行三维软件的学习。
- 在这里的成长很大，从前期看不懂复杂CAD图纸，经常因为尺寸问题导致车间生产的设备不满足客户要求。到后期我可以一个人很熟练的按照客户要求绘制图纸，并且提醒客户设计的缺陷；自己绘制的三维模型也经常获取公司内的最佳设计奖金。
- 有一段时间因为工期紧张，我完全呆在车间和师傅们一起制作泡豆设备，用差不多一个月时间学会了氩弧焊，并且可以徒手切割钢材和钢材后期抛光打磨，这样的学习正常的学徒需要三个月时间；这一段经历让我对于接触陌生领域不再恐惧，对自己的学习能力更加自信，只要我想学，就可以做好。

### 离职理由
- 在随公司技术团队参加展会期间接触到了互联网公司，而且正好当时到处都在说互联网转型的话题，所以想进入互联网企业，而且在短时间内我看不到公司转型互联网的意愿。
- 豆制品流水线设备已经有很成熟的设计方案了，不需要进行太多主观设计，基本都是拿之前的图纸进行小范围的修改即可，而我已经把公司每一种型号的设备都做了三维模型；在技术方面的提升已经到了尽头，而且企业也无法承受大规模创新可能导致的设备积压，所以内心也萌生了离职的念头。
---

# 开源项目和作品

## 开源项目

  - [myStudy](https://github.com/wmsj100/myStudy): 这是我自己在编程领域的摸爬滚打过程，有涉猎的语言，现在主攻`Linux`
  - [myapp](https://github.com/wmsj100/myapp): 自己写的电商页面

## 技术文章

- [我对BFC的理解](https://www.jianshu.com/p/76484dff1cb5)

# 技能清单

*以下均为我熟练使用的技能*

- Web框架：EasyUI/MiniUI/jQuery UI/TinyUI(华为专用)
- 前端框架：Bootstrap/AngularJS/EmberJS/HTML5/Backbone
- 前端工具：Bower/Gulp/LeSS/Echarts
- 编程语言：JavaScript/CSS/Python/Shell
- 数据库相关：MySQL
- 操作系统：Linux/Windows
- 版本管理、文档和自动化部署工具：Svn/Git
---
# 致谢
感谢您花时间阅读我的简历，期待能有机会和您共事。