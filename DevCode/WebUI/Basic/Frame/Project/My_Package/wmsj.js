	var wmsj = new Object();	// 库容器规划
// 
// 封装一个函数,计算wmsj封装的函数的数量,并且把函数名称以数组的形式导出.
// 
	wmsj.eventUtil = {	// 事件函数包
		addHandler: "这是一个事件封装函数。",
		removeHandler: "移除事件",
		getEvent: "获取event",
		getTarget: "获取target",
		preventDefault: "阻止默认事件",
		stopPropagation: "阻止事件冒泡",
		getClipboardText: "获取剪贴板数据",
		setClipboardText: "添加文本到剪贴板",
		isIE: "判断ie浏览器",
		beforeUnload: "卸载页面时候弹出警告框",
		assert: "抛出错误",
		urlQueryString: "处理url字符串除hostname之外的字符串,包括search(?)和hash(#)",
		addURLParam: "主要用于ajax的get方法给url添加查询名值对",
		ajax: "封装的ajax函数,支持`get和post俩种方法",
		isBoolean: "判断值val是不是原生布尔值",
		isString: "判断值val是不是原生字符串",
		isNumber: "判断值val是不是原生数值",
		isObject: "判断值val是不是原生对象",
		isArray: "判断值val是不是原生数组对象",
		isFunction: "判断值val是不是原生函数对象",
		isRegExp: "判断值val是不是原生正则对象",
		isNode: "判断是不是DOM节点",
		isEqualCount: "选择判断 -args--参数总数与期望总数的比较--和--val--参数之间的数组长度比较",
		bindFunc: "这是一个把函数fn绑定到环境context的函数,并且包含函数柯里化",
		createStaticObj: "创建防篡改对象",
		toStaticObj: "把已经存在的对象(对象或者数组)按照需求转换为防篡改对象(扩展, 封闭, 冻结)"
	}; 

	wmsj.sizeUtil = {		// 尺寸函数包
		scrollTop: "获取页面滚动距离"
	};

	wmsj.mouseUtil = {	// 鼠标事件存储器
		clientX: "获取鼠标的座标",
		clientY: "获取鼠标的座标",
		judgeKeyPress: "鼠标按键同时捕获键盘的按键",
		getRelatedTarget: "针对mouseover和mouseout判断相关元素(鼠标进入和离开的元素目标)",
		getButton: "判断鼠标按键的值",
		getCharCode: "获取目标的ASCII码",
		getChar: "把ASCII码转换为字符"
	};	

	wmsj.modelUtil = {	// 功能模块封装
		dom: {	// dom结构函数封装
			conTextMenu: "自定义右键菜单栏",
			checkDomLoaded: "检查dom的dom是否加载完成 在onload事件之前执行",
			eventProxy: "事件代理函数",
			formFocus: "表单的第一个控件自动获取焦点",
			formLimitedInput: "限制输入字符，是单个字符的限制，所以正则不需要使用-g",
			formLimitedPaste: "限制对文本框input的复制内容",
			inputDefaultValue: "如果文本框的内容没有变化，获取焦点时候内容为空，事情焦点恢复默认值",
			serialize: "获取表单form的提交数据,表单序列化",
			tabForward: "当文本框输入字符超过maxLength时候，自动把焦点跳转到下一个文本框",
			formRequired: "当input文本框设置-required-时候，ie浏览器会触发这个事件，ie不支持required",
			preventRepeatSubmit: "页面的所有表单form都可以通过冒泡到document触发事件禁止表单重复提交",
			getSelectedText: "获取选中的文本 调用的方法如下：",
			selectText: "选中文本框中的部分文字，只是界面选中",
			DragDrop: "拖动框封装函数，被拖动元素必须有-class值- draggable -DragDrop.enable()方式进行调用",
			getStyleValue: "获取页面节点node的-css-style-的属性值",
			CookieUtil: "封装了设置cookie的简单方法，有get, getAll, set, setAll, unset, unsetAll",
			setLinkTitle: "设置自定义的链接提示框，清除默认的值，需要设置class = tooltip"
		}, 
		func: {		// 功能性函数封装
			nodeListBind: "适用于一些节点列表绑定的相同的事件，而事件也只依赖于event的传递",
			toPostMessage: "跨域发起(postMessage)请求的方法",
			listenMessage: "目标源接收到postMessage并且验证之后发送数据给请求者",
			JSONP: "jsonp-- 跨域方法",
			windowName: "跨域 -- 使用window.name",
			chunk: "数组分块技术,一旦某个函数需要花50ms以上的时间执行，就可以考虑把循环分块",
			throttle: "函数节流，多用于`onresize, onscroll等高耗能操作",
			inheritPrototype: "获取superType的原型prototype并且赋值给subType.prototype",
			EventTarget: "自定义事件容器"
		}	
	};

	wmsj.jQuery	= {

		
	};

	wmsj.codeUtil = {
		dom: {
			eventValueLost: "定时器设置的闭包函数在给event添加属性value时候event已经不存在了",
			cors: 'php头部添加--header("Access-Control-Allow-Origin:http://a.com");',
			hoverEvent: "这个效果是鼠标hover时候，显示下面的元素，同时自己改变颜色。"
		},
		func: {
			safeCopeFunc: "这是一个安全的继承链，fn的this是安全的。",
			countFunc: "setTimeout模拟setInterval的效果",
			userDefinedEventExample: "自定义事件的范例",
			DragDropExample: "这是一个拖拽框的自定义事件效果，调用方法--DragDrop.enable();",
			inheritChain: "关于使用自定义事件-EventTarget-的俩种方法，直接使用效果和继承原型链，"
		},
		jQuery: {
			openFolder: "商品的展开和折叠例子"
		}
	}

	wmsj.abandon = {
		func: {
			argsCount: "判断传入的参数和期望的参数数目是否相同，不同就弹出警告，相同返回true"
		},
		dom: {

		}
	}

	// 这是一个事件封装函数。
	wmsj.eventUtil = {
		addHandler: function(node, eventType, handler) { // 添加事件
			if (node.addEventListener) {
				addHandler = function(node, eventType, handler) {
					node.addEventListener(eventType, handler, false);
				}
			} else if (node.attachEvent) {
				addHandler = function(node, eventType, handler) {
					node.attachEvent("on" + eventType, handler);
				}
			} else {
				addHandler = function(node, eventType, handler) {
					node["on" + eventType] = handler;
				}
			}
			return addHandler(node, eventType, handler);
		},

		removeHandler: function(node, eventType, handler) { // 移除事件
			if (node.removeEventListener) {
				removeHandler = function(node, eventType, handler) {
					node.removeEventListener(eventType, handler, false);
				};
			} else if (node.detachEvent) {
				removeHandler = function(node, eventType, handler) {
					node.detachEvent("on" + eventType, handler);
				}
			} else {
				removeHandler = function(node, eventType, handler) {
					node["on" + eventType] = null;
				}
			}
			return removeHandler(node, eventType, handler);
		},

		// 获取事件event
		getEvent: function(event) {
			if (event) {
				getEvent = function(event) {
					return event;
				}
			} else {
				getEvent = function(event) {
					return window.event;
				}
			}
			return getEvent(event);
		},

		// 获取事件目标
		getTarget: function(event) {
			if (event.target) {
				getTarget = function(event) {
					return event.target;
				}
			} else {
				getTarget = function(event) {
					return event.srcElement;
				}
			}
			return getTarget(event);
		},

		// 阻止默认事件
		preventDefault: function(event) {
			if (event.preventDefault) {
				preventDefault = function(event) {
					event.preventDefault();
				}
			} else {
				preventDefault = function(event) {
					window.event.returnValue = false;
				}
			}
			return preventDefault(event);
		},

		// 阻止事件冒泡
		stopPropagation: function(event) {
			if (event.stopPropagation) {
				stopPropagation = function(event) {
					event.stopPropagation();
				}
			} else {
				stopPropagation = function(event) {
					window.event.cancleBubble = true;
				}
			}
			return stopPropagation(event);
		},

		// 获取剪贴板数据
		getClipboardText: function(event) {
			var clipboardData = (event.clipboardData || window.clipboardData);
			return clipboardData.getData("text");
		},

		// 添加文本到剪贴板
		setClipboardText: function(event, value) {
			if (event.clipboardData) {
				return event.clipboardData.setData("text/plain", value);
			} else if (window.clipboardData) {
				return window.clipboardData.setData("text", value);
			}
		},

		
		// 判断是否是ie浏览器 -- 这个方法在没办法时候再用
		isIE: function() {
			if (navigator.userAgent.indexOf("MSIE") > -1) {
				isIE = function() {
					return true;
				}
			} else {
				isIE = function() {
					return false;
				}
			}
			return isIE();
		},

		// 卸载页面时候弹出警告框
		// 这个字符串str只会在ie中出现
		beforeUnload: function(str) {		
			wmsj.eventUtil.addHandler(window, "beforeunload", function(event) {  // 把事件监听在window上
				var message = String(str);  // 确保是字符串
				event = wmsj.eventUtil.getEvent(event);
				event.returnValue = message;	// 设置ie中的提示字符串
				return message;
			});
		},

		// 抛出错误
		// condition -- 表示控制的条件
		// message -- 表示抛出的错误信息
		assert: function(condition, message) {
			if (!condition) {		// 如果条件不成立
				throw new Error(message);		// 创建并抛出错误
			}
		},

		// 处理url字符串除hostname之外的字符串,包括search(?)和hash(#)
		// 如果想要解码就使用decodeURIComponent(url),参数为通过函数处理之后的字符串
		urlQueryString: function(url) {
			var searchNum = url.indexOf("?"), // 获取search字符串
				hashNum = url.indexOf("#"), // 获取hash字符串
				hostname = "", // 获取hostname
				query = ""; // 获取要处理的字符串
			if (searchNum > -1) { // 如果有search
				if (searchNum < hashNum) { // 如果同时还有hash字符串,并且?在#之前
					hostname = url.substring(0, searchNum); // 以?为分界符获取hosename字符串
					query = url.substring(searchNum); // 以?为分界符获取之后的字符串
					return hostname + encodeURIComponent(query); // 返回处理后的字符串
				} else { // 如果同时还有hash,并且#在?之前
					hostname = url.substring(0, hashNum); // 以#为分界符获取hosename字符串
					query = url.substring(hashNum); // 以#为分界符获取之后的字符串
					return hostname + encodeURIComponent(query); // 返回处理后的字符串
				}
			} else if (searchNum === -1 && hashNum > -1) {	// 没有？只有#时候
				hostname = url.substring(0, hashNum); // 以#为分界符获取hosename字符串
				query = url.substring(hashNum); // 以#为分界符获取之后的字符串
				return hostname + encodeURIComponent(query); // 返回处理后的字符串
			} else {
				return null; // 如果即不存在search也不存在hash,则不处理url
			}
		},

		// 主要用于ajax的get方法给url添加查询名值对
		// url -- 可以为目标网址url,必须为字符串，
		// url -- 也可以为 -- null / undefined,此时主要用于ajax的post请求拼接查询字符串
		// nameArr为查询名称,必须为数组
		// valueArr 为查询值,必须为数组
		addURLParam: function(url, nameArr, valueArr) {
			var error1 = "addURLParam:() url must be a String.",
				error2 = "addURLParam:() arguments must be array.",
				error3 = "addURLParam:() arguments.length must be equal.";
			// 判断url为字符串,否则抛出警告error1
			wmsj.eventUtil.assert((typeof url === "string" || url == null), error1);
			// 判断nameArr和valueArr都为数组,否则抛出警告error2
			wmsj.eventUtil.assert((nameArr instanceof Array && valueArr instanceof Array), error2);
			// 判断nameArr和valueArr的个数相同,否则抛出错误
			wmsj.eventUtil.assert((nameArr.length === valueArr.length), error3);

			var len = nameArr.length, // 获取数组长度
				query = "", // 保存查询字符串
				i,
				num; // 获取最后一个
			for (i = 0; i < len; i++) {
				// 查询字符串的名值对都必须使用 -- encodeURIComponent -- 进行编码
				query += encodeURIComponent(nameArr[i]) + "=" + encodeURIComponent(valueArr[i]) + "&";
			}

			if (typeof url === "string") {
				url += (url.indexOf("?") === -1) ? "?" : "&"; // 判断url中有没有`"?".
				url += query.substr(0, query.length - 1);
				return url;
			} else if (url == null) {
				return query.substr(0, query.length - 1);
			}
		},

		// 封装的ajax函数,支持`get和post俩种方法
		// type -- 数据发送形式,有get和post类型
		// url -- 目标网址
		// nameArr -- 请求名称数组
		// valueArr -- 请求值数组
		// handler -- 对返回值的处理函数
		// 
		// wmsj.eventUtil.ajax("get", "01.php", ["name", "age"], ["王浩", "维护"], function(str) {
		// 	console.log(str);
		// });
		ajax: function(type, url, nameArr, valueArr, handler) {
			var typeError = "ajax(): type must be get or post",	// 抛出的错误类型
					statusError = "ajax(): xhr.status is fault.",		// 抛出状态码错误
					headName,		// 自定义头部名称
					headValue,	// 自定义头部值
					request;		// send发送的参数
			// 如果不是get或者post,则抛出错误
			wmsj.eventUtil.assert((type === "get" || type === "post"), typeError);	

			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function() {
				if (xhr.readyState === 4) {
					var judge = (xhr.status >= 200 && xhr.status < 300) || xhr.status == 304;
					wmsj.eventUtil.assert(judge, statusError);
					handler(xhr.responseText);	// 把返回的值绑定给函数
				}
			}

			if (type === "get") {	// 如果类型为get
				url = wmsj.eventUtil.addURLParam(url, nameArr, valueArr);	// 更新url地址
				headName = null;	// 设置自定义头部名称为null
				headValue = null;	// 设置自定义头部值为null
				request = null;		// 设置send参数为null
			} else {
				headName = "Content-Type";	// 添加表单的头部和值
				headValue = "application/x-www-form-urlencoded";
				// request = wmsj.modelUtil.dom.serialize(form);
				// 
				// request = new FormData(form);
				// console.log(request);

				request = wmsj.eventUtil.addURLParam(null, nameArr, valueArr);	// 获取查询数组的字符串拼接
			}
			xhr.open(type, url, true);
			xhr.setRequestHeader(headName, headValue);
			xhr.send(request);
		},

		// 判断值val是不是原生布尔值
		isBoolean: function() {
			var typeError = "isBoolean(): The arguments must be all Boolean.",
				countError = "isBoolean(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (typeof args[i] === "boolean") &&
					(Object.prototype.toString.call(args[i]) === "[object Boolean]");
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值val是不是原生字符串
		isString: function() {
			var typeError = "isString(): The arguments must be all String.",
				countError = "isString(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (typeof args[i] === "string") &&
					(Object.prototype.toString.call(args[i]) === "[object String]");
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值val是不是原生数值
		isNumber: function() {
			var typeError = "isNumber(): The arguments must be all Number.",
				countError = "isNumber(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (typeof args[i] === "number") &&
					Object.prototype.toString.call(args[i]) === "[object Number]";
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值val是不是原生对象
		isObject: function() {
			var typeError = "isObject(): The arguments must be all Object.",
				countError = "isObject(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (args[i] instanceof Object) &&
					(Object.prototype.toString.call(args[i]) === "[object Object]");
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值val是不是原生数组对象
		isArray: function() {
			var typeError = "isArray(): The arguments must be all Array.",
				countError = "isArray(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (args[i] instanceof Array) &&
					(Object.prototype.toString.call(args[i]) === "[object Array]");
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值是不是原生函数对象
		isFunction: function() {
			var typeError = "isFunction(): The arguments must be all Function.",
				countError = "isFunction(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (args[i] instanceof Function) &&
					(Object.prototype.toString.call(args[i]) === "[object Function]");
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},
		// 判断值是不是原生正则对象
		isRegExp: function() {
			var typeError = "isRegExp(): The arguments must be all RegExp.",
				countError = "isRegExp(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length > 1), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (args[i] instanceof RegExp) &&
					Object.prototype.toString.call(args[i]) === "[object RegExp]";
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},

		// 判断是不是DOM节点
		isNode: function() {
			var typeError = "isNode(): The arguments must be all Node.",
				countError = "isString(): The arguments must more than one,",
				valError = "The first param must be type of 'boolean' or null.",
				args = Array.prototype.slice.call(arguments, 1),
				len = args.length,
				i,
				boolean;
			wmsj.eventUtil.assert((arguments.length >= 2), countError);
			wmsj.eventUtil.assert((arguments[0] === null || arguments[0] === "boolean"), valError);
			for (i = 0; i < len; i++) {
				boolean = (typeof args[i].nodeType !== "undefined") && (args[i].nodeType === 1);
				if (!boolean) {
					if (arguments[0] === "boolean") {
						return boolean;
					} else {
						throw new Error(typeError);
					}
				}
			}
			return true;
		},

		// 选择判断--参数总数与期望总数的比较--和--参数之间的数组长度比较
		// type -- 可以选择`- args -- 表示比较参数总数 -- val -- 比较参数数组的长度
		// numarr -- 传入的比较数组类型 范例如下
		// isEqualCount("args", [2,2]) -- 比较参数总数
		// isEqualCount("val", [[2,2],[3,4],[5,6]]) -- 比较参数数组长度
		isEqualCount: function(type, numArr) {
			var countError = "isEqualCount(): The arguments.length must be two.",
				typeError = "isEqualCount(): The type's value must be 'args' or 'val'.",
				numError = "isEqualCount(): The numArr.length must be two.",
				argsEqualError = "isEqualCount(): args和期望值num比较 The param of numArr must be equal.",
				valEqualError = "isEqualCount(): 参数之间的数组长度比较 The param of valArr must be equal.",
				boolean;
			wmsj.eventUtil.assert(arguments.length === 2, countError);
			wmsj.eventUtil.isString(null, type);
			wmsj.eventUtil.isArray(null, numArr); // type 和 第二个参数(numArr or valArr)必须是数组
			wmsj.eventUtil.assert((type === "args" || type === "val"), typeError); // 限制type的值

			if (type === "args") {
				wmsj.eventUtil.assert((numArr.length === 2), numError);
				wmsj.eventUtil.isNumber(null, numArr[0]);
				wmsj.eventUtil.isNumber(null, numArr[1]);
				wmsj.eventUtil.assert(numArr[0] === numArr[1], argsEqualError);
				return true;
			} else {
				boolean = numArr.every(function(item) {
					wmsj.eventUtil.isArray(null, item);	// 判断每一个对象都是数组
					return item.length === numArr[0].length;	// 每一个对象的长度都相同
				});
			wmsj.eventUtil.assert(boolean, valEqualError);
				return true;
			}
		},

		// 这是一个把函数fn绑定到环境context的函数
		bindFunc: function(fn, context) { // 这个函数通过惰性载入的方法封装
			var args = Array.prototype.slice.call(arguments, 2);
			if (Function.prototype.bind) { // 检测是否支持ES5推出的原生bind方法
				bindFunc = function(fn, context) { // 覆盖函数
					return fn.bind(context, args);
				}
			} else {
				bindFunc = function(fn, context) { // ie8不支持原生bind，
					return function() {
						var innerArgs = Array.prototype.slice.call(arguments);
						var finalArgs = args.concat(innerArgs);
						return fn.apply(context, finalArgs); // 通过闭包来保存fn的执行环境
					}
				}
			}
			return bindFunc(fn, context);
		},

		// 创建防篡改对象 --ie8不支持
		// propArr -- 要创建对象的属性数组
		// propValArr -- 要创建对象的属性对应的值
		createStaticObj: function(propArr, propValArr) {
			var	args = arguments.length;
			wmsj.eventUtil.isArray(null,propArr, propValArr);
			wmsj.eventUtil.isEqualCount("args",[args,2]);
			wmsj.eventUtil.isEqualCount("val",[propArr,propValArr]);

			var obj = new Object(), // 创建对象容器
				len = propArr.length,
				i;
			for (i = 0; i < len; i++) {
				Object.defineProperty(obj, propArr[i], {
					configurable: false, // 不可被删除
					enumerable: true, // 可以通过 for - in 循环遍历
					writable: false, // 不可被重置
					value: propValArr[i] // 写入值
				});
			}
			return obj;
		},

		// 把已经存在的对象(对象或者数组)按照需求转换为防篡改对象(扩展, 封闭, 冻结)
		// obj -- 要转换的对象或数组 --ie8不支持
		// level -- 要转换的等级，可选值有 0-冻结 1-封闭 2-不可扩展
		toStaticObj: function (obj, level) {
			var rangeError = "protectObj(): level must be 2(不可扩展) or 1(封闭) or 0(冻结)",
					typeError = "protectObj(): obj must be Object or Array.",
					isObject = wmsj.eventUtil.isObject("boolean", obj),	// 判断是对象
					isArray = wmsj.eventUtil.isArray("boolean", obj),	// 判断是数组
			args = arguments.length;	// 获取参数个数
			wmsj.eventUtil.assert((isObject || isArray), typeError); // 判断obj是对象或者数组
			wmsj.eventUtil.isNumber(null, level);	// 判断level是数值
			wmsj.eventUtil.isEqualCount("args",[2, args]);	// 判断参数个数

			switch (level) {
				case 2:
					if (Object.isExtensible(obj)) {		// 阻止扩展
						Object.preventExtensions(obj);	
					}
					break;
				case 1:
					if (!Object.isSealed(obj)) { 	// 封闭对象，阻止扩展和修改，可删除
						Object.seal(obj);		
					}
					break;
				case 0:
					if (!Object.isFrozen(obj)) {	// 冻结对象，阻止扩展和修改，不可删除
						Object.freeze(obj);
					}
					break;
				default:
					throw new Error(rangeError);	// 抛出数值错误。
			}
		}



	};

	// ------------------------------------------ sizeUtio -----------------

	// 兼容性的获取scrollTop
	wmsj.sizeUtil = {
		// 获取页面滚动距离
		scrollTop: function() {
			var body = document.body.scrollTop,
					doc = document.documentElement.scrollTop;
			return body ? body : doc;
		}


	}

	// --------------------------------------- mouseUtil -------------------
	
	wmsj.mouseUtil = {
		// 获取鼠标的座标-X
		clientX: function(node, event) {	
			var event = wmsj.eventUtil.getEvent(event);
			return event.clientX;
		},

		// 获取鼠标的座标-Y
		clientY: function(node, event) {	
			var event = wmsj.eventUtil.getEvent(event);
			return event.clientY;
		},

		// 鼠标按键同时捕获键盘的按键
		judgeKeyPress: function (event) {		
			var event = wmsj.eventUtil.getEvent(event),
					keys = new Array();

			if (event.shiftKey) {	// 检测`shift`键是否按下，按下返回`true`，否则返回`false`。
				keys.push("shift");
			}

			if (event.ctrlKey) {	// 检测`ctrl`键是否按下，按下返回`true`，否则返回`false`。
				keys.push("ctrl");
			}

			if (event.altKey) {	// 检测`alt`键是否按下，按下返回`true`，否则返回`false`。
				keys.push("alt");
			}

			if (event.metaKey) {	// 检测`meta`键是否按下，按下返回`true`，否则返回`false`。
				keys.push("meta");
			}
			return keys.length ? keys.join(",") : null;		// 检测keys是否为空
		},

		// 针对mouseover和mouseout判断相关元素(鼠标进入和离开的元素目标)
		getRelatedTarget: function (event) {	
			var event = wmsj.eventUtil.getEvent(event);

			if (event.relatedTarget) {	// 现代浏览器触发
				return event.relatedTarget;
			} else if (event.toElement) {	// ie事件mouseout触发
				return event.toElement;
			} else if(event.fromElement) {	// ie事件mouseover触发
				return event.fromElement;	
			} else {
				return null;
			}
		},

		// 判断鼠标按键的值
		getButton: function (event) {
			var event = wmsj.eventUtil.getEvent(event);
			if (document.implementation.hasFeature("MouseUtils", "2.0")) {	// 判断浏览器是否支持DOM2鼠标事件
				return event.button;
			} else {	// 否则就是ie
				switch (event.button) {
					case 0:  // 没有按下按钮
					case 1:  // 按下左键
					case 3:  // 同时按下左右键左键优先
					case 5:  // 同时按下左键和滚轮，左键优先
					case 7:  // 同时按下左中右键，左键优先
						return 0;  // 全部设置为标准键左键-0
					case 2:  // 按下右键
						return 2;  // 设置为标准键右键-2
					case 4:  // 按下中键滚轮
						return 1;  // 设置为标准键滚轮-1
				}
			}
		},

		// 这个是用在键盘事件中 - keyup,keydown, keypress
		getCharCode: function(event) {	// 获取字符的ASCII码
			var event = wmsj.eventUtil.getEvent(event);
			if (typeof event.charCode === "number") { // 判断是不是现代浏览器，有没有charCode方法。
				return event.charCode;
			} else {
				return event.keyCode;	// 返回ie8的方法
			}
		},

		// 和getCharCode是成对出现
		getChar: function (num) {
			return String.fromCharCode(num);
		}



	}



	// ----------------------------- modelUtil 模块封装 -----------------


	// ------------------------------ modelUtil.dom ------------------
	wmsj.modelUtil.dom = {
		// 自定义右键菜单栏
		conTextMenu: function (node, menu) {	// node表示触发自定义菜单的节点, menu表示自定义菜单栏
			var nodeType1 = (typeof node === "object") ? node.nodeType : null;	// 判断是对象，然后返回节点值
			var nodeType2 = (typeof menu === "object") ? menu.nodeType : null;	// 判断是对象，然后返回节点值
			if (nodeType1 === 1 && nodeType2 === 1) {	// 确定俩个对象都是元素

				wmsj.eventUtil.addHandler(node, "contextmenu", function(event) {	// 绑定contextmenu事件
					var left = event.clientX,		// 获取鼠标点击位置的座标-X
							top = event.clientY;		// 获取鼠标点击位置的座标-Y
					event = wmsj.eventUtil.getEvent(event);
					wmsj.eventUtil.preventDefault(event);	// 阻止默认的菜单弹出
					wmsj.eventUtil.addHandler(menu, "mousedown", function(event) {	// 给menu添加点击事件
						event = wmsj.eventUtil.getEvent(event);	
						wmsj.eventUtil.stopPropagation(event);	// 阻止事件冒泡

						if(wmsj.mouseUtil.getButton(event) !== 0){		// 判断点击的不是左键
							menu.style.visibility = "hidden";		// 如果不是左键就隐藏
						}
					});
					if (wmsj.mouseUtil.getButton(event) === 2) {	// 判断右键
						menu.style.top = top + "px";		// 重新定位menu菜单的位置-X
						menu.style.left = left + "px";		// 重新定位menu菜单的位置-Y
						menu.style.visibility = "visible";		// 设置可视
					}
				});

				wmsj.eventUtil.addHandler(document, "mousedown", function() {
					menu.style.visibility = "hidden";		// 点击页面隐藏菜单
				});
			} else {
				throw new Error("not a node");	//抛出一个错误提示
				// return null;
			}
		},

		// 检查dom的dom是否加载完成 在onload事件之前执行
		checkDomLoaded: function(handler) { // handler表示之后执行的事件
			if (document.implementation.hasFeature("DOMContentLoaded", "1.0")) { // 功能检测
				wmsj.eventUtil.addHandler(document, "DOMContentLoaded", function() { // 非`ie的方法
					handler(); // 绑定事件
				});
			} else {
				wmsj.eventUtil.addHandler(document, "readystatechange", function() { // ie的执行方法
					if (document.readyState == "interactive" || document.readyState == "complete") {
						wmsj.eventUtil.removeHandler(document, "readystatechange", arguments.callee); // 清除事件绑定
						handler(); // 绑定事件
					}
				});
			}
		},

		// 事件代理函数,
		// node -- 表示父节点,代理层函数绑定对象
		// targetNodeName -- 表示目标节点,只有该节点会触发事件
		eventProxy: function(node, targetNodeName, eventType, handler) {

			if (typeof node === "object" && node.nodeType === 1) {	// 判断node是不是元素
				if (typeof targetNodeName === "string") {		// 判断targetNodeName是不是字符串
					wmsj.eventUtil.addHandler(node, eventType, function(event) {
						event = wmsj.eventUtil.getEvent(event);
						var target = wmsj.eventUtil.getTarget(event);

						if (target.nodeName.toLowerCase() === targetNodeName.toLowerCase()) {		// 判断是不是目标节点
							handler(target);	// 绑定函数
						} else {
							return null;
						}
					});
				} else {
					throw('"' + targetNodeName + '"' + " is not a String!");	// 抛出错误
				}
			} else {
				throw('"' + node + '"' + " is not an Element!"); 	// 抛出错误
			}

		},

		// ------------------------------------- form start 表单模块 ------------
		// 表单的第一个控件自动获取焦点
		formFocus: function() {
			wmsj.eventUtil.addHandler(window, "load", function(event) {		// 在页面加载完成之后
				var target = document.forms[0].elements[0];		// 获取目标控件

				if (!!target.autofocus) {		// 检查是否在html内部有autofocus属性--H5标准 ie9不支持
					return null;							// 如果有的话就返回；
				}

				target.focus();		// 否则就表单focus方法，
				wmsj.eventUtil.addHandler(target, "focus", function(){
					target.select();		//自动选中文本
				})
			});
		},

		// 限制输入字符，是单个字符的限制，所以正则不需要使用-g
		// regexp -- new RegExp("\\d"); 只能输入数字；
		formLimitedInput: function (textbox, regexp) {

		wmsj.eventUtil.addHandler(textbox, "keypress", function(event) {	// 添加keypress事件
			event = wmsj.eventUtil.getEvent(event);
			var charCode = wmsj.mouseUtil.getCharCode(event),		// 获取输入字符的ASCII码
					input = wmsj.mouseUtil.getChar(charCode);		// 把数字转换为字符
				
			if (!(regexp.test(input))) {		// 进行正则判断
				wmsj.eventUtil.preventDefault(event);		// 如果不符合要求就阻止默认事件，即文本输入
			}
		});
		a.focus();	// 自动获取焦点
	},

		// 限制对文本框input的复制内容
		// regexp -- 限制规则 new RegExp("^\\d*$"); 只能是数字
		// warning -- 错误警告信息； "只能输入数字"
		formLimitedPaste: function(textbox, regexp, warning) {
			wmsj.eventUtil.addHandler(textbox, "paste", function(event) {		// 绑定paste事件
				event = wmsj.eventUtil.getEvent(event);
				var text = wmsj.eventUtil.getClipboardText(event);	// 获取剪贴板的数据

				if (!regexp.test(text)) {
					wmsj.eventUtil.preventDefault(event);		// 阻止默认事件
					throw new Error(warning);	// 抛出错误
				}
			});
		},

		// 如果文本框的内容没有变化，获取焦点时候内容为空，事情焦点恢复默认值
		// inputDefaultValue($("input"));
		inputDefaultValue: function(node) {
			$(node).focus(function() { // 获取焦点事件
				var $val = $(this).val();
				if ($val === this.defaultValue) { // 和input的默认值比较
					$(this).val("");
				}
			});
			$(node).blur(function() { // 失去焦点事件
				var $val = $(this).val();
				if (!$val) {
					$(this).val(this.defaultValue); // 和input的默认值比较
				}
			});
		},

		// 获取表单form的提交数据,表单序列化
		serialize: function(form) {
			var parts = [],
				field = null,
				i,
				len,
				j,
				optLen,
				option,
				optValue;
			for (i = 0, len = form.elements.length; i < len; i++) {
				field = form.elements[i];

				switch (field.type) {
					case "select-one":
					case "select-multiple":

						if (field.options.length) {
							for (j = 0, optLen = field.options.length; j < optLen; j++) {
								option = field.options[j];
								// console.log(j);
								if (option.selected) {
									optValue = "";
									if (option.hasAttribute) {
										optValue = (option.hasAttribute("value") ? option.value : option.text);
									} else {
										optValue = (option.attributes["value"].specified ? option.value : option.text);
									}
									parts.push(encodeURIComponent(field.name) + "=" + encodeURIComponent(optValue));
								}
							}
						}
						break;
					case undefined:
					case "file":
					case "submit":
					case "reset":
					case "button":
						break;
					case "radio":
					case "checkbox":
						if (!field.checked) {
							break;
						}
					default:
						if (field.name.length) {
							parts.push(encodeURIComponent(field.name) + "=" + encodeURIComponent(field.value));
						}
				}
			}
			return parts.join("&");
		},

		// 当文本框输入字符超过maxLength时候，自动把焦点跳转到下一个文本框
		// 这个函数搭配 --- nodeListBind -- 进行多个文本框的函数绑定最合适了。
		tabForward: function(event) {
			event = wmsj.eventUtil.getEvent(event);
			var target = wmsj.eventUtil.getTarget(event),
				form = target.form,
				len = form.elements.length,
				i;
			if ((target.type === "text" || target.type === "textarea") && target.maxLength) {
				if (target.value.length === target.maxLength) { // 输入的值和maxlength比较
					for (i = 0; i < len; i++) {
						if (form.elements[i] === target) { // 查询到目前的文本框对于的i值
							if (form.elements[i + 1]) { // 判断下一个文本框是否存在
								form.elements[i + 1].focus(); // 把焦点移动到下一个控件，不一定是文本框
							}
							return;
						}
					}
				}
			}
		},

		// 当input文本框设置-required-时候，ie浏览器会触发这个事件，ie不支持required
		// 警告的方式有俩种，一种是背景色变为 -- pink ， 还有一种是弹出-alert-框。
		// 这个事件是全局性的，会为页面的所有的表单的`-form-添加这个事件。是事件代理性质的
		formRequired: function() {
			var isRequiredSupport = "required" in document.createElement("input");	// 判断是否支持required
			if (isRequiredSupport) {		// 如果支持，则不做处理
				return null;
			} else {	// 否则就当作是ie浏览器
				var formsArr = document.forms,	// 获取所有的表单数组
					len = formsArr.length,	// 表单个数
					nodeArr = null,		// 预先声明表单内部的节点数组
					nodeLen = 0,		// 节点个数
					node = null;		// 节点
				while (len--) {		// 逆序循环
					(function(num) {		// 这个使用了闭包，这样才可以保存--num-的值。
						wmsj.eventUtil.addHandler(formsArr[num], "submit", function(event) {	// 给表单绑定-submit事件
							event = wmsj.eventUtil.getEvent(event);
							nodeArr = formsArr[num].elements;	// 获取表单没办的控件数组
							nodeLen = nodeArr.length;		// 表单控件数量
							while (nodeLen--) {		// 逆序提高性能
								node = nodeArr[nodeLen];	// 依次遍历控件
								if (node.type === "text" && node.value.length === 0) {	// 判断控件是文本框并且没有输入值
									if (node.hasAttribute("required")) {	// 判断控件设置了required属性
										wmsj.eventUtil.preventDefault(event);		// 阻止控件的默认事件
										node.style.backgroundColor = "pink";		// 设置控件的背景颜色为 - pink
										// alert (node.name+" is required.");		// 弹出警告框
									}
								}
							}
						});
					}(len));	// 闭包，把len当作参数传入闭包函数。
				}
			}
		},

		// 页面的所有表单form都可以通过冒泡到document触发事件禁止表单重复提交--hack--方法
		// 页面的所有表单的-submit-按钮都需要添加 - name="submit" - 因为要通过name值选中这个按钮
		preventRepeatSubmit: function() {
			wmsj.eventUtil.addHandler(document, "submit", function(event) { // 给document绑定表单的submit事件
				event = wmsj.eventUtil.getEvent(event);
				var goal = wmsj.eventUtil.getTarget(event), // 获取点击的目标表单
					frame = document.createElement("iframe"), // 创建一个内嵌的iframe
					btn = goal.elements["submit"], // 通过-name="submit"-获取submit按钮
					btnNameError = "preventRepeatSubmit(): The button of submit" + 
												 "must have property 'name=\"submit\"'.";
				wmsj.eventUtil.assert((typeof btn !== "undefined"), btnNameError);
				frame.name = "frame1"; // 设置frame的name值,为了表单通过`target指定
				frame.style.visibility = "hidden"; // 设置frame隐藏
				frame.style.width = 0; // 设置frame的宽度为0; 为了不引起页面跳动
				frame.style.height = 0; // 设置frame的高度为0; 为了不引起页面跳动
				goal.target = "frame1"; // 把from的target指向frame
				document.body.appendChild(frame); // 把frame加载到DOM树
				btn.disabled = true; //	设置submit按钮为禁用

				var loadIframe = function() { // frame加载完成的事件
					wmsj.eventUtil.removeHandler(frame, "load", loadIframe); // frame解绑load绑定的loadIframe事件
					document.body.removeChild(frame); // 从DOM树移除frame
					frame = null; // 注销对frame的变量引用
				};

				wmsj.eventUtil.addHandler(frame, "load", loadIframe); // frame绑定load事件
			});
		},

		// 获取选中的文本 调用的方法如下：
		// wmsj.eventUtil.addHandler(a, "select", function() {
		// 	var b = getSelectedText(a);
		// 	console.log(b);
		// });
		getSelectedText: function (node) {  // 获取文本的节点
			if (typeof node.selectionStart === "number") {  // 进行功能判断
				return node.value.substring(node.selectionStart, node.selectionEnd);
			} else {
				return document.selection.createRange().text;		// ie8的方法
			}
		},

		// 选中文本框中的部分文字，只是界面选中
		// textbox值文本框--input
		// startIndex--选中文本的其实下标
		// stopIndex--选中文本的终止下标的后一位
		selectText: function(textbox, startIndex, stopIndex) {
			if (textbox.setSelectionRange) { // 功能判断ie9+浏览器支持
				textbox.setSelectionRange(startIndex, stopIndex);
			} else if (textbox.createTextRange) { // 功能判断 ie8支持
				var range = textbox.createTextRange();
				range.collapse(true);
				range.moveStart("character", startIndex);
				range.moveEnd("character", stopIndex - startIndex);
				range.select();
			}
			textbox.focus();
		},

		// 拖动框封装函数，被拖动元素必须有-class值- draggable -DragDrop.enable()方式进行调用
		// 调用方式通过 -- DragDrop.enable().来绑定拖动事件
		// 解绑方式通过 -- DragDrop.disable().来绑定拖动事件
		DragDrop: function() {	// 一个自执行函数
			var dragging = null,	// 被拖动元素指针
				addHandler = wmsj.eventUtil.addHandler,	// 存储函数库路径
				removeHandler = wmsj.eventUtil.removeHandler, // 存储函数库路径
				getEvent = wmsj.eventUtil.getEvent,	// 存储函数库路径
				getTarget = wmsj.eventUtil.getTarget,	// 存储函数库路径
				diffX = 0,	// 鼠标指针和被拖动元素的x座标差值
				diffY = 0;	// 鼠标指针和被拖动元素的y座标差值

			function handlerEvent(event) {	// event指向事件数据数组指针
				event = getEvent(event);	
				var target = getTarget(event);
				switch (event.type) {	// 判断鼠标事件的类型
					case "mousedown":
					// 判断dragging没有被初始化，并且被点击元素有class属性为`draggable`
						if (dragging === null && target.className.indexOf("draggable") !== -1) {	
							dragging = target;	// 初始化，把dragging指向被点击元素
							diffX = event.clientX - target.offsetLeft;	// 计算x座标差值
							diffY = event.clientY - target.offsetTop;		// 计算y座标差值
							addHandler(document, "mousemove", handlerEvent);	// 绑定mousemove事件
							addHandler(document, "mouseup", handlerEvent);		// 绑定mouseup事件
						}
						break;

					case "mousemove":
						if (dragging !== null) {	// 判断dragging指向target的指针不为空
							dragging.style.left = (event.clientX - diffX) + "px";	// 计算x座标值
							dragging.style.top = (event.clientY - diffY) + "px";	// 计算target的y座标值
						}
						break;

					case "mouseup":
						dragging = null; 	// 移除dragging的target指针
						removeHandler(document, "mousemove", handlerEvent);	  // 移除鼠标事件
						removeHandler(document, "mouseup", handlerEvent);  // 移除鼠标事件
						break;
				}
			}

			return {  // 返回公共接口，
				enable: function() {
					addHandler(document, "mousedown", handlerEvent);	// 绑定鼠标点击事件
				},
				disable: function() {
					removeHandler(document, "mousedown", handlerEvent);	// 解绑鼠标点击事件
				}
			}
		}(),

		// 获取页面节点node的-css-style-的属性值，
		// 第一个参数为 DOM 节点，后面的参数必须是-css-属性。
		getStyleValue: function(node, CSSStyleProperty) {
			var event = wmsj.eventUtil,
				countError = "getStyleValue(): The arguments.length must more than one.",
				styleError = "getStyleValue(): The param must be CSS style property.",
				args = Array.prototype.slice.call(arguments),	// 获取arguments的副本
				len = args.length,
				result = {},
				styleUtil = {},
				node = arguments[0],
				i;

			event.assert(len > 1, countError);
			event.isNode(null, node);

			try {
				styleUtil = document.defaultView.getComputedStyle(node, null);	//非ie8获取style属性对象集合方法
			} catch (ex) {
				styleUtil = node.currentStyle;	// ie8的获取style属性对象集合方法
			}

			args.shift();
			for (i = 0; i < len; i++) {
				event.isString(null, args[i]);
				if (typeof styleUtil[args[i]] === "undefined") {
					throw new Error(styleError);
				} else {
					result[args[i]] = styleUtil[args[i]];
				}
			}
			return result;	//Object {width: "100px", height: "100px"}
		},

		// 封装了设置cookie的简单方法，有get, getAll, set, setAll, unset, unsetAll;
		// CookieUtil.get("name1","name6");	接受俩个参数，cookie的name值和子cookie的name值
		// CookieUtil.getAll("name2");	接受cookie的name值，返回这个值下的子cookie的键值对
		// CookieUtil.set("name1","name4",12);	接受一个cookie的name值和子cookie的name和要设置的值
		// 如果设置的name 不存在，则创建一个新cookie，
		// 如果设置的subName -  子cookie不存在，则创建一个新cookie。
		// CookieUtil.setAll("name1",{age: 12, male: "female"});
		// CookieUtil.unset("name1","name2");
		// CookieUtil.unsetAll("name2");
		CookieUtil: function() {
			var fn = function() {
				var event = wmsj.eventUtil;

				function get(name, subName) {
					var cookieArr = getAll(name),
						nameError = "CookieUtil.get(): The " + name + " of search is not exist in the cookies.",
						subNameError = "CookieUtil.get(): The " + subName + " of search is not exist in the cookies.";
					event.isString(null, name);
					event.isEqualCount("args", [arguments.length, 2]);
					if (cookieArr) {
						if (cookieArr[subName]) {
							return cookieArr[subName];
						} else {
							throw new Error(subNameError);
						}
					} else {
						throw new Error(nameError);
					}
				};

				function getAll(name) {
					var cookieArr = document.cookie.split("; "), // cookieArr >= 1;
						nameError = "CookieUtil.getAll(): The " + name + " of search is not exist in the cookies.",
						cookieError = "CookieUtil.getAll(): The cookies is empty.",
						subName,
						subValue,
						subArr,
						start,
						len,
						i,
						key,
						val,
						result = {};
					event.isString(null, name);
					event.assert(document.cookie, cookieError); // 如果cookie为空，抛出错误
					len = cookieArr.length;

					for (i = 0, len = cookieArr.length; i < len; i++) {
						start = cookieArr[i].indexOf("=");
						subName = cookieArr[i].substring(0, start);
						if (subName === name) {
							subValue = cookieArr[i].substring(start + 1);
							subArr = subValue.split("&");
							len = subArr.length;
							if (len > 1) {
								for (i = 0; i < len; i++) {
									key = subArr[i].split("=")[0];
									val = subArr[i].split("=")[1];
									result[key] = val;
								}
							} else if (len === 1) {
								result[subName] = subValue;
							}
							return result;
						}
					}
					throw new Error(nameError);
				};

				function set(name, subName, value, expires, path, domain, secure) {
					var cookieObj = null,
						cookieText = name + "=";

					try {
						cookieObj = getAll(name);
					} catch (ex) {
						cookieObj = null;
					}
					// console.log(cookieObj)
					event.isString(null, name);
					if (cookieObj !== null) { //	如果name存在现有的cookie中
						if (subName in cookieObj && cookieObj.hasOwnProperty(subName)) { // 如果subName是已经存在的
							if (cookieObj[subName] === value) { // 如果subName对应的值和要修改的值相同，则不处理
								return null;
							}
						}
						cookieObj[subName] = value; // 如果虽然subName存在，但对应的值不同，或者是不存在，则创建对象
						cookieText += objectToString(cookieObj);
						document.cookie = cookieText;
						// console.log(cookieText)
					} else { //	如果name不存在现有的cookie中
						cookieObj = {}; // 把cookieObj设置对对象
						cookieObj[subName] = value; // 填充值
						setAll(name, cookieObj, expires, path, domain, secure); // 通过setAll来创建新的cookie
					}
				};

				function objectToString(subcookies) {
					var subName,
						subcookiesParts = new Array();
					event.isObject(null, subcookies);
					for (subName in subcookies) {
						if (subName.length > 0 && subcookies.hasOwnProperty(subName)) {
							subcookiesParts.push(subName + "=" + subcookies[subName]);
						}
					}
					return subcookiesParts.join("&");
				};

				// 重置所有的内容
				function setAll(name, subcookies, expires, path, domain, secure) {
					var cookieText = name + "=";

					if (subcookies !== null) {
						cookieText += objectToString(subcookies);
					} else {
						cookieText += null;
					}
					if (expires instanceof Date) {
						cookieText += "; expires=" + expires.toGMTString();
					}
					if (path) {
						cookieText += "; path=" + path;
					}
					if (domain) {
						cookieText += "; domain=" + domain;
					}
					if (secure) {
						cookieText += "; secure";
					}
					document.cookie = cookieText;
				};

				function unset(name, subName, path, domain, secure) {
					var cookieObj = getAll(name),
						cookieText = name + "=";
					if (subName in cookieObj && cookieObj.hasOwnProperty(subName)) {
						cookieObj[subName] = null;
					}
					cookieText += objectToString(cookieObj);
					document.cookie = cookieText;
				};

				function unsetAll(name, path, domain, secure) {
					var cookieObj = getAll(name);
					setAll(name, null, new Date(0), path, domain, secure);
				}
				return {
					get: get, // CookieUtil.get("name1","name6");
					getAll: getAll, // CookieUtil.getAll("name2");
					set: set, // CookieUtil.set("name1","name4",12);
					setAll: setAll, // CookieUtil.setAll("name1",{age: 12, male: "female"});
					unset: unset, // CookieUtil.unset("name1","name2");
					unsetAll: unsetAll // CookieUtil.unsetAll("name2");
				}
			}();
			return fn;
		}(),

		// 设置自定义的链接提示框，清除默认的值,需要设置class = tooltip，
		// <a class="jsbin-embed" href="http://jsbin.com/noxodus/embed?html,css,js,output">JS Bin on jsbin.com</a><script src="http://static.jsbin.com/js/embed.min.js?3.36.10"></script>
		setLinkTitle: function() {

			var useOffset = {
				left: 20,
				top: 10
			};

			$("a.tooltip").mouseover(function(e) {
				var $src = $(this).find("img").attr("src"),
					alt = this.title,
					img = '<img src="' + $src + '"' + 'alt="' + this.title + '">',
					span = this.title ? "<br><span>" + this.title + "</span>" : "",
					cont = '<div class="toolTipBox">' + img + span + "</div>",
					$box = $(cont);
				$("body").append($box);
				$box.css({
					"left": e.clientX + useOffset.left + "px",
					"top": e.clientY + useOffset.top + "px"
				}).show("fast");
				$(this).removeAttr("title");

			}).mousemove(function(e) {
				$(".toolTipBox").css({
					"left": e.clientX + useOffset.left + "px",
					"top": e.clientY + useOffset.top + "px"
				});

			}).mouseout(function(e) {
				this.title = $(".toolTipBox").find("img").attr("alt");
				$(".toolTipBox").remove();
			});
		}



	// ------------------------------- form end ----------------------------
	
	};

	// ------------------------------ modelUtil.func ------------------
	wmsj.modelUtil.func = { // 函数模型的绑定
		// 适用于一些节点列表绑定的相同的事件，而事件也只依赖于event的传递
		// nodeList -- 表示绑定事件的节点列表
		// eventType -- 表示了触发这些事件的场景`click,keyup,focus...`
		// handler -- 要绑定的函数
		nodeListBind: function (nodeList, eventType, handler) {
			var arr = nodeList,		// 获取节点列表
					len = nodeList.length;		// 获取节点列表的长度
			while (len--) {
				wmsj.eventUtil.addHandler(arr[len], eventType, handler);
			}
		},

		// 跨域发起(postMessage)请求的方法
		// toUrl -- 内嵌的iframe的地址,即请求数据的目标网址
		// toData -- 发送请求时候的验证数据
		// handler -- 当接收到数据之后,对数据的处理
		// 
		// wmsj.modelUtil.func.toPostMessage(toUrl, toData, function(str) {
		// 	handler(str);
		// });
		toPostMessage: function(toUrl, toData, handler) {
			var frame = document.createElement("iframe"); // 创建内嵌框架
			frame.src = toUrl;
			frame.style.visibility = "hidden"; // 是内联框架隐藏,消除视觉闪动效果
			frame.style.width = 0;
			frame.style.height = 0;
			document.body.appendChild(frame); // 加载到`DOM树

			var postInfo = function(event) { // 创建发送信息函数
					frame.contentWindow.postMessage(toData, toUrl); // 获取iframe的window,并且绑定postMessage事件
				},
					getMessage = function(event) { // 给window添加`message监听事件
					event = wmsj.eventUtil.getEvent(event);

					if (toUrl.indexOf(event.origin) === 0) { // 判断发送信息的域名是否toUrl的hostname

						wmsj.eventUtil.removeHandler(frame, "load", postInfo); // 移除frame绑定的load事件
						frame.contentWindow.close(); // 关闭
						document.body.removeChild(frame); // 从DOM树移除frame
						frame = null; // 消除变量对内联框架的索引
						handler(event.data); // 接收到的数据传递给外部函数处理
					}
				};
			wmsj.eventUtil.addHandler(frame, "load", postInfo); // 监听iframe加载完成之后执行信息发送事件
			wmsj.eventUtil.addHandler(window, "message", getMessage);
		},

		// 目标源接收到postMessage并且验证之后发送数据给请求者
		// toUrl -- 允许的请求者链接,也是发送数据的目标
		// toData -- 发送的数据
		// handler -- 对请求者发送的数据的验证过程
		// 
		// wmsj.modelUtil.func.listenMessage(toUrl, toData, function(str) {
		// 	handler(str);
		// });
		listenMessage: function(toUrl, toData, handler) {
			var getMessage = function(event) { // 在window上面监听message事件
				event = wmsj.eventUtil.getEvent(event);

				if (toUrl.indexOf(event.origin) === 0) { // 判断请求源的hostname是否是允许的目标源hostname
					handler(event.data); // 验证通过后对请求源发送的数据进行处理
					event.source.postMessage(toData, toUrl); // 在请求源的资源上发送postMessage事件
				}
			};
			wmsj.eventUtil.addHandler(window, "message", getMessage);
		},

		// jsonp-- 跨域方法
		// url -- 目标地址
		// queryName -- 请求的名称
		// handlerName -- 请求的值
		JSONP: function(url, queryName, handlerName) {
			var urlError = "JSONP(): url must start with http://...!",
				script = null,
				event = wmsj.eventUtil,
				args = arguments.length;
			event.assert((url.indexOf("http://") === 0), urlError);	// 网址前缀判断
			event.isString(null,queryName, handlerName);
			event.isEqualCount("args",[args, 3]);
			script = document.createElement("script");
			script.src = url + "?" + queryName + "=" + handlerName;		// 更新url
			document.body.appendChild(script);
		},

		// 跨域 -- 使用window.name
		// toUrl -- 目标网址
		// proxyUrl -- 本域名下的一个空白网页，作用就是临时中转，空白页面加载速度会很快。
		// handler -- 绑定的函数
		// windowName("http://b.com/PHP/Month/June/25.html", "25.html", function(str) {
		// 	handler1(str);
		// });
		windowName: function(toUrl, proxyUrl, handler) {
			var frame = null,	// 临时框架
				state,		// 状态锁
				frameLoad,		// frame绑定的函数
				data,		// 获取的字符串
				event = wmsj.eventUtil,
				args = arguments.length;

			event.isEqualCount("args", [args, 3]);
			event.isString(null, toUrl, proxyUrl);
			event.isFunction(null, handler);

			frame = document.createElement("iframe");
			frame.src = toUrl;
			frame.style.visibility = "hidden";
			frame.style.width = 0;
			frame.style.height = 0;
			document.body.appendChild(frame);
			state = false;
			frameLoad = function(event) {
				if (state) {	// 如果状态state为true，表示frame.src = 代理，
					data = frame.contentWindow.name;	// 获取存放在frame的window.name中的值
					frame.contentWindow.name = null;	// 清空window.name的值
					wmsj.eventUtil.removeHandler(frame, "load", frameLoad);	// 解绑frame绑定的事件load
					document.body.removeChild(frame);	// 从DOM解绑frame框架
					frame = null;		// 清除对框架的变量索引
					handler(JSON.parse(data));	// 把值传递出去
				} else {
					state = true;		// 把状态码转换为true
					// 把iframe的网址从toUrl转换到代理网址,
					// 转换之后会又一次触发-frame-绑定的-load事件，然后会又一次指向frameLoad函数
					frame.contentWindow.location = proxyUrl;	
				}
			};

			wmsj.eventUtil.addHandler(frame, "load", frameLoad);	// 绑定事件frameLoad到load
		},

		// 数组分块技术,一旦某个函数需要花50ms以上的时间执行，就可以考虑把循环分块，
		// 将任务分割为一系列可以使用定时器的小任务；
		// 这样后面的代码也有机会执行，页面不会进入假死状态，交互性会好很多。如下面的例子
		// 
		// var data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
		// function print(item) {
		// 	console.log(item + "<br>");
		// }
		// wmsj.modelUtil.func.chunk(data, print);
		// wmsj.codeUtil.func.countFunc();
		chunk: function(data, handler, context) {
			setTimeout(function() {
				var item = data.shift();
				handler.call(context, item);
				if (data.length > 0) {
					setTimeout(arguments.callee, 100);
				}
			}, 100);
		},

		// 函数节流，多用于`onresize, onscroll等高耗能操作，
		// 把实时操作分割为每隔100ms操作一次
		// method -- 要节流的函数方法， context -- 运行环境
		// 这个比通过查看状态码state的布尔值的好处在于代码量很少，缺点是不能给method传参
		// 
		// function print() {console.log("hello")}
		// window.onresize = function() {wmsj.modelUtil.func.throttle(print)}
		throttle: function(method, context) {
			clearTimeout(method.tId);
			method.tId = setTimeout(function() {
				method.call(context);
			}, 100);
		},

		// 获取superType的原型prototype并且赋值给subType.prototype
		inheritPrototype: function(subType, superType) {
			// 获取原型的对象，通过Object可以获取函数的原型，而没有兼容性考虑，
			// 如果使用-Object.create-ie8不支持
			var prototype = Object(superType.prototype);	
			prototype.constructor = subType;
			subType.prototype = prototype;
			prototype = null;
		},

		// 自定义事件容器
		// userDefinedEventExample 这是基于自定义事件的一个范例，在codeModel模块中
		EventTarget: function() {	// 通过一个立即执行函数来封装内部函数
			function fn() {	// 创建函数
				this.handlers = {};	// 创建一个自定义事件容器
			}

			fn.prototype = {	
				constructor: fn,	// 把constructor指回函数fn

				// 注册给定事件的事件处理程序，接受俩个参数
				// type -- 要添加的事件类型
				// handler -- 对于type类型的处理程序
				addHandler: function(type, handler) {	
					if (typeof this.handlers[type] === "undefined") {	// 判断type类型是否已经存在
						this.handlers[type] = [];	// 如果不存在就创建这个类型的事件处理程序
					}
					// 把事件程序push到type类型的数组队列中，可能数组内部已经有方法了
					this.handlers[type].push(handler);	
				},

				// 用于触发一个事件，通过event对象的type类型来触发
				// event -- 是一个至少包含type属性的对象，还可以添加自定义属性
				// event = {type: "message", message: "hello world", x: event.clientX, y: event.clientY};
				fire: function(event) {
					if (!event.target) {	// 判断event对象有没有target属性，如果没有就给event对象创建target属性值
						event.target = this;	// 把target属性值设置为this，经过这个步骤，event对象就会增加target属性
					}
					// 判断对应类型type的事件是否存在事件容器handlers中，
					// 如果type类型事件存在，则事件就存储在事件列表中
					// 所以只需要判断对于type的值是不是数组就可以
					if (this.handlers[event.type] instanceof Array) {	
						var handlers = this.handlers[event.type];	// 获取对于类型type的事件列表
						for (var i = 0, len = handlers.length; i < len; i++) {	// 遍历这个事件列表
							// 把对象event参数传递给事件列表中的所以函数
							// 所以创建的函数都需要传入event参数，然后基于对象event的属性操作
							handlers[i](event);
						}
					}
				},
				// 移除类型type中的函数handler
				removeHandler: function(type, handler) {
					if (this.handlers[type] instanceof Array) {	// 判断类型type的事件列表是否存在
						var handlers = this.handlers[type];	// 获取type类型的事件列表
						for (var i = 0, len = handlers.length; i < len; i++) {	// 变量这个事件列表
							if (handlers[i] === handler) {	// 判断列表中的每一个函数和目标函数比较
								break;	// 如果找到了，就中断循环
							}
						}
						handlers.splice(i, 1);	 // 从事件列表的数组中移除i下标的函数。
					}
				}
			}
			return fn;	// 返回函数，是EventTarget的值返回一个函数
		}()

	};

	// ------------------------------------ collect code dom 有价值的代码收藏 ----------------
	wmsj.codeUtil.dom = {		// 关于dom的代码收集
		// 这个代码会报错,因为通过定时器设置的闭包函数在给event添加属性value时候event已经不存在了
		// event只有在函数运行时候可以访问到.
		eventValueLost: function() {
			wmsj.eventUtil.addHandler(document, "click", function(e) {
				event = wmsj.eventUtil.getEvent(e);
				setTimeout(function() {
					event.value = false;	// 此时event已经不存在,而给不存在的值添加属性会报错
				}, 1000);
			});
		},

		cors: function() {	// 跨域，适用于php动态页面
			// header("Access-Control-Allow-Origin:http://a.com");
			// $info = '{"name": "wmsj", "age": 10}';
			// echo $info;
		},

		// 这个效果是鼠标hover时候，显示下面的元素，同时自己改变颜色。
		hoverEvent: function() {
			$(function() {
				$("p").hover(function() {
					$(this).next().toggle();
					$(this).toggleClass("light");
				}, function() {
					$(this).next().toggle();
					$(this).toggleClass("light");
				});
			})
		}

	};


// ------------------------------------ collect code func ---------------------------
	wmsj.codeUtil.func = {
		// 这是一个安全的继承链，fn的this是安全的。
		safeCopeFunc: function() {
			function fn(name) {
				if (this instanceof fn) {
					this.name = name;
				} else {
					return new fn(name);
				}
			}

			function fn2(name, age) {
				fn.call(this, name);
				this.age = age;
			}
			fn2.prototype = new fn();
			var a = new fn2("wmsj", 12);
			a; //fn2 {name: "wmsj", age: 12}
			a instanceof fn2; //true
			a instanceof fn; //true
		},

		// setTimeout模拟setInterval的效果
		countFunc: function() {
			var timer = 0,
				num = 0;
			timer = setTimeout(function() {
				num++;
				console.log(num);
				if (num >= 10) {
					clearTimeout(timer);
				} else {
					timer = setTimeout(arguments.callee, 100);
				}

			}, 100);
		},

		// 自定义事件的范例
		userDefinedEventExample: function() {
			function People(name, age) {
				wmsj.modelUtil.func.EventTarget.call(this);	// 获取自定义事件的事件列表属性handlers
				this.name = name;
				this.age = age;
			}
			// 获取自定义事件的原型
			// 其实没必要这样获取eventTarget的原型，可以通过构造函数的实例来直接继承原型
			wmsj.modelUtil.func.inheritPrototype(People, wmsj.modelUtil.func.EventTarget);
			People.prototype.say = function(message) {	// 在原型上面添加方法
				this.fire({
					type: "message",
					message: message
				});
			}

			var person = new People("wmsj", 12);	// 创建实例

			function show(event) {
				console.log(event.target.name + " say: " + event.message);
			}

			function print(event) {
				document.write(event.target.name + " ," + event.target.age + " say: " + event.message);
			}

			person.addHandler("message", show);
			person.addHandler("message", print);
			person.say("hello wrold");
			// person.removeHandler("message",show);
			// person.removeHandler("message",print);
		},

		// 这是一个拖拽框的自定义事件效果，调用方法--DragDrop.enable();
		DragDropExample: function() {
			var fn = function() { // 一个自执行函数
				var dragging = null, // 被拖动元素指针
					addHandler = wmsj.eventUtil.addHandler, // 存储函数库路径
					removeHandler = wmsj.eventUtil.removeHandler, // 存储函数库路径
					getEvent = wmsj.eventUtil.getEvent, // 存储函数库路径
					getTarget = wmsj.eventUtil.getTarget, // 存储函数库路径
					EventTarget = wmsj.modelUtil.func.EventTarget, // 绑定自定义事件
					diffX = 0, // 鼠标指针和被拖动元素的x座标差值
					diffY = 0, // 鼠标指针和被拖动元素的y座标差值
					dragdrop = new EventTarget(); // 初始化自定义事件

				function handlerEvent(event) { // event指向事件数据数组指针
					event = getEvent(event);
					var target = getTarget(event);
					switch (event.type) { // 判断鼠标事件的类型
						case "mousedown":
							// 判断dragging没有被初始化，并且被点击元素有class属性为`draggable`
							if (dragging === null && target.className.indexOf("draggable") !== -1) {
								dragging = target; // 初始化，把dragging指向被点击元素
								diffX = event.clientX - target.offsetLeft; // 计算x座标差值
								diffY = event.clientY - target.offsetTop; // 计算y座标差值
								addHandler(document, "mousemove", handlerEvent); // 绑定mousemove事件
								addHandler(document, "mouseup", handlerEvent); // 绑定mouseup事件
								dragdrop.fire({
									type: "dragstart",
									target: dragging,
									x: event.target.offsetLeft,
									y: event.target.offsetTop
								});
							}
							break;

						case "mousemove":
							if (dragging !== null) { // 判断dragging指向target的指针不为空
								dragging.style.left = (event.clientX - diffX) + "px"; // 计算x座标值
								dragging.style.top = (event.clientY - diffY) + "px"; // 计算target的y座标值
								dragdrop.fire({
									type: "drag",
									target: dragging,
									x: event.target.offsetLeft,
									y: event.target.offsetTop
								});
							}
							break;

						case "mouseup":

							removeHandler(document, "mousemove", handlerEvent); // 移除鼠标事件
							removeHandler(document, "mouseup", handlerEvent); // 移除鼠标事件
							dragdrop.fire({
								type: "dragend",
								target: dragging,
								x: event.target.offsetLeft,
								y: event.target.offsetTop
							});
							dragging = null; // 移除dragging的target指针
							break;
					}
				}

				dragdrop.enable = function() {
					// document.body.innerHTML = '<style> .draggable{position: absolute; border: 1px solid; background-color: yellow; width: 100px; height: 100px; } </style> <div id="dragbox" class="draggable">hello world</div> <h3 class="status">hello</h3>';
					addHandler(document, "mousedown", handlerEvent); // 绑定鼠标点击事件
				},
				dragdrop.disable = function() {
					removeHandler(document, "mousedown", handlerEvent); // 解绑鼠标点击事件
				}
				return dragdrop;
			}();

			fn.addHandler("dragstart", dragStart);
			fn.addHandler("drag", dragged);
			fn.addHandler("dragend", dragEnd);

			function dragStart(event) {
				var status = document.querySelector(".status");
				status.innerHTML = event.target.id + "-" + event.type + "( " + event.x + "," + event.y + ")";
			}

			function dragged(event) {
				var status = document.querySelector(".status");
				status.innerHTML = event.target.id + "-" + event.type + "( " + event.x + "," + event.y + ")";
			}

			function dragEnd(event) {
				var status = document.querySelector(".status");
				status.innerHTML = event.target.id + "-" + event.type + "( " + event.x + "," + event.y + ")";
			}
			return fn;
		}(),

		// 关于使用自定义事件-EventTarget-的俩种方法，直接使用效果和继承原型链，
		// fn=wmsj.codeUtil.func.inheritChain;
		inheritChain: function() {
			var EventTarget = wmsj.modelUtil.func.EventTarget,
					inheritPrototype = wmsj.modelUtil.func.inheritPrototype;
			function people(name, age) {
				var obj = new EventTarget();
				obj.name = name;
				obj.age = age;
				return obj;
			}

			function people2(name, age) {
				EventTarget.call(this);
				this.name = name;
				this.age = age;
			}
			inheritPrototype(people2, EventTarget);

			var a = new people("wmsj", 12);
			var b = new people2("wanmei", 20);
			a instanceof people; //false;
			b instanceof people2; //true
			a instanceof EventTarget; //false
			b instanceof EventTarget; //true
			return {
				a: new people("wmsj", 12),
				b: new people2("wanmei", 20)
			}
		}()
		    
	};

	wmsj.codeUtil.jQuery = {
		openFolder: function() {
			var $ = new Function();
			$(function() {
				// 获取索引值大于5，并且不包含最后一项的元素
				var $category = $("ul>li:gt(5):not(:last)");
				$category.hide();
				var $btn = $(".showmore>a"),
					showMore = "显示全部品牌",
					showLess = "显示精简品牌";

				$btn.click(function() {
					if ($category.is(":visible")) { // 判断是否显示，如果显示
						$category.hide();
						// filter会在元素内寻找匹配元素，是一个对自身集合元素进行筛选
						$("ul li").filter(":contains(佳能),:contains(三星),:contains(柯达)").removeClass("promoted");
						// 设置图片的src地址，并且设置图片的下一个元素的文本值
						$(".showmore>a").find("img").attr("src", "../icon/向下翻页.svg").next().text(showMore);
						return false;
					} else {
						$category.show();
						$("ul li").filter(":contains(佳能),:contains(三星),:contains(柯达)").addClass("promoted");
						$(".showmore>a").find("img").attr("src", "../icon/向上翻页.svg").next().text(showLess);
						return false;
					}
				});
			});
		}()
	}

	// ---------------------------- wmsj.abandon 以废弃的模块封装 ---------------
	wmsj.abandon.func = {	// 废弃的函数
		// 判断传入的参数和期望的参数数目是否相同，不同就弹出警告，相同返回true
		// num -- 期望的参数数目
		// args -- 判断的函数实际的传入参数数目
		argsCount: function(num, args) {
			var countError = "argsCount(): arguments must be " + num + ".";
			wmsj.eventUtil.assert((num === args), countError);
			return true;
		}
	}