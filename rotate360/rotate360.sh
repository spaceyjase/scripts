#!/bin/sh

if [ $# != 1 ]; then
    echo "Usage: rotate360.sh <image_filename>"
    exit 1
fi

n=0
ext=${1##*.}
while [ $n -lt 360 ]
do
    target=`printf "%03d" $n`
    n=$(($n+1))
    # perform convert action
    convert $1 -matte \( +clone -background none -rotate $n \) -gravity center -compose Src -composite $target.$ext
done
