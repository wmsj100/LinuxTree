#!/bin/bash
a=0
for loop in 8 4 5
do
	if [ $loop -gt $a ]
	then
		let a=$loop
		echo $a, $loop
	fi
done

