#! /bin/sh
#
# a.sh
# Copyright (C) 2019 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.
# batch modify GB2312 to UTF-8
#


fileList=$(find . -type f -name "*.md")

for file in $fileList
do
	isoFile=$(file $file | cut -d ' ' -f 2)
	if [ -n $isoFile -a $isoFile != "UTF-8" ]
	then
		iconv -f GB2312 -t UTF-8 $file -o $file
		echo $isoFile, $file
	fi
done
