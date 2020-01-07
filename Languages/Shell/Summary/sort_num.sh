#! /bin/bash
#
# sort_num.sh
# Copyright (C) 2019 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.
#

if [ $# -lt 1 ];then
	echo "param error"
	exit 1
fi
index=0
for param in $@
do
	res[index]=$param
	echo ${res[@]}
	if [ $index -gt 0 ];then
		sec_i=0
		for res_item in ${res[@]}
		do
			if [ $res_item -gt ${res[index]} ];then
				res[sec_i]=${res[index]}
				res[index]=$res_item
			fi
			sec_i=$((sec_i+1))
		done
	fi
	index=$((index+1))
done
echo ${res[@]}

