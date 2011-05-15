#!/bin/sh

# need surname and subscriber number to work...
if [ $# != 2 ]; then
    echo "Usage: getter <surname> <subscriber number>"
    exit 1
fi
# assuming they're correct...

# create a cookie based on the args
cookie="Cookie: __utma=65394611.747858017.1258383664.1276678469.1282904913.14; __utmz=65394611.1276678470.13.1.utmccn=(organic)|utmcsr=google|utmctr=lxf|utmcmd=organic; SESSc1e62b721508fb7ffebc7f81393bd318=f1820353d1a384da69bf2727162f181b; rsi_ct=2010_8_27:9; rsi_segs=; __utmb=65394611; __utmc=65394611; SubName=$1; SubNumber=$2; SubExpire=1282993367; SubSum=65f0ca176f09038da4190bf3fc2e27d5dc01ab1c"

# pretend to be a decent browser ;)
browser="Mozilla/7.0 (X11; U; Linux i686; en-GB; rv:1.9.2.8) Gecko/20111231 Ubuntu/12.04 (spaceyjase) Firefox/7.6.5 GTB7.1" 

# lxf url with the archives
url="http://www.linuxformat.com/archives&listpdfs=1" 

echo Checking PDFs at "${url}"...
for f in `curl -s -H "${cookie}" -A "${browser}" "${url}" | grep -o -e '\/includes\/.*\?PDF=LXF[0-9]*\..*\.pdf' | sed 's/^\//http:\/\/linuxformat.com\//g'`
do
    echo -n .
	fo=`echo $f | awk -F= '{ printf "%s", $2 }'`
    filename=`echo $fo | awk -F. '{ printf "./downloads/%s/%s", $1, $0 }'`
	if [ ! -f $filename ]; then
        echo 
		echo Downloading: $f
		curl --create-dirs -# -H "${cookie}" -A "${browser}" $f -o $filename
        counter=30
        while [ $counter -gt 0 ]
        do
            printf "\rContinue in...%02d" $counter
            counter=`expr $counter - 1`
            sleep 1
        done
        echo
	fi
done
# put the prompt on a new line ;)
echo

