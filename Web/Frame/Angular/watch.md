# $watch 监听

- 这个方法之前一直是通过配合“contentLoaded”即等页面加载完成后进行监听vdcId的值

- 其实这个方法也可以用来监听“selectId”值的变化从而触发一些方法的执行。

'''js
$scope.$watch("selectId", function(newVal, oldVal){
	if(newVal !== oldVal){
		$scope.handle.queryUserlist();
	}
}
'''
