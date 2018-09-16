<?php
/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2016-04-15 16:59:12
 * @version $Id$
 */
$status = $_REQUEST["status"];
if($status === "1"){
	$content = array(
		"img05" => "img/05.jpg",
		"img06" => "img/06.jpg",
		"img07" => "img/07.jpg",
		"img08" => "img/08.jpg",
	);
	$status = array("status" => "success");
	$wrap = array($status,$content);
	echo json_encode($wrap);
}
