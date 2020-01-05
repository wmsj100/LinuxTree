#!/bin/bash

createTemplate(){
	if [ $# -lt 1 ];then
		echo "Please input title"
		return 1
	fi

	local title=$1
	local date=$(date +"%Y-%m-%d %H:%M:%S")
	local tag=$(basename `pwd`)
	local categories=$(basename $(dirname $(pwd)))
	local template="---\ntitle: ${title}\ndate: ${date}\nmodify: \ntags: [$tag]\ncategories: ${categories}\nauthor: wmsj100\nemail: wmsj100@hotmail.com\n---\n\n# ${title}\n\n## 概要\n\n## 参考\n"
	echo -e $template > ${PWD}/${title}.md
}

createTemplate $@
