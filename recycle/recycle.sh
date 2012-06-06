#!/bin/bash

# need email and password to work
if [ $# != 2 ]; then
    echo "Usage: recycle <email> <password>"
    exit 1
fi
# assuming they're correct...

browser="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0"

# here's the cookie, yum!
cookie=`mktemp`

# log in first...
curl --form-string "login[username]=$1" \
     --form-string "login[password]=$2" \
     --form-string "login[rememberme]=1" \
     -A "${browser}" \
     -c $cookie \
     "https://www.recyclebank.com/customer/auth/loginPost/"

# make curl do a POST request with the cookie above, spits out if it was successful or not.
curl --referer "https://www.recyclebank.com/how-to-earn/details/www.recyclebank.com/wbc" -A "${browser}" -b $cookie -X POST "https://www.recyclebank.com/curbside/irecycling/reportcurrentweek/"
