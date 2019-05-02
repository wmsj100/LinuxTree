#!/bin/bash
num=0;
a=0;
while (( $num<=100 ))
do
	if [ $[$num % 2] -eq 0 ]
	then
		let "a=a+num"
	fi
	let "num++"
done
echo $a;
