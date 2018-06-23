---
title: 表单验证-PHP-效果
date: 2016-4-4 13:04:44
tags: [PHP,函数,表单,验证]
categories: Dynamic
---
---
<!-- more -->
![](/file/img/tool/April/0404/01.gif)
```html
<!DOCTYPE html>
<html>
<head>	
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>formtest</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="//cdn.bootcss.com/normalize/3.0.3/normalize.min.css" rel="stylesheet">
<style>
	body{
		font-family: "Microsoft Yahei";
		color: #333;
	}
	.wrap{
		width: 600px;
		margin: 40px auto;
	}
	.font{
		display: inline-block;
		width: 80px;
		margin: 5px;
	}
	.php{
		width: 240px;
		margin-left: 92px;	
		margin-bottom: 20px;
		/*border-bottom: solid 1px #999;*/
		text-align: left;
		padding: 10px 0;
		font-size: 20px;
		color: #F23D3D;
		padding-left: 20px;
		/*display: none;*/
	}
	//无法控制弹出的PHP内容中带有边框
	.write{
		width: 260px;
	}
	.error:before{
		content: "*";
		margin-left: 10px;
	}
	.error{
		color: #F23D3D;
	}
	.submit{
		color: #F23D3D;
		font-weight: bold;
		margin-left: 180px;
		margin-top: 20px;
		padding: 3px 10px;
	}
	.submit:hover{
		color: #fff;
		background-color: #F23D3D;
	}
</style>
</head>
<body>

<div class="wrap">
<div class="php">
	<?php 
		$name=$email=$website=$comment=$gender="";
		$nameErr=$emailErr=$websiteErr=$commentErr=$genderErr="";
		if($_SERVER["REQUEST_METHOD"]==="POST"){
			if(empty($_POST["name"])){
				$nameErr="Name is required";
			}else{
				echo $name="name: ".input_test($_POST["name"]).";"."<br>";
			}
			if(empty($_POST["email"])){
				$emailErr="email is required";
			}else{
				echo $email="email: ".input_test($_POST["email"]).";"."<br>";
			}
			if(empty($_POST["website"])){
				$websiteErr="website is required";
			}else{
				echo $website="website: ".input_test($_POST["website"]).";"."<br>";
			}
			if(empty($_POST["comment"])){
				$commentErr="comment is required";
			}else{
				echo $comment="comment: ".input_test($_POST["comment"]).";"."<br>";
			}
			if(empty($_POST["gender"])){
				$genderErr="gender is required";
			}else{
				echo $gender="gender: ".input_test($_POST["gender"]).";"."<br>";
			}
		}

		function input_test($data){
			$data=trim($data);
			$data=stripslashes($data);
			$data=htmlspecialchars($data);
			return $data;
		}
	 ?>
 </div>
	<form method="post" action="<?php htmlspecialchars($_SERVER["PHP_SELF"]) ?>">
	    <span class="font">Name: </span><input class="write" type="text" name="name"><span class="error"> <?php echo $nameErr ?> </span><br>
	    <span class="font">Email: </span><input class="write" type="text" name="email"><span class="error"> <?php echo $emailErr ?> </span><br>
	    <span class="font">Website: </span><input class="write" type="text" name="website"><span class="error"> <?php echo $websiteErr ?> </span><br>
	    <span class="font">Comment: </span><textarea name="comment" cols="30" rows="10"></textarea><br>
	    <span class="font">Gender:</span>
	    <input type="radio" name="gender" value="female" id="female">
	    <label for="female">Female</label>
	    <input type="radio" name="gender" value="male" id="male">
	    <label for="male">Male</label><span class="error"> <?php echo $genderErr ?> </span><br>
	    <input type="submit" class="submit" value="Submit">
    </form>
</div>
</body>
</html>
```

