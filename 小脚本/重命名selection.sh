#! /bin/bash

for file in $(ls *\.txt); do
	newname=`echo $file | sed "s/"\(.*\)\.txt^"/\1_new\.txt/"`
	newFile2=`echo $newFile1 | sed "s/\(.*\)\.txt/\1_new\.txt/"`
	echo $newFile2
	#mv -i $file $newFile2
done
