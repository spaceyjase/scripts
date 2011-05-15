#!/bin/sh

for f in `ls *.pdf`
do
    oldfile=`echo $f`
    newdir=`echo $oldfile | awk -F. '{ printf "./%s/", $1 }'`
    echo Moving $oldfile to $newdir$oldfile
    mkdir -p $newdir 2>/dev/null
    mv $oldfile $newdir
done
